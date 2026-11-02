"""Testes de check_refs.py."""

import importlib.util
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "check_refs.py"


def _load_module(raiz):
    spec = importlib.util.spec_from_file_location("check_refs", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.RAIZ = raiz
    return module


def test_reference_to_existing_subsection_is_valid(tmp_path):
    (tmp_path / "a.md").write_text(
        "### 3.2 Contraste\n\nDetalhe em §3.2.\n", encoding="utf-8"
    )
    modulo = _load_module(tmp_path)
    orfas, _, subsecoes = modulo.referencias_orfas()
    assert orfas == []
    assert "3.2" in subsecoes


def test_reference_to_missing_subsection_is_orphan(tmp_path):
    (tmp_path / "a.md").write_text(
        "### 9.1 Existe\n\nVer §9.9, que não existe.\n", encoding="utf-8"
    )
    modulo = _load_module(tmp_path)
    orfas, _, _ = modulo.referencias_orfas()
    assert len(orfas) == 1
    assert orfas[0][2] == "9.9"


def test_reference_to_existing_top_level_section_does_not_need_a_subsection(tmp_path):
    """§6 sozinho é válido se `## 6.` existe, mesmo sem nenhuma `### 6.x`."""
    (tmp_path / "a.md").write_text(
        "## 6. PRINCÍPIOS\n\nVer §6 no geral.\n", encoding="utf-8"
    )
    modulo = _load_module(tmp_path)
    orfas, _, _ = modulo.referencias_orfas()
    assert orfas == []


def test_reference_to_right_section_wrong_subsection_number_is_orphan(tmp_path):
    """Acertar o §N e errar o .M também é bug, não é "quase certo"."""
    (tmp_path / "a.md").write_text(
        "## 11. DADOS\n\n### 11.1 Tabela\n\nVer §11.4, que não existe aqui.\n",
        encoding="utf-8",
    )
    modulo = _load_module(tmp_path)
    orfas, _, _ = modulo.referencias_orfas()
    assert len(orfas) == 1
    assert orfas[0][2] == "11.4"




def test_python_docstrings_are_also_checked(tmp_path):
    """Metade do valor deste script é pegar referência quebrada em .py, não só em .md."""
    (tmp_path / "s.py").write_text('"""Ver §42 para detalhes."""\n', encoding="utf-8")
    modulo = _load_module(tmp_path)
    orfas, _, _ = modulo.referencias_orfas()
    assert len(orfas) == 1
    assert orfas[0][2] == "42"


def test_python_headings_never_count_as_a_definition(tmp_path):
    """Um .py não define seção."""
    (tmp_path / "s.py").write_text("## 5. não é heading de verdade\n", encoding="utf-8")
    (tmp_path / "a.md").write_text("Ver §5 em algum lugar.\n", encoding="utf-8")
    modulo = _load_module(tmp_path)
    orfas, secoes, _ = modulo.referencias_orfas()
    assert "5" not in secoes
    assert len(orfas) == 1


def test_help_prints_usage_without_running_the_check():
    result = subprocess.run([sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage:" in result.stdout and "✓" not in result.stdout
