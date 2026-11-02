#!/usr/bin/env python3
"""
Confere a parte automática do checklist de §24 e imprime os itens manuais.

Uso:
    python check_checklist.py tela.tsx [outro.css ...]
    python check_checklist.py "src/**/*.tsx" --tokens src/app/globals.css

Entradas: arquivos ou globs de tela; --tokens com o CSS do projeto inclui
check_dominance.py e check_consumer.py.
Saída: 0 sem reprovação; 2 com reprovação.
"""

import argparse
import glob as globmod
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

INGLES = (r"\b(?-i:Loading|Draft|Submit|Delete|Cancel|Save|Search|Filter|Settings"
          r"|Status|Dashboard|Upload|Download)\b")

# (§, o que, esperado, regex da violação, regex que isenta o arquivo, severidade)
REGRAS = [
    # Isenta só o arquivo que desenha o anel: bloco :focus-visible com outline ou box-shadow.
    ("20.5", "foco visível removido", "anel em :focus-visible",
     r"outline\s*:\s*['\\\"]?(none|0)\b",
     r":focus-visible[^{]*\{[^}]*(?:outline\s*:(?!\s*['\"]?(?:none|0)\b)|box-shadow\s*:)|focus-within",
     "ERRO"),
    # Ícone seguido de texto visível já tem nome; só reprova ícone sozinho até o fechamento.
    # Componente que fecha em si (<Search />, <Icon name=… />) dentro do botão é ícone.
    ("20.7", "botão ou link só de ícone sem nome acessível", "aria-label",
     r"(?s)<(button|Button|a|Link)\b(?![^>]*(?:aria-label|aria-labelledby|title=))[^>]*>\s*"
     r"(?:<svg\b(?:[^>]*/>|(?:(?!</\1>).)*?</svg>)|<[A-Z]\w*\b[^>]*/>)"
     r"\s*</\1>",
     None, "ERRO"),
    ("20.8", "tabela montada com <div>", "<table>",
     r'(className|class)="[^"]*\b(data-?grid|table-wrap|tabela)\b[^"]*"[^>]*>\s*<div',
     r"<table", "AVISO"),
    ("17.5", "animação sem movimento reduzido", "prefers-reduced-motion ou tokens.css",
     r"@keyframes|animation\s*:", r"prefers-reduced-motion|tokens\.css", "AVISO"),
    ("20.13", "altura fixa em contêiner de texto", "min-height",
     r"(?<![\w-])(?:max-?)?height\s*:\s*['\"]?\d{3,}(?:px)?\b", None, "AVISO"),
    ("10.7", "erro só na borda", "mensagem em texto ligada por aria-describedby",
     r"border-color\s*:\s*var\(--danger|\bborder-(?:destructive|danger-\d{3}|\(--danger[\w-]*\))(?![\w-])",
     r"(role=\"alert\"|aria-invalid|\.err\b|aria-describedby)", "AVISO"),
    # Texto entre tags e atributo que a pessoa lê ou ouve.
    ("19.2", "termo em inglês na tela", "português",
     r"(?<![=-])>[^<{}]*" + INGLES + r"[^<{}]*<"
     r"|\b(?:placeholder|aria-label|title|alt)=[\"'][^\"']*" + INGLES,
     None, "ERRO"),
    ("17.4", "propriedade de layout animada", "opacity, transform ou cor",
     r"transition\s*:\s*['\\\"]?[^;'\\\"]*\b(width|height|top|left|margin|padding)\b",
     None, "AVISO"),
    ("3.10", "z-index avulso", "var(--z-*)",
     r"(z-index|zIndex)\s*:\s*['\\\"]?(?!var\()\d{4,}", None, "ERRO"),
]

COMENTARIO = re.compile(r"/\*.*?\*/|^\s*//.*$|\{/\*.*?\*/\}", re.S | re.M)
CAMPO = re.compile(r"<(?:input|Input|textarea|Textarea)\b[^>]*>")
SEM_ROTULO = re.compile(r"\btype\s*=\s*[\"'](?:hidden|submit|button|reset|image)[\"']", re.I)
ICONE_SO = r"(?:\s*<(?:svg\b.*?</svg>|(?:[A-Z]\w*Icon|Icone|Icon)\b[^>]*/>)\s*)*"
SELO = re.compile(r"<Badge\b[^>]*/>|<Badge\b[^>]*>" + ICONE_SO + r"</Badge>", re.S)
ITEM_MANUAL = re.compile(r"^- \[ \] (.+) \(§([\d.]+)\) · manual$")


def itens_manuais():
    with open(os.path.join(HERE, "tokens.json"), encoding="utf-8") as f:
        fonte = json.load(f).get("prose_sources", {}).get(
            "checklist", "ai-rules/anti-patterns-checklist.md")
    caminho = os.path.normpath(os.path.join(HERE, "..", fonte))
    if not os.path.isfile(caminho):
        return []
    with open(caminho, encoding="utf-8") as f:
        linhas = f.read().splitlines()
    return [(m.group(2), m.group(1)) for m in map(ITEM_MANUAL.match, linhas) if m]


def tem_rotulo(texto, m):
    """aria-label(ledby), <label for="id"> no arquivo (Label, FieldLabel), <label> envolvendo
    ou FormControl do shadcn, que liga o FormLabel por contexto."""
    tag = m.group(0)
    if re.search(r"aria-label(ledby)?\s*=", tag, re.I):
        return True
    ident = re.search(r"\bid\s*=\s*[\"']([^\"']+)", tag, re.I)
    if ident and re.search(r"<(?:\w*Label|label)\b[^>]*\b(for|htmlFor)\s*=\s*[\"']"
                           + re.escape(ident.group(1)) + r"[\"']", texto, re.I):
        return True
    antes = texto[:m.start()].lower()
    return any(antes.rfind(f"<{t}") > antes.rfind(f"</{t}>") for t in ("label", "formcontrol"))


def placeholder_sem_rotulo(texto):
    for m in CAMPO.finditer(texto):
        if "placeholder=" in m.group(0).lower() and not tem_rotulo(texto, m):
            yield m.start()


def campo_sem_rotulo(texto):
    for m in CAMPO.finditer(texto):
        tag = m.group(0)
        if "placeholder=" in tag.lower() or SEM_ROTULO.search(tag):
            continue
        if not tem_rotulo(texto, m):
            yield m.start()


def selo_sem_texto(texto):
    for m in SELO.finditer(texto):
        yield m.start()


def filtro_sem_estado(texto):
    """Botão dentro de grupo com aria-label "Filtro…". ToggleGroupItem passa: o Radix põe o estado."""
    for g in re.finditer(r"<(\w+)\b[^>]*aria-label=[\"']Filtro[^\"']*[\"'][^>]*>", texto):
        fim = texto.find(f"</{g.group(1)}>", g.end())
        bloco = texto[g.end():fim if fim != -1 else len(texto)]
        for b in re.finditer(r"<(?:button|Button)\b([^>]*)>", bloco):
            if not re.search(r"aria-(?:pressed|checked|haspopup)\b", b.group(1)):
                yield g.end() + b.start()


VERIFICACOES = [
    (selo_sem_texto, "12.2", "selo sem texto", "texto dentro do Badge"),
    (filtro_sem_estado, "7.6", "filtro sem estado", "aria-pressed, role=radio ou aria-haspopup"),
    (placeholder_sem_rotulo, "20.7", "placeholder como único rótulo", "<label> visível"),
    (campo_sem_rotulo, "20.7", "campo sem rótulo", "<label> visível ligado por htmlFor"),
]


def roda(script, *args):
    r = subprocess.run([sys.executable, os.path.join(HERE, script), *args],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def achados(texto):
    for sec, oque, esperado, padrao, isenta, sev in REGRAS:
        if isenta and re.search(isenta, texto, re.I):
            continue
        for m in re.finditer(padrao, texto, re.I):
            yield m.start(), sev, oque, esperado, sec
    for verifica, sec, oque, esperado in VERIFICACOES:
        for pos in verifica(texto):
            yield pos, "ERRO", oque, esperado, sec


def main():
    parser = argparse.ArgumentParser(description=" ".join(__doc__.split("\n\n")[0].split()))
    parser.add_argument("arquivos", nargs="+")
    parser.add_argument("--tokens", help="CSS do projeto")
    args = parser.parse_args()

    caminhos = []
    for padrao in args.arquivos:
        caminhos.extend(sorted(globmod.glob(padrao, recursive=True)) or [padrao])
    caminhos = [c for c in caminhos if os.path.isfile(c)]
    if not caminhos:
        sys.exit("nenhum arquivo encontrado")

    erros = avisos = 0
    for caminho in caminhos:
        with open(caminho, encoding="utf-8") as f:
            texto = COMENTARIO.sub("", f.read())
        lista = sorted(achados(texto))
        if not lista:
            continue
        print(f"── {os.path.basename(caminho)}")
        for pos, sev, oque, esperado, sec in lista:
            linha = texto.count("\n", 0, pos) + 1
            print(f"   [{sev}] linha {linha}: {oque} ({esperado}, §{sec})")
            if sev == "ERRO":
                erros += 1
            else:
                avisos += 1

    print("\n── outros verificadores")
    codigo, saida = roda("lint_output.py", *caminhos)
    print(f"   lint_output.py .......... {'✗' if codigo else '✓'} "
          f"{saida.splitlines()[-1] if saida else ''}")
    for linha in saida.splitlines():
        if linha.lstrip().startswith(("── ", "[ERRO]", "[AVISO]")):
            print("     " + linha.strip())
    resumo = re.search(r"(\d+) erro\(s\), (\d+) aviso\(s\)\.\s*$", saida)
    if resumo:
        erros += int(resumo.group(1))
        avisos += int(resumo.group(2))
    elif codigo:
        erros += 1

    if args.tokens:
        codigo, saida = roda("check_dominance.py", args.tokens)
        print(f"   check_dominance.py ...... {'✗' if codigo else '✓'}")
        if codigo:
            print("     " + "\n     ".join(l for l in saida.splitlines() if "[ERRO]" in l))
            erros += 1
        codigo, saida = roda("check_consumer.py", args.tokens, "--quiet")
        print(f"   check_consumer.py ....... {'✗' if codigo else '✓'} "
              f"{saida.splitlines()[-1] if saida else ''}")
        erros += 1 if codigo else 0
    else:
        print("   (passe --tokens <globals.css> para incluir dominância e sincronia de token)")

    manuais = itens_manuais()
    print(f"\n── manual ({len(manuais)} itens)")
    for sec, item in manuais:
        print(f"   □ {item} (§{sec})")

    print(f"\n{erros} reprovação(ões), {avisos} aviso(s). "
          "Os itens manuais completam o checklist de §24.")
    return 2 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
