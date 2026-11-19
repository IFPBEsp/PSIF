"""O @theme de §26.8 bate com o tokens.json: breakpoints e altura de linha de cada tamanho."""

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
TOKENS = json.loads((RAIZ / "scripts" / "tokens.json").read_text(encoding="utf-8"))
TAILWIND = (RAIZ / "ai-rules" / "tailwind-integration.md").read_text(encoding="utf-8")


def test_tailwind_breakpoints_match_the_tokens():
    declarados = {nome: float(rem) * 16 for nome, rem in
                  re.findall(r"--breakpoint-(\w+):\s*([\d.]+)rem", TAILWIND)}
    for nome in ("md", "lg"):
        esperado = float(TOKENS["breakpoint"][f"bp-{nome}"].rstrip("px"))
        assert declarados.get(nome) == esperado, (
            f"--breakpoint-{nome} em §26.8: {declarados.get(nome)}px; tokens.json: {esperado}px")


def test_section_26_8_line_heights_match_tokens_json():
    mapa = TOKENS["typography"]["line_height_by_size"]
    declarados = set(re.findall(r"--text-([\w-]+):\s*var\(--fs-[\w-]+\)", TAILWIND))
    alturas = dict(re.findall(r"--text-([\w-]+)--line-height:\s*var\(--(lh-[\w-]+)\)", TAILWIND))
    assert declarados, "a §26.8 não declara mais os tamanhos --text-*"
    faltando = sorted(declarados - set(alturas))
    assert not faltando, f"tamanho sem --line-height na §26.8: {faltando}"
    erradas = {n: (a, mapa.get(f"fs-{n}")) for n, a in alturas.items() if mapa.get(f"fs-{n}") != a}
    assert not erradas, f"§26.8 diverge do tokens.json (§26.8, tokens.json): {erradas}"


def test_every_font_size_has_a_line_height():
    tamanhos = set(TOKENS["typography"]["font_size"])
    mapa = TOKENS["typography"]["line_height_by_size"]
    assert tamanhos == set(mapa), f"sem altura: {sorted(tamanhos - set(mapa))}; sobrando: {sorted(set(mapa) - tamanhos)}"
    assert set(mapa.values()) <= set(TOKENS["typography"]["line_height"])
