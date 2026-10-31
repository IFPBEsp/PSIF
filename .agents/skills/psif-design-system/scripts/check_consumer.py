#!/usr/bin/env python3
"""
Acusa divergência entre os tokens da skill e a cópia colada num projeto.

Por quê: "cole, não redigite" (SKILL.md, passo 1) mata o drift na origem, mas cria duas
cópias — a da skill e a do `globals.css` (ou equivalente) do projeto que
consome. `gen_tokens_css.py --check` cobre a primeira e não sabe da segunda.
Sem isto, a paleta do produto e a paleta da skill divergem em silêncio, que é
o mesmo modo de falha que o `--check` existe para impedir, um nível acima.

Uso:
    python check_consumer.py caminho/para/globals.css
    python check_consumer.py app/globals.css --quiet   # só o resumo

Exit 0 = nenhuma divergência. Exit 2 = divergência encontrada.

O que ele NÃO faz: reclamar de token que o projeto inventou. `--primary`,
`--sidebar`, `--table-head` são do consumidor. Só entra no relatório o que tem
nome de token da skill e valor diferente — ou nome quase igual, que costuma
ser erro de digitação.
"""

import argparse
import difflib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOKENS_PATH = os.path.join(HERE, "tokens.json")

# Grupos que guardam valores/exceções, não nomes de token (mesma lista do lint).
NAO_SAO_TOKENS = {
    "gradient_literals", "translucent_literals", "named_colors_allowed",
    "text_color_banlist", "icon_color_allowed", "browser_surfaces",
    "spacing_exceptions", "wcag_minimum", "touch_target_min_px", "_comment",
    "absent_groups",
}

DECL = re.compile(r"(?<![\w-])--([\w-]+)\s*:\s*([^;{}]+)(?=[;}])")
ALIAS = re.compile(r"^var\(\s*--([\w-]+)\s*\)$")

# Escopos que legitimamente redefinem token e NÃO são divergência:
#   @theme      — ponte de namespace do Tailwind v4 (§27.2)
#   .dark etc.  — sobrescrita de modo escuro (§26)
ESCOPO_LEGITIMO = re.compile(
    r"(^|\s)(@theme\b|\.dark\b|\[data-theme|@media[^{]*prefers-color-scheme)"
)


def tokens_da_skill():
    with open(TOKENS_PATH, encoding="utf-8") as f:
        dados = json.load(f)
    plano = {}

    def colhe(no):
        for chave, valor in no.items():
            if isinstance(valor, dict):
                colhe(valor)
            elif isinstance(chave, str) and not chave.startswith("_"):
                plano[chave] = str(valor)

    for grupo, conteudo in dados.items():
        if grupo in NAO_SAO_TOKENS or not isinstance(conteudo, dict):
            continue
        colhe(conteudo)
    return plano


def normaliza(valor):
    """Compara significado, não formatação: caixa, espaço e aspas não contam."""
    valor = " ".join(valor.split()).strip().strip("\'\"")
    return valor.lower().replace(", ", ",")


def blocos_base(css):
    """Devolve só os trechos de escopo base — tipicamente `:root`.

    Sem isto o checker acusa a ponte `--radius-md: var(--tw-radius-md)` do
    `@theme` e toda sobrescrita do `.dark` como divergência, que é ruído: as
    duas são o uso previsto (§26, §27.2). Um checker com 20 falsos positivos
    é pior que checker nenhum — ninguém lê o vigésimo primeiro.
    """
    trechos, i = [], 0
    while True:
        abre = css.find("{", i)
        if abre == -1:
            break
        seletor = css[css.rfind("}", 0, abre) + 1: abre]
        profundidade, fim = 1, abre + 1
        while profundidade and fim < len(css):
            if css[fim] == "{":
                profundidade += 1
            elif css[fim] == "}":
                profundidade -= 1
            fim += 1
        if not ESCOPO_LEGITIMO.search(seletor):
            trechos.append((abre + 1, css[abre + 1:fim - 1]))
        i = fim
    return trechos


def resolve(nome, valor, skill):
    """`--surface-base: var(--sky-100)` não é divergência: é o alias que o
    próprio tokens.css da skill emite. Segue o ponteiro antes de comparar."""
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
        # Resolve os DOIS lados: o tokens.json guarda `--surface-base` como
        # "var(--ink-50)" e o projeto pode ter o hex, ou vice-versa. Comparar
        # ponteiro com valor acusaria divergência onde não há.
        efetivo = resolve(nome, valor_projeto, skill)
        esperado = resolve(nome, valor_skill, skill)
        if normaliza(efetivo) != normaliza(esperado):
            divergentes.append((nome, valor_skill, normaliza(valor_projeto), linha))

    nomes_skill = set(skill)
    for nome, (_, linha) in vistos.items():
        if nome in nomes_skill or nome.startswith("tw-") or len(nome) < 6:
            continue
        perto = difflib.get_close_matches(nome, sorted(nomes_skill), n=1, cutoff=0.92)
        # Sufixo de escala próprio do Tailwind (2xl, 3xl…) não é typo da skill.
        #
        # A isenção já foi `-\d?xl$|-\d+$`, e o segundo ramo engolia a regra
        # inteira: toda família de escala da skill termina em número
        # (`navy-900`, `ink-700`, `sp-4`), então o detector de typo ficava
        # cego para o grosso da paleta — `--navi-900` passava calado enquanto
        # `--surfce-base` era pego. Só o sufixo `xl` precisa da isenção.
        if perto and not re.search(r"-\d?xl$", nome):
            parecidos.append((nome, perto[0], linha))

    return divergentes, ausentes, parecidos


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("arquivo", help="CSS do projeto consumidor (ex.: globals.css)")
    parser.add_argument("--quiet", action="store_true", help="só o resumo")
    args = parser.parse_args()

    if not os.path.isfile(args.arquivo):
        sys.exit(f"arquivo não encontrado: {args.arquivo}")

    skill = tokens_da_skill()
    divergentes, ausentes, parecidos = analisa(args.arquivo, skill)

    if not args.quiet:
        for nome, esperado, achado, linha in divergentes:
            print(f"[DIVERGE] linha {linha}: --{nome} vale '{achado}' no projeto, "
                  f"'{esperado}' na skill. Um dos dois está desatualizado — "
                  f"a skill é a fonte (§3).")
        for nome, sugestao, linha in parecidos:
            print(f"[AVISO] linha {linha}: --{nome} não existe na skill, mas é "
                  f"quase --{sugestao}. Erro de digitação vira token morto: o "
                  f"browser descarta a declaração em silêncio.")
        if ausentes and not divergentes:
            print(f"[INFO] {len(ausentes)} token(s) da skill não aparecem neste "
                  f"arquivo — normal se o projeto usa só parte do sistema.")

    print(f"\n{len(divergentes)} divergência(s), {len(parecidos)} aviso(s), "
          f"{len(skill) - len(ausentes)}/{len(skill)} tokens da skill presentes.")
    return 2 if divergentes else 0


if __name__ == "__main__":
    sys.exit(main())
