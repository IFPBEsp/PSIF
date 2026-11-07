"""Testes de check_consumer.py."""

import re
import subprocess
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _fixtures import concreto
from _fixtures import (ESTRUTURAL_500, ESTRUTURAL_700, ESTRUTURAL_800,
                       ESTRUTURAL_900, APOIO_700, HEX_ESTRUTURAL_700,
                       HEX_APOIO_700, ALIASES)

SCRIPT = Path(__file__).resolve().parent.parent / "check_consumer.py"


def _run(tmp_path, css, *extra_args):
    css = concreto(css)  # placeholders -> tokens reais desta skill
    f = tmp_path / "globals.css"
    f.write_text(css, encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(f), *extra_args],
        capture_output=True,
        text=True,
    )


def test_value_matching_skill_passes(tmp_path):
    result = _run(tmp_path, f":root {{ --{ESTRUTURAL_700}: {HEX_ESTRUTURAL_700}; }}")
    assert result.returncode == 0, result.stdout
    assert "0 divergência" in result.stdout


def test_diverging_value_is_flagged(tmp_path):
    result = _run(tmp_path, f":root {{ --{ESTRUTURAL_700}: #FF0000; }}")
    assert result.returncode == 2, result.stdout
    assert "[ERRO]" in result.stdout
    assert f"--{ESTRUTURAL_700}" in result.stdout


def test_legitimate_alias_is_not_a_false_positive(tmp_path):
    """`--alias-700."""
    if not ALIASES:
        return  # nenhuma família alias declarada nesta skill.

    from _fixtures import CORES
    alias, alvo = next(iter(ALIASES.items()))
    nome_alvo = f"{alvo}-700"
    assert nome_alvo in CORES, (
        f"`alias_families` aponta {alias!r} para {alvo!r}, mas {nome_alvo} não "
        f"existe no tokens.json.")
    css = (f":root {{ --{nome_alvo}: {CORES[nome_alvo]}; "
           f"--{alias}-700: var(--{nome_alvo}); }}")
    result = _run(tmp_path, css)
    assert result.returncode == 0, result.stdout
    assert "0 divergência" in result.stdout


def test_dark_scope_override_is_not_a_divergence(tmp_path):
    """`.dark` redefine token de propósito (§25)."""
    css = """
    :root { --TOKEN_ESTRUTURAL: HEX_ESTRUTURAL; }
    .dark { --TOKEN_ESTRUTURAL: #000000; }
    """
    result = _run(tmp_path, css)
    assert result.returncode == 0, result.stdout


def test_theme_bridge_scope_is_not_a_divergence(tmp_path):
    """`@theme` com apelido de namespace do Tailwind (§26.2) não é divergência."""
    css = """
    :root { --TOKEN_ESTRUTURAL: HEX_ESTRUTURAL; }
    @theme inline { --color-TOKEN_ESTRUTURAL: var(--TOKEN_ESTRUTURAL); }
    """
    result = _run(tmp_path, css)
    assert result.returncode == 0, result.stdout


def test_near_miss_name_is_reported_as_typo_warning(tmp_path):
    """Nome quase igual a um token real vira token morto."""
    result = _run(tmp_path, ":root { --surface-bas: #F6F9FC; }")
    assert result.returncode == 0, result.stdout  # aviso não derruba o exit code
    assert "[AVISO]" in result.stdout
    assert "--surface-bas" in result.stdout
    assert "--surface-base" in result.stdout


def test_quiet_flag_suppresses_the_line_by_line_report(tmp_path):
    result = _run(tmp_path, f":root {{ --{ESTRUTURAL_700}: #FF0000; }}", "--quiet")
    assert result.returncode == 2, result.stdout
    assert "[ERRO]" not in result.stdout
    assert "divergência" in result.stdout


def test_typo_in_scale_family_is_reported(tmp_path):
    """Só o sufixo de escala do Tailwind (`-xl`, `-2xl`) fica isento; erro de grafia na família é acusado."""
    # O typo é DERIVADO do nome real da família: escrito à mão, ele deixaria
    # de ser um typo assim que a skill renomeasse a paleta — e o teste passaria
    # a verificar um nome que ninguém erra.
    familia, degrau = ESTRUTURAL_900.rsplit("-", 1)
    typo = f"{familia[:-1]}-{degrau}"
    result = _run(tmp_path, f":root {{ --{typo}: #052540; }}")
    assert result.returncode == 0, result.stdout
    assert "[AVISO]" in result.stdout
    assert f"--{typo}" in result.stdout
    assert f"--{ESTRUTURAL_900}" in result.stdout


def test_tailwind_xl_scale_suffix_is_not_a_typo(tmp_path):
    """O que a isenção de sufixo existe para proteger."""
    result = _run(tmp_path, ":root { --radius-3xl: 24px; }")
    assert result.returncode == 0, result.stdout
    assert "[AVISO]" not in result.stdout


def test_skill_tokens_css_has_no_divergence():
    css = SCRIPT.parent.parent / "assets" / "tokens.css"
    result = subprocess.run([sys.executable, str(SCRIPT), str(css)],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stdout
    assert "0 divergência" in result.stdout
    presentes, total = map(int, re.search(r"(\d+)/(\d+) tokens", result.stdout).groups())
    assert presentes == total, result.stdout


def test_shadcn_bridge_is_not_divergence(tmp_path):
    css = (":root { --background: var(--surface-base); --primary: var(--navy-700); "
           "--radius: var(--radius-md); }")
    result = _run(tmp_path, css)
    assert result.returncode == 0, result.stdout
    assert "[ERRO]" not in result.stdout


def test_theme_block_redefining_a_skill_token_is_flagged(tmp_path):
    css = ("@theme inline {\n  --radius-lg: calc(var(--radius) + 4px);\n"
           "  --radius-sm: var(--radius-xs);\n  --color-primary: var(--primary);\n}\n")
    result = _run(tmp_path, css)
    assert result.returncode == 2, result.stdout
    assert "linha 2: redefine --radius-lg no @theme" in result.stdout
    assert "--radius-sm" not in result.stdout


def test_reference_globals_of_section_26_8_has_no_divergence(tmp_path):
    md = (SCRIPT.parent.parent / "ai-rules" / "tailwind-integration.md").read_text(encoding="utf-8")
    secao = md.split("### 26.8", 1)[1].split("\n### ", 1)[0]
    css = re.search(r"```css\n(.*?)```", secao, re.S).group(1)
    result = _run(tmp_path, css)
    assert result.returncode == 0, result.stdout
    assert "0 divergência" in result.stdout


def test_findings_are_sorted_by_line_and_cite_26_5(tmp_path):
    css = ":root {\n  --surfce-base: #fff;\n  --sky-100: #000;\n}\n"
    linhas = [l for l in _run(tmp_path, css).stdout.splitlines() if l.startswith("[")]
    numeros = [int(re.search(r"linha (\d+)", l).group(1)) for l in linhas]
    assert numeros == sorted(numeros) and len(numeros) == 2, linhas
    assert all("§26.5" in l for l in linhas)


def test_number_spelling_is_not_divergence(tmp_path):
    """Formatador que troca `.2` por `0.2` não muda o valor."""
    tokens = (SCRIPT.parent.parent / "assets" / "tokens.css").read_text(encoding="utf-8")
    original = re.search(r"--ease-standard:\s*([^;]+);", tokens).group(1)
    formatado = re.sub(r"(?<![\d.])\.(\d)", r"0.\1", original)
    assert formatado != original
    result = _run(tmp_path, f":root {{ --ease-standard: {formatado}; }}")
    assert "[ERRO]" not in result.stdout, result.stdout
