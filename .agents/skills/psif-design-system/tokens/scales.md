### 3.4 Elevação e Sombra

O protótipo usa sombra em dois lugares só: botão primário e cartão de login.
Cartão comum **não tem sombra**: ele se separa do fundo céu pelo branco.

| Token | Valor | Uso |
|---|---|---|
| `--sh-sm` | `0 4px 4px rgba(36,74,105,.25)` | botão primário, cartão de login (medido: geometria do Figma, tinta trocada) |
| `--sh-md` | `0 12px 32px rgba(36,74,105,.24)` | folha flutuante: seletor de data, menu (derivado) |

A sombra do Figma é preta (`rgba(0,0,0,.25)`); sobre o fundo céu ela suja o
azul de cinza. Aqui a tinta é `--navy-700` com alpha: mesma geometria, sem
o cinza. Nunca `rgba(0,0,0,…)`.

### 3.5 Desfoque, vidro, véu e opacidade

O PSIF **não usa** blur nem glass (declarado em `absent_groups`). Superfície
que flutua é branca e opaca.

| Token | Valor | Uso |
|---|---|---|
| `--overlay` | `rgba(36,74,105,.48)` | véu atrás de folha modal (seletor de data, confirmação): derivado |
| `--o-disabled` | `.45` | elemento desabilitado: derivado |

### 3.6 Raio (border-radius)

| Token | Valor | Uso |
|---|---|---|
| `--radius-xs` | `2px` | caixa de seleção (medido) |
| `--radius-md` | `8px` | **o raio do PSIF**: cartão, botão, campo, atalho, filtro (medido em todos) |
| `--radius-lg` | `10px` | cartão de login (medido) |
| `--radius-pill` | `999px` | avatar circular |

Filho nunca tem raio maior que o pai. Nenhum outro valor.

### 3.7 Espaçamento (base 4px)

Escala: `--sp-1` 4px · `--sp-2` 8px · `--sp-3` 12px · `--sp-4` 16px ·
`--sp-5` 20px · `--sp-6` 24px · `--sp-8` 32px · `--sp-10` 40px · `--sp-12` 48px.

Padding de componente:

| Token | Valor | Onde |
|---|---|---|
| `--page-pad` | `24px` | margem lateral da tela (medido: cartões a 22–24px da borda) |
| `--card-pad` | `16px` | interior de cartão (medido) |
| `--list-row-pad` | `16px` | linha de lista dentro de cartão |
| `--btn-pad` | `12px 16px` | botão (derivado: altura vai de 37–39px para 48px, §20.6) |
| `--input-pad` | `12px 16px` | campo (derivado, mesmo motivo) |
| `--chip-pad` | `8px 16px` | filtro (derivado: o protótipo tem 23px de altura) |
| `--appbar-pad` | `8px 16px` | barra superior |

Entre cartões da mesma tela: `--sp-6`. Entre rótulo e campo: `--sp-2`. Entre
campos: `--sp-6`.

### 3.8 Tamanhos de Ícone

| Token | Valor | Uso |
|---|---|---|
| `--ic-sm` | `16px` | voltar (←), chevron (›), ícone dentro de campo |
| `--ic-md` | `20px` | ícone de ação em linha |
| `--ic-lg` | `24px` | ícone de atalho |
| `--ic-xl` | `32px` | símbolo do PSIF na barra lateral |
| `--ic-brand` | `136px` | símbolo do PSIF no splash (medido: 137×130 no Figma; o símbolo é quadrado) |

### 3.9 Movimento (tokens)

`--dur-fast` 150ms · `--dur-normal` 200ms · `--dur-slow` 300ms ·
`--ease-standard` · `--ease-out`. Todos derivados: o protótipo é estático.
Uso em §17.

### 3.10 Superfície e Z-index

Superfícies:

| Token | Aponta para | Uso |
|---|---|---|
| `--surface-base` | `--sky-100` | fundo da tela |
| `--surface-raised` | `--white` | cartão, campo |
| `--surface-sunken` | `--ink-100` | área de ícone dentro de cartão |
| `--surface-overlay` | `--white` | folha modal |
| `--surface-brand` | `--navy-700` | splash |

Camadas: `--z-base` 0 · `--z-raised` 10 · `--z-sticky` 100 (barra superior e
botão de rodapé) · `--z-overlay` 300 · `--z-modal` 400 · `--z-toast` 600. Nunca
um z-index avulso.
