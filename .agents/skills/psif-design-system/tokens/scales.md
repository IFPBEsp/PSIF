Os valores destas escalas estão em `assets/tokens.css`; aqui fica o papel de
cada token.

### 3.4 Sombra

Cartão comum não tem sombra: ele se separa do céu pelo branco.

| Token | Uso |
|---|---|
| `--sh-sm` | botão primário, cartão de login |
| `--sh-md` | o que flutua: folha, diálogo, menu suspenso, toast, gaveta, resultados da busca global |

A tinta é `--navy-700` com alpha; nunca `rgba(0,0,0,…)`.

### 3.5 Véu, opacidade e linhas

Sem blur e sem vidro: o que flutua é branco e opaco.

| Token | Uso |
|---|---|
| `--overlay` | véu atrás de folha, diálogo e gaveta |
| `--o-disabled` | elemento desabilitado |
| `--line-on-sky` | borda do filtro inativo e da área de envio (contraste em §3.2) |
| `--divider-on-sky` | linha acima da barra de ação da tela estreita |

### 3.6 Raio

| Token | Uso |
|---|---|
| `--radius-xs` | caixa de seleção |
| `--radius-md` | quadro de ícone, linha clicável, item de menu, atalho |
| `--radius-lg` | botão, campo, folha e diálogo, cartão de login, item da barra lateral |
| `--radius-xl` | cartão em tela estreita, cartão do pé da barra lateral |
| `--radius-2xl` | cartão em tela larga |
| `--radius-pill` | avatar, filtro, selo, botão só de ícone |

Filho nunca tem raio maior que o pai; pílula e círculo não contam.

### 3.7 Espaçamento

Escala de 4px: `--sp-1` a `--sp-12`. Entre cartões e entre campos `--sp-6`;
entre rótulo e campo `--sp-2`.

| Token | Onde |
|---|---|
| `--page-pad` | margem lateral em tela estreita |
| `--card-pad` | interior de cartão |
| `--list-row-pad` | linha de lista |
| `--btn-pad` · `--input-pad` | botão e campo |
| `--chip-pad` | filtro |

### 3.8 Ícone e quadro de ícone

| Token | Uso |
|---|---|
| `--ic-sm` | voltar, chevron, cadeado do selo "Sigiloso" |
| `--ic-md` | ícone em linha e em campo |
| `--ic-lg` | ícone de atalho e da barra lateral |
| `--ic-xl` | símbolo na barra lateral |
| `--tile-icon` | quadro de ícone em lista e tabela |
| `--tile-icon-lg` | quadro de ícone em cartão de destaque e na área de envio; símbolo no cartão de login |

Quadro de ícone: `--radius-md`, fundo `--sky-100`, ícone `--ic-md` em
`--navy-700`.

### 3.9 Movimento

`--dur-fast`, `--dur-normal`, `--ease-standard`, `--ease-out`. Uso em §17.

### 3.10 Superfície e camada

| Token | Uso |
|---|---|
| `--surface-base` | fundo da tela |
| `--surface-raised` | cartão, campo |
| `--surface-overlay` | folha, diálogo, menu |

Camadas, de baixo para cima: `--z-base`, `--z-raised`, `--z-sticky` (barra de
ação), `--z-overlay`, `--z-modal`, `--z-toast`. Nunca um z-index avulso.
