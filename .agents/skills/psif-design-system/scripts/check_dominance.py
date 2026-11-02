#!/usr/bin/env python3
"""
Mede a proporção de cor por papel (§3.3): neutro, estrutural e apoio.

Conta declarações por família de token, não área renderizada: pega inversão
grosseira, não 61% contra 59%.

Uso:
    python check_dominance.py globals.css
    python check_dominance.py "src/app/**/*.tsx" --escopo dark

Saída: 0 dentro da regra; 2 inversão.
"""

import argparse
import glob as globmod
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOKENS_PATH = os.path.join(HERE, "tokens.json")

def carrega_familias():
    """Papel -> prefixos de token, de tokens.json["dominance_families"]; sem padrão."""
    with open(TOKENS_PATH, encoding="utf-8") as f:
        tokens = json.load(f)
    familias = tokens.get("dominance_families")
    if not familias:
        sys.exit('[ERRO] tokens.json sem dominance_families '
                 '({"neutro": [...], "estrutural": [...], "apoio": [...]}, §3.3)')
    return {papel: tuple(prefixos) for papel, prefixos in familias.items()}


PAPEIS = ("neutro", "estrutural", "apoio")
ALVOS = {"neutro": "~60%", "estrutural": "~30%", "apoio": "fração de ~10%"}

FAMILIAS = carrega_familias()

_faltando = [p for p in PAPEIS if p not in FAMILIAS]
if _faltando:
    sys.exit(f"[ERRO] dominance_families sem {_faltando} (os papéis {PAPEIS}, §3.3)")

PINTA_AREA = ("background", "background-color", "border-color", "fill")
SO_MARCA = ("color", "border", "outline", "outline-color", "stroke",
            "box-shadow", "caret-color", "text-decoration-color")

DECL = re.compile(r"(?<![\w-])(--[a-z][\w-]*|[a-z][a-z-]*)\s*:\s*([^;{}\n]+)")

# No shadcn a dominância nasce no mapa papel -> escala (--card: var(--navy-800)).
PAPEL_DE_MARCA = re.compile(
    r"(foreground|border|ring|input|outline|shadow|caret|placeholder)$")


def papel_pinta_area(nome):
    """Custom property de papel: pinta área, a menos que seja marca."""
    return not PAPEL_DE_MARCA.search(nome)


USO_TOKEN = re.compile(r"var\(\s*--([\w-]+)")
UTIL = re.compile(r"\b(bg|text|border|fill|ring|from|to|via)-([a-z]+-\d{2,3}|white)\b")

ESCOPO_ESCURO = re.compile(r"(^|\s)(\.dark\b|\[data-theme=[\"']?dark)")


def familia(nome):
    for fam, prefixos in FAMILIAS.items():
        if any(nome.startswith(p) for p in prefixos):
            return fam
    return None


def mapeia_papeis(css):
    """`--primary: var(--<estrutural>-700)` → primary conta como 'estrutural'."""
    mapa = {}
    for m in re.finditer(r"--([\w-]+)\s*:\s*var\(\s*--([\w-]+)\s*\)", css):
        mapa[m.group(1)] = m.group(2)
    return mapa


def resolve_familia(nome, mapa, profundidade=0):
    """Segue o var() antes de olhar o prefixo: o alias pinta a cor para onde aponta."""
    alvo = mapa.get(nome)
    if alvo and profundidade <= 5:
        return resolve_familia(alvo, mapa, profundidade + 1)
    return familia(nome)


def analisa(textos, escopo_escuro):
    css_total = "\n".join(textos)
    mapa = mapeia_papeis(css_total)

    contagem = {"area": {}, "marca": {}}

    for texto in textos:
        for bloco_sel, corpo in blocos(texto):
            eh_escuro = bool(ESCOPO_ESCURO.search(bloco_sel))
            if eh_escuro != escopo_escuro:
                continue
            for m in DECL.finditer(corpo):
                prop, valor = m.group(1), m.group(2)
                if prop.startswith("--"):
                    grupo = "area" if papel_pinta_area(prop[2:]) else "marca"
                    if familia(prop[2:]):
                        continue
                else:
                    grupo = ("area" if prop in PINTA_AREA
                             else "marca" if prop in SO_MARCA else None)
                if grupo is None:
                    continue
                for uso in USO_TOKEN.finditer(valor):
                    fam = resolve_familia(uso.group(1), mapa)
                    if fam:
                        contagem[grupo][fam] = contagem[grupo].get(fam, 0) + 1
        for m in UTIL.finditer(texto):
            papel, nome = m.group(1), m.group(2)
            fam = resolve_familia(nome, mapa)
            if not fam:
                continue
            grupo = "area" if papel in ("bg", "fill", "from", "to", "via") else "marca"
            contagem[grupo][fam] = contagem[grupo].get(fam, 0) + 1
    return contagem


def blocos(css):
    """(seletor, corpo) de cada bloco."""
    saida, i = [], 0
    while True:
        abre = css.find("{", i)
        if abre == -1:
            if i == 0:
                saida.append(("", css))
            break
        seletor = css[css.rfind("}", 0, abre) + 1: abre]
        prof, fim = 1, abre + 1
        while prof and fim < len(css):
            prof += (css[fim] == "{") - (css[fim] == "}")
            fim += 1
        saida.append((seletor, css[abre + 1:fim - 1]))
        i = fim
    return saida


def relatorio(contagem, rotulo):
    area = contagem["area"]
    total_area = sum(area.values())
    print(f"\n── Dominância — {rotulo}")
    if not total_area:
        print("   nenhuma declaração de fundo com token reconhecido.")
        return 0

    # Cor de estado só pinta quando o estado acontece: fica fora da base.
    base = {f: area.get(f, 0) for f in PAPEIS}
    total_base = sum(base.values()) or 1
    print("   Regime permanente (fundo, borda de área, fill):")
    prop = {}
    for fam in PAPEIS:
        pct = 100 * base[fam] / total_base
        prop[fam] = pct
        alvo = ALVOS[fam]
        print(f"     {fam:10s} {base[fam]:4d}  {pct:5.1f}%   (alvo {alvo})")
    n_sem = area.get("semantica", 0)
    if n_sem:
        print(f"     {'estado':10s} {n_sem:4d}   —      (condicional: success/"
              f"warning/danger não somam no regime)")

    falhas = []
    if prop["estrutural"] > prop["neutro"]:
        falhas.append(
            f"estrutural pinta mais área que neutro, {prop['estrutural']:.0f}% contra "
            f"{prop['neutro']:.0f}% (neutro acima, §3.3; no escuro, §25.1)")
    if prop["apoio"] > 15:
        falhas.append(
            f"apoio em {prop['apoio']:.0f}% das superfícies (até 15%, §3.3)")
    if prop["neutro"] < 40:
        falhas.append(
            f"neutro em só {prop['neutro']:.0f}% das superfícies (perto de 60%, §3.3)")

    for f in falhas:
        print(f"   [ERRO] {f}")
    if not falhas:
        print("   ✓ proporção dentro da regra de ouro.")
    return len(falhas)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("arquivos", nargs="+")
    parser.add_argument("--escopo", choices=["claro", "dark", "ambos"],
                        default="ambos", help="qual tema medir (padrão: ambos)")
    args = parser.parse_args()

    caminhos = []
    for padrao in args.arquivos:
        caminhos.extend(globmod.glob(padrao, recursive=True) or [padrao])
    textos = []
    for c in caminhos:
        if not os.path.isfile(c):
            sys.exit(f"[ERRO] arquivo não encontrado: {c}")
        with open(c, encoding="utf-8") as f:
            textos.append(f.read())

    falhas = 0
    escopos = ([("claro", False), ("modo escuro", True)]
               if args.escopo == "ambos"
               else [("claro", False)] if args.escopo == "claro"
               else [("modo escuro", True)])
    for rotulo, escuro in escopos:
        contagem = analisa(textos, escuro)
        falhas += relatorio(contagem, rotulo)

    return 2 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
