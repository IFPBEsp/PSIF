## 20. ACESSIBILIDADE (WCAG 2.2 AA, inegociável)

### 20.1 Contraste (WCAG 1.4.3 / 1.4.11)

Pares verificados em §3.2 (escuro em §25.5). Par fora da tabela passa por
`check_contrast.py`.

### 20.2 Cor nunca é o único canal (WCAG 1.4.1)

Situação do aluno, tipo de evento da linha do tempo e severidade de
notificação sempre têm texto. A cor repete o texto, não o substitui. Estado
vai em texto e ícone, nunca numa faixa colorida na borda de cartão, alerta
ou linha.

### 20.3 Teclado (WCAG 2.1.1 / 2.1.2)

Cartão que abre detalhe é `<a>` ou `<button>` inteiro, nunca `<div>` com
clique. Folha, diálogo e gaveta prendem o foco e fecham com Esc.

### 20.4 Ordem de foco (WCAG 2.4.3)

- Tela de tarefa: voltar → título → campos → botão primário. O botão vem
  depois dos campos no DOM em qualquer largura (§5.6).
- Tela-raiz na tela estreita: ☰ → título ou saudação → conteúdo, a ordem do
  DOM (§5.1). Com a gaveta aberta, o foco fica nela (§7.9).
- A partir de `--bp-md`: "Pular para o conteúdo" (link que aparece ao
  receber foco) → barra lateral → conteúdo.

### 20.5 Foco visível (WCAG 2.4.7 / 2.4.11)

**Botões, links e abas.** Anel de foco: outline de 2px sólido em
`var(--navy-700)`, offset 2px. O offset deixa uma faixa do fundo entre o
botão primário e o anel, que é da mesma cor do botão; por isso não é
opcional. O tokens.css já aplica o anel em `:focus-visible`.

**Campos.** O foco marca o campo inteiro, não só o `<input>` de dentro:

- O `<input>`/`<textarea>` interno fica com `outline: none`; o anel vai no
  contêiner do campo (o `<label>` ou `<div>` que segura ícone, texto e
  botão), via `:focus-within`.
- Anel interno de 2px, por `box-shadow: inset`, sem offset, acompanhando o
  `--radius-lg` do campo.
- Campo com borda (texto, data, seleção, texto longo): a borda de 1px passa
  para `--navy-700` e ganha `inset 0 0 0 1px var(--navy-700)`, somando 2px.
  O fundo continua `--white`.
- Campo sem borda (busca, fundo `--ink-100`): o fundo vira `--white` e ganha
  `inset 0 0 0 2px var(--navy-700)`.
- Com erro (§10.7), o anel e a borda usam `--danger-700` no lugar de
  `--navy-700`.
- Transição de fundo e sombra em `--dur-fast` `--ease-standard`.
- Vale para clique e teclado (`:focus-within`, não `:focus-visible`): quem
  digita precisa ver onde está o cursor.

Nunca `outline: none` sem um desses substitutos.

Tailwind (§26.8). O `aria-invalid` fica no `<input>`, por isso o contêiner
lê o erro com `has-[[aria-invalid=true]]:`:

    contêiner: rounded-lg border border-input bg-card
               focus-within:border-primary focus-within:ring-1
               focus-within:ring-inset focus-within:ring-primary
               has-[[aria-invalid=true]]:border-destructive
               has-[[aria-invalid=true]]:focus-within:ring-destructive
               transition-[background-color,box-shadow] duration-(--dur-fast)
    busca:     rounded-lg bg-ink-100 focus-within:bg-card
               focus-within:ring-2 focus-within:ring-inset
               focus-within:ring-primary

### 20.6 Alvos (WCAG 2.5.8)

Todo clicável tem `min-width` e `min-height` de `var(--target-min)`; botão
primário de largura total e campo, `var(--control-min)`; botão compacto,
`var(--target-min)` (§8.1). Ícone pequeno não encolhe a área: voltar, menu e
chevron mantêm o alvo. As exceções, com mouse e no calendário, estão em
§5.12.

### 20.7 Rótulos, nomes e ARIA

- Todo campo tem `<label>` visível; placeholder não é rótulo. A busca é a
  única exceção (§7.7).
- Botão só de ícone tem `aria-label`: "Voltar", "Abrir menu", "Abrir perfil
  de Maria Ana".
- Senha tem botão "Mostrar senha" com `aria-pressed`.

### 20.8 Leitores de tela

- Barra de ações em `<header>`, conteúdo em `<main>`, barra lateral e gaveta
  em `<nav aria-label="Principal">` com `aria-current="page"` no destino
  ativo.
- Indicador é lido como frase: "8 atendimentos hoje".
- Lista de alunos, documentos e notificações é `<ul>`; tabela é `<table>`,
  nunca grade de `<div>`.

### 20.9 Estados acessíveis

Erro de campo em `--danger-700` abaixo do campo, ligado por
`aria-describedby`, com `aria-invalid="true"` no campo. Confirmação
("Instruções enviadas") em `role="status"`.

### 20.10 Movimento (WCAG 2.3.3)

Respeite `prefers-reduced-motion` (§17.5). Barra de progresso vira estado
estático, com o mesmo rótulo da ação ("Enviando…", §10.4).

### 20.11 Daltonismo

As cores da linha do tempo se confundem para parte das pessoas: o tipo de
evento vai escrito (§11.5).

### 20.12 Aluno presente

A tela pode estar virada para o aluno ou para a família. Dado sensível só
dentro do perfil, depois de abrir o item (§16.3).

### 20.13 Zoom e reflow (WCAG 1.4.4 / 1.4.10)

Cartão com texto não tem altura fixa: cresce. A 200% e a 320px de largura a
página não rola na horizontal; só a linha de filtros (§7.6) e a tabela larga
(§11.8) rolam dentro de si. Os indicadores seguem em 2×2: cada célula fica com
uns 120px (320 − 2 × `--page-pad` − 2 × `--card-pad`, dividido por 2), que
comportam o número e o rótulo em duas linhas.

### 20.14 Tema escuro

Toda tela é conferida nos dois temas: contraste (§25.5), foco visível e
estado que não depende só da cor.
