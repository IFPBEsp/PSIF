#!/usr/bin/env python3
"""
Gera assets/tokens.css a partir de scripts/tokens.json.

Uso:
    python gen_tokens_css.py            # escreve ../assets/tokens.css
    python gen_tokens_css.py --check    # só confere, sem escrever

Saída: 0 escreveu ou está em dia; 2 tokens.css defasado (--check); 1 fonte inválida.
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOKENS_PATH = os.path.join(HERE, "tokens.json")
CSS_PATH = os.path.normpath(os.path.join(HERE, "..", "assets", "tokens.css"))


def _prosa(chave, padrao_arquivo, padrao_secao=None):
    """(caminho, seção) de prosa_sources: string com o arquivo ou {"file", "section"}."""
    bruto = TOKENS.get("prose_sources", {}).get(chave, padrao_arquivo)
    if isinstance(bruto, dict):
        arquivo = bruto.get("file", padrao_arquivo)
        secao = bruto.get("section", padrao_secao)
    else:
        arquivo, secao = bruto, padrao_secao
    return os.path.normpath(os.path.join(HERE, "..", arquivo)), secao


with open(TOKENS_PATH, encoding="utf-8") as _f:
    TOKENS = json.load(_f)

sys.path.insert(0, HERE)
from skill_config import config as _config  # noqa: E402

TITULO = _config().titulo

MOTION_MD, MOTION_SECAO = _prosa("motion", "tokens/motion-icons.md",
                                 "17.5 Motion reduction")
A11Y_MD, _ = _prosa("accessibility", "foundations/accessibility.md")

_FOCO = TOKENS.get("focus_ring", {})
FOCUS_OUTLINE_PX = _FOCO.get("width", "2.5px")
FOCUS_OUTLINE_TOKEN = _FOCO.get("token", "")
FOCUS_OFFSET_PX = _FOCO.get("offset", "2px")

if not FOCUS_OUTLINE_TOKEN:
    sys.exit('[ERRO] tokens.json sem focus_ring.token '
             '({"token": "navy-700", "width": "2px", "offset": "2px"}, §20.5)')


def read_md(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def extract_block(md, section, needle):
    """Bloco ```css``` da seção, copiado sem mudança."""
    corpo = re.split(r"\n#{2,4} ", md)
    for parte in corpo:
        if parte.startswith(section):
            m = re.search(r"```css\n(.*?)```", parte, re.S)
            if m and needle in m.group(1):
                return m.group(1).strip()
    sys.exit(f"[ERRO] bloco css com '{needle}' não encontrado "
             f"(um bloco ```css``` na seção, §{section.split()[0]})")


def assert_in_md(md, *trechos):
    faltando = [t for t in trechos if t not in md]
    if faltando:
        sys.exit("[ERRO] accessibility.md sem " + ", ".join(repr(t) for t in faltando)
                 + " (os valores de focus_ring do tokens.json, §20.5)")


def header():
    linhas = [f"/* {TITULO}: tokens. Gerado de scripts/tokens.json por "
              "gen_tokens_css.py; não edite.",
              " * Consuma por var(--token)."]
    banidos = TOKENS.get("text_color_banlist", [])
    if banidos:
        linhas.append(" * Nunca como cor de texto: "
                      + ", ".join(f"--{n}" for n in banidos) + " (§3.2).")
    linhas.append(" */")
    return "\n".join(linhas)


# Título e § de cada grupo podem vir de tokens.json["groups"].
GROUPS_PADRAO = [
    ("color", "Cor — paleta canônica"),
    ("shadow", "Elevação e sombra"),
    ("blur", "Blur"),
    ("glass", "Glass — só em chrome sobreposto"),
    ("overlay", "Scrim de modal e drawer"),
    ("line", "Linhas sobre o céu"),
    ("opacity", "Opacidade"),
    ("radius", "Raio — filho sempre com raio menor ou igual ao do pai"),
    ("spacing", "Espaçamento"),
    ("component_padding", "Padding canônico de componente"),
    ("icon_size", "Tamanho de ícone"),
    ("touch_target", "Alvo de toque — mínimo de todo clicável; botão e campo têm o seu"),
    ("avatar", "Avatar — cartão de aluno e perfil"),
    ("zindex", "Z-index — cada camada tem seu valor nominal, nunca 9999 avulso"),
    ("surface", "Superfície"),
    ("dark", "Superfícies do modo escuro"),
    ("width", "Larguras: conteúdo, barra lateral, coluna lateral, diálogo e login"),
    ("breakpoint", "Breakpoints — da tela estreita para a larga, por min-width"),
]

TYPO_GROUPS_PADRAO = [
    ("font_family", "Família"),
    ("font_size", "Escala tipográfica"),
    ("line_height", "Altura de linha"),
]


def _rotula(padroes):
    overrides = TOKENS.get("groups", {})
    saida = []
    for chave, titulo in padroes:
        o = overrides.get(chave, {})
        saida.append((chave, o.get("title", titulo), o.get("section", "")))
    return saida


GROUPS = _rotula(GROUPS_PADRAO)
TYPO_GROUPS = _rotula(TYPO_GROUPS_PADRAO)


def _secao(chave):
    return TOKENS.get("groups", {}).get(chave, {}).get("section", "")


def _ref(chave):
    s = _secao(chave)
    return f" ({s})" if s else ""


def block(title, section, pairs):
    rotulo = f"{title} — {section}" if section else title
    out = [f"\n  /* {rotulo} */"]
    out += [f"  --{name}: {value};" for name, value in pairs]
    return out


def color_pairs(colors):
    """Família em alias_families sai como var() da gêmea quando o hex é o mesmo."""
    aliases = TOKENS.get("alias_families", {})
    pairs = []
    for name, value in colors.items():
        familia = name.split("-", 1)[0]
        alvo = aliases.get(familia)
        if alvo and "-" in name:
            gemeo = f"{alvo}-{name.split('-', 1)[1]}"
            if colors.get(gemeo) == value:
                value = f"var(--{gemeo})"
        pairs.append((name, value))
    return pairs


def superficies_do_navegador(tokens):
    sup = tokens.get("browser_surfaces")
    if not sup:
        return []
    conhecidos = set(tokens.get("color", {})) | set(
        (tokens.get("typography") or {}).get("font_size", {}))
    faltando = [v for v in sup.values() if v not in conhecidos]
    if faltando:
        sys.exit(f"[ERRO] browser_surfaces aponta para token inexistente: {faltando} "
                 "(token de color ou font_size, §2.4)")
    return [
        f"/* Superfícies do navegador{_ref('browser')} */",
        f"::selection {{ background: var(--{sup['selection_bg']}); "
        f"color: var(--{sup['selection_text']}); }}",
        f":root {{ accent-color: var(--{sup['accent']}); }}",
        f"input, textarea {{ caret-color: var(--{sup['accent']}); }}",
        "a { text-underline-offset: .2em; }",
        "time, data, td { font-variant-numeric: tabular-nums; }",
        f"input, select, textarea {{ font-size: var(--{sup['field_font']}); }}",
        "",
    ]


def bloco_escuro(tokens):
    """Bloco .dark: cada --dark-X substitui --X."""
    escuro = tokens.get("dark")
    if not escuro:
        return []
    cores = tokens.get("color", {})
    pares = (set(cores) | set(tokens.get("overlay", {})) | set(tokens.get("shadow", {}))
             | set(tokens.get("line", {})))
    orfaos = [n for n in escuro if n.removeprefix("dark-") not in pares]
    if orfaos:
        sys.exit(f"[ERRO] grupo dark com token sem par: {orfaos} "
                 "(par em color, overlay, shadow ou line, §25)")
    faltando = [n for n in cores if f"dark-{n}" not in escuro]
    if faltando:
        sys.exit(f"[ERRO] grupo dark sem o par escuro de: {faltando} (um dark-X por cor, §25)")
    return [
        f"/* Modo escuro{_ref('dark')}: .dark no <html> */",
        ":root.dark {",
        "  color-scheme: dark;",
        *[f"  --{n.removeprefix('dark-')}: var(--{n});" for n in escuro],
        "}",
        "",
    ]


def render(tokens):
    motion_block = extract_block(
        read_md(MOTION_MD), MOTION_SECAO, "prefers-reduced-motion"
    )
    assert_in_md(
        read_md(A11Y_MD),
        FOCUS_OUTLINE_PX, FOCUS_OUTLINE_TOKEN, f"offset {FOCUS_OFFSET_PX}",
    )
    lines = [header(), "", ":root {"]

    ausentes = tokens.get("absent_groups", {})
    for key, title, section in GROUPS:
        group = tokens.get(key)
        if not group:
            if key in ausentes:
                continue
            sys.exit(f"[ERRO] tokens.json sem o grupo '{key}' "
                     f"(o grupo, ou absent_groups.{key} com o motivo)")
        pairs = color_pairs(group) if key == "color" else group.items()
        lines += block(title, section, pairs)

    typo = tokens.get("typography") or {}
    for key, title, section in TYPO_GROUPS:
        group = typo.get(key)
        if not group:
            sys.exit(f"[ERRO] tokens.json sem typography.{key} (o grupo, §4)")
        lines += block(title, section, group.items())

    motion = tokens.get("motion") or {}
    for key, title in (("duration", "Duração"), ("easing", "Easing")):
        group = motion.get(key)
        if not group:
            sys.exit(f"[ERRO] tokens.json sem motion.{key} (o grupo, §3.9)")
        lines += block(f"Motion — {title}", _secao("motion"), group.items())

    lines += [
        "}",
        "",
        *bloco_escuro(tokens),
        "/* Regras de elemento em @layer base: a utilitária da tela vence. */",
        "@layer base {",
        "",
        "body {",
        "  margin: 0;",
        "  font-family: var(--font-sans);",
        "  font-size: var(--fs-body);",
        "  line-height: var(--lh-normal);",
        "  color: var(--ink-900);",
        "  background: var(--surface-base);",
        "  -webkit-font-smoothing: antialiased;",
        "}",
        "",
        f"/* Foco visível{_ref('focus')} */",
        ":where(a, button, input, select, textarea, [tabindex]):focus-visible {",
        f"  outline: {FOCUS_OUTLINE_PX} solid var(--{FOCUS_OUTLINE_TOKEN});",
        f"  outline-offset: {FOCUS_OFFSET_PX};",
        "}",
        "",
        *superficies_do_navegador(tokens),
        f"/* Movimento reduzido (§{MOTION_SECAO.split()[0]}) */",
        motion_block,
        "",
        "}",
    ]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=" ".join(__doc__.split("\n\n")[0].split()))
    parser.add_argument(
        "--check",
        action="store_true",
        help="não escreve; saída 2 se assets/tokens.css estiver defasado",
    )
    args = parser.parse_args()

    with open(TOKENS_PATH, encoding="utf-8") as f:
        css = render(json.load(f))

    current = None
    if os.path.exists(CSS_PATH):
        with open(CSS_PATH, encoding="utf-8") as f:
            current = f.read()

    if args.check:
        if current == css:
            print("✓ assets/tokens.css está em sincronia com scripts/tokens.json.")
            return 0
        print("✗ assets/tokens.css está defasado de scripts/tokens.json. "
              "Rode: python scripts/gen_tokens_css.py", file=sys.stderr)
        return 2

    if current == css:
        print("assets/tokens.css já estava atualizado.")
        return 0

    os.makedirs(os.path.dirname(CSS_PATH), exist_ok=True)
    with open(CSS_PATH, "w", encoding="utf-8") as f:
        f.write(css)
    n = sum(1 for line in css.splitlines() if line.strip().startswith("--"))
    print(f"assets/tokens.css escrito — {n} tokens, {len(css.splitlines())} linhas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
