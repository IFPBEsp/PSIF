#!/usr/bin/env python3
"""
Gera assets/DESIGN.md: frontmatter do tokens.json e corpo de
scripts/design_md_body.md, com cada {{token}} preenchido.

Uso:
    python gen_design_md.py            # escreve ../assets/DESIGN.md
    python gen_design_md.py --check    # não escreve; saída 2 se defasado
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOKENS_PATH = os.path.join(HERE, "tokens.json")
BODY_PATH = os.path.join(HERE, "design_md_body.md")
OUT_PATH = os.path.normpath(os.path.join(HERE, "..", "assets", "DESIGN.md"))

sys.path.insert(0, HERE)
from skill_config import config as _config  # noqa: E402

with open(TOKENS_PATH, encoding="utf-8") as _f:
    TOKENS = json.load(_f)

TYPO_MD = os.path.normpath(os.path.join(HERE, "..", "tokens", "typography.md"))
LINHA_TIPO = re.compile(r"^\| `--fs-([\w-]+)` \| (\d+)px \| (\d{3}) \|", re.M)

# "grupo:token": cor, tipografia e raio viram {grupo.token}; o resto, o valor.
COMPONENTES = [
    ("button-primary", {
        "backgroundColor": "colors:navy-700", "textColor": "colors:white",
        "typography": "typography:h2", "rounded": "rounded:radius-lg",
        "padding": "component_padding:btn-pad", "height": "touch_target:control-min"}),
    ("button-primary-hover", {"backgroundColor": "colors:navy-800"}),
    ("button-primary-active", {"backgroundColor": "colors:navy-900"}),
    ("button-secondary", {
        "backgroundColor": "colors:white", "textColor": "colors:navy-700",
        "rounded": "rounded:radius-lg", "padding": "component_padding:btn-pad",
        "height": "touch_target:control-min"}),
    ("input", {
        "backgroundColor": "colors:white", "textColor": "colors:navy-700",
        "typography": "typography:h3", "rounded": "rounded:radius-lg",
        "padding": "component_padding:input-pad", "height": "touch_target:control-min"}),
    ("card", {
        "backgroundColor": "colors:white", "rounded": "rounded:radius-xl",
        "padding": "component_padding:card-pad"}),
    ("card-wide", {"rounded": "rounded:radius-2xl"}),
    ("chip", {
        "textColor": "colors:navy-700",
        "typography": "typography:small", "rounded": "rounded:radius-pill",
        "padding": "component_padding:chip-pad", "height": "touch_target:target-min"}),
    ("chip-selected", {"backgroundColor": "colors:navy-700", "textColor": "colors:white"}),
    ("badge-success", {
        "backgroundColor": "colors:success-100", "textColor": "colors:success-700",
        "typography": "typography:caption", "rounded": "rounded:radius-pill"}),
    ("badge-warning", {
        "backgroundColor": "colors:warning-100", "textColor": "colors:warning-700",
        "typography": "typography:caption", "rounded": "rounded:radius-pill"}),
    ("icon-tile", {
        "backgroundColor": "colors:sky-100", "textColor": "colors:navy-700",
        "rounded": "rounded:radius-md", "size": "icon_size:tile-icon"}),
    ("quick-action", {
        "backgroundColor": "colors:sky-300", "textColor": "colors:navy-700",
        "rounded": "rounded:radius-md", "size": "spacing:sp-12"}),
    ("nav-item-active", {
        "backgroundColor": "colors:sky-100", "textColor": "colors:navy-700",
        "rounded": "rounded:radius-lg"}),
]


def q(valor):
    return '"' + str(valor).replace("\\", "\\\\").replace('"', '\\"') + '"'


def tipografia():
    """Papel -> (tamanho, peso, altura), com o peso lido da tabela de §4.2."""
    tamanhos = TOKENS["typography"]["font_size"]
    alturas = TOKENS["typography"]["line_height"]
    with open(TYPO_MD, encoding="utf-8") as f:
        linhas = LINHA_TIPO.findall(f.read())
    if not linhas:
        sys.exit("[ERRO] typography.md sem a tabela de escala "
                 "(| `--fs-x` | Npx | peso |, §4.2)")
    papeis = {}
    for nome, px, peso in linhas:
        token = f"fs-{nome}"
        if tamanhos.get(token) != f"{px}px":
            sys.exit(f"[ERRO] typography.md: {token} = {px}px "
                     f"({tamanhos.get(token)} no tokens.json, §4.2)")
        por_tamanho = TOKENS["typography"].get("line_height_by_size", {})
        if token not in por_tamanho:
            sys.exit(f"[ERRO] tokens.json sem typography.line_height_by_size.{token} "
                     "(uma altura por tamanho, §4.4)")
        altura = alturas[por_tamanho[token]]
        papeis[nome] = (f"{px}px", int(peso), altura)
    return papeis


# Chaves são nomes de token, mas o valor é outro nome: achatadas, sobrescreveriam o token.
NAO_SAO_VALOR = {"line_height_by_size"}

GRUPOS_DO_CORPO = ("color", "shadow", "overlay", "line", "opacity", "radius",
                   "spacing", "component_padding", "icon_size", "touch_target",
                   "avatar", "width", "breakpoint", "typography")


def planos():
    """Todo token com valor num mapa só; falha se duas chaves colidirem."""
    plano, origem = {}, {}

    def colhe(no, caminho):
        for chave, valor in no.items():
            if chave in NAO_SAO_VALOR:
                continue
            if isinstance(valor, dict):
                colhe(valor, f"{caminho}.{chave}")
            elif isinstance(valor, (str, int, float)):
                if chave in plano and plano[chave] != str(valor):
                    sys.exit(f"[ERRO] tokens.json: '{chave}' em {origem[chave]} e em "
                             f"{caminho} com valores diferentes (um valor por nome)")
                plano[chave], origem[chave] = str(valor), caminho

    for grupo in GRUPOS_DO_CORPO:
        colhe(TOKENS.get(grupo, {}), grupo)
    return plano


def resolve(ref, papeis):
    grupo, token = ref.split(":", 1)
    if grupo == "colors":
        if token not in TOKENS["color"]:
            sys.exit(f"[ERRO] componente aponta para cor inexistente: {token} (token de color)")
        return "{colors." + token + "}"
    if grupo == "typography":
        if token not in papeis:
            sys.exit(f"[ERRO] componente aponta para papel inexistente: {token} (linha da tabela de §4.2)")
        return "{typography." + token + "}"
    if grupo == "rounded":
        if token not in TOKENS["radius"]:
            sys.exit(f"[ERRO] componente aponta para raio inexistente: {token} (token de radius, §3.6)")
        return "{rounded." + token + "}"
    valor = TOKENS.get(grupo, {}).get(token)
    if valor is None:
        sys.exit(f"[ERRO] componente aponta para token inexistente: {grupo}.{token} (token do tokens.json)")
    return valor


def frontmatter():
    papeis = tipografia()
    # Fora do CSS, o var() do next/font vira o fallback literal.
    familia = re.sub(r"var\(\s*--[\w-]+\s*,\s*([^)]*)\)", r"\1",
                     TOKENS["typography"]["font_family"]["font-sans"])
    linhas = ["---", f"name: {q(_config().titulo)}",
              f"description: {q(TOKENS.get('golden_rule', ''))}", "colors:"]
    linhas += [f"  {k}: {q(v)}" for k, v in TOKENS["color"].items()]
    linhas.append("typography:")
    for papel, (tamanho, peso, altura) in papeis.items():
        linhas += [f"  {papel}:", f"    fontFamily: {q(familia)}",
                   f"    fontSize: {q(tamanho)}", f"    fontWeight: {peso}",
                   f"    lineHeight: {altura}"]
    linhas.append("rounded:")
    linhas += [f"  {k}: {q(v)}" for k, v in TOKENS["radius"].items()]
    linhas.append("spacing:")
    linhas += [f"  {k}: {q(v)}" for k, v in TOKENS["spacing"].items()]
    linhas.append("components:")
    for nome, props in COMPONENTES:
        linhas.append(f"  {nome}:")
        linhas += [f"    {p}: {q(resolve(r, papeis))}" for p, r in props.items()]
    linhas.append("---")
    return "\n".join(linhas)


def corpo():
    with open(BODY_PATH, encoding="utf-8") as f:
        texto = f.read()
    plano = planos()

    def troca(m):
        nome = m.group(1)
        if nome not in plano:
            sys.exit(f"[ERRO] design_md_body.md cita {{{{{nome}}}}} (token do tokens.json)")
        return plano[nome]

    return re.sub(r"\{\{([\w-]+)\}\}", troca, texto)


def render():
    aviso = ("<!-- GERADO por scripts/gen_design_md.py: frontmatter do tokens.json, "
             "corpo de scripts/design_md_body.md. Não edite aqui. -->")
    return f"{frontmatter()}\n\n{aviso}\n\n{corpo().strip()}\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("--check", action="store_true",
                        help="não escreve; saída 2 se assets/DESIGN.md estiver defasado")
    args = parser.parse_args()

    novo = render()
    atual = None
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH, encoding="utf-8") as f:
            atual = f.read()

    if args.check:
        if atual == novo:
            print("✓ assets/DESIGN.md está em sincronia com tokens.json e o corpo.")
            return 0
        print("✗ assets/DESIGN.md está defasado. Rode: python scripts/gen_design_md.py",
              file=sys.stderr)
        return 2

    if atual == novo:
        print("assets/DESIGN.md já estava atualizado.")
        return 0
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(novo)
    print(f"assets/DESIGN.md escrito — {len(novo.splitlines())} linhas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
