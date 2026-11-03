# scripts/

Python 3 puro, sem dependência.

Mudar token: edite `scripts/tokens.json` e rode `gen_tokens_css.py` e
`gen_design_md.py` (`--check` confere sem escrever).

Mensagens de erro: `[ERRO] linha N: <o que> (<esperado>, §X.Y)`.

## `scripts/check_all.py`

Roda todos os `--check`, o `check_refs.py` e a suíte. É o que o CI chama.

```sh
python3 scripts/check_all.py           # tudo
python3 scripts/check_all.py --quick   # só os --check
```

## `scripts/check_refs.py`

Toda referência `§N` / `§N.M` precisa de heading. `--quiet` só imprime os
erros.

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

Cor fora da paleta ou escrita literal, token banido como texto, `var()` para
token inexistente, raio e espaçamento fora da escala, sombra preta, z-index
avulso, foco, fonte, alvo, altura fixa e `max-w`. Classe do Tailwind passa
pelas mesmas regras; o que fica com a revisão está em §26.4.

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

Compara os tokens colados no `globals.css` do projeto com o `:root` de
`assets/tokens.css` e acusa token da skill redefinido no `@theme` (§26.5).

```sh
python3 scripts/check_consumer.py src/app/globals.css
```

---

> **Cópia de consumo.** Esta pasta é a cópia de `psif-design-system` para o
> projeto: catálogos, verificadores, geradores de token e testes
> (`scripts/check_all.py` roda tudo). Versão e pacote ficam no
> repositório de origem da skill.
>
> Token muda em `scripts/tokens.json`, com `gen_tokens_css.py` e
> `gen_design_md.py` em seguida. Regra muda na origem, e a skill é exportada
> de novo.
