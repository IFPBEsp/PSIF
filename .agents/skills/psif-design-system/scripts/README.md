# scripts/

Python 3 puro, sem dependência.

Mudar token: edite `scripts/tokens.json` e rode `gen_tokens_css.py` e
`gen_design_md.py` (`--check` confere sem escrever).

Mensagens de erro: `[ERRO] linha N: <o que> (<esperado>, §X.Y)`.

## `scripts/check_all.py`

Roda todos os `--check`, o `check_refs.py` e a suíte. É o que o hook e o CI
chamam.

```sh
python3 scripts/check_all.py           # tudo
python3 scripts/check_all.py --quick   # só os --check
```

## `scripts/check_refs.py`

Toda referência `§N` / `§N.M` precisa de heading.

## `scripts/tests/`

Suíte de regressão, com pytest quando existe e coletor embutido quando não.

## `scripts/gen_tokens_css.py`

Gera `assets/tokens.css` a partir de `scripts/tokens.json`. Lê o bloco de
movimento reduzido de §17.5 e confere o anel de foco contra §20.5.

## `scripts/gen_design_md.py`

Gera `assets/DESIGN.md` (formato lido pela impeccable e pelo Stitch):
frontmatter do `tokens.json`, pesos da tabela de §4.2 e corpo de
`scripts/design_md_body.md`, com cada `{{token}}` preenchido.

## `scripts/skill_config.py`

Lê `skill.config.json`.

## `scripts/check_checklist.py`

Confere a parte automática do checklist de §24, chama `lint_output.py` (e,
com `--tokens`, `check_dominance.py` e `check_consumer.py`) e imprime os
itens manuais.

```sh
python3 scripts/check_checklist.py tela.tsx --tokens src/app/globals.css
```

## `scripts/lint_output.py`

Cor fora da paleta, token banido como texto, `var()` para token inexistente,
raio e espaçamento fora da escala, sombra preta, z-index avulso, fonte e alvo.
Classe utilitária só em parte.

```sh
python3 scripts/lint_output.py tela.tsx [--strict]
```

## `scripts/check_contrast.py`

Contraste WCAG de um par fora da tabela de §3.2. Compõe cor translúcida
sobre o fundo.

```sh
python3 scripts/check_contrast.py ink-700 sky-100
```

## `scripts/check_dominance.py`

Proporção de cor por papel (§3.3), por contagem de declaração.

## `scripts/check_consumer.py`

Compara os tokens colados no `globals.css` do projeto com o `tokens.json`.

---

> **Cópia de consumo.** Esta pasta foi exportada pelo `export_skill.py` do
> repositório de origem de `psif-design-system`: catálogos, verificadores, geradores de
> token e testes (`scripts/check_all.py` roda tudo). Hook, versionamento e
> pacote `dist/` ficam na origem.
>
> Token muda em `scripts/tokens.json`, com `gen_tokens_css.py` e
> `gen_design_md.py` em seguida. Regra muda na origem, e a skill é exportada
> de novo.
