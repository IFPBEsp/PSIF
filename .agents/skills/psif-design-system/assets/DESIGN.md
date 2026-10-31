---
name: "PSIF Design System"
description: "fundo céu, cartão branco, ação em marinho: o marinho marca o que se clica e o que se lê primeiro; nunca pinta área grande fora do splash"
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
  splash:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "36px"
    fontWeight: 400
    lineHeight: 1.2
  display:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "32px"
    fontWeight: 600
    lineHeight: 1.2
  splash-sub:
    fontFamily: "'Figtree', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: "26px"
    fontWeight: 400
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
  card-web:
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
- Raio por papel: cartão 12px no celular e 16px no web;
  botão, campo e folha 10px; quadro de ícone 8px; pílula
  em avatar, filtro e selo.
- WCAG 2.2 AA inegociável: o protótipo foi corrigido onde reprovava.

## Colors

Azul institucional sobre céu claro; cor de estado só onde carrega significado.

### Primary
- **Marinho IFPB** (#244A69): ação primária, título de tela, número de
  indicador, nome e horário: o que se clica e o que se lê primeiro. Hover
  (#1D3B54) e pressionado (#162E41) do botão primário.

### Tertiary
- **Céu médio** (#A4C7E4): só o fundo do atalho de Ações rápidas e a
  seleção de texto.
- **Azul da marca** (#1760B1, #72BAFC): só logo e ícone do app.
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
**A Regra de Ouro.** Fundo céu, cartão branco, ação em marinho. Fora do
splash, o único bloco largo de marinho na tela é o botão primário.

**A Regra do Cinza que Não É Texto.** `ink-600`, `ink-500`, `navy-500`,
`sky-300` e `blue-300` nunca pintam texto: todos reprovam AA. O cinza do
protótipo (#7D7D7D) vira #616161 quando é texto.

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
- **H3** (500, 16px): rótulo e valor de campo: 16px evita o zoom do iPhone.
- **Body** (400, 15px, 1.5): linha de lista e texto de cartão;
  título de cartão em 600. Texto corrido até 70ch.
- **Small** (400, 14px): descrição, placeholder, filtro.
- **Caption** (400, 12px): metadado, rótulo de atalho e de barra.
  Nada abaixo disso.

### Named Rules
**A Regra do Número Tabular.** Horário, data, indicador e matrícula em
`tabular-nums`, para que a coluna não dance.

## Layout

Celular primeiro, no quadro de 390px. Margem lateral de 24px,
ritmo de 4px, 24px entre cartões e entre campos. O rodapé fixo só existe
em tela de tarefa, com o botão primário; a navegação fica numa gaveta aberta
pelo menu.
Acima da barra superior, só a área segura do aparelho, com mínimo de
16px.

A partir de 768px, a gaveta vira barra lateral fixa de 240px. O conteúdo ocupa a área ao lado dela, com margem de 32px,
sem largura máxima, alinhado à esquerda; texto corrido até 70ch e formulário
em 3 colunas. No
web, o título da tela fica à esquerda e a ação primária sobe para o topo, à
direita.
Indicadores em linha de 4; grade de 3 colunas, com a lista principal em 2 e
o cartão de apoio em 1.

Alvo de toque mínimo de 44px; botão e campo com 48px.

## Elevation & Depth

Plano por padrão: o cartão se separa do céu pelo branco. A sombra é tingida
de marinho, nunca preta, e só aparece no que flutua ou chama a ação: botão
primário, cartão de login, folha modal, toast, gaveta do celular e resultados
da busca global.

### Shadow Vocabulary
- **Ação** (`box-shadow: 0 4px 4px rgba(36,74,105,.25)`): botão primário e cartão de login.
- **Flutuante** (`box-shadow: 0 12px 32px rgba(36,74,105,.24)`): folha modal, seletor de data,
  toast, gaveta e resultados da busca, os dois primeiros sobre o véu
  (rgba(36,74,105,.48)).

### Named Rules
**A Regra do Plano.** Sem gradiente, sem vidro, sem desfoque, sem sombra em
cartão comum.

## Shapes

O raio segue o papel. Cartão 12px no celular e 16px no
web; botão, campo, folha e cartão de login 10px; quadro de ícone,
linha clicável e atalho 8px; caixa de seleção 2px;
pílula em avatar, filtro, selo e botão só de ícone. Borda existe em campo e
em botão secundário; filtro inativo e área de envio usam uma linha
translúcida de marinho sobre o céu.

## Components

### Buttons
- **Shape:** 10px, altura mínima 48px, largura total.
- **Primary:** fundo marinho, texto branco em 600, sombra de ação. Um por tela.
- **Hover / Focus:** hover #1D3B54, pressionado #162E41; foco com
  anel de 2px em marinho, afastado 2px.
- **Secondary:** fundo branco, borda de 1px e texto em marinho.

### Chips
- **Style:** pílula transparente com borda de 1px em rgba(36,74,105,.35), texto
  marinho 500 em 14px, altura mínima 44px. No celular a linha
  rola na horizontal.
- **State:** ativo em marinho com texto branco 600; filtro que abre folha
  mostra o valor e × para limpar.

### Badges
- **Style:** pílula com fundo da família em -100 e texto -700, 600 em
  12px, ponto de 6px antes do texto. Sempre com texto.
- **Use:** situação no cabeçalho do perfil; "Sigiloso" em documento.

### Cards / Containers
- **Corner Style:** 12px no celular, 16px no web
- **Background:** branco
- **Shadow Strategy:** nenhuma (ver Elevation & Depth)
- **Border:** nenhuma
- **Internal Padding:** 16px

### Inputs / Fields
- **Style:** fundo branco, borda de 1px #7D7D7D, raio 10px, valor em marinho 500 de
  16px, rótulo visível acima. Opcional leva "(opcional)" no rótulo.
- **Focus:** anel de foco padrão.
- **Error / Disabled:** borda #B42318 e mensagem em texto abaixo;
  desabilitado com opacidade .45.

### Navigation
- **Celular:** a mesma barra lateral, como gaveta aberta pelo menu; sem
  barra inferior.
- **Web:** barra lateral branca com a busca global sob a marca e, no pé, o
  cartão do usuário; item ativo com fundo #CFE7F5, raio 10px e
  texto marinho em 600; hover #F3F3F3. No topo do conteúdo, breadcrumbs e
  Notificações.

### Ações rápidas
Até quatro atalhos por linha no Início (hoje três: Agenda, Meu perfil,
Notificações), quebrando linha em vez de encolher: quadrado #A4C7E4 de 48px com
ícone marinho e rótulo de 12px embaixo.

## Do's and Don'ts

### Do:
- **Do** consumir só `var(--token)` do `tokens.css` da skill.
- **Do** desenhar os estados vazio, erro e carregando: o protótipo só tem o
  estado cheio.
- **Do** escrever tipo e situação em texto; a cor só repete.
- **Do** usar ícones de linha com traço de 2px, no estilo Material Symbols
  Rounded.

### Don't:
- **Don't** pintar área grande de marinho fora do splash.
- **Don't** usar #7D7D7D como cor de texto.
- **Don't** usar emoji como ícone ou marcador.
- **Don't** pôr dois botões primários, cartão dentro de cartão ou faixa
  colorida na borda de cartão.
- **Don't** usar texto abaixo de 12px nem campo abaixo de 16px.
