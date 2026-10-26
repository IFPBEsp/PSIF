#!/usr/bin/env python3
"""
Mede a regra 60-30-10 (§3.3) — a regra de ouro, até aqui a única sem instrumento.

Por quê: "cubra mentalmente a cor de apoio" é experimento mental. Uma violação
real (um modo escuro inteiro tingido de estrutural) passou por lint, checklist e revisão, e só
apareceu quando alguém olhou a tela. O que o olho viu era mensurável: dez
papéis de superfície apontando para duas cores de chrome.

MÉTODO E SEU LIMITE. Proporção de verdade é área renderizada, e área depende de
layout — este script não renderiza. Ele conta DECLARAÇÕES por família de token,
separadas por papel (fundo, texto, borda), porque é onde a dominância nasce:
fundo pinta área, texto e borda não. É aproximação, e a aproximação erra quando
uma tela tem um `<div>` de fundo gigante e vinte cards pequenos. Serve para
pegar inversão grosseira — que é o modo de falha real —, não para auditar 61%
contra 59%.

Uso:
    python check_dominance.py globals.css
    python check_dominance.py src/app/**/*.tsx --escopo dark

Exit 0 = dentro da regra. Exit 2 = inversão detectada.
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
    """Famílias de dominância: papel visual -> prefixos de token.

    Vem de `dominance_families` em tokens.json e NÃO tem default. Um default
    aqui seria a pior falha possível deste script: ele mediria a proporção de
    famílias que a skill não tem, acharia 0% em tudo, e imprimiria um ✓. A
    guarda que passa medindo a coisa errada é pior que a guarda ausente.
    """
    with open(TOKENS_PATH, encoding="utf-8") as f:
        tokens = json.load(f)
    familias = tokens.get("dominance_families")
    if not familias:
        sys.exit(
            "tokens.json sem `dominance_families`.\n"
            "  A regra de dominância é a proporção entre papéis de cor "
            "(ex.: neutro/estrutural/apoio/semântica),\n"
            "  e só a skill sabe quais são os seus. Declare o mapa "
            "papel -> prefixos de token, ex.:\n"
            '    "dominance_families": {"neutro": ["ink-", "white"], '
            '"estrutural": ["ocean-"], "apoio": ["accent-"]}'
        )
    return {papel: tuple(prefixos) for papel, prefixos in familias.items()}


# Vocabulário canônico de papéis. Os PREFIXOS são da skill; os NOMES dos
# papéis, não: a lógica compara "quem pinta mais área que quem", e para isso
# precisa saber qual papel é o fundo, qual é a estrutura e qual é o acento.
# Papel livre viraria um script que mede quatro números sem saber o que
# significam.
PAPEIS = ("neutro", "estrutural", "apoio")
ALVOS = {"neutro": "~60%", "estrutural": "~30%", "apoio": "fração de ~10%"}

FAMILIAS = carrega_familias()

_faltando = [p for p in PAPEIS if p not in FAMILIAS]
if _faltando:
    sys.exit(
        f"tokens.json: `dominance_families` sem o(s) papel(éis) {_faltando}.\n"
        f"  Os três papéis {PAPEIS} são obrigatórios — a regra de dominância é\n"
        f"  a proporção ENTRE eles. 'semantica' é opcional e não entra na base."
    )

# Propriedades que pintam área vs. as que só marcam.
PINTA_AREA = ("background", "background-color", "border-color", "fill")
SO_MARCA = ("color", "border", "outline", "outline-color", "stroke",
            "box-shadow", "caret-color", "text-decoration-color")

# Casa `--card: ...` (custom property) OU `background: ...` (propriedade
# plana). Só o primeiro ramo existia antes — PINTA_AREA/SO_MARCA nunca batiam
# de verdade, porque nenhuma declaração sem `--` era capturada.
DECL = re.compile(r"(?<![\w-])(--[a-z][\w-]*|[a-z][a-z-]*)\s*:\s*([^;{}\n]+)")

# Num projeto shadcn/Tailwind a dominância NÃO se decide em `background:` — se
# decide no mapeamento papel→escala (`--card: var(--ocean-800)`). Sem contar a
# declaração de custom property, o medidor fica cego justamente no arquivo onde
# a inversão acontece: foi assim que dez papéis de superfície mudaram de cor sem
# ninguém ver.
PAPEL_DE_MARCA = re.compile(
    r"(foreground|border|ring|input|outline|shadow|caret|placeholder)$")


def papel_pinta_area(nome):
    """Custom property de papel: pinta área, a menos que seja marca."""
    return not PAPEL_DE_MARCA.search(nome)
USO_TOKEN = re.compile(r"var\(\s*--([\w-]+)")
# Utilitária do Tailwind: bg-ocean-700, text-ink-500, border-accent-200…
UTIL = re.compile(r"\b(bg|text|border|fill|ring|from|to|via)-([a-z]+-\d{2,3}|white)\b")

ESCOPO_ESCURO = re.compile(r"(^|\s)(\.dark\b|\[data-theme=[\"']?dark)")


def familia(nome):
    for fam, prefixos in FAMILIAS.items():
        if any(nome.startswith(p) for p in prefixos):
            return fam
    return None


def carrega_semanticos():
    """Papéis do shadcn (`--primary`, `--card`) apontam para a escala. Sem
    seguir o ponteiro, uma tela inteira em `bg-primary` não classifica nada."""
    with open(TOKENS_PATH, encoding="utf-8") as f:
        json.load(f)  # valida o arquivo; nomes vêm do CSS analisado
    return {}


def mapeia_papeis(css):
    """`--primary: var(--<estrutural>-700)` → primary conta como 'estrutural'."""
    mapa = {}
    for m in re.finditer(r"--([\w-]+)\s*:\s*var\(\s*--([\w-]+)\s*\)", css):
        mapa[m.group(1)] = m.group(2)
    return mapa


def resolve_familia(nome, mapa, profundidade=0):
    fam = familia(nome)
    if fam or profundidade > 5:
        return fam
    alvo = mapa.get(nome)
    return resolve_familia(alvo, mapa, profundidade + 1) if alvo else None


def analisa(textos, escopo_escuro):
    css_total = "\n".join(textos)
    mapa = mapeia_papeis(css_total)

    contagem = {"area": {}, "marca": {}}
    exemplos = {}

    for texto in textos:
        for bloco_sel, corpo in blocos(texto):
            eh_escuro = bool(ESCOPO_ESCURO.search(bloco_sel))
            if eh_escuro != escopo_escuro:
                continue
            for m in DECL.finditer(corpo):
                prop, valor = m.group(1), m.group(2)
                if prop.startswith("--"):
                    # Declaração de papel: --card: var(--ocean-800)
                    grupo = "area" if papel_pinta_area(prop[2:]) else "marca"
                    if familia(prop[2:]):
                        continue  # é token da escala, não papel: não conta 2x
                else:
                    grupo = ("area" if prop in PINTA_AREA
                             else "marca" if prop in SO_MARCA else None)
                if grupo is None:
                    continue
                for uso in USO_TOKEN.finditer(valor):
                    fam = resolve_familia(uso.group(1), mapa)
                    if fam:
                        contagem[grupo][fam] = contagem[grupo].get(fam, 0) + 1
                        exemplos.setdefault((grupo, fam), []).append(
                            f"{prop}: var(--{uso.group(1)})")
        for m in UTIL.finditer(texto):
            papel, nome = m.group(1), m.group(2)
            fam = resolve_familia(nome, mapa)
            if not fam:
                continue
            grupo = "area" if papel in ("bg", "fill", "from", "to", "via") else "marca"
            contagem[grupo][fam] = contagem[grupo].get(fam, 0) + 1
            exemplos.setdefault((grupo, fam), []).append(f"{papel}-{nome}")
    return contagem, exemplos


def blocos(css):
    """(seletor, corpo) de cada bloco, para saber se estamos no `.dark`."""
    saida, i = [], 0
    while True:
        abre = css.find("{", i)
        if abre == -1:
            if i == 0:
                saida.append(("", css))  # arquivo sem blocos (ex.: .tsx)
            break
        seletor = css[css.rfind("}", 0, abre) + 1: abre]
        prof, fim = 1, abre + 1
        while prof and fim < len(css):
            prof += (css[fim] == "{") - (css[fim] == "}")
            fim += 1
        saida.append((seletor, css[abre + 1:fim - 1]))
        i = fim
    return saida


def relatorio(contagem, exemplos, rotulo):
    area = contagem["area"]
    total_area = sum(area.values())
    print(f"\n── Dominância — {rotulo}")
    if not total_area:
        print("   nenhuma declaração de fundo com token reconhecido.")
        return 0

    # Cor semântica é CONDICIONAL: success/warning/danger só pintam quando o
    # estado acontece, e são mutuamente exclusivas. Contá-las no regime
    # permanente infla o denominador e afunda o neutro artificialmente.
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
            f"estrutural pinta mais área que neutro ({prop['estrutural']:.0f}% vs "
            f"{prop['neutro']:.0f}%). A cor estrutural governa os PAPÉIS (chrome, ação), "
            f"não as superfícies — §3.3. Em modo escuro, ver §27.1.")
    if prop["apoio"] > 15:
        falhas.append(
            f"apoio em {prop['apoio']:.0f}% das superfícies — o teto "
            f"prático é uma fração dos 10% de acento (§3.3).")
    if prop["neutro"] < 40:
        falhas.append(
            f"neutro em só {prop['neutro']:.0f}% das superfícies; a regra pede "
            f"~60%. Tela sem respiro neutro lê como monocromática.")

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
            sys.exit(f"arquivo não encontrado: {c}")
        with open(c, encoding="utf-8") as f:
            textos.append(f.read())

    falhas = 0
    escopos = ([("claro", False), ("modo escuro", True)]
               if args.escopo == "ambos"
               else [("claro", False)] if args.escopo == "claro"
               else [("modo escuro", True)])
    for rotulo, escuro in escopos:
        contagem, exemplos = analisa(textos, escuro)
        falhas += relatorio(contagem, exemplos, rotulo)

    print("\nLimite do método: conta declaração, não área renderizada (ver "
          "docstring). Pega inversão grosseira, não ajusta 61% contra 59%.")
    return 2 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
