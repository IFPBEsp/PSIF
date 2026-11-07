"""Testes de lint_output.py."""

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _fixtures import TOKENS, concreto, ESTRUTURAL_700, HEX_ESTRUTURAL_700  # noqa: E402

SCRIPT = Path(__file__).resolve().parent.parent / "lint_output.py"


def _run(tmp_path, html, *extra_args):
    f = tmp_path / "sample.html"
    f.write_text(html, encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(f), *extra_args],
        capture_output=True,
        text=True,
    )


BAD_HTML = """
<style>
.btn-primary {
  background: #FF00FF;
  color: var(--accent-500);
  border-radius: 7px;
  padding: 13px 18px;
  box-shadow: 0 2px 4px rgba(0,0,0,.4);
  font-family: Arial, sans-serif;
}
.icon-btn { height: 24px; }
.card { color: var(--fs-subtitlee); }
</style>
<button class="btn-primary">Salvar</button>
<div class="icon-btn">x</div>
"""

GOOD_HTML = """
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
GOOD_HTML = concreto(GOOD_HTML)

WARNING_ONLY_CSS = """
<style>.card { box-shadow: 0 2px 4px rgba(0,0,0,.4); }</style>
"""


def test_catches_every_planted_violation(tmp_path):
    result = _run(tmp_path, BAD_HTML)
    assert result.returncode == 2, result.stdout
    out = result.stdout
    assert "cor '#FF00FF' fora da paleta (var(--token), §3.1)" in out
    assert "--accent-500 não existe" in out
    assert "border-radius 7px fora da escala" in out
    assert "13px" in out and "18px" in out
    assert "preto puro" in out
    assert "font-family 'Arial, sans-serif' fora da família (var(--font-sans), §4.1)" in out
    assert "--fs-subtitlee não existe" in out
    assert "abaixo do alvo mínimo de 44px (var(--target-min), §20.6)" in out


def test_findings_are_grouped_by_file_and_summary_is_last(tmp_path):
    result = _run(tmp_path, BAD_HTML)
    linhas = result.stdout.strip().splitlines()
    assert linhas[0] == "── sample.html"
    assert all(l.startswith("   [") for l in linhas[1:-2]), result.stdout
    assert re.fullmatch(r"\d+ erro\(s\), \d+ aviso\(s\)\.", linhas[-1])


def test_clean_file_has_zero_findings(tmp_path):
    result = _run(tmp_path, GOOD_HTML)
    assert result.returncode == 0, result.stdout
    assert "Nenhum problema encontrado" in result.stdout
    assert result.stdout.strip().splitlines()[-1] == "0 erro(s), 0 aviso(s)."


def test_the_skills_own_generated_css_passes_its_own_lint():
    css = SCRIPT.parent.parent / "assets" / "tokens.css"
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(css), "--strict"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, (
        "assets/tokens.css não passa no lint da própria skill:\n" + result.stdout
    )


def test_strict_flag_turns_warnings_into_failures(tmp_path):
    normal = _run(tmp_path, WARNING_ONLY_CSS)
    strict = _run(tmp_path, WARNING_ONLY_CSS, "--strict")
    assert normal.returncode == 0, normal.stdout
    assert "AVISO" in normal.stdout
    assert strict.returncode == 2, strict.stdout


def test_stdin_mode_via_dash():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "-"],
        input=GOOD_HTML,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


ICONE_OK = TOKENS["icon_color_allowed"][0]
ICONE_RUIM = next(n for n in TOKENS["text_color_banlist"]
                  if n not in TOKENS["icon_color_allowed"])

ICON_HTML = """
<style>.lista .chevron { color: var(--TOKEN_ICONE); }</style>
<a href="#">Maria Ana
  <svg style="color: var(--TOKEN_ICONE)" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"></path></svg>
  <span class="material-symbols-rounded" style="color: var(--TOKEN_ICONE)">chevron_right</span>
</a>
""".replace("TOKEN_ICONE", ICONE_OK)

TEXT_HTML = """
<style>.icon-label { color: var(--TOKEN_ICONE); }</style>
<p style="color: var(--TOKEN_ICONE)">Informática · 3º ano</p>
""".replace("TOKEN_ICONE", ICONE_OK)

BAD_ICON_HTML = """
<svg style="color: var(--TOKEN_RUIM)"><path d="M9 6l6 6-6 6"></path></svg>
""".replace("TOKEN_RUIM", ICONE_RUIM)


def test_icon_takes_the_ui_floor_not_the_text_floor(tmp_path):
    icone = _run(tmp_path, ICON_HTML)
    assert icone.returncode == 0, icone.stdout

    texto = _run(tmp_path, TEXT_HTML)
    assert texto.returncode == 2, texto.stdout
    assert "2 erro(s)" in texto.stdout and "cor de texto" in texto.stdout

    ruim = _run(tmp_path, BAD_ICON_HTML)
    assert ruim.returncode == 2, ruim.stdout
    assert "cor de ícone" in ruim.stdout


INLINE_TARGET_HTML = """
<style>.cartao { padding: var(--sp-4); }</style>
<button class="btn" style="min-height: 32px">Salvar</button>
<a href="#" style="height: 30px">Início</a>
<span style="height: 30px">texto</span>
<button style="min-height: 48px"><svg style="width: 16px; height: 16px"></svg> Ok</button>
"""


def test_inline_touch_target_is_checked(tmp_path):
    result = _run(tmp_path, INLINE_TARGET_HTML)
    assert result.stdout.count("abaixo do alvo mínimo") == 2, result.stdout
    assert "<button> declara min-height: 32px" in result.stdout
    assert "<a> declara height: 30px" in result.stdout


def test_hex_cited_in_a_comment_is_not_a_palette_error(tmp_path):
    html = """
<style>
/* Antes era #FF00FF. */
.nota { color: var(--ink-900); }
</style>
<!-- antes: #FF00FF -->
<p class="nota">Texto</p>
"""
    result = _run(tmp_path, html)
    assert "#FF00FF" not in result.stdout, result.stdout


def test_banned_gray_on_an_icon_utility_is_allowed_but_not_on_text(tmp_path):
    tsx = (
        '<Search className="size-5 text-ink-600" aria-hidden />\n'
        '<svg className="size-5 text-ink-600" aria-hidden="true"></svg>\n'
        '<p className="text-ink-600">texto</p>\n'
    )
    f = tmp_path / "a.tsx"
    f.write_text(tsx, encoding="utf-8")
    result = subprocess.run([sys.executable, str(SCRIPT), str(f)], capture_output=True, text=True)
    assert result.stdout.count("pinta texto com --ink-600") == 1, result.stdout
    assert "linha 3" in result.stdout, result.stdout


def test_shadcn_role_variables_are_known_tokens(tmp_path):
    result = _run(tmp_path, '<div style="background: var(--popover); color: var(--popover-foreground)"></div>')
    assert "--popover" not in result.stdout, result.stdout


MOUSE_CSS = """
<style>
@media (hover: hover) and (pointer: fine) {
  .row-btn { min-height: 32px; }
  .menu-item { min-height: 20px; }
}
.icon-btn { min-height: 32px; }
</style>
"""


def test_target_fine_is_accepted_only_under_fine_pointer(tmp_path):
    out = _run(tmp_path, MOUSE_CSS).stdout
    assert "'.row-btn'" not in out, out
    assert "'.menu-item' declara min-height: 20px, abaixo do alvo mínimo de 32px" in out
    assert "§5.12" in out
    assert "'.icon-btn' declara min-height: 32px, abaixo do alvo mínimo de 44px" in out


def _run_as(tmp_path, texto, nome):
    f = tmp_path / nome
    f.write_text(texto, encoding="utf-8")
    return subprocess.run([sys.executable, str(SCRIPT), str(f)], capture_output=True, text=True)


def test_tailwind_arbitrary_values_follow_the_css_rules(tmp_path):
    tsx = ('<p className="text-[10px] text-[#7D7D7D] bg-[#244A69] dark:bg-black">a</p>\n'
           '<p className="text-black bg-blue-700">b</p>\n'
           "<p style={{ color: '#7D7D7D' }}>c</p>\n")
    result = _run_as(tmp_path, tsx, "a.tsx")
    out = result.stdout
    assert result.returncode == 2, out
    assert "'text-[10px]' fora da escala" in out and "§4.2" in out
    assert out.count("é --ink-600 como cor de texto") == 2
    assert "cor literal em 'bg-[#244A69]'" in out and "§26.6" in out
    assert "variante dark: em 'dark:bg-black'" in out and "§25.2" in out
    assert "'text-black' com cor fora da paleta" in out
    assert "'bg-blue-700' fora do símbolo" in out and "§1.4" in out


def test_token_scale_in_brackets_passes(tmp_path):
    result = _run_as(tmp_path, '<p className="text-[12px] rounded-[8px] z-[100]">a</p>', "a.tsx")
    assert "fora da escala" not in result.stdout, result.stdout


def test_dark_token_used_directly_is_flagged(tmp_path):
    result = _run_as(tmp_path, ".x { color: var(--dark-ink-900); }", "a.css")
    assert result.returncode == 2, result.stdout
    assert "--dark-ink-900 usado direto na tela" in result.stdout


def test_help_does_not_crash():
    r = subprocess.run([sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "usage" in r.stdout


def test_classes_inside_cn_and_cva_are_checked(tmp_path):
    tsx = ('const v = cva("rounded-[7px] text-[#7D7D7D] dark:bg-black", '
           '{ variants: { size: { sm: "h-8" } } });\n'
           '<p className={cn("text-[10px] bg-red-500", c)}>a</p>\n')
    out = _run_as(tmp_path, tsx, "a.tsx").stdout
    assert "border-radius 7px fora da escala" in out
    assert "é --ink-600 como cor de texto" in out
    assert "variante dark: em 'dark:bg-black'" in out
    assert "'text-[10px]' fora da escala" in out
    assert "'bg-red-500' com a família 'red'" in out


def test_opacity_suffix_does_not_hide_the_color(tmp_path):
    tsx = '<p className="text-black/50 text-ink-600/80 bg-red-500/50 text-[#7D7D7D]/50">a</p>'
    out = _run_as(tmp_path, tsx, "a.tsx").stdout
    assert "'text-black/50' com cor fora da paleta" in out
    assert "pinta texto com --ink-600" in out
    assert "família 'red'" in out
    assert "'#7D7D7D' é --ink-600 como cor de texto" in out


def test_token_reference_in_class_follows_banlist_and_theme(tmp_path):
    tsx = ('<p className="text-(--ink-600)">a</p>\n<p className="text-[var(--ink-600)]">b</p>\n'
           '<p className="text-[var(--dark-navy-700)]">c</p>\n')
    out = _run_as(tmp_path, tsx, "a.tsx").stdout
    assert "linha 1: --ink-600 como cor de texto" in out, out
    assert "linha 2: --ink-600 como cor de texto" in out, out
    assert "--dark-navy-700 usado direto na tela" in out


def test_black_shadow_in_hex_keyword_and_utility(tmp_path):
    for texto, nome in ((".x { box-shadow: 0 2px 4px #000; }", "a.css"),
                        (".x { box-shadow: 0 2px 4px black; }", "b.css"),
                        ('<div className="shadow-[0_4px_8px_#000]">a</div>', "c.tsx")):
        assert "preto puro" in _run_as(tmp_path, texto, nome).stdout, nome


def test_tailwind_z_index_needs_a_layer_token(tmp_path):
    out = _run_as(tmp_path, '<div className="z-50 z-0 z-(--z-modal)">a</div>', "a.tsx").stdout
    assert "'z-50': z-index fora das camadas" in out
    assert "'z-0'" not in out and "z-(--z-modal)'" not in out


def test_fixed_white_does_not_follow_the_theme(tmp_path):
    out = _run_as(tmp_path, '<p className="text-white bg-white">a</p>', "a.tsx").stdout
    assert out.count("branco fixo do Tailwind") == 2, out
    css = _run_as(tmp_path, ":root { --x: #fff; }\n.y { color: #fff; background: url(white.png); }",
                  "a.css").stdout
    assert css.count("é branco fixo") == 1, css


def test_css_font_size_follows_the_scale(tmp_path):
    out = _run_as(tmp_path, ".a { font-size: 11px; }\n.b { font-size: 15px; }", "a.css").stdout
    assert "tamanho '11px' em 'font-size' fora da escala" in out
    assert "'15px'" not in out


def test_class_attribute_before_style_does_not_hide_the_declaration(tmp_path):
    out = _run_as(tmp_path, '<p class="md:p-4" style="color:#7D7D7D">x</p>', "a.html").stdout
    assert "é --ink-600 como cor de texto" in out


def test_touch_target_in_utility_classes(tmp_path):
    tsx = ('<button className="size-6">a</button>\n'
           '<Button className="mouse:size-6 size-(--target-min)">b</Button>\n'
           '<Button className="size-(--target-min) mouse:size-(--target-fine)">c</Button>\n'
           '<Link className="h-8">d</Link>\n'
           '<Icon className="size-4" />\n')
    out = _run_as(tmp_path, tsx, "a.tsx").stdout
    assert "linha 1: <button> com 'size-6' (24px), abaixo do alvo de 44px" in out
    assert "linha 2: <Button> com 'size-6' (24px), abaixo do alvo de 32px" in out and "§5.12" in out
    assert "linha 3" not in out
    assert "linha 4: <Link> com 'h-8'" in out
    assert "linha 5" not in out


def test_outline_none_needs_focus_visible(tmp_path):
    out = _run_as(tmp_path, '<button className="outline-none">a</button>\n'
                            '<button className="outline-none focus-visible:ring-2">b</button>',
                  "a.tsx").stdout
    assert "linha 1: 'outline-none' sem anel em focus-visible:" in out
    assert "linha 2" not in out


def test_layout_transition_and_fixed_height_in_brackets(tmp_path):
    out = _run_as(tmp_path, '<div className="transition-[width] h-[300px] min-h-[300px]">a</div>',
                  "a.tsx").stdout
    assert "'transition-[width]' anima width" in out
    assert "'h-[300px]': altura fixa" in out
    assert "'min-h-[300px]'" not in out


def test_lucide_icons_take_the_icon_floor(tmp_path):
    tsx = ('import { ChevronRight, X as Fechar } from "lucide-react";\n'
           '<ChevronRight className="size-4 text-ink-600" />\n'
           '<Fechar className="text-ink-600" />\n'
           '<Seta className="text-ink-600" />\n')
    out = _run_as(tmp_path, tsx, "a.tsx").stdout
    assert "linha 2" not in out and "linha 3" not in out
    assert "linha 4: classe 'text-ink-600' pinta texto" in out


def test_inner_input_outline_none_passes_when_container_has_focus_within(tmp_path):
    tsx = ('<label className="rounded-lg border border-input focus-within:ring-1 '
           'focus-within:ring-inset focus-within:ring-primary">\n'
           '<input className="outline-none" aria-label="Pesquisar aluno" />\n</label>\n')
    result = _run_as(tmp_path, tsx, "campo.tsx")
    assert "outline-none" not in result.stdout, result.stdout
    sem_anel = _run_as(tmp_path, '<input className="outline-none" />\n', "solto.tsx")
    assert "'outline-none' sem anel" in sem_anel.stdout, sem_anel.stdout


def test_strict_passes_a_correct_tailwind_screen(tmp_path):
    tela = tmp_path / "cartao.tsx"
    tela.write_text(
        '<a href="/agenda" className="flex min-h-(--target-min) items-center gap-4 '
        'rounded-xl bg-card p-4 hover:bg-ink-100 md:rounded-2xl">\n'
        '  <span className="text-h3 font-semibold text-primary">Quinta, 05/11</span>\n'
        '  <span className="text-small text-ink-700">Atendimento individual</span>\n</a>\n',
        encoding="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPT), "--strict", str(tela)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout
    assert "[INFO]" in r.stdout


def test_fixed_height_in_tailwind_scale_is_flagged(tmp_path):
    tsx = ('<div className="h-30 rounded-xl bg-card p-4"><p>Texto</p></div>\n'
           '<img className="h-32" alt="Foto" />\n<div className="h-10">ok</div>\n')
    result = _run_as(tmp_path, tsx, "a.tsx")
    assert result.stdout.count("altura fixa") == 1, result.stdout
    assert "'h-30'" in result.stdout


def test_max_width_outside_tokens_is_flagged(tmp_path):
    tsx = ('<main className="mx-auto max-w-(--w-content)">a</main>\n'
           '<div className="max-w-[70ch] max-w-full">b</div>\n'
           '<div className="max-w-7xl">c</div>\n'
           '<div className="max-w-[900px]">d</div>\n'
           '<div className="max-w-(--qualquer)">e</div>\n'
           '<p className="max-w-prose">f</p>\n'
           '<style>.x { max-width: 960px; } .y { max-width: var(--w-form); }</style>\n')
    result = _run_as(tmp_path, tsx, "a.tsx")
    out = result.stdout
    assert out.count("fora dos tokens de largura") == 4, out
    assert "'max-w-prose'" in out, out
    assert "max-width: 960px fora dos tokens" in out, out
    assert "max-w-(--w-content)'" not in out and "max-w-[70ch]'" not in out


def test_focus_visible_outline_none_is_not_a_ring(tmp_path):
    tsx = ('<button className="focus-visible:outline-none">a</button>\n'
           '<button className="outline-hidden">b</button>\n'
           '<button className="outline-none focus-visible:ring-2 focus-visible:ring-ring">c</button>\n')
    out = _run_as(tmp_path, tsx, "a.tsx").stdout
    assert "linha 1: 'outline-none' sem anel" in out, out
    assert "linha 2: 'outline-hidden' sem anel" in out, out
    assert "linha 3" not in out, out


def test_palette_color_written_literal_in_css_is_flagged(tmp_path):
    css = (f".card {{ background: {HEX_ESTRUTURAL_700}; }}\n"
           f":root {{ --{ESTRUTURAL_700}: {HEX_ESTRUTURAL_700}; }}\n"
           f".ok {{ background: var(--{ESTRUTURAL_700}); }}\n")
    css += ".sombra { box-shadow: 0 1px 2px rgba(36, 74, 105, .08); }\n"
    out = _run_as(tmp_path, css, "a.css").stdout
    assert out.count("cor literal") == 1, out
    assert f"linha 1: cor literal '{HEX_ESTRUTURAL_700}' (--{ESTRUTURAL_700})" in out, out
    assert "§26.6" in out


def test_tailwind_black_shadow_and_radius_off_scale(tmp_path):
    tsx = '<div className="shadow-lg rounded-3xl shadow-acao rounded-2xl shadow-none">a</div>\n'
    result = _run_as(tmp_path, tsx, "a.tsx")
    out = result.stdout
    assert "'shadow-lg' é a sombra preta do Tailwind" in out and "§3.4" in out, out
    assert "'rounded-3xl' fora da escala de raio" in out and "§3.6" in out, out
    assert "shadow-acao'" not in out and "rounded-2xl'" not in out and "shadow-none'" not in out


def test_fixed_height_is_fine_on_media_skeleton_and_scroll_area(tmp_path):
    tsx = ('<Image className="h-40" src="/a.png" alt="" />\n'
           '<Skeleton className="h-32 w-full" />\n'
           '<ScrollArea className="h-72">a</ScrollArea>\n'
           '<div className="h-40"><p>Texto</p></div>\n')
    out = _run_as(tmp_path, tsx, "a.tsx").stdout
    assert out.count("altura fixa") == 1 and "linha 4" in out, out


def test_max_width_accepts_size_tokens_and_component_vars(tmp_path):
    tsx = ('<span className="max-w-(--target-min) max-w-(--avatar-md)">a</span>\n'
           '<aside className="max-w-(--sidebar-width)">b</aside>\n')
    out = _run_as(tmp_path, tsx, "a.tsx").stdout
    assert "fora dos tokens de largura" not in out, out


def test_stray_z_index_is_an_error_in_css_like_in_the_utility(tmp_path):
    result = _run_as(tmp_path, ".x { z-index: 9999; }", "a.css")
    assert result.returncode == 2, result.stdout
    assert "[ERRO] linha 1: z-index 9999 fora das camadas" in result.stdout


def test_js_line_comment_is_not_a_declaration(tmp_path):
    result = _run_as(tmp_path, "// z-index: 9999;\nconst a = 1;\n", "a.tsx")
    assert result.returncode == 0, result.stdout
