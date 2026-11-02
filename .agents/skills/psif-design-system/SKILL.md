---
name: psif-design-system
description: >
  Design system do PSIF, a Plataforma de Suporte Psicopedagógico do IFPB. Use
  ao criar, revisar ou ajustar qualquer tela, página, componente ou protótipo
  do PSIF, em tela estreita ou larga: código React/TSX em Next.js com Tailwind
  e shadcn/ui, CSS ou HTML (Início, atendimentos, alunos, perfil do aluno,
  relatórios, agenda, documentos, evolução, notificações, login, página
  pública). Use também quando o pedido não cita o PSIF pelo nome mas fala de
  sistema de psicopedagogia, de acompanhamento psicopedagógico ou de
  atendimento a alunos no IFPB; ao escolher cor, fonte, espaçamento, ícone,
  tema escuro ou texto de interface para esse produto; e ao ligar os tokens ao
  Tailwind e ao shadcn no frontend do PSIF.
metadata:
  version: "0.18.7"
  last-updated: "2026-11"
---

# PSIF Design System

O PSIF é um sistema web responsivo, sem app nativo. A psicopedagoga o abre
entre um atendimento e outro, em qualquer aparelho, às vezes com o aluno na
sala; o aluno é adolescente, e o laudo dele não pode aparecer numa
notificação. Tudo funciona a partir de 320px de largura.

## Prioridades

Quando duas regras brigarem, vale esta ordem:

1. **Sigilo do aluno** (§16.3).
2. **Acessibilidade WCAG 2.2 AA** (§20).
3. **Consistência**: reutilize o padrão existente antes de inventar variação.

A regra de ouro do visual está em §2.2: fundo céu, cartão branco, ação em
marinho.

## Como usar

1. **Ligue os tokens ao Tailwind e ao shadcn** (§26). Na tela, só utilitária
   ligada a token ou `var(--token)`.
2. **Monte com os componentes de §6.** Se o projeto já tem o componente em
   `src/shared/components`, use o dele.
3. **Desenhe os estados** vazio, erro e carregando, e o dado real (§10).
4. **Decida tela estreita e larga juntas** (§5.11), e toque e mouse (§5.12).
5. **Confira os dois temas** (§25) e **o perfil de quem vê** (§16).
6. **Verifique antes de entregar** (fim deste arquivo).

Caso que a skill não cobre: derive do token existente e do componente mais
parecido. Valor novo entra no `tokens.json` como regra; dúvida de produto vai
para §27.

## Mapa de referências

Cada regra mora num arquivo só, o dono do §; os outros apontam para ele, e o
`scripts/check_refs.py` trava que toda referência resolve.

| Arquivo | § | Abra quando |
|---|---|---|
| `tokens/brand-identity.md` | §1 | a tela mostra o símbolo ou o nome PSIF |
| `foundations/visual-philosophy.md` | §2 | decide camada (céu, cartão, marinho) ou decoração |
| `tokens/colors.md` | §3.1–§3.3 | precisa de cor ou de par de contraste |
| `tokens/scales.md` | §3.4–§3.10 | sombra, raio, espaçamento, ícone, superfície, z-index |
| `tokens/typography.md` | §4 | tamanho e peso de um texto |
| `tokens/layout-grid.md` | §5 | esqueleto da tela, larguras, toque e mouse |
| `components/principles.md` | §6 | qual componente do shadcn faz cada peça, e os estados |
| `components/navigation.md` | §7 | barra lateral, gaveta, barra de ações, breadcrumbs, busca, filtros |
| `components/inputs-actions.md` | §8 | botão, campo, seleção, data, envio de arquivo, caixa de seleção |
| `components/surfaces-overlays.md` | §9 | cartões e folha ou diálogo |
| `ux-patterns/feedback-and-states.md` | §10 | vazio, erro, carregando, toast, confirmação, dado real |
| `components/lists-and-calendar.md` | §11 | listas, tabela, linha do tempo, calendário |
| `components/people-and-status.md` | §12 | avatar, situação do aluno, observações |
| `components/screen-structures.md` | §13 | estrutura de uma tela nova |
| `screen-patterns/dashboards-and-forms.md` | §14–§15 | Início ou formulário |
| `ux-patterns/profiles-and-privacy.md` | §16 | perfis e sigilo |
| `tokens/motion-icons.md` | §17–§18 | movimento ou ícone |
| `ux-patterns/language.md` | §19 | qualquer texto de interface |
| `foundations/accessibility.md` | §20 | rótulo, foco, alvo, leitor de tela |
| `foundations/ux-principles.md` | §21 | fluxo que a skill não cobre |
| `ai-rules/prompt-engineering.md` | §22–§23 | prompt para gerar tela |
| `ai-rules/anti-patterns-checklist.md` | §24 | revisão antes de entregar |
| `tokens/dark-mode.md` | §25 | tema escuro |
| `ai-rules/tailwind-integration.md` | §26 | código de tela: tokens no Tailwind v4 e no shadcn |
| `tokens/palette-backlog.md` | §27 | decisões de produto em aberto |

## Cheat sheet

Única cópia permitida das regras: o mínimo para quem não abre outro arquivo.

```
Fonte:              Figtree, pesos 400/500/600
Camadas:            fundo --surface-base, cartão --surface-raised, ação --navy-700 (§2.2)
Cartão:             --radius-xl (estreita) / --radius-2xl (larga), sem borda, sem sombra
Ação primária:      --navy-700, texto --white, --control-min de altura, --radius-lg
Título de tela:     --fs-display 600 --navy-700, à esquerda (§4.3)
Texto:              --ink-900 · dado-chave --navy-700 · secundário --ink-700
Corpo:              --fs-body · campo --fs-h3 · menor texto --fs-caption
Espaçamento:        escala de 4px · margem --page-pad (larga: --sp-8)
Raio:               por papel (§3.6)
Alvo:               --target-min no toque (§20.6) · --target-fine no mouse (§5.12)
Nunca como texto:   a banlist de scripts/tokens.json (§3.2)
Tema escuro:        mesmos tokens, .dark no <html>, nada de dark: na tela
```

## Assets e scripts

- `assets/tokens.css`: todos os tokens e o bloco `.dark`; entra no
  `globals.css` (§26).
- `assets/icones.svg`: ícones, pelo componente `Icon` (§18).
- `assets/simbolo-psif*.svg|png`: o símbolo (§1).
- `assets/DESIGN.md`: o sistema no formato da skill impeccable, gerado a
  partir dos tokens. `assets/PRODUCT.md`: o produto, no mesmo formato.
- `scripts/check_checklist.py`, `scripts/lint_output.py`,
  `scripts/check_contrast.py`, `scripts/check_dominance.py`,
  `scripts/check_consumer.py`: verificadores (uso em `scripts/README.md`).
- `scripts/tokens.json`: fonte dos tokens. Mudou? Rode
  `scripts/gen_tokens_css.py` e `scripts/gen_design_md.py`; nunca edite
  `tokens.css` nem `DESIGN.md` à mão.
- `scripts/check_all.py`: roda os `--check`, o `check_refs.py` e a suíte de
  `scripts/tests/`.

## Antes de entregar

1. `check_checklist.py` no que você gerou (ele já roda o `lint_output.py`).
   Corrija todo `[ERRO]`; cada `[AVISO]` pede correção ou justificativa.
2. Os itens manuais de §24 que ele lista.
