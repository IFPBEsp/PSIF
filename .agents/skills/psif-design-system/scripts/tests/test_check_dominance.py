"""Testes de check_dominance.py."""

import subprocess
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _fixtures import concreto
from _fixtures import (ESTRUTURAL_500, ESTRUTURAL_700, ESTRUTURAL_800,
                       ESTRUTURAL_900, APOIO_700, HEX_ESTRUTURAL_700,
                       HEX_APOIO_700, ALIASES)

SCRIPT = Path(__file__).resolve().parent.parent / "check_dominance.py"


def _run(tmp_path, css, *extra_args):
    css = concreto(css)  # placeholders -> tokens reais desta skill
    f = tmp_path / "tokens.css"
    f.write_text(css, encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(f), *extra_args],
        capture_output=True,
        text=True,
    )


def test_blue_role_mapping_alone_triggers_dominance_even_without_background(tmp_path):
    """`--card` em marinho pinta área: inverte a regra mesmo sem `background`."""
    result = _run(tmp_path, f":root {{ --card: var(--{ESTRUTURAL_800}); }}")
    assert result.returncode == 2, result.stdout
    assert "estrutural pinta mais área que neutro" in result.stdout


def test_foreground_role_is_marca_not_area(tmp_path):
    """`--card-foreground` marca texto, não pinta fundo (§3.3)."""
    result = _run(tmp_path, f":root {{ --card-foreground: var(--{ESTRUTURAL_800}); }}")
    assert result.returncode == 0, result.stdout
    assert "nenhuma declaração de fundo com token reconhecido" in result.stdout


def test_balanced_declarations_pass(tmp_path):
    css = """
    :root {
      --page-bg: var(--surface-base);
      --card: var(--surface-raised);
      --panel: var(--surface-sunken);
      --modal-bg: var(--surface-overlay);
      --header-bg: var(--TOKEN_ESTRUTURAL_900);
      --sidebar: var(--TOKEN_ESTRUTURAL_800);
      --badge-bg: var(--TOKEN_APOIO);
    }
    """
    result = _run(tmp_path, css)
    assert result.returncode == 0, result.stdout
    assert "proporção dentro da regra de ouro" in result.stdout


def test_support_orange_over_ceiling_is_flagged(tmp_path):
    css = """
    :root {
      --page-bg: var(--surface-base);
      --card: var(--surface-raised);
      --header: var(--TOKEN_ESTRUTURAL_800);
      --badge1-bg: var(--TOKEN_APOIO);
      --badge2-bg: var(--TOKEN_APOIO);
    }
    """
    result = _run(tmp_path, css)
    assert result.returncode == 2, result.stdout
    assert "apoio em" in result.stdout


def test_semantic_colors_are_excluded_from_permanent_regime(tmp_path):
    """success/warning/danger só pintam quando o estado acontece."""
    css = """
    :root { --page-bg: var(--surface-base); }
    .badge-danger { background: var(--danger-100); }
    .badge-success { background: var(--success-100); }
    """
    result = _run(tmp_path, css)
    assert result.returncode == 0, result.stdout
    assert "condicional: success/" in result.stdout


def test_dark_scope_is_isolated_from_light_scope(tmp_path):
    """Um `.dark` 100% estrutural não pode ficar escondido atrás de um `:root` limpo."""
    css = """
    :root { --page-bg: var(--surface-base); }
    .dark {
      --card: var(--TOKEN_ESTRUTURAL_800);
      --sidebar: var(--TOKEN_ESTRUTURAL_900);
      --panel: var(--TOKEN_ESTRUTURAL);
    }
    """
    ambos = _run(tmp_path, css)
    assert ambos.returncode == 2, ambos.stdout
    assert "no escuro, §25.1" in ambos.stdout

    claro = _run(tmp_path, css, "--escopo", "claro")
    assert claro.returncode == 0, claro.stdout

    escuro = _run(tmp_path, css, "--escopo", "dark")
    assert escuro.returncode == 2, escuro.stdout


def test_neutral_prefixed_alias_follows_its_pointer(tmp_path):
    """`--surface-acao` começa com `surface-` (neutro), mas aponta para a cor estrutural."""
    css = f"""
    :root {{ --surface-acao: var(--{ESTRUTURAL_700}); }}
    .tela {{ background: var(--surface-acao); }}
    """
    result = _run(tmp_path, css)
    assert result.returncode == 2, result.stdout
    assert "estrutural pinta mais área que neutro" in result.stdout


def test_dark_scope_in_root_dark_selector_is_read(tmp_path):
    css = (f":root.dark {{ --background: var(--{ESTRUTURAL_900}); --card: var(--{ESTRUTURAL_800}); }}\n"
           f".dark-mode-x {{ --popover: var(--{ESTRUTURAL_800}); }}\n")
    result = _run(tmp_path, css, "--escopo", "dark")
    assert result.returncode == 2, result.stdout
    assert "estrutural    2" in result.stdout, result.stdout
