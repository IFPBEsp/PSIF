"""O @theme de §26.8 põe md: e lg: do Tailwind nos breakpoints do tokens.json."""

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
TOKENS = json.loads((RAIZ / "scripts" / "tokens.json").read_text(encoding="utf-8"))
TAILWIND_MD = RAIZ / "ai-rules" / "tailwind-integration.md"


def test_tailwind_breakpoints_match_the_tokens():
    texto = TAILWIND_MD.read_text(encoding="utf-8")
    declarados = {nome: float(rem) * 16 for nome, rem in
                  re.findall(r"--breakpoint-(\w+):\s*([\d.]+)rem", texto)}
    for nome in ("md", "lg"):
        esperado = float(TOKENS["breakpoint"][f"bp-{nome}"].rstrip("px"))
        assert declarados.get(nome) == esperado, (
            f"--breakpoint-{nome} em §26.8: {declarados.get(nome)}px; tokens.json: {esperado}px")
