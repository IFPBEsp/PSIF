"""Testes de check_contrast.py."""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "check_contrast.py"
TOKENS = json.loads((SCRIPT.parent / "tokens.json").read_text(encoding="utf-8"))


def _run(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args], capture_output=True, text=True
    )


def test_black_on_white_is_the_maximum_ratio():
    """21:1 é o teto da fórmula — qualquer constante errada o desloca."""
    result = _run("#000000", "#FFFFFF")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "21.00:1" in result.stdout


def test_aa_threshold_is_exact_at_4_5():
    """#767676 é o cinza mais claro que passa AA sobre branco (4.54:1); #777777, o seguinte, já falha (4.48:1)."""
    passa = _run("#767676", "#FFFFFF")
    falha = _run("#777777", "#FFFFFF")
    assert passa.returncode == 0 and "4.54:1" in passa.stdout, passa.stdout
    assert falha.returncode == 2 and "4.48:1" in falha.stdout, falha.stdout


def test_ui_threshold_differs_from_text_threshold():
    """O mesmo par passa 3:1 (borda/ícone, --size ui) e falha 4.5:1 (texto)."""
    ui = _run("#949494", "#FFFFFF", "--size", "ui")
    normal = _run("#949494", "#FFFFFF", "--size", "normal")
    assert ui.returncode == 0, ui.stdout
    assert normal.returncode == 2, normal.stdout


def test_translucent_foreground_is_composited_before_measuring():
    """Branco a 60% sobre preto vira #999999 (255 × .6 = 153, sem arredondamento em jogo)."""
    result = _run("rgba(255,255,255,.6)", "#000000")
    assert result.returncode == 0, result.stdout
    assert "composto sobre o fundo" in result.stdout
    assert "#999999" in result.stdout


def test_banlisted_token_is_announced_as_such():
    """Token da banlist usado como texto tem que ser dito em voz alta, passe ou não passe a razão naquele fundo."""
    banidos = list(TOKENS.get("text_color_banlist", {}))
    if not banidos:
        return  # skill sem banlist declarada — nada a anunciar.
    result = _run(banidos[0], "white")
    assert "banlist" in result.stdout.lower(), result.stdout


def test_unknown_token_reports_friendly_error_not_crash():
    """Entrada inválida sai com erro legível (exit 1) e a lista de tokens disponíveis."""
    result = _run("naoexiste-500", "white")
    assert result.returncode == 1
    assert "não é uma cor reconhecível" in result.stderr
