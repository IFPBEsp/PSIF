## 1. MARCA E IDENTIDADE

**PSIF (Plataforma de Suporte Psicopedagógico)**, do IFPB, usado pela
psicopedagoga, pelos professores, pelos alunos atendidos e pelos responsáveis
(§16.2).

### 1.1 Símbolo

O símbolo é o cérebro com cruz, branco, sobre quadrado `--blue-300` de cantos
arredondados. Aparece no topo da barra lateral (§7.10, em `--ic-xl`), no
cartão de login (§9.8), no cabeçalho da página pública (em branco sobre
quadrado `--navy-700`) e como favicon.

- `assets/simbolo-psif.svg`: o símbolo completo, para colar inline.
- `assets/simbolo-psif-glifo.svg`: só o glifo, em `currentColor`: branco
  sobre `--blue-300` ou `--navy-700`, `--navy-700` sobre branco ou céu.
- `assets/simbolo-psif.png` e `assets/simbolo-psif-quadrado.png` (sem recorte,
  para favicon e ícone de atalho do navegador): 512px, onde SVG não entra.

Não redesenhe, não distorça e não ponha texto por cima. Inline, leva
`aria-hidden="true"` quando "PSIF" está escrito ao lado; sozinho,
`role="img"` e `aria-label="PSIF"`. O símbolo é isento de contraste (WCAG
1.4.3) e mantém as cores próprias nos dois temas (§25.3).

### 1.2 Nome

- Sigla em caixa alta: **PSIF**.
- Por extenso: "Plataforma de Suporte Psicopedagógico", sem "PSIF -" na
  frente, exceto no título da página pública.

### 1.3 Marca dentro do sistema

A marca aparece no topo da barra lateral (§7.10), no login e no cabeçalho da
página pública. A barra de ações de cada tela é funcional (§7.3), sem marca.

### 1.4 Tokens de marca

`--blue-700` e `--blue-300` existem só para o símbolo. Em interface (botão,
link, ícone, seleção) o azul é `--navy-700`; um `--blue-*` fora da marca é
uma segunda cor de ação.
