#!/usr/bin/env python3
"""
Verificador de contraste WCAG 2.2 para o design system desta skill.

Por quê este script existe: a Seção 3.2 do design system já documenta o
contraste de todo par de token de design usado hoje em produção. Mas toda vez que uma
tela nova propõe uma combinação de cor que NÃO está nessa tabela pré-calculada
(um token novo, um par de tokens que ainda não foi testado, uma cor translúcida
sobre um fundo diferente), confiar em "isso parece que passa" é exatamente o
tipo de erro que a acessibilidade não perdoa. No PSIF, a tela é lida de
relance entre atendimentos, às vezes com o aparelho virado para a família.
Em vez de estimar de cabeça, rode este script e tenha uma resposta objetiva.

Uso:
    python check_contrast.py <cor-texto> <cor-fundo> [--size normal|large|ui]
    python check_contrast.py navy-700 white
    python check_contrast.py "#244A69" "#FFFFFF" --size large
    python check_contrast.py "rgba(255,255,255,.7)" navy-800
    python check_contrast.py dark-ink-700 dark-white

<cor-texto> e <cor-fundo> aceitam:
  · nome de token da skill (ex.: navy-700, ink-900, dark-white), com ou sem `--`
  · var(--navy-700)
  · hex de 3, 4, 6 ou 8 dígitos (#fff, #0B5FA5, #0B5FA580)
  · rgb()/rgba()/hsl()/hsla()

Cor de texto translúcida (alpha < 1, via hex de 4/8 dígitos ou rgba/hsla) é
composta sobre o fundo antes do cálculo — é assim que o navegador desenha, e
ignorar isso superestima o contraste real.

Exit code: 0 se passa AA · 1 em erro de entrada · 2 se NÃO passa AA.
"""

import argparse
import json
import re
import sys
from pathlib import Path

TOKENS_PATH = Path(__file__).parent / "tokens.json"

# Rótulo humano de cada contexto + de onde sai o limiar em tokens.json.
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
    """Todo token com valor em hex, de QUALQUER grupo do tokens.json.

    Lia só o grupo `color`, e por isso não enxergava os oito tokens de
    superfície do modo escuro (§26, grupo `dark`): pedir o contraste de um par
    de §26 devolvia "não é uma cor reconhecível" — logo na seção mais nova e
    menos rodada da skill, cujos nove pares AAA ninguém conseguia conferir com
    a ferramenta da própria skill.

    É a mesma correção que colher_paleta() recebeu em lint_output.py na 3.5.1;
    o outro consumidor do tokens.json ficou para trás. Varrer por formato do
    valor faz o próximo grupo de cor entrar sozinho.
    """
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
    """Aceita token, var(--token), hex de 3/4/6/8 dígitos ou rgb()/hsl().

    Retorna (r, g, b, alpha).
    """
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
        f"'{value}' não é uma cor reconhecível nem um token da skill. "
        f"Tokens disponíveis: {', '.join(sorted(colors))}"
    )


def composite(fg, bg):
    """Achata a cor de frente translúcida sobre o fundo (fundo sempre opaco)."""
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
    """Razão pela qual este token nunca deve ser COR DE TEXTO, se for o caso.

    A banlist é uma regra sobre uso como texto — usar o mesmo token como FUNDO
    (navy-700 atrás de texto branco, por exemplo) é uso previsto, então o
    chamador só consulta isto para a cor de frente.
    """
    name = value.strip().lstrip("-")
    var_match = re.fullmatch(r"var\(\s*--([A-Za-z0-9-]+)\s*\)", name)
    if var_match:
        name = var_match.group(1)
    return tokens.get("text_color_banlist", {}).get(name)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
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
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

    if bg[3] < 1:
        print(
            f"Aviso: o fundo '{args.background}' é translúcido (alpha {bg[3]:.2f}). "
            f"Tratando como opaco — para um resultado fiel, informe o fundo já achatado.",
            file=sys.stderr,
        )
        bg = bg[:3] + (1.0,)

    fg_effective = composite(fg, bg) if fg[3] < 1 else fg

    ratio = contrast_ratio(fg_effective, bg)
    min_aa = minimums[SIZE_TO_MIN_KEY[args.size]]

    print(f"{args.foreground} ({to_hex(fg)}) sobre {args.background} ({to_hex(bg)})")
    print(f"Contexto: {SIZE_LABEL[args.size]}")
    if fg[3] < 1:
        print(
            f"Alpha {fg[3]:.2f} composto sobre o fundo -> cor efetiva {to_hex(fg_effective)} "
            f"(é o que o olho vê, e o que a norma mede)."
        )
    print(f"Razão de contraste: {ratio:.2f}:1")

    passes_aa = ratio >= min_aa
    print(f"WCAG AA (mínimo {min_aa}:1):  {'✓ PASSA' if passes_aa else '✗ NÃO PASSA'}")

    if args.size == "ui":
        # WCAG 1.4.11 (non-text contrast) existe só em nível AA, com piso de 3:1.
        # Não há nível AAA para elemento não-textual — reportar um "AAA de UI"
        # seria inventar norma.
        print("WCAG AAA: não se aplica a elemento não-textual (1.4.11 só tem nível AA).")
    else:
        target = minimums["internal_target_aaa"] if args.size == "normal" else minimums["body_text"]
        passes_aaa = ratio >= target
        print(
            f"WCAG AAA (meta {target}:1):   "
            f"{'✓ PASSA' if passes_aaa else '✗ não passa (mas AA já é o mínimo aceitável)'}"
        )

    reason = banlist_reason(args.foreground, tokens)
    if reason:
        print(f"\n⚠ ATENÇÃO — {args.foreground} está na banlist de cor de texto: {reason}")

    if not passes_aa:
        print(
            "\n✗ Esta combinação NÃO é aceitável. Troque por um token mais "
            "escuro/claro da mesma família (ver tokens/colors.md §3.2) "
            "até passar AA — 4.5:1 é o piso inegociável, não uma meta a se aproximar."
        )
        sys.exit(2)


if __name__ == "__main__":
    main()
