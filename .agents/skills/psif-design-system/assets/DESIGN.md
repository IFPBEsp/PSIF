---
name: "PSIF Design System"
description: "fundo céu, cartão branco, ação em marinho; o marinho marca o que se clica e o que se lê primeiro e nunca pinta área grande"
colors:
  navy-900: "#162E41"
  navy-800: "#1D3B54"
  navy-700: "#244A69"
  navy-500: "#5586A3"
  sky-300: "#A4C7E4"
  sky-100: "#CFE7F5"
  blue-700: "#1760B1"
  blue-300: "#72BAFC"
  success-700: "#0E782E"
  success-100: "#E3F1E7"
  warning-700: "#8A5300"
  warning-100: "#FDF3D6"
  danger-700: "#B42318"
  danger-100: "#FDECEA"
  ink-900: "#000000"
  ink-700: "#616161"
  ink-600: "#7D7D7D"
  ink-500: "#999999"
  ink-200: "#E8E8E8"
  ink-100: "#F3F3F3"
  white: "#FFFFFF"
typography:
  display:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "32px"
    fontWeight: 600
    lineHeight: 1.2
  h1:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.2
  h2:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "18px"
    fontWeight: 600
    lineHeight: 1.2
  h3:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "16px"
    fontWeight: 500
    lineHeight: 1.2
  body:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.5
  small:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.35
rounded:
  radius-xs: "2px"
  radius-md: "8px"
  radius-lg: "10px"
  radius-xl: "12px"
  radius-2xl: "16px"
  radius-pill: "999px"
spacing:
  sp-1: "4px"
  sp-2: "8px"
  sp-3: "12px"
  sp-4: "16px"
  sp-5: "20px"
  sp-6: "24px"
  sp-8: "32px"
  sp-10: "40px"
  sp-12: "48px"
components:
  button-primary:
    backgroundColor: "{colors.navy-700}"
    textColor: "{colors.white}"
    typography: "{typography.h2}"
    rounded: "{rounded.radius-lg}"
    padding: "12px 16px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.navy-800}"
  button-primary-active:
    backgroundColor: "{colors.navy-900}"
  button-secondary:
    backgroundColor: "{colors.white}"
    textColor: "{colors.navy-700}"
    rounded: "{rounded.radius-lg}"
    padding: "12px 16px"
    height: "48px"
  input:
    backgroundColor: "{colors.white}"
    textColor: "{colors.navy-700}"
    typography: "{typography.h3}"
    rounded: "{rounded.radius-lg}"
    padding: "12px 16px"
    height: "48px"
  card:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.radius-xl}"
    padding: "16px"
  card-wide:
    rounded: "{rounded.radius-2xl}"
  chip:
    textColor: "{colors.navy-700}"
    typography: "{typography.small}"
    rounded: "{rounded.radius-pill}"
    padding: "8px 16px"
    height: "44px"
  chip-selected:
    backgroundColor: "{colors.navy-700}"
    textColor: "{colors.white}"
  badge-success:
    backgroundColor: "{colors.success-100}"
    textColor: "{colors.success-700}"
    typography: "{typography.caption}"
    rounded: "{rounded.radius-pill}"
  badge-warning:
    backgroundColor: "{colors.warning-100}"
    textColor: "{colors.warning-700}"
    typography: "{typography.caption}"
    rounded: "{rounded.radius-pill}"
  icon-tile:
    backgroundColor: "{colors.sky-100}"
    textColor: "{colors.navy-700}"
    rounded: "{rounded.radius-md}"
    size: "40px"
  quick-action:
    backgroundColor: "{colors.sky-300}"
    textColor: "{colors.navy-700}"
    rounded: "{rounded.radius-md}"
    size: "48px"
  nav-item-active:
    backgroundColor: "{colors.sky-100}"
    textColor: "{colors.navy-700}"
    rounded: "{rounded.radius-lg}"
---

<!-- GERADO por scripts/gen_design_md.py: frontmatter do tokens.json, corpo de scripts/design_md_body.md. Não edite aqui. -->

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
- Símbolo: cérebro com cruz, branco, sobre quadrado #72BAFC de cantos
  arredondados (`assets/simbolo-psif.svg`; só o glifo, em `currentColor`, em
  `simbolo-psif-glifo.svg`). Glifo só em branco ou marinho.
- Três planos: céu no chão, cartão branco para o conteúdo, marinho para a ação.
- Uma família tipográfica, pesos 400, 500 e 600.
- Plano por padrão: cartão sem borda e sem sombra.
- Raio por papel: cartão 12px na tela estreita e 16px na
  larga; botão, campo e folha 10px; quadro de ícone 8px;
  pílula em avatar, filtro e selo.
- Web responsivo a partir de 320px, com toque ou mouse em qualquer largura.
- WCAG 2.2 AA inegociável.

## Colors

Azul institucional sobre céu claro; cor de estado só onde carrega significado.

### Primary
- **Marinho IFPB** (#244A69): ação primária, título de tela, número de
  indicador, nome e horário: o que se clica e o que se lê primeiro. Hover
  (#1D3B54) e pressionado (#162E41) do botão primário.

### Tertiary
- **Céu médio** (#A4C7E4): fundo do atalho de Ações rápidas, do avatar
  sem foto e da seleção de texto.
- **Azul da marca** (#1760B1, #72BAFC): só o símbolo.
- **Estados**: sucesso (#0E782E), atenção (#8A5300) e erro
  (#B42318), com os fundos claros da mesma família: sempre com texto
  junto, nunca só a cor.

### Neutral
- **Céu** (#CFE7F5): fundo de toda tela; item ativo da barra lateral.
- **Branco** (#FFFFFF): cartão, campo, barra lateral, folha modal.
- **Tinta** (#000000): texto principal. **Cinza de leitura**
  (#616161): texto secundário.
- **Cinza de ícone** (#7D7D7D): chevron, ícone de campo, borda de campo.
- **Divisória** (#E8E8E8) e **fundo de hover** (#F3F3F3).

### Named Rules
**A Regra de Ouro.** Fundo céu, cartão branco, ação em marinho. O único
bloco largo de marinho na tela é o botão primário.

**A Regra do Cinza que Não É Texto.** `ink-600`, `ink-500`, `navy-500`, `sky-300` e `blue-300` nunca pintam
texto: todos reprovam AA. Texto secundário é #616161.

## Typography

**Body Font:** Figtree (with system-ui)

**Character:** Uma família só, humanista e legível, carrega título, rótulo,
número e corpo. Hierarquia por tamanho e peso, nunca por caixa alta.

### Hierarchy
- **Display** (600, 32px): título de tela em marinho, à esquerda,
  abaixo da barra de ações (folha e autenticação centralizam); número de
  indicador; título da página pública.
- **H1** (600, 20px): saudação do Início; marca na barra lateral.
- **H2** (600, 18px): nome do aluno em cartão; rótulo do botão primário.
- **H3** (500, 16px): rótulo e valor de campo.
- **Body** (400, 15px, 1.5): linha de lista e texto de cartão;
  título de cartão em 600. Texto corrido até 70ch.
- **Small** (400, 14px): descrição, placeholder, filtro.
- **Caption** (400, 12px): metadado, rótulo de atalho. Nada abaixo
  disso.

### Named Rules
**A Regra do Número Tabular.** Horário, data, indicador e matrícula em
`tabular-nums`, para que a coluna não dance.

## Layout

Web responsivo, da tela estreita para a larga, por `min-width`. Ritmo em
degraus de 4px, 24px entre cartões e entre campos.

- **Estreita** (abaixo de 768px): coluna única, margem de 24px,
  navegação em gaveta, ação primária numa faixa presa à base. Acima da barra
  de ações, a área segura do aparelho, com mínimo de 16px.
- **Larga, faixa intermediária** (768px a 1200px): barra lateral
  recolhida a ícones, painel e perfil em coluna única, margem de 32px,
  folha vira diálogo, listagem vira tabela com as colunas principais.
- **A partir de 1200px:** barra lateral aberta de 240px,
  indicadores em linha de 4, grade de 3 colunas com a lista principal em 2 e
  o apoio em 1; formulário em 3 colunas.
- **Monitor grande:** conteúdo até 1440px, centralizado ao lado da
  barra lateral. Texto corrido até 70ch, diálogo até 720px, login até
  400px.

A ação primária fica à direita do título a partir de 768px. Alvo mínimo
de 44px; botão e campo com 48px. Com mouse, ação densa
pode usar 32px.

## Elevation & Depth

Plano por padrão: o cartão se separa do céu pelo branco. A sombra é tingida
de marinho, nunca preta, e só aparece no que flutua ou chama a ação: botão
primário, cartão de login, folha, diálogo, toast, gaveta e resultados da
busca global.

### Shadow Vocabulary
- **Ação** (`box-shadow: 0 4px 4px rgba(36,74,105,.25)`): botão primário e cartão de login.
- **Flutuante** (`box-shadow: 0 12px 32px rgba(36,74,105,.24)`): folha, diálogo, toast, gaveta e
  resultados da busca; folha e diálogo sobre o véu (rgba(36,74,105,.48)).

### Named Rules
**A Regra do Plano.** Sem gradiente, sem vidro, sem desfoque, sem sombra em
cartão comum.

## Shapes

O raio segue o papel. Cartão 12px na tela estreita e 16px
na larga; botão, campo, folha e cartão de login 10px; quadro de
ícone, linha clicável e atalho 8px; caixa de seleção 2px;
pílula em avatar, filtro, selo e botão só de ícone. Borda existe em campo e em
botão secundário; filtro inativo e área de envio usam uma linha translúcida de
marinho sobre o céu.

## Components

Valores no frontmatter; regra completa no § da skill.

### Buttons (§8.1)
- **Primary:** fundo #244A69, texto branco 600, 10px, altura
  48px, sombra de ação; largura total na tela estreita, automática
  na larga. Um por tela.
- **Hover / Pressed / Focus:** #1D3B54, #162E41 e o anel de §20.5.
- **Secondary:** fundo branco, borda de 1px e texto em marinho.

### Chips (§7.6)
- Pílula com borda de 1px em rgba(36,74,105,.35), texto marinho em 14px,
  altura 44px; ativo em marinho com texto branco.

### Badges (§12.2)
- Pílula com fundo -100 e texto -700 da família, 12px 600, ponto de
  8px antes do texto. Sempre com texto.

### Cards / Containers (§9.1)
- 12px na tela estreita, 16px na larga; branco, sem borda
  e sem sombra, 16px.

### Inputs / Fields (§8.3, §20.5)
- Fundo branco, borda de 1px #7D7D7D, 10px, altura
  48px, valor em 16px 500 marinho, rótulo visível acima.
- Foco no contêiner, por `:focus-within`; erro em #B42318 com
  mensagem em texto; desabilitado em .45.

### Navigation (§7)
- Gaveta na tela estreita; barra lateral a partir de 768px, recolhida a
  ícones até 1200px; item ativo em #CFE7F5 com texto marinho 600.

### Ações rápidas (§7.8)
- Até quatro por linha; quadrado #A4C7E4 de 48px com ícone marinho
  e rótulo em 12px.

## Do's and Don'ts

### Do:
- **Do** consumir só `var(--token)` do `tokens.css` da skill.
- **Do** desenhar os estados vazio, erro e carregando.
- **Do** conferir cada tela em 320px, em 768px e em 1200px.
- **Do** escrever tipo e situação em texto; a cor só repete.
- **Do** usar ícones de linha do sprite da skill (§18).

### Don't:
- **Don't** pintar área grande de marinho.
- **Don't** depender de hover: menu suspenso e alvo menor só com mouse.
- **Don't** usar #7D7D7D como cor de texto.
- **Don't** usar emoji como ícone ou marcador.
- **Don't** pôr dois botões primários, cartão dentro de cartão ou faixa
  colorida na borda de cartão.
- **Don't** usar texto abaixo de 12px nem campo abaixo de 16px.
