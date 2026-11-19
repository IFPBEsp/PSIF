#!/usr/bin/env python3
"""
Confere que toda referência §N ou §N.M da skill tem heading `## N.` ou
`### N.M` num .md de conteúdo. Lê os .md e os .py de scripts/ (menos
tests/).

Uso:
    python check_refs.py
    python check_refs.py --quiet   # só os erros

Saída: 0 tudo resolve; 2 referência sem seção.
"""

import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
EXCLUI_ARQ = set()
EXCLUI_DIR = {"__pycache__", "tests"}

HEADING_SECAO = re.compile(r'^##\s+(\d+)\.\s')
HEADING_SUBSECAO = re.compile(r'^###\s+(\d+\.\d+)\s')
REF = re.compile(r'§(\d+(?:\.\d+)?)')


def _elegivel(caminho):
    if any(parte in EXCLUI_DIR for parte in caminho.relative_to(RAIZ).parts):
        return False
    if caminho.suffix == ".md":
        return caminho.name not in EXCLUI_ARQ
    return caminho.suffix == ".py"


def arquivos():
    return sorted(p for p in RAIZ.rglob("*") if p.is_file() and _elegivel(p))


def secoes_definidas():
    """(seções, subseções) dos headings dos .md."""
    secoes, subsecoes = set(), set()
    for caminho in arquivos():
        if caminho.suffix != ".md":
            continue
        for linha in caminho.read_text(encoding="utf-8").splitlines():
            m = HEADING_SECAO.match(linha)
            if m:
                secoes.add(m.group(1))
                continue
            m = HEADING_SUBSECAO.match(linha)
            if m:
                subsecoes.add(m.group(1))
    return secoes, subsecoes


def referencias_orfas():
    secoes, subsecoes = secoes_definidas()
    orfas = []
    for caminho in arquivos():
        texto = caminho.read_text(encoding="utf-8")
        for n_linha, linha in enumerate(texto.splitlines(), start=1):
            for m in REF.finditer(linha):
                numero = m.group(1)
                valido = (numero in subsecoes) if "." in numero else (numero in secoes)
                if not valido:
                    orfas.append((caminho.relative_to(RAIZ), n_linha, numero, linha.strip()))
    return orfas, secoes, subsecoes


def main():
    parser = argparse.ArgumentParser(description=" ".join(__doc__.split("\n\n")[0].split()))
    parser.add_argument("--quiet", action="store_true", help="não imprime o resumo sem erro")
    args = parser.parse_args()

    orfas, secoes, subsecoes = referencias_orfas()

    if not orfas:
        if not args.quiet:
            print(f"✓ toda referência §N/§N.M resolve para uma seção real "
                  f"({len(secoes)} seções, {len(subsecoes)} subseções)")
        return 0

    for caminho, n_linha, numero, linha in orfas:
        print(f"[ERRO] {caminho} linha {n_linha}: §{numero} sem seção "
              f"(heading ## N. ou ### N.M)")
    print(f"\n{len(orfas)} referência(s) órfã(s).", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
