# Design System: PSIF

Resumo do design system para ferramentas que leem `DESIGN.md` na raiz do
projeto (impeccable, Stitch). A fonte completa é a skill `psif-design-system`;
as § citadas são dela. Em conflito, a skill vence.

## Overview

**Creative North Star: "Céu, cartão, marinho"**

O PSIF é a ferramenta de trabalho da psicopedagoga do IFPB, aberta entre um
atendimento e outro, às vezes com o aluno na sala. O visual é calmo e
institucional, não clínico: uma família de azul, fundo claro, nada que pisque.
Cada cartão branco responde uma pergunta ("quem atendo hoje?", "o que
falta?"), e o dado vem primeiro: nome, horário e número em marinho.

É uma ferramenta, não uma vitrine. A marca vive na cor, na fonte e na
densidade; navegação e controles são os que todo mundo já sabe usar. Só a
página pública pode chamar atenção.

**Key Characteristics:**
- Símbolo: cérebro com cruz, branco, sobre quadrado {{blue-300}} de cantos
  arredondados (`assets/simbolo-psif.svg`; só o glifo, em `currentColor`, em
  `simbolo-psif-glifo.svg`). Glifo só em branco ou marinho.
- Três planos: céu no chão, cartão branco para o conteúdo, marinho para a ação.
- Uma família tipográfica, pesos 400, 500 e 600.
- Plano por padrão: cartão sem borda e sem sombra.
- Raio por papel: cartão {{radius-xl}} na tela estreita e {{radius-2xl}} na
  larga; botão, campo e folha {{radius-lg}}; quadro de ícone {{radius-md}};
  pílula em avatar, filtro e selo.
- Web responsivo a partir de 320px, com toque ou mouse em qualquer largura.
- WCAG 2.2 AA inegociável.

## Colors

Azul institucional sobre céu claro; cor de estado só onde carrega significado.

### Primary
- **Marinho IFPB** ({{navy-700}}): ação primária, título de tela, número de
  indicador, nome e horário: o que se clica e o que se lê primeiro. Hover
  ({{navy-800}}) e pressionado ({{navy-900}}) do botão primário.

### Tertiary
- **Céu médio** ({{sky-300}}): fundo do atalho de Ações rápidas, do avatar
  sem foto e da seleção de texto.
- **Azul da marca** ({{blue-700}}, {{blue-300}}): só o símbolo.
- **Estados**: sucesso ({{success-700}}), atenção ({{warning-700}}) e erro
  ({{danger-700}}), com os fundos claros da mesma família: sempre com texto
  junto, nunca só a cor.

### Neutral
- **Céu** ({{sky-100}}): fundo de toda tela; item ativo da barra lateral.
- **Branco** ({{white}}): cartão, campo, barra lateral, folha modal.
- **Tinta** ({{ink-900}}): texto principal. **Cinza de leitura**
  ({{ink-700}}): texto secundário.
- **Cinza de ícone** ({{ink-600}}): chevron, ícone de campo, borda de campo.
- **Divisória** ({{ink-200}}) e **fundo de hover** ({{ink-100}}).

### Named Rules
**A Regra de Ouro.** Fundo céu, cartão branco, ação em marinho. O único
bloco largo de marinho na tela é o botão primário.

**A Regra do Cinza que Não É Texto.** `ink-600`, `ink-500`, `navy-500`,
`sky-300` e `blue-300` nunca pintam texto: todos reprovam AA. Texto
secundário é {{ink-700}}.

## Typography

**Body Font:** Figtree (with system-ui)

**Character:** Uma família só, humanista e legível, carrega título, rótulo,
número e corpo. Hierarquia por tamanho e peso, nunca por caixa alta.

### Hierarchy
- **Display** (600, {{fs-display}}): título de tela em marinho, à esquerda,
  abaixo da barra de ações (folha e autenticação centralizam); número de
  indicador; título da página pública.
- **H1** (600, {{fs-h1}}): saudação do Início; marca na barra lateral.
- **H2** (600, {{fs-h2}}): nome do aluno em cartão; rótulo do botão primário.
- **H3** (500, {{fs-h3}}): rótulo e valor de campo.
- **Body** (400, {{fs-body}}, {{lh-normal}}): linha de lista e texto de cartão;
  título de cartão em 600. Texto corrido até 70ch.
- **Small** (400, {{fs-small}}): descrição, placeholder, filtro.
- **Caption** (400, {{fs-caption}}): metadado, rótulo de atalho. Nada abaixo
  disso.

### Named Rules
**A Regra do Número Tabular.** Horário, data, indicador e matrícula em
`tabular-nums`, para que a coluna não dance.

## Layout

Web responsivo, da tela estreita para a larga, por `min-width`. Ritmo em degraus de {{sp-1}},
{{sp-6}} entre cartões e entre campos.

- **Estreita** (abaixo de {{bp-md}}): coluna única, margem de {{page-pad}},
  navegação em gaveta, ação primária numa faixa presa à base. Acima da barra
  de ações, a área segura do aparelho, com mínimo de {{sp-4}}.
- **Larga, faixa intermediária** ({{bp-md}} a {{bp-lg}}): barra lateral recolhida a
  ícones, painel e perfil em coluna única, margem de {{sp-8}}, folha vira diálogo,
  listagem vira tabela com as colunas principais.
- **A partir de {{bp-lg}}:** barra lateral aberta de {{w-sidebar}},
  indicadores em linha de 4, grade de 3 colunas com a lista principal em 2 e
  o apoio em 1; formulário em 3 colunas.
- **Monitor grande:** conteúdo até {{w-content}}, centralizado ao lado da
  barra lateral. Texto corrido até 70ch, diálogo até {{w-form}}, login até
  {{w-auth}}.

A ação primária fica à direita do título a partir de {{bp-md}}. Alvo mínimo
de {{target-min}}; botão e campo com {{control-min}}. Com mouse, ação densa
pode usar {{target-fine}}.

## Elevation & Depth

Plano por padrão: o cartão se separa do céu pelo branco. A sombra é tingida
de marinho, nunca preta, e só aparece no que flutua ou chama a ação: botão
primário, cartão de login, folha, diálogo, toast, gaveta e resultados da
busca global.

### Shadow Vocabulary
- **Ação** (`box-shadow: {{sh-sm}}`): botão primário e cartão de login.
- **Flutuante** (`box-shadow: {{sh-md}}`): folha, diálogo, toast, gaveta e
  resultados da busca; folha e diálogo sobre o véu ({{overlay}}).

### Named Rules
**A Regra do Plano.** Sem gradiente, sem vidro, sem desfoque, sem sombra em
cartão comum.

## Shapes

O raio segue o papel. Cartão {{radius-xl}} na tela estreita e
{{radius-2xl}} na larga; botão, campo, folha e cartão de login {{radius-lg}}; quadro de ícone,
linha clicável e atalho {{radius-md}}; caixa de seleção {{radius-xs}};
pílula em avatar, filtro, selo e botão só de ícone. Borda existe em campo e
em botão secundário; filtro inativo e área de envio usam uma linha
translúcida de marinho sobre o céu.

## Components

Valores no frontmatter; regra completa no § da skill.

### Buttons (§8.1)
- **Primary:** fundo {{navy-700}}, texto branco 600, {{radius-lg}}, altura
  {{control-min}}, sombra de ação; largura total na tela estreita, automática
  na larga. Um por tela.
- **Hover / Pressed / Focus:** {{navy-800}}, {{navy-900}} e o anel de §20.5.
- **Secondary:** fundo branco, borda de 1px e texto em marinho.

### Chips (§7.6)
- Pílula com borda de 1px em {{line-on-sky}}, texto marinho em {{fs-small}},
  altura {{target-min}}; ativo em marinho com texto branco.

### Badges (§12.2)
- Pílula com fundo -100 e texto -700 da família, {{fs-caption}} 600, ponto de
  {{sp-2}} antes do texto. Sempre com texto.

### Cards / Containers (§9.1)
- {{radius-xl}} na tela estreita, {{radius-2xl}} na larga; branco, sem borda
  e sem sombra, {{card-pad}}.

### Inputs / Fields (§8.3, §20.5)
- Fundo branco, borda de 1px {{ink-600}}, {{radius-lg}}, altura
  {{control-min}}, valor em {{fs-h3}} 500 marinho, rótulo visível acima.
- Foco no contêiner, por `:focus-within`; erro em {{danger-700}} com
  mensagem em texto; desabilitado em {{o-disabled}}.

### Navigation (§7)
- Gaveta na tela estreita; barra lateral a partir de {{bp-md}}, recolhida a
  ícones até {{bp-lg}}; item ativo em {{sky-100}} com texto marinho 600.

### Ações rápidas (§7.8)
- Até quatro por linha; quadrado {{sky-300}} de {{sp-12}} com ícone marinho
  e rótulo em {{fs-caption}}.

## Do's and Don'ts

### Do:
- **Do** consumir só `var(--token)` do `tokens.css` da skill.
- **Do** desenhar os estados vazio, erro e carregando.
- **Do** conferir cada tela em 320px, em {{bp-md}} e em {{bp-lg}}.
- **Do** escrever tipo e situação em texto; a cor só repete.
- **Do** usar ícones de linha do sprite da skill (§18).

### Don't:
- **Don't** pintar área grande de marinho.
- **Don't** depender de hover: menu suspenso e alvo menor só com mouse.
- **Don't** usar {{ink-600}} como cor de texto.
- **Don't** usar emoji como ícone ou marcador.
- **Don't** pôr dois botões primários, cartão dentro de cartão ou faixa
  colorida na borda de cartão.
- **Don't** usar texto abaixo de {{fs-caption}} nem campo abaixo de {{fs-h3}}.
