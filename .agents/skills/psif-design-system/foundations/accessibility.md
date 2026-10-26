## 20. ACESSIBILIDADE (WCAG 2.2 AA: inegociável)

Onde o protótipo reprova, a skill corrige, e a correção está em aberto em
§29 até o design ratificar.

### 20.1 Contraste (WCAG 1.4.3 / 1.4.11)

Tabela verificada em §3.2. As três armadilhas do PSIF:

1. Texto secundário em `#7D7D7D` (como no protótipo) reprova: use
   `--ink-700`.
2. "Em acompanhamento" em `--success-700` passa sobre branco e **reprova**
   sobre o céu: situação só dentro de cartão.
3. `--navy-500` é cor de ilustração: como texto, reprova.

### 20.2 Cor nunca é o único canal (WCAG 1.4.1)

Situação do aluno, tipo de evento na linha do tempo e severidade de
notificação sempre têm **texto**. O marcador colorido repete o texto; não o
substitui.

### 20.3 Teclado (WCAG 2.1.1 / 2.1.2 / 2.4.7)

Todo cartão que abre detalhe é um `<a>` ou `<button>` inteiro, não um `<div>`
com clique. Folha modal prende o foco e fecha com Esc.

### 20.4 Ordem de foco (WCAG 2.4.3)

Voltar (←) → título → conteúdo na ordem visual → botão primário do rodapé.
Nas telas-raiz, que não têm voltar: título (ou saudação) → ☰ → conteúdo. Com
a gaveta aberta, o foco fica nela (§7.9). No web: "Pular para o conteúdo" (link que aparece ao receber foco)
→ barra lateral → conteúdo.

### 20.5 Foco visível (WCAG 2.4.7 / 2.4.11)

<!-- ⚠️  Esta seção é CONTRATO de script: `gen_tokens_css.py` confere que os
     três valores abaixo aparecem aqui antes de escrever o anel de foco no
     tokens.css. Mantenha-os em sincronia com `focus_ring` do tokens.json. -->

Anel de foco visível: outline de **2px** sólido em `var(--navy-700)`, com
offset 2px. Contraste do anel: 9.30:1 sobre branco, 7.26:1 sobre o céu. Sobre
o botão primário (que já é `--navy-700`), o offset deixa uma faixa do fundo
entre botão e anel: por isso o offset não é opcional. Nunca `outline: none`
sem substituto.

### 20.6 Alvos de toque e clique (WCAG 2.5.8)

Mínimo **44×44px**: o token `--target-min`. Use `var(--target-min)` em
`min-width` e `min-height` de todo elemento clicável, nunca 44px literal. O
protótipo reprova em quatro lugares:

| Elemento | Protótipo | PSIF |
|---|---|---|
| botão primário | 37–39px de altura | `min-height: var(--control-min)` (48px) |
| campo | 39px | `min-height: var(--control-min)` (48px) |
| filtro (Turma, Série, Período) | 23px | `min-height: var(--target-min)` |
| atalho de Ações Rápidas | 48×43px | 48×48px |

Voltar, menu e chevron: ícone pequeno, área de toque `--target-min`.

### 20.7 Rótulos, nomes e ARIA

- Todo campo tem `<label>` visível. O login e o "Recuperar senha" do
  protótipo usam só placeholder ("Seu E-mail"), o que reprova: o rótulo some
  quando o usuário digita.
- Botão só com ícone (←, ☰, ›) tem `aria-label`: "Voltar", "Abrir menu",
  "Abrir perfil de Maria Ana".
- Senha tem botão "Mostrar senha" com `aria-pressed`.

### 20.8 Leitores de tela

- Barra superior é `<header>`, conteúdo é `<main>`, barra lateral e gaveta são
  `<nav aria-label="Principal">` com `aria-current="page"` no destino ativo.
- Indicador é lido como frase: "8 atendimentos hoje", não "08" seguido de
  rótulo solto.
- Lista de alunos, documentos e notificações é `<ul>`; dados tabulares
  (se houver) são `<table>`, nunca grade de `<div>`.

### 20.9 Estados e feedback acessíveis

Erro de campo: texto em `--danger-700` abaixo do campo, ligado por
`aria-describedby`, campo com `aria-invalid="true"`. Confirmação de envio
("Instruções enviadas") em região `role="status"`.

### 20.10 Movimento e animação (WCAG 2.3.3 / 2.3.1)

Respeite `prefers-reduced-motion` (§17.5). A barra de progresso do splash vira
estado estático com texto "Carregando".

### 20.11 Daltonismo e visão de cores

Verde, amarelo e azul da linha do tempo são indistinguíveis para parte dos
usuários: por isso o tipo de evento é escrito (§11.5).

### 20.12 Contexto de uso: atendimento com o aluno presente

A tela pode estar virada para o aluno ou para a família. Nada sensível
(laudo, diagnóstico, observação) aparece em tela de lista, em notificação ou
em pré-visualização; só dentro do perfil, depois de um toque deliberado
(§16.3).

### 20.13 Zoom, reflow e redimensionamento (WCAG 1.4.4 / 1.4.10)

Nada de altura fixa em cartão com texto: o cartão cresce. A 200% e a 320px de
largura, a grade de indicadores vira coluna única e nada rola na horizontal.

### 20.14 Tema escuro

O tema "Sistema" segue `prefers-color-scheme` do aparelho, e o escuro usa só
os pares verificados de §27.5. Toda tela é conferida nos dois temas: contraste,
foco visível e estado que não depende só da cor.
