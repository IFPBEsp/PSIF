"""Testes de gen_tokens_css.py."""

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "gen_tokens_css.py"
TOKENS_JSON = SCRIPT.parent / "tokens.json"
SKILL_ROOT = SCRIPT.parent.parent

# Nomes que aparecem em var(...) na prosa como marcador, não como token real.
# "X" é o marcador genérico usado ao descrever a própria regra ("todo var(--X)
# resolve para um token real") — sem ele, o teste acusa a documentação dele mesmo.
VAR_PLACEHOLDERS = {"token", "X"}


def _load_module():
    spec = importlib.util.spec_from_file_location("gen_tokens_css", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_repo_tokens_css_is_currently_in_sync():
    """Guarda de CI."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--check"], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_every_alias_token_currently_mirrors_its_twin():
    """Invariante de DADOS, não só de código."""
    dados = json.loads(TOKENS_JSON.read_text(encoding="utf-8"))
    aliases = dados.get("alias_families", {})
    colors = dados["color"]
    diverged = []
    for name, value in colors.items():
        familia = name.split("-", 1)[0]
        alvo = aliases.get(familia)
        if alvo and "-" in name:
            gemeo = f"{alvo}-{name.split('-', 1)[1]}"
            if colors.get(gemeo) != value:
                diverged.append((name, value, gemeo, colors.get(gemeo)))
    assert not diverged, f"famílias alias divergiram: {diverged}"


def test_every_var_reference_in_the_docs_resolves_to_a_real_token():
    """Todo var(--x) citado na documentação existe no tokens.json."""
    sys.path.insert(0, str(SCRIPT.parent))
    from lint_output import collect_token_names

    known = collect_token_names(json.loads(TOKENS_JSON.read_text(encoding="utf-8")))
    orphans = {}
    for md in sorted(SKILL_ROOT.glob("*/*.md")) + [SKILL_ROOT / "SKILL.md"]:
        texto = md.read_text(encoding="utf-8")
        # Papel declarado no próprio trecho (`--primary: var(--navy-700)` no
        # globals.css de §26.8) resolve ali mesmo: é do consumidor, não da skill.
        declarados = set(re.findall(r"^\s*--([\w-]+)\s*:", texto, re.M))
        for m in re.finditer(r"var\(\s*--([\w-]+)", texto):
            name = m.group(1)
            # `--tw-*` são apelidos de repasse do projeto consumidor para o
            # namespace de tema do Tailwind — não são token da skill.
            if (name in known or name in VAR_PLACEHOLDERS or name in declarados
                    or name.endswith("-") or name.startswith("tw-")):
                continue
            orphans.setdefault(md.name, set()).add(name)
    assert not orphans, f"var() na doc apontando para token inexistente: {orphans}"


def test_color_pairs_emits_var_alias_when_values_match():
    """Unidade pura."""
    module = _load_module()
    original = module.TOKENS
    try:
        module.TOKENS = dict(original, alias_families={"velho": "novo"})
        pairs = dict(module.color_pairs(
            {"novo-700": "#A55708", "velho-700": "#A55708"}))
        assert pairs["velho-700"] == "var(--novo-700)"
        assert pairs["novo-700"] == "#A55708"

        # E não aliasa quando os valores DIFEREM: aí são duas cores mesmo.
        pairs = dict(module.color_pairs(
            {"novo-700": "#A55708", "velho-700": "#FF0000"}))
        assert pairs["velho-700"] == "#FF0000"
    finally:
        module.TOKENS = original
