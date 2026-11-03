"""O DESIGN.md recebe valor de CSS em todo {{token}} do corpo."""

import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
CORPO = RAIZ / "scripts" / "design_md_body.md"
DESIGN = RAIZ / "assets" / "DESIGN.md"


def test_every_fs_placeholder_becomes_a_px_value():
    sys.path.insert(0, str(RAIZ / "scripts"))
    import gen_design_md
    plano = gen_design_md.planos()
    citados = set(re.findall(r"\{\{(fs-[\w-]+)\}\}", CORPO.read_text(encoding="utf-8")))
    assert citados, "o corpo não cita mais nenhum {{fs-*}}"
    errados = {n: plano.get(n) for n in citados if not re.fullmatch(r"\d+px", plano.get(n, ""))}
    assert not errados, f"{{{{fs-*}}}} sem valor em px: {errados}"


def test_design_md_has_no_line_height_names_in_place_of_sizes():
    texto = DESIGN.read_text(encoding="utf-8")
    assert not re.search(r"\blh-(tight|snug|normal)\b", texto), "nome de lh-* no lugar de valor"


def test_body_writes_values_only_as_tokens():
    corpo = (Path(__file__).resolve().parent.parent / "design_md_body.md").read_text(encoding="utf-8")
    px = sorted(set(re.findall(r"\b(\d+)px\b", corpo)) - {"1", "320"})
    assert not px, f"px escrito à mão no corpo: {px}; use {{{{token}}}}"
    assert not re.search(r"#[0-9A-Fa-f]{3,8}\b", corpo), "hex escrito à mão no corpo"
    assert not re.search(r"\d+\.\d+:1", corpo), "razão de contraste escrita à mão no corpo"
