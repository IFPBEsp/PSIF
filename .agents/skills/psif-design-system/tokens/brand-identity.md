## 1. MARCA E IDENTIDADE

**PSIF (Plataforma de Suporte Psicopedagógico)**, do IFPB. Usado pela
psicopedagoga, pelos professores, pelos alunos atendidos e pelos responsáveis
(§16.2).

### 1.1 Símbolo e logo

**O símbolo do PSIF é o cérebro com cruz**: branco, sobre quadrado
`--blue-300` de cantos arredondados (raio de 21% do lado: 29px em 137px no
Figma). Aparece no splash (`--ic-brand`), no topo da barra lateral do web
(§7.10, em `--ic-xl`) e como ícone do app. No cabeçalho da página pública ele
vem em branco sobre quadrado `--navy-700`.

Arquivos: o SVG é o principal; é texto, então cola direto no HTML, sem
arquivo de imagem:

- `assets/simbolo-psif.svg`: o símbolo completo (quadrado `--blue-300` e
  glifo branco), `viewBox="0 0 512 512"`.
- `assets/simbolo-psif-glifo.svg`: só o cérebro com cruz, em
  `fill="currentColor"`: herda a cor de onde é colado. Branco sobre
  `--blue-300` ou `--navy-700`; `--navy-700` sobre branco ou céu. Outra cor,
  não (§1.4).
- `assets/simbolo-psif.png` (cantos recortados) e
  `assets/simbolo-psif-quadrado.png` (sem recorte, para ícone de sistema
  operacional, que aplica a própria máscara): 512px, para onde SVG não
  entra.

O vetor foi traçado da imagem do protótipo (98% de sobreposição com ela). Não
redesenhe nem distorça: o quadro do Figma é 137×130; o símbolo é quadrado,
e não ponha texto por cima. Inline, leva `aria-hidden="true"` quando "PSIF"
está escrito ao lado; sozinho, `role="img"` e `aria-label="PSIF"` (o
`simbolo-psif.svg` já vem assim).

O **logo de login**: coração formado por dois hemisférios de cérebro, traço
`--blue-700`, seguido de "PSIF" em `--blue-700`, peso 700, sobre branco,
fica só no cartão de login, até o design decidir se o símbolo o substitui
(§29.4).

Logo é isento de contraste (WCAG 1.4.3), mas nunca recebe texto por cima nem
é recolorido para outra família.

### 1.2 Nome e assinatura

- Sigla sempre em caixa alta: **PSIF**.
- Por extenso: "Plataforma de Suporte Psicopedagógico", sem "PSIF -" na
  frente, exceto no título da página pública.
- Assinatura institucional: "Acesso exclusivo para psicopedagogos e
  professores do IFPB" no rodapé do login.

### 1.3 Marca dentro do app

No web, a barra lateral abre com o símbolo e o nome PSIF (§7.10).

O PSIF não tem cabeçalho de marca dentro do app: a barra superior é funcional
(§7.3) e a marca aparece só no splash (§13.5), no login e no cabeçalho da
página pública (ícone do app à esquerda, "Entrar" à direita, fundo branco).

### 1.4 Regra dos Tokens de Marca

`--blue-700` e `--blue-300` existem **só** para logo e ícone do app. Em UI,
botão, link, ícone, seleção: o azul é `--navy-700`. Se um `--blue-*` aparece
fora da marca, a tela ganhou uma segunda cor de ação.
