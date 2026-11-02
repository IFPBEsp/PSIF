#!/usr/bin/env python3
"""
Confere cor, raio, espaçamento, sombra, z-index, fonte, alvo e nome de token numa tela.

Uso:
    python lint_output.py tela.html [Componente.tsx estilos.css ...]
    cat tela.html | python lint_output.py -
    python lint_output.py tela.html --strict

Entradas: arquivos HTML, CSS, JSX ou TSX, ou - para ler da entrada padrão;
--strict faz [AVISO] contar como reprovação. Classes do Tailwind (no atributo
e em cn, cva, clsx, twMerge e tv) passam pelas mesmas regras do CSS.
Saída: 0 limpo; 2 com [ERRO] (ou [AVISO], com --strict); 1 arquivo ausente.
"""

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

TOKENS_PATH = Path(__file__).parent / "tokens.json"

# Só dentro destas propriedades uma palavra como "red" conta como cor.
COLOR_PROPS = {
    "color", "background", "background-color", "background-image", "border",
    "border-color", "border-top", "border-right", "border-bottom", "border-left",
    "border-top-color", "border-right-color", "border-bottom-color",
    "border-left-color", "border-inline-color", "border-block-color",
    "outline", "outline-color", "fill", "stroke", "box-shadow", "text-shadow",
    "caret-color", "accent-color", "text-decoration-color", "column-rule-color",
    "-webkit-text-fill-color", "text-emphasis-color",
}

RADIUS_PROPS = {
    "border-radius", "border-top-left-radius", "border-top-right-radius",
    "border-bottom-left-radius", "border-bottom-right-radius",
    "border-start-start-radius", "border-start-end-radius",
    "border-end-start-radius", "border-end-end-radius",
}

SPACING_PROPS = {
    "padding", "padding-top", "padding-right", "padding-bottom", "padding-left",
    "padding-inline", "padding-block", "padding-inline-start",
    "padding-inline-end", "padding-block-start", "padding-block-end",
    "margin", "margin-top", "margin-right", "margin-bottom", "margin-left",
    "margin-inline", "margin-block", "margin-inline-start", "margin-inline-end",
    "margin-block-start", "margin-block-end",
    "gap", "row-gap", "column-gap", "grid-gap", "grid-row-gap",
    "grid-column-gap",
}

SIZE_PROPS = {"height", "min-height", "width", "min-width", "block-size", "inline-size"}

INTERACTIVE_HINT = re.compile(
    r"\b(btn|button|icon-btn|fab|tab|chip|input|textarea|select|link|anchor|"
    r"nav-item|nav-link|menu-item|option|checkbox|radio|switch|toggle|stepper-dot|"
    r"close|dismiss|action|pagination|page-link|sort|filter-chip)\b",
    re.IGNORECASE,
)

NAMED_COLORS = {
    "red", "blue", "green", "black", "gray", "grey", "orange", "yellow",
    "purple", "pink", "brown", "cyan", "magenta", "lime", "navy", "teal",
    "olive", "maroon", "silver", "gold", "coral", "salmon", "khaki", "indigo",
    "violet", "crimson", "tomato", "orangered", "dodgerblue", "steelblue",
    "lightblue", "darkblue", "lightgray", "lightgrey", "darkgray", "darkgrey",
    "whitesmoke", "ghostwhite", "aliceblue", "beige", "ivory", "snow", "azure",
    "linen", "wheat", "plum", "orchid", "turquoise", "aqua", "fuchsia",
    "chartreuse", "seagreen", "forestgreen", "darkgreen", "midnightblue",
    "slategray", "slategrey", "gainsboro", "hotpink", "deeppink", "skyblue",
    "powderblue", "lavender", "thistle", "tan", "sienna", "chocolate", "peru",
    "firebrick", "darkred", "rebeccapurple", "goldenrod", "seashell",
}

def font_families(tokens):
    """Primeira família de cada pilha de typography.font_family."""
    familias = set()
    for pilha in tokens.get("typography", {}).get("font_family", {}).values():
        pilha = re.sub(r"var\(\s*--[\w-]+\s*,\s*([^)]*)\)", r"\1", str(pilha))
        primeira = pilha.split(",")[0].strip().strip("'\"").lower()
        if primeira:
            familias.add(primeira)
    return familias


def color_families(tokens):
    """navy-700 -> navy; white -> white."""
    familias = set()
    for nome in tokens.get("color", {}):
        familias.add(nome.rsplit("-", 1)[0] if "-" in nome else nome)
    return familias

DECL_RE = re.compile(r"(?<![\w-])(-{0,2}[a-zA-Z][a-zA-Z0-9-]*)\s*:\s*([^;{}\n]*)")
HEX_RE = re.compile(r"#([0-9A-Fa-f]{3,8})\b")
FUNC_COLOR_RE = re.compile(r"\b(rgba?|hsla?)\(([^()]*)\)", re.IGNORECASE)
CLASS_ATTR_RE = re.compile(
    r"""(?:class|className)\s*=\s*(?:"([^"]*)"|'([^']*)'|\{\s*[`"']([^`"']*)[`"']\s*\})"""
)
UTILITY_HINT = re.compile(
    r"^(flex|grid|block|inline|hidden|absolute|relative|fixed|sticky|"
    r"w-|h-|p[xytrbl]?-|m[xytrbl]?-|text-|bg-|border|rounded|shadow|gap-|"
    r"items-|justify-|self-|font-|leading-|tracking-|space-[xy]-|z-|"
    r"overflow-|max-|min-|ring|opacity-|truncate|divide)"
)
COLOR_UTILS = "text|bg|border|ring|fill|stroke|outline|from|to|via|divide|decoration|caret|accent"
UTILITY_COLOR_RE = re.compile(rf"^({COLOR_UTILS})-([a-z]+)-(\d{{2,3}})$")
UTILITY_KEYWORD_RE = re.compile(rf"^({COLOR_UTILS})-([a-z]+)$")
UTILITY_DARK_TOKEN_RE = re.compile(rf"^({COLOR_UTILS})-(?:\(--)?dark-")
ARBITRARY_RE = re.compile(r"^([a-z-]+)-\[([^\]]+)\]$")
LENGTH_RE = re.compile(r"^(-?\d*\.?\d+)(px|rem)$")
LITERAL_COLOR_RE = re.compile(r"^(#[0-9A-Fa-f]{3,8}|(?:rgba?|hsla?)\([^()]*\))$", re.I)
UTILITY_VAR_RE = re.compile(rf"^({COLOR_UTILS})-(?:\((--[\w-]+)\)|\[var\((--[\w-]+)\)\])$")
OPACITY_SUFFIX_RE = re.compile(rf"^((?:{COLOR_UTILS})-.+?)/(?:\d{{1,3}}|\[[^\]]+\])$")
Z_UTILITY_RE = re.compile(r"^-?z-(\d+)$")
SIZE_UTILITY_RE = re.compile(r"^(size|h|min-h|w|min-w)-(?:(\d+(?:\.5)?)|\[(\d*\.?\d+)px\])$")
CLASS_HELPER_RE = re.compile(r"\b(?:cn|cva|clsx|twMerge|tv)\s*\(")
STRING_LIT_RE = re.compile(r'"([^"\\\n]*)"|\'([^\'\\\n]*)\'|`([^`$]*)`')
LUCIDE_IMPORT_RE = re.compile(r"import\s*\{([^}]*)\}\s*from\s*[\"']lucide-react[\"']")
LUCIDE_NS_RE = re.compile(r"import\s*\*\s*as\s+(\w+)\s+from\s*[\"']lucide-react[\"']")
WHITE_FIXO_RE = re.compile(r"#fff(?:fff)?\b|\bwhite\b|rgba?\(\s*255[\s,]+255[\s,]+255\s*[,/)]", re.I)
INTERACTIVE_COMPONENTS = {"Button", "Link", "NavLink", "TabsTrigger", "ToggleGroupItem",
                          "SelectTrigger", "DropdownMenuTrigger", "DropdownMenuItem"}
PX_RE = re.compile(r"(-?\d*\.?\d+)px\b")

# Grupos do tokens.json que guardam valores ou exceções, não nomes de token.
NON_TOKEN_GROUPS = {
    "gradient_literals", "translucent_literals", "named_colors_allowed",
    "text_color_banlist", "icon_color_allowed", "browser_surfaces",
    "spacing_exceptions", "wcag_minimum", "touch_target_min_px", "absent_groups",
    "brand_only",
}

def eh_icone(texto, inicio, fim, importados=frozenset()):
    """A tag é ícone: <svg>, componente *Icon/*Icone, importado do lucide-react ou aria-hidden."""
    abre = texto.rfind("<", 0, inicio)
    fecha = texto.find(">", fim)
    if abre == -1:
        return False
    tag = texto[abre:fecha + 1 if fecha != -1 else fim]
    nome = re.match(r"<\s*([\w.]+)", tag)
    nome = nome.group(1) if nome else ""
    return (nome.lower() in SVG_TAGS or bool(re.search(r"(?:Icon|Icone)$", nome))
            or eh_importado(nome, importados) or bool(re.search(r"\baria-hidden\b", tag)))


def eh_importado(nome, importados):
    return nome in importados or nome.split(".")[0] + "." in importados


def icones_importados(texto):
    """Nomes locais dos ícones importados de lucide-react; namespace termina em '.'."""
    nomes = set()
    for m in LUCIDE_IMPORT_RE.finditer(texto):
        for item in m.group(1).split(","):
            partes = item.split(" as ")
            if partes[-1].strip():
                nomes.add(partes[-1].strip())
    nomes |= {m.group(1) + "." for m in LUCIDE_NS_RE.finditer(texto)}
    return frozenset(nomes)


def fim_da_chamada(texto, abre):
    """Posição do ')' que fecha o '(' em `abre`, pulando strings."""
    nivel, i = 0, abre
    while i < len(texto):
        c = texto[i]
        if c in "\"'`":
            fecha = texto.find(c, i + 1)
            i = fecha if fecha != -1 else len(texto)
        elif c == "(":
            nivel += 1
        elif c == ")":
            nivel -= 1
            if nivel == 0:
                return i
        i += 1
    return len(texto)


def grupos_de_classe(texto):
    """[(início, [(posição, classes), ...])] de cada class/className literal e de cada cn/cva/clsx/twMerge/tv."""
    grupos = []
    for m in CLASS_ATTR_RE.finditer(texto):
        g = next(i for i in (1, 2, 3) if m.group(i) is not None)
        grupos.append((m.start(), [(m.start(g), m.group(g))]))
    for m in CLASS_HELPER_RE.finditer(texto):
        fim = fim_da_chamada(texto, m.end() - 1)
        trecho = []
        for lit in STRING_LIT_RE.finditer(texto, m.end(), fim):
            g = next(i for i in (1, 2, 3) if lit.group(i) is not None)
            trecho.append((lit.start(g), lit.group(g)))
        if trecho:
            grupos.append((m.start(), trecho))
    return grupos


def apaga_classes(texto):
    """Troca o conteúdo das classes por espaços: 'md:p-4' não vira declaração CSS."""
    chars = list(texto)
    for _, trechos in grupos_de_classe(texto):
        for pos, conteudo in trechos:
            for i in range(pos, pos + len(conteudo)):
                if chars[i] != "\n":
                    chars[i] = " "
    return "".join(chars)


def tag_em_volta(texto, pos):
    """(nome, texto da tag) se `pos` está dentro de uma tag aberta; senão None. Ignora '=>'."""
    lt = texto.rfind("<", 0, pos)
    if lt == -1 or not re.match(r"<\s*[A-Za-z]", texto[lt:lt + 3]):
        return None
    if re.search(r"(?<!=)>", texto[lt:pos]):
        return None
    fim = re.compile(r"(?<!=)>").search(texto, pos)
    tag = texto[lt:fim.end() if fim else len(texto)]
    nome = re.match(r"<\s*([A-Za-z][\w.]*)", tag).group(1)
    return nome, tag


SVG_TAGS = {"svg", "path", "circle", "rect", "line", "polyline", "polygon",
            "ellipse", "g", "use"}
ICON_CLASS_RE = re.compile(
    r"(?:^|[-_])(?:icon|icons|ico|chevron)$|^material-(?:symbols|icons)",
    re.IGNORECASE,
)

VAR_USE_RE = re.compile(r"var\(\s*--([\w-]+)")


def load_tokens():
    with open(TOKENS_PATH, encoding="utf-8") as f:
        return json.load(f)


def find_line(text, pos):
    return text.count("\n", 0, pos) + 1


def expand_hex(digits):
    """Normaliza hex de 3/4/6/8 dígitos para (#rrggbb, tem_alpha)."""
    d = digits.lower()
    if len(d) in (3, 4):
        rgb = "".join(c * 2 for c in d[:3])
        return f"#{rgb}", len(d) == 4
    if len(d) in (6, 8):
        return f"#{d[:6]}", len(d) == 8
    return None, False


def hex_to_triple(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def hsl_to_triple(h, s, l):
    """h em graus, s e l em 0..1. Retorna (r, g, b) 0..255."""
    c = (1 - abs(2 * l - 1)) * s
    hp = (h % 360) / 60.0
    x = c * (1 - abs(hp % 2 - 1))
    if hp < 1:
        rgb = (c, x, 0)
    elif hp < 2:
        rgb = (x, c, 0)
    elif hp < 3:
        rgb = (0, c, x)
    elif hp < 4:
        rgb = (0, x, c)
    elif hp < 5:
        rgb = (x, 0, c)
    else:
        rgb = (c, 0, x)
    m = l - c / 2
    return tuple(round((v + m) * 255) for v in rgb)


def parse_func_color(kind, inner):
    """Devolve (triple, alpha_explicito) ou (None, False) se não der para resolver."""
    parts = [p.strip() for p in re.split(r"[,/\s]+", inner.strip()) if p.strip()]
    if len(parts) < 3 or any("var(" in p or "calc(" in p for p in parts):
        return None, False
    has_alpha = len(parts) >= 4
    try:
        if kind.lower().startswith("rgb"):
            vals = []
            for p in parts[:3]:
                if p.endswith("%"):
                    vals.append(round(float(p[:-1]) * 255 / 100))
                else:
                    vals.append(int(round(float(p))))
            return tuple(vals), has_alpha
        hue = float(re.sub(r"(deg|grad|rad|turn)$", "", parts[0]))
        sat = float(parts[1].rstrip("%")) / 100.0
        lig = float(parts[2].rstrip("%")) / 100.0
        return hsl_to_triple(hue, sat, lig), has_alpha
    except ValueError:
        return None, False


def kebab(prop):
    """borderColor -> border-color; COLOR -> color; --x fica igual."""
    if prop.startswith("--"):
        return prop
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", prop).lower()


def clean_value(raw):
    """Tira aspas de valor de style JSX e lixo de fim de declaração."""
    v = raw.strip().rstrip(",").strip()
    if v[:1] in ("'", '"'):
        quote = v[0]
        end = v.find(quote, 1)
        return v[1:end] if end > 0 else v[1:]
    for quote in ("'", '"'):
        if quote in v:
            v = v.split(quote, 1)[0].strip()
    return v


def nearest_selector(text, pos):
    """Texto do seletor do bloco onde `pos` está. Vazio em style inline."""
    open_brace = text.rfind("{", 0, pos)
    if open_brace == -1:
        return ""
    start = max(
        text.rfind("}", 0, open_brace),
        text.rfind("{", 0, open_brace),
        text.rfind(";", 0, open_brace),
        text.rfind(">", 0, open_brace),
    )
    return text[start + 1 : open_brace].strip()


HEX_PURO = re.compile(r"^#[0-9a-fA-F]{3,8}$")


def colher_paleta(tokens):
    """Todo token com valor hex, de qualquer grupo do tokens.json."""
    paleta = {}

    def colhe(no):
        for chave, valor in no.items():
            if isinstance(valor, dict):
                colhe(valor)
            elif isinstance(valor, str) and HEX_PURO.match(valor.strip()):
                paleta[chave] = valor.strip().lower()

    for grupo, conteudo in tokens.items():
        if grupo in NON_TOKEN_GROUPS or not isinstance(conteudo, dict):
            continue
        colhe(conteudo)
    return paleta


def collect_token_names(node, out=None):
    if out is None:
        out = set()
    if not isinstance(node, dict):
        return out
    for key, value in node.items():
        if key.startswith("_") or key in NON_TOKEN_GROUPS:
            continue
        if isinstance(value, dict):
            collect_token_names(value, out)
        else:
            out.add(key)
    return out


def blank_comments(text):
    """Troca comentário CSS e HTML por espaços, mantendo posição e número de linha."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))

    return re.sub(r"/\*.*?\*/|<!--.*?-->", blank, text, flags=re.S)


def declared_locally(text):
    return set(re.findall(r"(?<!var\()--([\w-]+)\s*:", text))


def targets_interactive_element(selector):
    """Só o último seletor simples conta: ícone dentro do botão não é o alvo."""
    for branch in selector.split(","):
        parts = re.split(r"[\s>+~]+", branch.strip())
        parts = [p for p in parts if p]
        if parts and INTERACTIVE_HINT.search(parts[-1]):
            return True
    return False


def _icon_classes(classes):
    return any(ICON_CLASS_RE.search(c) for c in classes)


INTERACTIVE_TAGS = {"a", "button", "input", "select", "textarea", "summary"}
INTERACTIVE_ROLE = re.compile(
    r"\brole\s*=\s*[\"'](button|link|tab|menuitem|checkbox|radio|switch|option)[\"']")


def inline_tag(text, pos):
    """(nome, texto da tag) quando `pos` está num style inline; senão None."""
    lt = text.rfind("<", 0, pos)
    if lt == -1 or ">" in text[lt:pos]:
        return None
    fim = text.find(">", pos)
    tag = text[lt:fim if fim != -1 else len(text)]
    nome = re.match(r"<\s*([a-zA-Z][\w-]*)", tag)
    return (nome.group(1).lower() if nome else ""), tag


def _classes_da_tag(tag):
    m = re.search(r"\bclass(?:Name)?\s*=\s*[\"']([^\"']*)", tag)
    return m.group(1).split() if m else []


def tag_interativa(nome, tag):
    return (nome in INTERACTIVE_TAGS or bool(INTERACTIVE_ROLE.search(tag))
            or any(INTERACTIVE_HINT.search(c) for c in _classes_da_tag(tag)))


def paints_icon(text, pos, importados=frozenset()):
    """O color em pos pinta ícone (SVG ou classe de ícone no último seletor de todo ramo)."""
    inline = inline_tag(text, pos)
    if inline is not None:
        nome, tag = inline
        original = re.match(r"<\s*([\w.]+)", tag)
        return (nome in SVG_TAGS or _icon_classes(_classes_da_tag(tag))
                or bool(original and eh_importado(original.group(1), importados)))

    ramos = [b for b in nearest_selector(text, pos).split(",") if b.strip()]
    if not ramos:
        return False
    for ramo in ramos:
        ultimo = [p for p in re.split(r"[\s>+~]+", ramo.strip()) if p][-1]
        tipo = re.match(r"[a-zA-Z][\w-]*", ultimo)
        if not ((tipo and tipo.group(0).lower() in SVG_TAGS)
                or _icon_classes(re.findall(r"\.([\w-]+)", ultimo))):
            return False
    return True


def _px(bruto):
    px = float(str(bruto).strip().rstrip("px"))
    return int(px) if px.is_integer() else px


def target_min_px(tokens):
    bruto = tokens.get("touch_target", {}).get("target-min")
    if bruto is None:
        return tokens.get("touch_target_min_px", 44)
    return _px(bruto)


def target_fine_px(tokens):
    bruto = tokens.get("touch_target", {}).get("target-fine")
    return None if bruto is None else _px(bruto)


MOUSE_MEDIA = re.compile(r"@media[^{]*\(\s*pointer\s*:\s*fine\s*\)[^{]*\{")


def faixas_mouse(text):
    """(início, fim) de cada bloco @media com (pointer: fine)."""
    faixas = []
    for m in MOUSE_MEDIA.finditer(text):
        nivel, i = 1, m.end()
        while i < len(text) and nivel:
            if text[i] == "{":
                nivel += 1
            elif text[i] == "}":
                nivel -= 1
            i += 1
        faixas.append((m.end(), i))
    return faixas


def iter_declarations(text):
    """(propriedade, valor, posição) de CSS e de style JSX."""
    for m in DECL_RE.finditer(text):
        prop = kebab(m.group(1))
        value = clean_value(m.group(2))
        if value:
            yield prop, value, m.start()


def _length_px(valor):
    m = LENGTH_RE.match(valor.strip())
    return float(m.group(1)) * (16 if m.group(2) == "rem" else 1)


class Linter:
    def __init__(self, tokens):
        self.tokens = tokens
        self.findings = []
        self.palette = colher_paleta(tokens)
        self.known_hex = set(self.palette.values())
        self.known_hex |= {k.lower() for k in tokens.get("gradient_literals", {})}
        self.hex_to_names = {}
        for name, hex_v in self.palette.items():
            self.hex_to_names.setdefault(hex_v, []).append(name)
        self.palette_triples = {hex_to_triple(h) for h in self.known_hex}
        self.translucent = {
            tuple(int(p) for p in key.split(",")): why
            for key, why in tokens.get("translucent_literals", {}).items()
        }
        self.banlist = tokens["text_color_banlist"]
        self.icon_ok = frozenset(tokens.get("icon_color_allowed", []))
        self.allowed_named = {c.lower() for c in tokens.get("named_colors_allowed", [])}
        self.allowed_radius = set(tokens["radius"].values()) | {"0", "0px"}
        self.allowed_spacing_px = {
            float(v.rstrip("px")) for v in tokens["spacing"].values()
        } | {0.0}
        self.spacing_exceptions = {
            re.sub(r"\s+", " ", k.strip().lower())
            for k in tokens.get("spacing_exceptions", {})
        }
        self.known_z = set(tokens["zindex"].values())
        self.target_min = target_min_px(tokens)
        self.target_fine = target_fine_px(tokens)
        self.known_tokens = collect_token_names(tokens)
        self.font_families = font_families(tokens)
        self.brand_only = tokens.get("brand_only", {})
        self.focus_within = False
        self.font_sizes_px = {
            float(v.rstrip("px")) for v in tokens["typography"]["font_size"].values()
            if str(v).endswith("px")
        }
        self.color_families = color_families(tokens)
        self.importados = frozenset()

    def add(self, severity, line, oque, esperado, secao):
        self.findings.append((severity, line, oque, esperado, secao))

    def banned_names_for_hex(self, hex_value):
        return [n for n in self.hex_to_names.get(hex_value, []) if n in self.banlist]

    def check_palette(self, text):
        for m in HEX_RE.finditer(text):
            normalized, _ = expand_hex(m.group(1))
            if normalized is None:
                continue
            if normalized not in self.known_hex:
                self.add("ERRO", find_line(text, m.start()),
                         f"cor '{m.group(0)}' fora da paleta", "var(--token)", "3.1")

        for m in FUNC_COLOR_RE.finditer(text):
            triple, has_alpha = parse_func_color(m.group(1), m.group(2))
            if triple is None:
                continue
            # Preto puro fica para a regra de sombra.
            if triple == (0, 0, 0):
                continue
            if triple in self.palette_triples:
                continue
            if has_alpha and triple in self.translucent:
                continue
            as_hex = "#{:02x}{:02x}{:02x}".format(*triple)
            self.add("ERRO", find_line(text, m.start()),
                     f"cor '{m.group(0)}' ({as_hex}) fora da paleta",
                     "var(--token); tinta crua só com alpha, em sombra e véu", "3.1")

    def check_declarations(self, text):
        mouse = faixas_mouse(text)
        for prop, value, pos in iter_declarations(apaga_classes(text)):
            line = find_line(text, pos)
            low = value.lower()

            if not prop.startswith("--"):
                self.check_theme_and_brand_vars(value, line)
            if prop in COLOR_PROPS:
                self.check_named_color(prop, value, line)
                sem_url = re.sub(r"url\([^)]*\)", " ", value, flags=re.I)
                if WHITE_FIXO_RE.search(sem_url) and "var(" not in sem_url:
                    self.add("AVISO", line, f"{prop}: {value} é branco fixo, não troca no tema",
                             "var(--white)", "25.3")
            if prop == "font-size" and LENGTH_RE.match(value.strip()):
                self.check_font_size(value.strip(), "font-size", line,
                                     "var(--fs-caption) até var(--fs-display)")
            if prop == "color" and paints_icon(text, pos, self.importados):
                self.check_text_banlist(value, line, self.icon_ok, "cor de ícone")
            elif prop == "color":
                self.check_text_banlist(value, line)
            if prop in RADIUS_PROPS:
                self.check_radius(value, line)
            if prop in SPACING_PROPS:
                self.check_spacing(prop, value, line)
            if prop == "box-shadow":
                self.check_shadow(value, line)
            if prop == "z-index":
                self.check_zindex(value, line)
            if prop == "font-family":
                self.check_font(value, line)
            if prop in SIZE_PROPS:
                self.check_touch_target(prop, low, text, pos, line,
                                        any(a <= pos < b for a, b in mouse))
            if prop == "max-width" and re.search(r"\d(px|rem|em)\b", low):
                self.add("AVISO", line, f"max-width: {value} fora dos tokens",
                         "var(--w-content), var(--w-form), var(--w-auth) ou 70ch", "5.2")

    def check_max_width(self, cls, line):
        valor = cls[len("max-w-"):]
        larguras = set(self.tokens.get("width", {}))
        token = re.fullmatch(r"\((?:length:)?--([\w-]+)\)|\[var\(--([\w-]+)\)\]", valor)
        if token and (token.group(1) or token.group(2)) in larguras:
            return
        if valor in ("none", "full", "fit", "min", "max", "prose", "[70ch]"):
            return
        self.add("AVISO", line, f"'{cls}' fora dos tokens de largura",
                 "max-w-(--w-content), max-w-(--w-form), max-w-(--w-auth) ou max-w-[70ch]", "5.2")

    def check_theme_and_brand_vars(self, value, line):
        for m in VAR_USE_RE.finditer(value):
            nome = m.group(1)
            if nome.startswith("dark-"):
                self.add("ERRO", line, f"--{nome} usado direto na tela",
                         f"var(--{nome.removeprefix('dark-')}), que troca no tema", "25.2")
            elif nome in self.brand_only:
                self.add("AVISO", line, f"--{nome} fora do símbolo",
                         self.brand_only[nome].rstrip("."), "1.4")

    def check_named_color(self, prop, value, line):
        # "red" em url(banners/red.png) não é cor.
        value = re.sub(r"url\([^)]*\)", " ", value, flags=re.IGNORECASE)
        for word in re.findall(r"[a-zA-Z][a-zA-Z-]*", value):
            w = word.lower()
            if w in self.allowed_named or w not in NAMED_COLORS:
                continue
            self.add("ERRO", line, f"cor nomeada '{word}' em {prop}", "var(--token)", "3.1")

    def check_text_banlist(self, value, line, permitidos=frozenset(), uso="cor de texto"):
        """Token banido pelo nome, pelo hex ou por rgb()/hsl(); em ícone, permitidos passam."""
        secao = "18" if uso == "cor de ícone" else "3.2"
        banidos = {n: r.rstrip(".") for n, r in self.banlist.items() if n not in permitidos}
        for token_name, reason in banidos.items():
            if re.search(rf"--{re.escape(token_name)}\b", value):
                self.add("ERRO", line, f"--{token_name} como {uso}", reason, secao)

        for m in HEX_RE.finditer(value):
            normalized, _ = expand_hex(m.group(1))
            if not normalized:
                continue
            banned = [n for n in self.banned_names_for_hex(normalized) if n in banidos]
            if banned:
                self.add("ERRO", line,
                         f"'{m.group(0)}' é --{banned[0]} como {uso}",
                         banidos[banned[0]], secao)

        for m in FUNC_COLOR_RE.finditer(value):
            triple, _ = parse_func_color(m.group(1), m.group(2))
            if triple is None:
                continue
            as_hex = "#{:02x}{:02x}{:02x}".format(*triple)
            banned = [n for n in self.banned_names_for_hex(as_hex) if n in banidos]
            if banned:
                self.add("ERRO", line,
                         f"'{m.group(0)}' é --{banned[0]} como {uso}",
                         banidos[banned[0]], secao)

    def check_radius(self, value, line):
        if "var(" in value or "%" in value:
            return
        for m in PX_RE.finditer(value):
            px = f"{m.group(1)}px"
            if px not in self.allowed_radius and float(m.group(1)) != 0:
                scale = ", ".join(
                    sorted(
                        (v for v in self.tokens["radius"].values()),
                        key=lambda x: float(x.rstrip("px")),
                    )
                )
                self.add("ERRO", line, f"border-radius {px} fora da escala", scale, "3.6")

    def check_spacing(self, prop, value, line):
        normalized = re.sub(r"\s+", " ", value.strip().lower())
        if normalized in self.spacing_exceptions or "var(" in value or "calc(" in value:
            return
        for m in PX_RE.finditer(value):
            px = abs(float(m.group(1)))
            if px not in self.allowed_spacing_px:
                self.add("AVISO", line,
                         f"{prop}: {value} usa {m.group(1)}px, fora da escala de 4px",
                         "var(--sp-N)", "3.7")

    def check_token_names(self, text):
        code = blank_comments(text)
        local = declared_locally(code)
        for m in VAR_USE_RE.finditer(code):
            name = m.group(1)
            if name in self.known_tokens or name in local:
                continue
            perto = difflib.get_close_matches(name, sorted(self.known_tokens), n=1, cutoff=0.7)
            esperado = (f"--{perto[0]}?" if perto
                        else "token do tokens.json ou declarado em :root neste arquivo")
            self.add("ERRO", find_line(text, m.start()),
                     f"--{name} não existe", esperado, "3")

    def check_shadow(self, value, line):
        if re.search(r"rgba?\(\s*0[\s,]+0[\s,]+0\s*[,/)]|#0{3}(?:0|0{3}|0{3}[0-9a-f]{2})?\b|\bblack\b",
                     value, re.I):
            self.add("AVISO", line, "box-shadow com preto puro",
                     "var(--sh-sm) ou var(--sh-md), sombra tingida", "3.4")

    def check_zindex(self, value, line):
        m = re.fullmatch(r"-?\d+", value.strip())
        if not m:
            return
        if int(value) not in self.known_z:
            self.add("AVISO", line, f"z-index {value} fora das camadas",
                     "var(--z-*)", "3.10")

    def check_font(self, value, line):
        low = value.lower()
        if any(ok in low for ok in ("system-ui", "inherit", "var(")):
            return
        primeira = low.split(",")[0].strip().strip("'\"")
        if primeira in self.font_families:
            return
        self.add("ERRO", line, f"font-family '{value}' fora da família",
                 "var(--font-sans)", "4.1")

    def check_touch_target(self, prop, value, text, pos, line, mouse=False):
        m = PX_RE.fullmatch(value.strip())
        if not m:
            return
        px = float(m.group(1))
        minimo = self.target_fine if mouse and self.target_fine else self.target_min
        if px >= minimo or px == 0:
            return
        inline = inline_tag(text, pos)
        if inline is not None:
            nome, tag = inline
            if not tag_interativa(nome, tag):
                return
            alvo = f"<{nome}>"
        else:
            selector = nearest_selector(text, pos)
            if not selector or not targets_interactive_element(selector):
                return
            alvo = f"'{selector}'"
        com_mouse = minimo != self.target_min
        self.add("AVISO", line,
                 f"{alvo} declara {prop}: {m.group(0)}, abaixo do alvo mínimo de {minimo}px",
                 "var(--target-fine), só com mouse" if com_mouse else "var(--target-min)",
                 "5.12" if com_mouse else "20.6")

    def check_utility_classes(self, text, componente_ui=False):
        utility_count = 0
        for inicio, trechos in grupos_de_classe(text):
            tag = tag_em_volta(text, inicio)
            icone = bool(tag) and eh_icone(text, inicio, inicio, self.importados)
            bases = []
            for pos, raw in trechos:
                line = find_line(text, pos)
                for cls in raw.split():
                    partes = cls.split(":")
                    base = partes[-1].lstrip("!")
                    bases.append((base, partes[:-1], line))
                    if "dark" in partes[:-1] and not componente_ui:
                        self.add("ERRO", line, f"variante dark: em '{cls}'",
                                 "token que troca sozinho no tema", "25.2")
                    if UTILITY_HINT.match(base):
                        utility_count += 1
                    self.check_utility_class(base, line, icone)
            self.check_class_group(bases, tag)

        if utility_count >= 6:
            self.add("INFO", None,
                     f"{utility_count} classes utilitárias; o lint confere cor, dark:, z-index, "
                     f"foco, alvo e valor entre colchetes",
                     "papel da cor e degrau de espaçamento e raio conferidos à mão", "26.4")

    def check_class_group(self, bases, tag):
        """Regras que olham o conjunto de classes de uma tag ou de uma chamada cn/cva."""
        tem_foco = (self.focus_within
                    or any("focus-visible" in v for _, vs, _ in bases for v in vs))
        for base, variantes, line in bases:
            if base in ("outline-none", "outline-0") and not tem_foco:
                self.add("ERRO", line, f"'{base}' sem anel em focus-visible:",
                         "focus-visible:ring-2, ou anel no contêiner com focus-within:", "20.5")
            altura = re.fullmatch(r"h-(\d+(?:\.\d+)?)", base)
            midia = tag and tag[0].lower() in {"img", "video", "canvas", "iframe", "svg", "picture"}
            if altura and float(altura.group(1)) * 4 >= 100 and not midia:
                self.add("AVISO", line, f"'{base}': altura fixa em contêiner",
                         f"min-{base}", "20.13")
        if not tag:
            return
        nome, texto_tag = tag
        if not (tag_interativa(nome.lower(), texto_tag) or nome in INTERACTIVE_COMPONENTS):
            return
        com_token = {"mouse" in vs for b, vs, _ in bases
                     if re.search(r"--(?:target-min|target-fine|control-min)\b", b)}
        for base, variantes, line in bases:
            m = SIZE_UTILITY_RE.match(base)
            com_mouse = "mouse" in variantes and bool(self.target_fine)
            if not m or com_mouse in com_token:
                continue
            px = float(m.group(2)) * 4 if m.group(2) else float(m.group(3))
            minimo = self.target_fine if com_mouse else self.target_min
            if px >= minimo or px == 0:
                continue
            self.add("AVISO", line,
                     f"<{nome}> com '{base}' ({px:g}px), abaixo do alvo de {minimo}px",
                     "mouse:size-(--target-fine)" if com_mouse else "size-(--target-min)",
                     "5.12" if com_mouse else "20.6")

    def check_utility_class(self, cls, line, icone=False):
        if cls.startswith("max-w-"):
            self.check_max_width(cls, line)
            return
        original = cls
        opaca = OPACITY_SUFFIX_RE.match(cls)
        if opaca:
            cls = opaca.group(1)
        if UTILITY_DARK_TOKEN_RE.match(cls):
            self.add("ERRO", line, f"classe '{original}' usa --dark-* direto",
                     "a utilitária do token, que troca no tema", "25.2")
            return
        var = UTILITY_VAR_RE.match(cls)
        if var:
            valor = f"var({var.group(2) or var.group(3)})"
            self.check_theme_and_brand_vars(valor, line)
            if var.group(1) == "text":
                if icone:
                    self.check_text_banlist(valor, line, self.icon_ok, "cor de ícone")
                else:
                    self.check_text_banlist(valor, line)
            return
        z = Z_UTILITY_RE.match(cls)
        if z:
            if int(z.group(1)) != 0:
                self.add("ERRO", line, f"classe '{original}': z-index fora das camadas",
                         "z-(--z-*)", "3.10")
            return
        keyword = UTILITY_KEYWORD_RE.match(cls)
        if keyword:
            palavra = keyword.group(2)
            if palavra == "white":
                self.add("ERRO", line, f"classe '{original}' usa o branco fixo do Tailwind",
                         "text-primary-foreground ou bg-card, que trocam no tema", "25.3")
            elif palavra in NAMED_COLORS and palavra not in self.allowed_named:
                self.add("ERRO", line, f"classe '{original}' com cor fora da paleta",
                         "utilitária do token, como text-foreground ou bg-card", "3.1")
            return
        color_m = UTILITY_COLOR_RE.match(cls)
        if color_m:
            prefix, family, step = color_m.groups()
            token = f"{family}-{step}"
            if token in self.brand_only and not icone:
                self.add("AVISO", line, f"classe '{cls}' fora do símbolo",
                         self.brand_only[token].rstrip("."), "1.4")
            if family not in self.color_families:
                self.add("ERRO", line, f"classe '{cls}' com a família '{family}', fora da paleta",
                         ", ".join(sorted(color_families(self.tokens))), "3.1")
            elif prefix == "text" and token in self.banlist and not (icone and token in self.icon_ok):
                self.add("ERRO", line, f"classe '{cls}' pinta texto com --{token}",
                         self.banlist[token].rstrip("."), "3.2")
            elif token not in self.palette:
                self.add("AVISO", line, f"classe '{cls}' aponta para --{token}, que não existe",
                         "um degrau da paleta", "3.1")
            return

        arb = ARBITRARY_RE.match(cls)
        if not arb:
            return
        prefix, inner = arb.groups()
        inner = inner.replace("_", " ")
        raiz = prefix.split("-")[0]
        if raiz in COLOR_UTILS.split("|") and LITERAL_COLOR_RE.match(inner):
            self.check_arbitrary_color(raiz, inner, cls, line, icone)
        elif raiz == "text" and LENGTH_RE.match(inner):
            self.check_font_size(inner, cls, line)
        elif raiz == "z":
            self.check_zindex(inner, line)
        elif raiz == "transition":
            caras = re.findall(r"\b(width|height|top|left|right|bottom|margin|padding)\b", inner)
            if caras:
                self.add("AVISO", line, f"'{cls}' anima {', '.join(caras)}",
                         "opacity, transform ou cor", "17.4")
        elif prefix == "h" and LENGTH_RE.match(inner) and _length_px(inner) >= 100:
            self.add("AVISO", line, f"'{cls}': altura fixa em contêiner",
                     f"min-h-[{inner}]", "20.13")
        elif raiz == "shadow":
            self.check_shadow(inner, line)
        elif raiz == "font" and not inner.isdigit():
            self.check_font(inner, line)
        elif prefix.startswith("rounded"):
            self.check_radius(inner, line)
        elif prefix.split("-")[0] in {"p", "px", "py", "pt", "pr", "pb", "pl",
                                      "m", "mx", "my", "mt", "mr", "mb", "ml",
                                      "gap", "space"}:
            self.check_spacing(prefix, inner, line)

    def check_arbitrary_color(self, raiz, valor, cls, line, icone):
        """Banlist em texto; cor da paleta escrita literal pede a utilitária. Fora da paleta fica com check_palette."""
        antes = len(self.findings)
        if raiz == "text":
            if icone:
                self.check_text_banlist(valor, line, self.icon_ok, "cor de ícone")
            else:
                self.check_text_banlist(valor, line)
        if len(self.findings) > antes:
            return
        hexa = None
        if valor.startswith("#"):
            hexa, _ = expand_hex(valor[1:])
        else:
            m = FUNC_COLOR_RE.match(valor)
            triple, _ = parse_func_color(m.group(1), m.group(2)) if m else (None, None)
            if triple is not None:
                hexa = "#{:02x}{:02x}{:02x}".format(*triple)
        if hexa and hexa in self.known_hex:
            nomes = ", ".join(f"--{n}" for n in self.hex_to_names.get(hexa, [])) or "token"
            self.add("ERRO", line, f"cor literal em '{cls}' ({nomes})",
                     "utilitária do token, como text-primary ou bg-card", "26.6")

    def check_font_size(self, valor, onde, line, esperado="text-caption até text-display"):
        if _length_px(valor) in self.font_sizes_px:
            return
        self.add("ERRO", line, f"tamanho '{valor}' em '{onde}' fora da escala", esperado, "4.2")

    def run(self, text, componente_ui=False):
        self.findings = []
        self.importados = icones_importados(text)
        self.focus_within = "focus-within" in text
        self.check_palette(blank_comments(text))
        self.check_token_names(text)
        self.check_declarations(text)
        self.check_utility_classes(text, componente_ui)
        seen = set()
        unique = []
        for f in self.findings:
            if f not in seen:
                seen.add(f)
                unique.append(f)
        rank = {"ERRO": 0, "AVISO": 1, "INFO": 2}
        return sorted(unique, key=lambda f: (f[1] is None, f[1] or 0, rank[f[0]]))


def formata(severity, line, oque, esperado, secao):
    loc = f"linha {line}: " if line else ""
    return f"[{severity}] {loc}{oque} ({esperado}, §{secao})"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("arquivos", nargs="+", help="HTML, CSS, JSX ou TSX; - lê da entrada padrão")
    parser.add_argument("--strict", action="store_true", help="[AVISO] também reprova")
    args = parser.parse_args()

    linter = Linter(load_tokens())
    erros = avisos = 0

    for src in args.arquivos:
        if src == "-":
            text, nome, ui = sys.stdin.read(), "stdin", False
        else:
            caminho = Path(src)
            if not caminho.is_file():
                print(f"[ERRO] arquivo não encontrado: {src}", file=sys.stderr)
                sys.exit(1)
            text, nome = caminho.read_text(encoding="utf-8"), caminho.name
            ui = "components/ui/" in caminho.as_posix()
        achados = linter.run(text, ui)
        if not achados:
            continue
        print(f"── {nome}")
        for f in achados:
            print("   " + formata(*f))
        erros += sum(1 for f in achados if f[0] == "ERRO")
        avisos += sum(1 for f in achados if f[0] == "AVISO")

    if not (erros or avisos):
        print("✓ Nenhum problema encontrado.")
    print(f"\n{erros} erro(s), {avisos} aviso(s).")
    if erros or (args.strict and avisos):
        sys.exit(2)


if __name__ == "__main__":
    main()
