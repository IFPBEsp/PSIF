"""A tabela §3.2 é dado escrito em prosa — aqui ela passa a ser verificada."""

import importlib.util
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
COLORS_MD = SCRIPTS.parent / "tokens" / "colors.md"
DARK_MD = SCRIPTS.parent / "tokens" / "dark-mode.md"

# Piso WCAG 2.2 por nível declarado na tabela, para texto normal.
PISO = {"AA": 4.5, "AAA": 7.0}

def _check_contrast():
    spec = importlib.util.spec_from_file_location(
        "check_contrast", SCRIPTS / "check_contrast.py"
    )
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _limpa(cor):
    """A tabela anota a cor de várias formas."""
    cor = re.sub(r"\(.*?\)", "", cor).strip()
    partes = cor.split()
    for parte in partes:
        if parte.startswith("#"):
            return parte
    return partes[0].lstrip("-")


def test_every_approved_pair_in_the_table_really_passes():
    modulo = _check_contrast()
    tokens = modulo.load_tokens()
    texto = COLORS_MD.read_text(encoding="utf-8")

    padrao = re.compile(
        r"^(?P<frente>[^/\n│]+?)\s*/\s*(?P<fundo>[^:\n]+?):\s*"
        r"(?:(?P<razao>[\d.]+):1\s*)?✓\s*(?P<nivel>AAA|AA)\b",
        re.M,
    )
    conferidas = 0
    erradas = []
    for m in padrao.finditer(texto):
        frente, fundo = _limpa(m.group("frente")), _limpa(m.group("fundo"))
        try:
            rgb_f = modulo.resolve_color(frente, tokens)
            rgb_b = modulo.resolve_color(fundo, tokens)
        except SystemExit:
            continue  # linha de prosa que casou por acidente
        except Exception:
            continue
        if rgb_f[3] < 1:
            rgb_f = modulo.composite(rgb_f, rgb_b)
        real = modulo.contrast_ratio(rgb_f, rgb_b)
        nivel = m.group("nivel")
        conferidas += 1
        if real + 0.005 < PISO[nivel]:
            erradas.append(
                f"{frente} / {fundo}: tabela diz ✓ {nivel} "
                f"(piso {PISO[nivel]}:1), real {real:.2f}:1"
            )
        declarada = m.group("razao")
        if declarada and abs(float(declarada) - real) > 0.06:
            erradas.append(
                f"{frente} / {fundo}: tabela diz {declarada}:1, real {real:.2f}:1"
            )

    assert conferidas >= 10, f"só {conferidas} pares casaram — o formato da §3.2 mudou"
    assert not erradas, "pares aprovados na §3.2 que não passam:\n  " + "\n  ".join(erradas)


def test_every_approved_pair_in_the_dark_mode_table_really_passes():
    """Mesma guarda para §25, que estava fora de qualquer verificação."""
    modulo = _check_contrast()
    tokens = modulo.load_tokens()
    if "dark" in tokens.get("absent_groups", {}):
        return  # skill sem modo escuro, declarado em absent_groups.
    texto = DARK_MD.read_text(encoding="utf-8")

    padrao = re.compile(
        r"^\s*(?P<frente>#fff|--[\w-]+)\s*/\s*(?P<fundo>--[\w-]+)\s+"
        r"(?P<razao>[\d.]+):1\s+✓\s+(?P<nivel>AAA|AA)\b",
        re.M,
    )
    conferidas, erradas = 0, []
    for m in padrao.finditer(texto):
        frente = "#FFFFFF" if m.group("frente") == "#fff" else m.group("frente").lstrip("-")
        fundo = m.group("fundo").lstrip("-")
        rgb_f = modulo.resolve_color(frente, tokens)
        rgb_b = modulo.resolve_color(fundo, tokens)
        if rgb_f[3] < 1:
            rgb_f = modulo.composite(rgb_f, rgb_b)
        real = modulo.contrast_ratio(rgb_f, rgb_b)
        conferidas += 1
        nivel = m.group("nivel")
        if real + 0.005 < PISO[nivel]:
            erradas.append(f"{frente} / {fundo}: diz ✓ {nivel}, real {real:.2f}:1")
        if abs(float(m.group("razao")) - real) > 0.06:
            erradas.append(f"{frente} / {fundo}: diz {m.group('razao')}:1, real {real:.2f}:1")

    assert conferidas >= 9, f"só {conferidas} pares casaram — o formato da §25 mudou"
    assert not erradas, "pares aprovados na §25 que não passam:\n  " + "\n  ".join(erradas)
