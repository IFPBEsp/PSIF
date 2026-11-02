#!/usr/bin/env python3
"""
Contraste WCAG 2.2 entre duas cores.

Uso:
    python check_contrast.py <texto> <fundo> [--size normal|large|ui]
    python check_contrast.py navy-700 white
    python check_contrast.py "rgba(255,255,255,.7)" navy-800

Entradas: token (navy-700, dark-white), var(--token), hex de 3/4/6/8 dígitos,
rgb()/rgba()/hsl()/hsla(). Texto translúcido é composto sobre o fundo.
Saída: 0 passa AA; 1 entrada inválida; 2 não passa AA.
"""

import argparse
import json
import re
import sys
from pathlib import Path

TOKENS_PATH = Path(__file__).parent / "tokens.json"

SIZE_LABEL = {
    "normal": "texto de corpo (<18px)",
    "large": "texto grande/bold (>=18px, ou >=14px bold)",
    "ui": "componente de interface (borda, ícone, indicador)",
}
SIZE_TO_MIN_KEY = {"normal": "body_text", "large": "large_text", "ui": "ui_component"}


def load_tokens():
    with open(TOKENS_PATH, encoding="utf-8") as f:
        return json.load(f)


def expand_hex(digits):
    """Hex de 3/4/6/8 dígitos -> (r, g, b, alpha)."""
    d = digits.lower()
    if len(d) in (3, 4):
        d = "".join(c * 2 for c in d)
    if len(d) not in (6, 8):
        raise ValueError(f"hex de tamanho inesperado: #{digits}")
    rgb = tuple(int(d[i : i + 2], 16) for i in (0, 2, 4))
    alpha = int(d[6:8], 16) / 255.0 if len(d) == 8 else 1.0
    return rgb + (alpha,)


def hsl_to_rgb(h, s, l):
    c = (1 - abs(2 * l - 1)) * s
    hp = (h % 360) / 60.0
    x = c * (1 - abs(hp % 2 - 1))
    table = [(c, x, 0), (x, c, 0), (0, c, x), (0, x, c), (x, 0, c), (c, 0, x)]
    r, g, b = table[min(int(hp), 5)]
    m = l - c / 2
    return tuple(round((v + m) * 255) for v in (r, g, b))


def colher_cores(tokens):
    """Todo token com valor hex, de qualquer grupo."""
    cores = {}

    def colhe(no):
        for chave, valor in no.items():
            if isinstance(valor, dict):
                colhe(valor)
            elif isinstance(valor, str) and re.fullmatch(r"#[0-9A-Fa-f]{6}", valor.strip()):
                cores.setdefault(chave, valor.strip())

    colhe(tokens)
    return cores


def resolve_color(value, tokens):
    """-> (r, g, b, alpha)."""
    v = value.strip()
    colors = colher_cores(tokens)

    var_match = re.fullmatch(r"var\(\s*--([A-Za-z0-9-]+)\s*\)", v)
    if var_match:
        v = var_match.group(1)

    func = re.fullmatch(r"(rgba?|hsla?)\(([^)]*)\)", v, re.IGNORECASE)
    if func:
        kind = func.group(1).lower()
        parts = [p for p in re.split(r"[,/\s]+", func.group(2).strip()) if p]
        if len(parts) < 3:
            raise ValueError(f"'{value}' não tem componentes suficientes")
        alpha = 1.0
        if len(parts) >= 4:
            alpha = float(parts[3].rstrip("%")) / (100.0 if parts[3].endswith("%") else 1.0)
        if kind.startswith("rgb"):
            rgb = tuple(
                round(float(p[:-1]) * 255 / 100) if p.endswith("%") else int(round(float(p)))
                for p in parts[:3]
            )
        else:
            hue = float(re.sub(r"(deg|grad|rad|turn)$", "", parts[0]))
            rgb = hsl_to_rgb(hue, float(parts[1].rstrip("%")) / 100, float(parts[2].rstrip("%")) / 100)
        return rgb + (alpha,)

    hex_match = re.fullmatch(r"#?([0-9A-Fa-f]{3,8})", v)
    if hex_match and len(hex_match.group(1)) in (3, 4, 6, 8):
        return expand_hex(hex_match.group(1))

    name = v.lstrip("-")
    if name in colors:
        return expand_hex(colors[name].lstrip("#"))

    raise ValueError(
        f"'{value}' não é uma cor reconhecível (token, hex, rgb() ou hsl(); "
        f"tokens: {', '.join(sorted(colors))})"
    )


def composite(fg, bg):
    """Cor de frente translúcida sobre fundo opaco."""
    r_f, g_f, b_f, a = fg
    r_b, g_b, b_b, _ = bg
    return (
        round(r_f * a + r_b * (1 - a)),
        round(g_f * a + g_b * (1 - a)),
        round(b_f * a + b_b * (1 - a)),
        1.0,
    )


def relative_luminance(rgb):
    def channel(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(rgb_a, rgb_b):
    lum_a = relative_luminance(rgb_a)
    lum_b = relative_luminance(rgb_b)
    lighter, darker = max(lum_a, lum_b), min(lum_a, lum_b)
    return (lighter + 0.05) / (darker + 0.05)


def to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb[:3])


def banlist_reason(value, tokens):
    """Motivo da banlist de texto; só vale para a cor de frente."""
    name = value.strip().lstrip("-")
    var_match = re.fullmatch(r"var\(\s*--([A-Za-z0-9-]+)\s*\)", name)
    if var_match:
        name = var_match.group(1)
    return tokens.get("text_color_banlist", {}).get(name)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n")[1]
    )
    parser.add_argument("foreground", help="Cor do texto/elemento: token, hex, rgb() ou hsl()")
    parser.add_argument("background", help="Cor de fundo: token, hex, rgb() ou hsl()")
    parser.add_argument(
        "--size",
        choices=["normal", "large", "ui"],
        default="normal",
        help="normal = texto de corpo (<18px); large = texto grande/bold (>=18px ou >=14px bold); "
        "ui = componente de interface (borda, ícone). Default: normal.",
    )
    args = parser.parse_args()

    tokens = load_tokens()
    minimums = tokens["wcag_minimum"]

    try:
        fg = resolve_color(args.foreground, tokens)
        bg = resolve_color(args.background, tokens)
    except ValueError as e:
        print(f"[ERRO] {e}", file=sys.stderr)
        sys.exit(1)

    if bg[3] < 1:
        print(f"[AVISO] fundo translúcido (alpha {bg[3]:.2f}) tratado como opaco "
              "(informe o fundo já composto)", file=sys.stderr)
        bg = bg[:3] + (1.0,)

    fg_effective = composite(fg, bg) if fg[3] < 1 else fg

    ratio = contrast_ratio(fg_effective, bg)
    min_aa = minimums[SIZE_TO_MIN_KEY[args.size]]

    print(f"{args.foreground} ({to_hex(fg)}) sobre {args.background} ({to_hex(bg)})")
    print(f"Contexto: {SIZE_LABEL[args.size]}")
    if fg[3] < 1:
        print(f"Alpha {fg[3]:.2f} composto sobre o fundo: {to_hex(fg_effective)}")
    print(f"Razão de contraste: {ratio:.2f}:1")

    passes_aa = ratio >= min_aa
    print(f"WCAG AA (mínimo {min_aa}:1):  {'✓ PASSA' if passes_aa else '✗ NÃO PASSA'}")

    if args.size == "ui":
        print("WCAG AAA: não se aplica a elemento não textual (1.4.11).")
    else:
        target = minimums["internal_target_aaa"] if args.size == "normal" else minimums["body_text"]
        passes_aaa = ratio >= target
        print(
            f"WCAG AAA (meta {target}:1):   "
            f"{'✓ PASSA' if passes_aaa else '✗ não passa (AA é o mínimo)'}"
        )

    reason = banlist_reason(args.foreground, tokens)
    if reason:
        print(f"\n[AVISO] {args.foreground} está na banlist de texto: {reason} (§3.2)")

    if not passes_aa:
        print(f"\n[ERRO] contraste {ratio:.2f}:1 ({min_aa}:1 no mínimo, §3.2)")
        sys.exit(2)


if __name__ == "__main__":
    main()
