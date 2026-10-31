#!/usr/bin/env python3
"""
Lint de conformidade com o design system desta skill.

Por quê este script existe: a Seção 24 (anti-padrões) e o checklist da Seção 25
descrevem em texto o que nunca deve aparecer numa tela — mas texto é
fácil de esquecer no meio de gerar centenas de linhas de HTML/CSS/JSX. Este
script faz uma varredura objetiva e barata (regex, sem dependências externas)
no código que você está prestes a entregar.

O que ele checa:
  (Neste script, "token" é sempre token de DESIGN — um valor do sistema
  visual, como --<cor>-700 ou --sp-4. Nunca token de LLM.)

  1. Cor fora da paleta — hex de 3/4/6/8 dígitos, rgb()/rgba(), hsl()/hsla()
     e cor nomeada de CSS (red, black, gray...).
  2. Token banido como cor de texto — pelo nome (var(--<cor>-500)), pelo hex
     literal equivalente ou pela classe utilitária (text-<cor>-500). A lista
     é `text_color_banlist` do tokens.json. Quando o `color` pinta ícone
     (elemento SVG, classe de ícone), vale o piso de UI: os tokens de
     `icon_color_allowed` passam (§18).
  3. border-radius fora da escala (§3.6), inclusive em valor múltiplo.
  4. padding/margin/gap fora da escala de 4px (§3.7) — como [AVISO], porque
     espaçamento denso (chip, badge, gap de ícone) é decisão consciente, não
     violação certa. Use --strict para que derrube o exit code.
  5. Sombra preta pura em vez de tingida pela tinta da skill (§3.4).
  6. z-index fora das camadas nominais (§3.10).
  7. font-family fora das famílias de `typography.font_family` (§4.1).
  8. Alvo de toque abaixo de `--target-min` (grupo `touch_target`, §20.6) no
     seletor do próprio elemento interativo — ícone ou avatar dentro de um
     botão não conta, a área é do pai.
  9. var(--token) apontando para um nome que não existe no tokens.json nem é
     declarado no próprio arquivo (o browser ignora em silêncio).
 10. Classes utilitárias (Tailwind & cia.) — checa o que dá, e avisa que o
     resto da tela fica fora do alcance deste lint.

O que ele NÃO checa: tudo que exige julgamento (estado vazio explica o motivo,
hierarquia visual, dominância de cor por área de tela, qualidade do texto) e a
cor de `stroke`/`fill` — ilustração decorativa não tem piso de contraste, ícone
que informa precisa de 3:1, e só o olho separa os dois.
É rede de segurança antes de entregar, não o critério final de qualidade — o
checklist qualitativo de ai-rules/anti-patterns-checklist.md §25 continua
obrigatório.

Uso:
    python lint_output.py caminho/para/tela.html
    python lint_output.py Componente.tsx tela.html estilos.css
    cat tela.html | python lint_output.py -
    python lint_output.py tela.html --strict   # AVISO também derruba o exit code

Exit code: 0 limpo · 2 com [ERRO] (ou com [AVISO], se --strict).
"""

import difflib
import json
import re
import sys
from pathlib import Path

TOKENS_PATH = Path(__file__).parent / "tokens.json"

# Propriedades cujo valor é (ou pode conter) cor. Só dentro delas uma palavra
# como "red" é interpretada como cor — fora daqui seria falso positivo em prosa.
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

# Seletor/classe que denuncia elemento clicável — usado só na regra de alvo de toque.
INTERACTIVE_HINT = re.compile(
    r"\b(btn|button|icon-btn|fab|tab|chip|input|textarea|select|link|anchor|"
    r"nav-item|nav-link|menu-item|option|checkbox|radio|switch|toggle|stepper-dot|"
    r"close|dismiss|action|pagination|page-link|sort|filter-chip)\b",
    re.IGNORECASE,
)

# Cores nomeadas de CSS mais prováveis de aparecer em código gerado. Não é a
# lista completa do CSS — é a lista do que a IA realmente escreve por descuido.
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

# Famílias de cor da paleta — usadas para julgar classe utilitária tipo
# bg-red-500. MEDIDAS em tokens.json, não digitadas: uma lista à mão aqui é
# uma segunda definição da paleta, e a segunda definição é a que fica velha.
def font_families(tokens):
    """Famílias aceitas em font-family — a PRIMEIRA de cada pilha declarada.

    Lidas de `typography.font_family`, não digitadas: a fonte é a decisão de
    identidade mais visível de uma skill, e um nome fixo aqui obrigava toda
    skill derivada a usar a fonte da skill de origem ou a forkar o lint.
    """
    familias = set()
    for pilha in tokens.get("typography", {}).get("font_family", {}).values():
        pilha = re.sub(r"var\(\s*--[\w-]+\s*,\s*([^)]*)\)", r"\1", str(pilha))
        primeira = pilha.split(",")[0].strip().strip("'\"").lower()
        if primeira:
            familias.add(primeira)
    return familias


def color_families(tokens):
    """{"navy", "ink", ...} a partir dos nomes de cor de tokens.json.

    `navy-700` -> navy · `warning-border` -> warning · `white` -> white.
    """
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
UTILITY_COLOR_RE = re.compile(r"^(text|bg|border|ring|fill|stroke|from|to|via|divide)-([a-z]+)-(\d{2,3})$")
ARBITRARY_RE = re.compile(r"^([a-z-]+)-\[([^\]]+)\]$")
PX_RE = re.compile(r"(-?\d*\.?\d+)px\b")

# Grupos do tokens.json que guardam valores/exceções, não nomes de token.
NON_TOKEN_GROUPS = {
    "gradient_literals", "translucent_literals", "named_colors_allowed",
    "text_color_banlist", "icon_color_allowed", "browser_surfaces",
    "spacing_exceptions", "wcag_minimum", "touch_target_min_px", "absent_groups",
}

# Onde `color` pinta ícone (via currentColor), e não texto.
def eh_icone(texto, inicio, fim):
    """A tag que leva este class/className é ícone? <svg>, componente que
    termina em Icon/Icone (lucide, o `Icon` do projeto) ou elemento com
    aria-hidden. `text-ink-600` pinta ícone (§18), não texto; sem isto o lint
    reprovava a cor que a própria §6 manda usar no ícone de campo."""
    abre = texto.rfind("<", 0, inicio)
    fecha = texto.find(">", fim)
    if abre == -1:
        return False
    tag = texto[abre:fecha + 1 if fecha != -1 else fim]
    nome = re.match(r"<\s*([\w.]+)", tag)
    nome = nome.group(1) if nome else ""
    return (nome.lower() in SVG_TAGS or bool(re.search(r"(?:Icon|Icone)$", nome))
            or bool(re.search(r"\baria-hidden\b", tag)))


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
    """borderColor -> border-color. Mantém custom properties (--x) intactas.

    A quebra só acontece na fronteira minúscula->maiúscula, para que CSS escrito
    em caixa alta (COLOR: red) caia em 'color' em vez de virar 'c-o-l-o-r' e
    escapar de todas as regras.
    """
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
    """Todo token com valor de cor em hex, de QUALQUER grupo do tokens.json.

    Antes isto lia só o grupo `color`, e o grupo `dark` (§26) entrou fora do
    alcance: o lint passou a reprovar quatro hexes do próprio assets/tokens.css
    da skill. Varrer por formato do valor, e não por nome de grupo, faz o
    próximo grupo de cor entrar sozinho — a mesma razão de collect_token_names
    ser genérica.
    """
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
    """Todo nome de token declarado no tokens.json, de qualquer grupo.

    Aceita grupos aninhados (motion.duration, typography.font_size) e ignora
    chaves que não são token — as de metadados começam com '_', e listas de
    literais/exceções guardam valores, não nomes.
    """
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
    """Apaga o conteúdo de comentários CSS e HTML, preservando as quebras de linha.

    Comentário é prosa: o `var(--token)` de um comentário explicando a regra não
    é uso de token. Trocar por espaços (em vez de remover) mantém todos os
    deslocamentos, e com eles o número de linha de qualquer achado seguinte.
    """
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))

    return re.sub(r"/\*.*?\*/|<!--.*?-->", blank, text, flags=re.S)


def declared_locally(text):
    """Custom properties que o próprio arquivo declara (`--sidebar-w: 260px`).

    Uma tela pode ter token local de layout — isso é legítimo. O que não é
    legítimo é CONSUMIR um nome que ninguém definiu: o browser não avisa, só
    ignora a declaração e herda outro valor.
    """
    return set(re.findall(r"(?<!var\()--([\w-]+)\s*:", text))


def targets_interactive_element(selector):
    """O seletor mede o elemento clicável em si, e não um filho dele?

    `.btn` e `.toolbar .btn` medem o alvo — 32px ali é problema real. Já
    `.btn-clear svg` e `.user-chip .av` medem o ícone/avatar DENTRO do alvo,
    onde 16px é o tamanho correto e a área de 44px vem do pai. Cobrar 44px do
    ícone é o falso positivo que faz a pessoa parar de ler os avisos, então a
    dica interativa precisa estar no ÚLTIMO seletor simples, não em qualquer
    ancestral.
    """
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
    """A tag do style inline é o alvo clicável em si?"""
    return (nome in INTERACTIVE_TAGS or bool(INTERACTIVE_ROLE.search(tag))
            or any(INTERACTIVE_HINT.search(c) for c in _classes_da_tag(tag)))


def paints_icon(text, pos):
    """O `color` declarado em `pos` pinta um ícone, e não texto?

    Ícone segue o piso de contraste de UI (3:1, WCAG 1.4.11); texto, o de
    texto (4.5:1). Cobrar do ícone o piso de texto reprovava o chevron em
    --ink-600 que a própria skill manda usar (§9.3, §18). É ícone o style
    inline de elemento SVG ou de tag com classe de ícone, e a regra cujo
    ÚLTIMO seletor simples, em todos os ramos, é elemento SVG ou classe de
    ícone. `.icon-label` continua sendo texto.
    """
    inline = inline_tag(text, pos)
    if inline is not None:  # style inline: a tag decide
        nome, tag = inline
        return nome in SVG_TAGS or _icon_classes(_classes_da_tag(tag))

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


def target_min_px(tokens):
    """Alvo mínimo de toque em px, lido do token `--target-min` (§20.6).

    Era um escalar solto (`touch_target_min_px`) que o CSS não enxergava, e a
    tela escrevia 44px literal em todo botão de ícone. O escalar continua
    aceito para tokens.json antigo.
    """
    bruto = tokens.get("touch_target", {}).get("target-min")
    if bruto is None:
        return tokens.get("touch_target_min_px", 44)
    px = float(str(bruto).strip().rstrip("px"))
    return int(px) if px.is_integer() else px


def iter_declarations(text):
    """Rende (prop_kebab, valor_limpo, posicao) para CSS e style de JSX.

    O valor para no primeiro `;`, `}`, `{` ou fim de linha — sem isso, uma
    declaração sem ponto-e-vírgula antes do `}` engolia o resto do arquivo
    (era o bug do regex `[^;]+;` das versões anteriores).
    """
    for m in DECL_RE.finditer(text):
        prop = kebab(m.group(1))
        value = clean_value(m.group(2))
        if value:
            yield prop, value, m.start()


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
        self.known_tokens = collect_token_names(tokens)
        self.font_families = font_families(tokens)

    # ---------- infra ----------

    def add(self, severity, line, message):
        self.findings.append((severity, line, message))

    def banned_names_for_hex(self, hex_value):
        return [n for n in self.hex_to_names.get(hex_value, []) if n in self.banlist]

    # ---------- regras ----------

    def check_palette(self, text):
        """Regra 1: toda cor literal do arquivo tem de existir na paleta."""
        for m in HEX_RE.finditer(text):
            normalized, _ = expand_hex(m.group(1))
            if normalized is None:
                continue
            if normalized not in self.known_hex:
                self.add(
                    "ERRO",
                    find_line(text, m.start()),
                    f"Cor '{m.group(0)}' não está na paleta de tokens da skill. "
                    f"Use um token de tokens/colors.md §3.1, ou rode "
                    f"check_contrast.py se for um token novo que precisa ser validado.",
                )

        for m in FUNC_COLOR_RE.finditer(text):
            triple, has_alpha = parse_func_color(m.group(1), m.group(2))
            if triple is None:
                continue
            if triple == (0, 0, 0):
                continue  # tratado pela regra de sombra preta, com mensagem própria
            if triple in self.palette_triples:
                continue
            if has_alpha and triple in self.translucent:
                continue
            as_hex = "#{:02x}{:02x}{:02x}".format(*triple)
            hint = (
                f" Equivale a {as_hex}."
                if as_hex in self.known_hex
                else f" Equivale a {as_hex}, que também não é token."
            )
            self.add(
                "ERRO",
                find_line(text, m.start()),
                f"Cor '{m.group(0)}' fora da paleta da skill.{hint} Use var(--token) "
                f"em vez de rgb()/hsl() literal — as únicas tintas cruas permitidas são "
                f"as de sombra/glass documentadas em §3.4/§3.5.",
            )

    def check_declarations(self, text):
        for prop, value, pos in iter_declarations(text):
            line = find_line(text, pos)
            low = value.lower()

            if prop in COLOR_PROPS:
                self.check_named_color(prop, value, line)
            if prop == "color" and paints_icon(text, pos):
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
                self.check_touch_target(prop, low, text, pos, line)

    def check_named_color(self, prop, value, line):
        # url(...) sai do caminho: "red" em url(banners/red.png) não é cor.
        value = re.sub(r"url\([^)]*\)", " ", value, flags=re.IGNORECASE)
        for word in re.findall(r"[a-zA-Z][a-zA-Z-]*", value):
            w = word.lower()
            if w in self.allowed_named or w not in NAMED_COLORS:
                continue
            self.add(
                "ERRO",
                line,
                f"Cor nomeada de CSS '{word}' em '{prop}'. A skill não usa cor "
                f"nomeada — todo valor sai de var(--token) (§3.1).",
            )

    def check_text_banlist(self, value, line, permitidos=frozenset(), uso="cor de texto"):
        """Token banido como cor de texto, seja pelo nome ou pelo hex equivalente.

        Em ícone, `permitidos` são os tokens que passam o piso de UI
        (`icon_color_allowed`); o resto da lista continua reprovado.
        """
        banidos = {n: r for n, r in self.banlist.items() if n not in permitidos}
        for token_name, reason in banidos.items():
            if re.search(rf"--{re.escape(token_name)}\b", value):
                self.add("ERRO", line, f"'{token_name}' usado como {uso}: {reason}")

        for m in HEX_RE.finditer(value):
            normalized, _ = expand_hex(m.group(1))
            if not normalized:
                continue
            banned = [n for n in self.banned_names_for_hex(normalized) if n in banidos]
            if banned:
                self.add(
                    "ERRO",
                    line,
                    f"Hex '{m.group(0)}' é o valor de {'/'.join(banned)}, banido como "
                    f"{uso}: {banidos[banned[0]]} Escrever o hex direto não muda "
                    f"a regra — e some do grep por nome de token.",
                )

        for m in FUNC_COLOR_RE.finditer(value):
            triple, _ = parse_func_color(m.group(1), m.group(2))
            if triple is None:
                continue
            as_hex = "#{:02x}{:02x}{:02x}".format(*triple)
            banned = [n for n in self.banned_names_for_hex(as_hex) if n in banidos]
            if banned:
                self.add(
                    "ERRO",
                    line,
                    f"'{m.group(0)}' equivale a {'/'.join(banned)} ({as_hex}), banido como "
                    f"{uso}: {banidos[banned[0]]}",
                )

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
                self.add(
                    "ERRO",
                    line,
                    f"border-radius '{px}' fora da escala da skill ({scale}).",
                )

    def check_spacing(self, prop, value, line):
        normalized = re.sub(r"\s+", " ", value.strip().lower())
        if normalized in self.spacing_exceptions or "var(" in value or "calc(" in value:
            return
        for m in PX_RE.finditer(value):
            px = abs(float(m.group(1)))
            if px not in self.allowed_spacing_px:
                self.add(
                    "AVISO",
                    line,
                    f"'{prop}: {value}' usa {m.group(1)}px, fora da escala de 4px do "
                    f"da skill. Troque pelo var(--sp-N) "
                    f"mais próximo. Se for espaçamento denso (chip, badge, gap de ícone), "
                    f"onde 4px aperta e 8px alarga, isso é decisão a tomar de propósito e "
                    f"documentar — não um valor solto no olho.",
                )

    def check_token_names(self, text):
        """Todo var(--x) aponta para um token que existe?

        Um `var(--fs-subtitle)` que nunca foi criado não quebra a tela de
        forma visível: o browser descarta a declaração e o elemento herda
        outro valor. O resultado é uma tela quase certa, que ninguém revisa
        de novo. Também é a única defesa contra token renomeado numa mudança
        futura de paleta — sem isto, as telas antigas quebram caladas.
        """
        code = blank_comments(text)
        local = declared_locally(code)
        for m in VAR_USE_RE.finditer(code):
            name = m.group(1)
            if name in self.known_tokens or name in local:
                continue
            perto = difflib.get_close_matches(name, sorted(self.known_tokens), n=1, cutoff=0.7)
            dica = (
                f" Você quis dizer --{perto[0]}?" if perto
                else " Se for um token local da tela, declare-o em :root antes de usar."
            )
            self.add(
                "ERRO",
                find_line(text, m.start()),
                f"Token '--{name}' não existe em scripts/tokens.json e não é declarado "
                f"neste arquivo. O browser ignora a declaração em silêncio e herda "
                f"outro valor.{dica}",
            )

    def check_shadow(self, value, line):
        if re.search(r"rgba?\(\s*0\s*,\s*0\s*,\s*0\s*[,/)]", value):
            self.add(
                "AVISO",
                line,
                "box-shadow com preto puro (rgba(0,0,0,...)). Nesta skill, sombra é "
                "tingida pela tinta declarada em `translucent_literals` — ver §3.4.",
            )

    def check_zindex(self, value, line):
        m = re.fullmatch(r"-?\d+", value.strip())
        if not m:
            return
        if int(value) not in self.known_z:
            self.add(
                "AVISO",
                line,
                f"z-index '{value}' não corresponde a nenhuma camada nominal da skill "
                f"(ver §3.10). Evite valores avulsos como 9999.",
            )

    def check_font(self, value, line):
        low = value.lower()
        if any(ok in low for ok in ("system-ui", "inherit", "var(")):
            return
        primeira = low.split(",")[0].strip().strip("'\"")
        if primeira in self.font_families:
            return
        nomes = ", ".join(sorted(self.font_families)) or "var(--font-sans)"
        self.add(
            "ERRO",
            line,
            f"font-family '{value}' fora das famílias declaradas em "
            f"typography.font_family ({nomes}) — use var(--font-sans) (§4.1).",
        )

    def check_touch_target(self, prop, value, text, pos, line):
        m = PX_RE.fullmatch(value.strip())
        if not m:
            return
        px = float(m.group(1))
        if px >= self.target_min or px == 0:
            return
        inline = inline_tag(text, pos)
        if inline is not None:  # style inline: quem decide é a tag, não o CSS acima
            nome, tag = inline
            if not tag_interativa(nome, tag):
                return
            alvo = f"<{nome}>"
        else:
            selector = nearest_selector(text, pos)
            if not selector or not targets_interactive_element(selector):
                return
            alvo = f"'{selector}'"
        self.add(
            "AVISO",
            line,
            f"{alvo} declara {prop}: {m.group(0)}, abaixo do alvo mínimo de "
            f"{self.target_min}px da skill. Se este elemento é clicável, aumente a área "
            f"(padding conta) — ver §20.",
        )

    def check_utility_classes(self, text):
        utility_count = 0
        for m in CLASS_ATTR_RE.finditer(text):
            line = find_line(text, m.start())
            raw = next(g for g in m.groups() if g is not None)
            icone = eh_icone(text, m.start(), m.end())
            for cls in raw.split():
                base = cls.split(":")[-1].lstrip("!")
                if UTILITY_HINT.match(base):
                    utility_count += 1
                self.check_utility_class(base, line, icone)

        if utility_count >= 6:
            self.add(
                "AVISO",
                None,
                f"{utility_count} classes utilitárias detectadas. Este lint enxerga só "
                f"parte delas (cor de família estranha, valor arbitrário entre colchetes). "
                f"Estilo aplicado por classe utilitária de escala própria escapa das regras "
                f"de escala da skill — confira cor, espaçamento e raio à mão, ou gere "
                f"CSS com var(--token).",
            )

    def check_utility_class(self, cls, line, icone=False):
        color_m = UTILITY_COLOR_RE.match(cls)
        if color_m:
            prefix, family, step = color_m.groups()
            token = f"{family}-{step}"
            if family not in color_families(self.tokens):
                self.add(
                    "ERRO",
                    line,
                    f"Classe '{cls}' usa a família de cor '{family}', que não existe "
                    f"na paleta desta skill. Famílias válidas: "
                    f"{', '.join(sorted(color_families(self.tokens)))}.",
                )
            elif prefix == "text" and token in self.banlist and not (icone and token in self.icon_ok):
                self.add(
                    "ERRO",
                    line,
                    f"Classe '{cls}' pinta texto com '{token}', banido: {self.banlist[token]}",
                )
            elif token not in self.palette:
                self.add(
                    "AVISO",
                    line,
                    f"Classe '{cls}' referencia '{token}', que não é um token da skill — "
                    f"confira o degrau na escala de §3.1.",
                )
            return

        arb = ARBITRARY_RE.match(cls)
        if not arb:
            return
        prefix, inner = arb.groups()
        if prefix.startswith("rounded"):
            self.check_radius(inner, line)
        elif prefix.split("-")[0] in {"p", "px", "py", "pt", "pr", "pb", "pl",
                                      "m", "mx", "my", "mt", "mr", "mb", "ml",
                                      "gap", "space"}:
            self.check_spacing(prefix, inner, line)

    # ---------- entrada ----------

    def run(self, text):
        self.findings = []
        self.check_palette(blank_comments(text))
        self.check_token_names(text)
        self.check_declarations(text)
        self.check_utility_classes(text)
        seen = set()
        unique = []
        for f in self.findings:
            if f not in seen:
                seen.add(f)
                unique.append(f)
        rank = {"ERRO": 0, "AVISO": 1, "INFO": 2}
        return sorted(unique, key=lambda f: (f[1] is None, f[1] or 0, rank[f[0]]))


def report(findings, label=None):
    if label:
        print(f"── {label}")
    if not findings:
        print("✓ Nenhum problema encontrado pelo lint automático.")
        print("Lembrete: isto cobre só os desvios detectáveis por padrão de texto. Ainda")
        print("passe pelo checklist qualitativo em ai-rules/anti-patterns-checklist.md §25.")
        return 0, 0

    for severity, line, message in findings:
        loc = f"linha {line}: " if line else ""
        print(f"[{severity}] {loc}{message}")

    errors = sum(1 for f in findings if f[0] == "ERRO")
    warnings = sum(1 for f in findings if f[0] == "AVISO")
    print(f"\n{errors} erro(s), {warnings} aviso(s).")
    return errors, warnings


def main():
    argv = [a for a in sys.argv[1:] if a != "--strict"]
    strict = "--strict" in sys.argv[1:]

    if not argv:
        print(__doc__)
        sys.exit(1)

    linter = Linter(load_tokens())
    total_errors = total_warnings = 0

    for src in argv:
        text = sys.stdin.read() if src == "-" else Path(src).read_text(encoding="utf-8")
        label = src if len(argv) > 1 else None
        errors, warnings = report(linter.run(text), label)
        total_errors += errors
        total_warnings += warnings

    if total_errors or (strict and total_warnings):
        sys.exit(2)


if __name__ == "__main__":
    main()
