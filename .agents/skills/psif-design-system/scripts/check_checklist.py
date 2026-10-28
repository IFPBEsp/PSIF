#!/usr/bin/env python3
"""
Automatiza a parte checável do §25 e diz, em voz alta, o que sobra manual.

A assimetria que este script existe para corrigir: §27.4 declara que, em
projeto Tailwind, o lint cobre pouco e "o checklist §25 passa a ser o
instrumento principal" — e o §25 era 100% manual. A skill instrumentava o que
declarou secundário e deixava cru o que declarou principal.

Dos 60 itens do §25, cerca de um terço é decidível por leitura estática. Este
script roda esse terço, chama os outros scripts para o que já tinham (contraste,
paleta, dominância) e **imprime a lista do que continua sendo julgamento
humano** — porque checklist parcial que se apresenta como completo é pior que
checklist nenhum.

Uso:
    python check_checklist.py tela.tsx [outro.css ...]
    python check_checklist.py "src/**/*.tsx" --tokens app/globals.css

Exit 0 = nada reprovado no que é automatizável. Exit 2 = reprovação.
"""

import argparse
import glob as globmod
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (§, descrição, regex de violação, regex que isenta, severidade)
REGRAS = [
    ("20.5", "foco visível removido sem substituto",
     r"outline\s*:\s*['\\\"]?(none|0)\b", r":focus-visible", "ERRO"),
    # Só ícone até o </button>: ícone seguido de texto visível já tem nome.
    ("20.7", "botão só com ícone sem nome acessível",
     r"(?s)<button(?![^>]*(aria-label|aria-labelledby|title=))[^>]*>\s*"
     r"(?:<svg\b(?:[^>]*/>|(?:(?!</button>).)*?</svg>)|<(?:Icon|[A-Z]\w*Icon)\b[^>]*>)"
     r"\s*</button>",
     None, "ERRO"),
    ("20.8", "tabela de dados montada com <div> em vez de <table>",
     r'(className|class)="[^"]*\b(data-?grid|table-wrap|tabela)\b[^"]*"[^>]*>\s*<div',
     r"<table", "AVISO"),
    ("20.10", "animação sem respeitar movimento reduzido",
     r"@keyframes|animation\s*:", r"prefers-reduced-motion|tokens\.css", "AVISO"),
    ("20.13", "unidade fixa em container de texto (quebra zoom 200%)",
     r"(?<!min-)(?:max-)?height\s*:\s*\d{3,}px", None, "AVISO"),
    ("24.4", "erro comunicado só por borda, sem texto",
     r"border-color\s*:\s*var\(--danger", r"(role=\"alert\"|aria-invalid|\.err\b|aria-describedby)", "AVISO"),
    ("19.2", "jargão técnico ou inglês na interface",
     r">\s*(Loading|Draft|Submit|Delete|Cancel|Save|Search|Filter|Settings)\s*<",
     None, "ERRO"),
    ("24.5", "propriedade cara animada (layout/paint)",
     r"transition\s*:\s*['\\\"]?[^;'\\\"]*\b(width|height|top|left|margin|padding)\b",
     None, "AVISO"),
    ("3.10", "z-index avulso",
     r"(z-index|zIndex)\s*:\s*['\\\"]?(?!var\()\d{4,}", None, "ERRO"),
]

# O que NÃO é decidível por leitura estática — impresso sempre.
def carrega_manuais():
    """Itens do checklist que nenhum script decide — vêm de tokens.json.

    Ficavam em código, com o texto de uma skill específica dentro do script.
    Item de checklist é
    conteúdo da skill, não lógica: em código, ele obriga um fork do script por
    skill — que é como um verificador vira cinco verificadores divergentes.

    Sem a lista, o script imprime a seção vazia e DIZ que está vazia. Fingir
    que nada é manual é a mentira que este script existe para desfazer.
    """
    with open(os.path.join(HERE, "tokens.json"), encoding="utf-8") as f:
        itens = json.load(f).get("manual_checklist", [])
    return [(str(sec), str(texto)) for sec, texto in itens]


FICA_MANUAL = carrega_manuais()


# JSX escreve `style={{ outline: 'none', zIndex: 9999 }}` — as regras acima
# aceitam as duas grafias porque metade das violações reais chega em .tsx, não
# em .css. Regra que só entende CSS puro é regra cega no projeto de verdade.
COMENTARIO = re.compile(r"/\*.*?\*/|^\s*//.*$|\{/\*.*?\*/\}", re.S | re.M)


INPUT = re.compile(r"<input\b[^>]*>", re.I)


def placeholder_sem_rotulo(texto):
    """Posição de cada <input> com placeholder e sem rótulo de verdade.

    A regra antiga isentava qualquer input com `id=`, mesmo sem um
    `<label for>` apontando para ele, e quase nunca disparava. Conta como
    rótulo: aria-label, aria-labelledby, `<label for="id">` no arquivo, ou o
    input estar dentro de um `<label>` aberto.
    """
    for m in INPUT.finditer(texto):
        tag = m.group(0)
        if "placeholder=" not in tag.lower():
            continue
        if re.search(r"aria-label(ledby)?\s*=", tag, re.I):
            continue
        ident = re.search(r"\bid\s*=\s*[\"']([^\"']+)", tag, re.I)
        if ident and re.search(r"<label\b[^>]*\b(for|htmlFor)\s*=\s*[\"']"
                               + re.escape(ident.group(1)) + r"[\"']", texto, re.I):
            continue
        antes = texto[:m.start()].lower()
        if antes.rfind("<label") > antes.rfind("</label>"):
            continue
        yield m.start()


def sem_comentarios(texto):
    return COMENTARIO.sub("", texto)


def roda(script, *args):
    r = subprocess.run([sys.executable, os.path.join(HERE, script), *args],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("arquivos", nargs="+")
    parser.add_argument("--tokens", help="CSS do projeto, para medir dominância "
                                         "e conferir os tokens colados")
    args = parser.parse_args()

    caminhos = []
    for padrao in args.arquivos:
        caminhos.extend(sorted(globmod.glob(padrao, recursive=True)) or [padrao])
    caminhos = [c for c in caminhos if os.path.isfile(c)]
    if not caminhos:
        sys.exit("nenhum arquivo encontrado")

    erros = avisos = 0
    print("── §25 automatizado")

    for caminho in caminhos:
        with open(caminho, encoding="utf-8") as f:
            bruto = f.read()
        texto = sem_comentarios(bruto)
        for sec, desc, padrao, isenta, sev in REGRAS:
            for m in re.finditer(padrao, texto, re.I):
                if isenta and re.search(isenta, texto, re.I):
                    continue
                linha = texto.count("\n", 0, m.start()) + 1
                print(f"   [{sev}] {os.path.basename(caminho)}:{linha} §{sec} — {desc}")
                if sev == "ERRO":
                    erros += 1
                else:
                    avisos += 1
        for pos in placeholder_sem_rotulo(texto):
            linha = texto.count("\n", 0, pos) + 1
            print(f"   [ERRO] {os.path.basename(caminho)}:{linha} §20.7 — "
                  "placeholder usado como único rótulo")
            erros += 1

    # Delega o que outros scripts já sabem fazer melhor.
    print("\n── delegado aos scripts existentes")
    codigo, saida = roda("lint_output.py", *caminhos)
    print(f"   lint_output.py .......... {'✗' if codigo else '✓'} "
          f"{saida.splitlines()[-1] if saida else ''}")
    erros += 1 if codigo else 0

    if args.tokens:
        codigo, saida = roda("check_dominance.py", args.tokens)
        print(f"   check_dominance.py ...... {'✗' if codigo else '✓'} (§3.3/§25.1)")
        if codigo:
            print("     " + "\n     ".join(
                l for l in saida.splitlines() if "[ERRO]" in l))
            erros += 1
        codigo, saida = roda("check_consumer.py", args.tokens, "--quiet")
        print(f"   check_consumer.py ....... {'✗' if codigo else '✓'} "
              f"{saida.splitlines()[-1] if saida else ''}")
        erros += 1 if codigo else 0
    else:
        print("   (passe --tokens <globals.css> para incluir dominância "
              "e sincronia de token)")

    if FICA_MANUAL:
        print(f"\n── continua MANUAL — {len(FICA_MANUAL)} itens que nenhum "
              f"script decide")
        for sec, item in FICA_MANUAL:
            print(f"   □ §{sec} {item}")
    else:
        print("\n── continua MANUAL — nenhum item declarado.")
        print("   Isto quase certamente está errado: nenhum checklist de "
              "qualidade é 100% automatizável. Declare `manual_checklist` em")
        print("   tokens.json — a lista existe para o script não fingir "
              "cobertura que não tem.")

    print(f"\n{erros} reprovação(ões), {avisos} aviso(s) no que é automatizável.")
    print("Isto NÃO é o §25 completo. É o terço que se decide por leitura "
          "estática; o resto está na lista acima e no "
          "ai-rules/anti-patterns-checklist.md.")
    return 2 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
