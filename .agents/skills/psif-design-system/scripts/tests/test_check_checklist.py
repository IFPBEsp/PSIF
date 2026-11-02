"""Testes de check_checklist.py."""

import re
import subprocess
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _fixtures import concreto
from _fixtures import (ESTRUTURAL_500, ESTRUTURAL_700, ESTRUTURAL_800,
                       ESTRUTURAL_900, APOIO_700, HEX_ESTRUTURAL_700,
                       HEX_APOIO_700, ALIASES)

SCRIPT = Path(__file__).resolve().parent.parent / "check_checklist.py"

CLEAN_HTML = """
<style>
.btn-primary {
  background: var(--TOKEN_ESTRUTURAL);
  color: var(--white);
  border-radius: var(--radius-md);
  padding: var(--sp-3) var(--sp-4);
  box-shadow: var(--sh-sm);
  font-family: var(--font-sans);
}
.icon-btn { height: 44px; width: 44px; }
</style>
<button class="btn-primary">Salvar Cadastro</button>
<div class="icon-btn">x</div>
"""
CLEAN_HTML = concreto(CLEAN_HTML)


def _run(tmp_path, texto, nome="a.tsx", *extra_args):
    f = tmp_path / nome
    f.write_text(texto, encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(f), *extra_args],
        capture_output=True,
        text=True,
    )


def test_clean_file_passes_and_still_lists_the_manual_items(tmp_path):
    result = _run(tmp_path, CLEAN_HTML, "clean.html")
    assert result.returncode == 0, result.stdout
    assert "0 reprovação" in result.stdout
    md = (SCRIPT.parent.parent / "ai-rules" / "anti-patterns-checklist.md").read_text(encoding="utf-8")
    esperado = len(re.findall(r"^- \[ \] .+ · manual$", md, re.M))
    assert esperado > 0
    assert result.stdout.count("   □ ") == esperado
    assert "completam o checklist de §24" in result.stdout


def test_messages_follow_the_line_format(tmp_path):
    result = _run(tmp_path, "\n.x { outline: none; }", "a.css")
    assert "[ERRO] linha 2: foco visível removido (anel em :focus-visible, §20.5)" in result.stdout


def test_removed_focus_without_substitute_is_flagged(tmp_path):
    result = _run(tmp_path, ".x { outline: none; }", "a.css")
    assert result.returncode == 2, result.stdout
    assert "§20.5" in result.stdout
    assert "foco visível removido" in result.stdout


def test_removed_focus_with_focus_visible_elsewhere_is_exempt(tmp_path):
    css = (".x { outline: none; }\n:focus-visible { outline: 2px solid "
           f"var(--{ESTRUTURAL_500}); }}")
    result = _run(tmp_path, css, "a.css")
    assert "foco visível removido" not in result.stdout
    assert result.returncode == 0, result.stdout


def test_placeholder_as_only_label_is_flagged(tmp_path):
    result = _run(tmp_path, '<input placeholder="Nome" />')
    assert result.returncode == 2, result.stdout
    assert "§20.7" in result.stdout
    assert "placeholder como único rótulo" in result.stdout


def test_placeholder_with_id_but_no_matching_label_is_flagged(tmp_path):
    result = _run(tmp_path, '<input id="nome" placeholder="Nome" />', "a.html")
    assert result.returncode == 2, result.stdout
    assert "placeholder como único rótulo" in result.stdout


def test_placeholder_with_label_for_or_wrapping_label_passes(tmp_path):
    html = ('<label for="nome">Nome</label><input id="nome" placeholder="Ana" />'
            '<label class="campo">E-mail <input type="email" placeholder="ana@ifpb.edu.br"></label>')
    result = _run(tmp_path, html, "a.html")
    assert "placeholder como único rótulo" not in result.stdout, result.stdout


def test_icon_only_button_without_accessible_name_is_flagged(tmp_path):
    result = _run(tmp_path, "<button><svg /></button>")
    assert result.returncode == 2, result.stdout
    assert "botão ou link só de ícone sem nome acessível" in result.stdout


def test_icon_followed_by_visible_text_is_not_icon_only(tmp_path):
    icone = '<svg viewBox="0 0 24 24"><path d="M5 12h11"></path></svg>'
    com_texto = _run(
        tmp_path,
        f'<button type="button">{icone}\nSair</button>\n'
        f'<button aria-label="Abrir menu">{icone}\n</button>',
        "a.html")
    assert "só de ícone" not in com_texto.stdout, com_texto.stdout

    so_icone = _run(tmp_path, f'<button type="button">{icone}\n</button>', "b.html")
    assert "só de ícone" in so_icone.stdout, so_icone.stdout


def test_english_jargon_is_flagged(tmp_path):
    result = _run(tmp_path, "<span>Loading</span>")
    assert result.returncode == 2, result.stdout
    assert "§19.2" in result.stdout


def test_stray_z_index_is_flagged_in_css_and_jsx_syntax(tmp_path):
    result = _run(tmp_path, ".x { z-index: 9999; }\n<div style={{ zIndex: 9999 }} />")
    assert result.returncode == 2, result.stdout
    assert result.stdout.count("z-index avulso") == 2, result.stdout


def test_z_index_via_token_is_not_flagged(tmp_path):
    result = _run(tmp_path, ".x { z-index: var(--z-modal); }")
    assert "z-index avulso" not in result.stdout
    assert result.returncode == 0, result.stdout


def test_comments_are_stripped_before_matching(tmp_path):
    texto = "/* outline: none; */\n// z-index: 9999;\n{/* zIndex: 9999 */}\n"
    result = _run(tmp_path, texto)
    assert result.returncode == 0, result.stdout
    assert "0 reprovação" in result.stdout


def test_lint_output_delegation_counts_toward_failure(tmp_path):
    result = _run(tmp_path, '<div style="color: #FF00FF">x</div>', "a.html")
    assert result.returncode == 2, result.stdout
    assert "lint_output.py .......... ✗" in result.stdout


def test_tokens_flag_delegates_to_dominance_and_consumer(tmp_path):
    tokens = tmp_path / "globals.css"
    tokens.write_text(f":root {{ --{ESTRUTURAL_700}: {HEX_ESTRUTURAL_700}; }}",
                      encoding="utf-8")
    result = _run(tmp_path, CLEAN_HTML, "clean.html", "--tokens", str(tokens))
    assert "check_dominance.py" in result.stdout
    assert "check_consumer.py" in result.stdout


def test_without_tokens_flag_prints_the_hint_instead(tmp_path):
    result = _run(tmp_path, CLEAN_HTML, "clean.html")
    assert "passe --tokens" in result.stdout
    assert "check_dominance.py ......" not in result.stdout
    assert "check_consumer.py ......." not in result.stdout


def test_min_height_is_not_a_fixed_height(tmp_path):
    result = _run(tmp_path, "textarea { min-height: 120px; }", "a.css")
    assert "altura fixa" not in result.stdout, result.stdout
    fixa = _run(tmp_path, ".card { height: 120px; }", "a.css")
    assert "altura fixa" in fixa.stdout, fixa.stdout


def test_animation_in_a_page_that_links_tokens_css_is_not_flagged(tmp_path):
    html = ('<link rel="stylesheet" href="tokens.css"><style>'
            '.x { animation: psif-sobe var(--dur-normal) var(--ease-out); }</style>')
    result = _run(tmp_path, html, "a.html")
    assert "movimento reduzido" not in result.stdout, result.stdout


def test_badge_without_text_is_flagged_and_badge_with_text_passes(tmp_path):
    tsx = ('<Badge className="bg-success-100" />\n'
           '<Badge><svg aria-hidden="true"><use href="#psif-cadeado" /></svg></Badge>\n'
           '<Badge className="bg-warning-100">Sigiloso</Badge>\n')
    result = _run(tmp_path, tsx, "a.tsx")
    assert result.stdout.count("selo sem texto") == 2, result.stdout


def test_filter_without_state_is_flagged(tmp_path):
    tsx = ('<div role="group" aria-label="Filtros de documentos">\n'
           '<Button aria-pressed={true}>Todos</Button>\n'
           '<Button>Laudos</Button>\n'
           '<Button aria-haspopup="dialog">Turma</Button>\n'
           '</div>\n')
    result = _run(tmp_path, tsx, "a.tsx")
    assert result.stdout.count("filtro sem estado") == 1, result.stdout


def test_tailwind_violations_fail_through_the_delegated_lint(tmp_path):
    tsx = ('<div className="z-50 shadow-[0_2px_4px_#000] h-[300px] transition-[width]">\n'
           '<button className="size-6 outline-none">x</button>\n</div>\n')
    result = _run(tmp_path, tsx)
    assert result.returncode == 2, result.stdout
    assert "lint_output.py .......... ✗" in result.stdout


def test_lint_warnings_are_counted_in_the_summary(tmp_path):
    result = _run(tmp_path, '<div className="h-[300px] transition-[width]">x</div>')
    assert result.returncode == 0, result.stdout
    assert "0 reprovação(ões), 2 aviso(s)" in result.stdout


def test_english_terms_from_the_rule_are_flagged(tmp_path):
    tsx = ("<span>Status</span>\n<h1>Dashboard</h1>\n<button>Upload</button>\n"
           "<p>Loading…</p>\n<p>Status do ciclo</p>\n")
    result = _run(tmp_path, tsx)
    assert result.stdout.count("termo em inglês") == 5, result.stdout


def test_english_rule_ignores_code(tmp_path):
    tsx = "const x = items.filter((i) => status === 1);\n<p>Situação do ciclo</p>\n"
    result = _run(tmp_path, tsx)
    assert "termo em inglês" not in result.stdout, result.stdout


def test_fixed_height_in_jsx_style_is_flagged(tmp_path):
    result = _run(tmp_path, "<div style={{ height: '120px' }}>b</div>\n<div style={{ minHeight: 120 }}>c</div>\n")
    assert result.stdout.count("altura fixa") == 1, result.stdout


def test_delegated_lint_findings_are_shown(tmp_path):
    result = _run(tmp_path, '<div className="h-[120px]"><p>Texto</p></div>\n')
    assert "altura fixa em contêiner" in result.stdout, result.stdout


def test_icon_only_shadcn_button_and_link_are_flagged(tmp_path):
    tsx = ('<Button variant="ghost" size="icon"><Search /></Button>\n'
           '<Link href="/alunos"><Icon name="psif-voltar" /></Link>\n'
           '<Button variant="ghost" size="icon" aria-label="Pesquisar"><Search /></Button>\n'
           '<Button><Search /> Pesquisar</Button>\n')
    result = _run(tmp_path, tsx)
    assert result.stdout.count("só de ícone sem nome acessível") == 2, result.stdout


def test_field_without_label_is_flagged(tmp_path):
    tsx = ('<Input id="nome" />\n'
           '<Label htmlFor="email">E-mail</Label><Input id="email" />\n'
           '<FieldLabel htmlFor="turma">Turma</FieldLabel><Input id="turma" />\n'
           '<FormItem><FormLabel>Nome</FormLabel><FormControl><Input /></FormControl></FormItem>\n'
           '<input type="hidden" name="id" />\n')
    result = _run(tmp_path, tsx)
    assert result.stdout.count("campo sem rótulo") == 1, result.stdout
    assert "linha 1: campo sem rótulo" in result.stdout


def test_focus_visible_block_that_removes_the_outline_is_not_an_exemption(tmp_path):
    result = _run(tmp_path, ".x:focus-visible { outline: none; }", "a.css")
    assert "foco visível removido" in result.stdout, result.stdout
    anel = _run(tmp_path, ".x { outline: none; }\n.x:focus-visible { box-shadow: 0 0 0 2px "
                          f"var(--{ESTRUTURAL_500}); }}", "b.css")
    assert "foco visível removido" not in anel.stdout, anel.stdout


def test_error_only_on_the_tailwind_border_is_flagged(tmp_path):
    result = _run(tmp_path, '<div className="border border-destructive">x</div>')
    assert "erro só na borda" in result.stdout, result.stdout
    ligado = _run(tmp_path, '<Input aria-invalid={true} aria-describedby="erro-nome" '
                            'className="border-destructive" aria-label="Nome" />')
    assert "erro só na borda" not in ligado.stdout, ligado.stdout


def test_english_in_attributes_is_flagged(tmp_path):
    tsx = ('<Input placeholder="Search" aria-label="Pesquisar" />\n'
           '<Button aria-label="Settings"><Icon name="psif-ajustes" /></Button>\n'
           '<Input placeholder="Pesquisar aluno" aria-label="Pesquisar aluno" />\n')
    result = _run(tmp_path, tsx)
    assert result.stdout.count("termo em inglês") == 2, result.stdout


def test_each_lint_error_counts_in_the_summary(tmp_path):
    tsx = ('<button className="focus-visible:outline-none">a</button>\n'
           f'<div style={{{{ background: "{HEX_ESTRUTURAL_700}" }}}}>b</div>\n')
    result = _run(tmp_path, tsx)
    assert result.returncode == 2, result.stdout
    assert "2 reprovação(ões)" in result.stdout, result.stdout
