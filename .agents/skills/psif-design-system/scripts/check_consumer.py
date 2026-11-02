#!/usr/bin/env python3
"""
Compara os tokens colados num projeto com o :root de assets/tokens.css da skill.

Uso:
    python check_consumer.py src/app/globals.css [--quiet]

Entrada: o CSS do projeto. Token que o projeto inventou não conta; só nome da
skill com outro valor, ou nome quase igual a um da skill.
Saída: 0 sem divergência; 2 com divergência.
"""

import argparse
import difflib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSS_DA_SKILL = os.path.normpath(os.path.join(HERE, "..", "assets", "tokens.css"))

DECL = re.compile(r"(?<![\w-])--([\w-]+)\s*:\s*([^;{}]+)(?=[;}])")
ALIAS = re.compile(r"^var\(\s*--([\w-]+)\s*\)$")

# @theme (§26.2) e .dark (§25) redefinem token de propósito.
ESCOPO_LEGITIMO = re.compile(
    r"@theme\b|\.dark\b|\[data-theme|@media[^{]*prefers-color-scheme"
)


def blocos(css):
    """(seletor, deslocamento, corpo) de cada bloco de primeiro nível."""
    i = 0
    while True:
        abre = css.find("{", i)
        if abre == -1:
            return
        seletor = css[css.rfind("}", 0, abre) + 1: abre].strip()
        profundidade, fim = 1, abre + 1
        while profundidade and fim < len(css):
            if css[fim] == "{":
                profundidade += 1
            elif css[fim] == "}":
                profundidade -= 1
            fim += 1
        yield seletor, abre + 1, css[abre + 1:fim - 1]
        i = fim


def tokens_da_skill():
    with open(CSS_DA_SKILL, encoding="utf-8") as f:
        css = re.sub(r"/\*.*?\*/", "", f.read(), flags=re.S)
    plano = {}
    for seletor, _, corpo in blocos(css):
        if seletor == ":root":
            for m in DECL.finditer(corpo):
                plano.setdefault(m.group(1), m.group(2).strip())
    return plano


def normaliza(valor):
    """Ignora caixa, espaço e aspas."""
    valor = " ".join(valor.split()).strip().strip("\'\"")
    return valor.lower().replace(", ", ",")


def blocos_base(css):
    """(deslocamento, corpo) dos blocos fora de @theme e .dark."""
    return [(ini, corpo) for seletor, ini, corpo in blocos(css)
            if not ESCOPO_LEGITIMO.search(seletor)]


def resolve(nome, valor, skill):
    """Segue var(--token) da skill antes de comparar."""
    m = ALIAS.match(valor.strip())
    if m and m.group(1) in skill:
        return skill[m.group(1)]
    return valor


def analisa(caminho, skill):
    with open(caminho, encoding="utf-8") as f:
        css = f.read()

    vistos = {}
    for deslocamento, trecho in blocos_base(css):
        for m in DECL.finditer(trecho):
            nome, valor = m.group(1), m.group(2)
            linha = css.count("\n", 0, deslocamento + m.start()) + 1
            vistos.setdefault(nome, (valor, linha))

    divergentes, ausentes, parecidos = [], [], []

    for nome, valor_skill in skill.items():
        if nome not in vistos:
            ausentes.append(nome)
            continue
        valor_projeto, linha = vistos[nome]
        efetivo = resolve(nome, valor_projeto, skill)
        esperado = resolve(nome, valor_skill, skill)
        if normaliza(efetivo) != normaliza(esperado):
            divergentes.append((nome, valor_skill, normaliza(valor_projeto), linha))

    nomes_skill = set(skill)
    for nome, (_, linha) in vistos.items():
        if nome in nomes_skill or nome.startswith("tw-") or len(nome) < 6:
            continue
        perto = difflib.get_close_matches(nome, sorted(nomes_skill), n=1, cutoff=0.92)
        # Só o sufixo xl do Tailwind fica isento; isentar número cegaria a paleta inteira.
        if perto and not re.search(r"-\d?xl$", nome):
            parecidos.append((nome, perto[0], linha))

    tema = []
    for seletor, ini, corpo in blocos(re.sub(r"/\*.*?\*/", lambda m: " " * len(m.group(0)), css, flags=re.S)):
        if not seletor.startswith("@theme"):
            continue
        for m in DECL.finditer(corpo):
            if m.group(1) in skill:
                tema.append((m.group(1), css.count("\n", 0, ini + m.start()) + 1))

    return divergentes, ausentes, parecidos, tema


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("arquivo", help="CSS do projeto consumidor (ex.: globals.css)")
    parser.add_argument("--quiet", action="store_true", help="só o resumo")
    args = parser.parse_args()

    if not os.path.isfile(args.arquivo):
        sys.exit(f"[ERRO] arquivo não encontrado: {args.arquivo}")

    skill = tokens_da_skill()
    divergentes, ausentes, parecidos, tema = analisa(args.arquivo, skill)

    if not args.quiet:
        linhas = [(linha, f"[ERRO] linha {linha}: --{nome} vale '{achado}' "
                          f"('{esperado}' na skill, §26.5)")
                  for nome, esperado, achado, linha in divergentes]
        linhas += [(linha, f"[ERRO] linha {linha}: redefine --{nome} no @theme "
                           f"(apague a escala calculada, §26.3)")
                   for nome, linha in tema]
        linhas += [(linha, f"[AVISO] linha {linha}: --{nome} não existe na skill "
                           f"(--{sugestao}?, §26.5)")
                   for nome, sugestao, linha in parecidos]
        for _, texto in sorted(linhas):
            print(texto)
        if ausentes and not (divergentes or tema):
            print(f"[INFO] {len(ausentes)} token(s) da skill fora deste arquivo.")

    erros = len(divergentes) + len(tema)
    print(f"\n{erros} divergência(s), {len(parecidos)} aviso(s), "
          f"{len(skill) - len(ausentes)}/{len(skill)} tokens da skill presentes.")
    return 2 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
