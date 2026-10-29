## 17. MICROINTERAÇÕES E MOVIMENTO

O protótipo é estático; tudo nesta seção é derivado e mínimo. O PSIF é
ferramenta de trabalho usada entre atendimentos: movimento serve para
confirmar uma ação, nunca para decorar.

### 17.1 Durações e easing (ver tokens §3.9)

- `--dur-fast` (150ms): hover, pressionado, troca de cor.
- `--dur-normal` (200ms): abrir e fechar folha, expandir item.
- `--dur-slow` (300ms): barra de progresso do splash.
- Entrada com `--ease-out`; o resto com `--ease-standard`.

### 17.2 Estados de microinteração (por gatilho)

- Botão primário: hover `--navy-800`, pressionado `--navy-900`.
- Linha de lista com chevron: fundo `--ink-100` ao pressionar.
- Atalho de Ações Rápidas: pressionado, o fundo clareia de `--sky-300` para
  `--sky-100`: o mesmo azul, sem cor nova (é o que baixar a opacidade sobre
  o branco daria, sem token de opacidade a mais); foco ganha o anel padrão
  (§20.5).
- Hover (mouse, no web): linha de lista, indicador, cartão clicável e item
  da barra lateral ganham fundo `--ink-100`, como no pressionado; atalho,
  `--sky-100`. O hover só repete o que o toque já mostra: nada aparece ou
  some só no hover.

### 17.3 Transições de layout

Navegação entre telas: troca direta, sem animação de deslize obrigatória.
Folha modal sobe da base e a gaveta entra pela esquerda com `--dur-normal`
`--ease-out`; o véu aparece junto. O `Sheet` do shadcn já anima; ajuste a
duração dele para `--dur-normal` em vez de escrever a animação de novo.

### 17.4 Propriedades seguras e limites

Anime só `opacity`, `transform` e cor. Nunca `width`, `height`, `top`,
`margin` (§24.5).

### 17.5 Movimento reduzido (obrigatório)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition: none !important; animation: none !important; }
}
```

## 18. ICONOGRAFIA

Ícones de linha, traço uniforme (~2px), cantos arredondados: o estilo do
protótipo (Material Symbols Rounded é o mais próximo). A cor sai do papel do
ícone:

| Papel | Cor |
|---|---|
| botão só de ícone: ← e ☰ da barra superior, calendário do campo de data | `--ink-900`: o preto do protótipo (§7.3) |
| destino ativo da navegação, ícone de atalho (§7.8) | `--navy-700` |
| destino inativo da navegação | `--ink-700`, igual ao rótulo (§7.1) |
| indicação sem ação própria: chevron ›, ⌄ da seleção, ícone à esquerda do campo (envelope, cadeado, lupa) | `--ink-600`: passa 3:1 como ícone, nunca como texto |

| Ícone | Onde | Tamanho |
|---|---|---|
| ← seta | voltar, canto superior esquerdo | `--ic-sm` em alvo `--target-min` |
| › chevron | fim de linha que abre detalhe | `--ic-sm` |
| ☰ menu | telas-raiz no celular, canto superior direito (§7.2) | `--ic-lg` em alvo `--target-min` |
| ⌄ seta para baixo | campo de seleção | `--ic-md` |
| calendário | campo de data | `--ic-md` |
| envelope | campo de e-mail | `--ic-md` |
| lupa | busca | `--ic-md` |
| calendário · pessoa · sino | Ações rápidas: Agenda · Meu perfil · Notificações (§7.8) | `--ic-lg` |
| documento | Termo, escondido até decidir o que é (§28.4) | `--ic-lg` |
| o mesmo do destino nas Ações rápidas | barra lateral e gaveta (§7.9, §7.10) | `--ic-lg` |
| porta com seta para fora | Sair, no pé da barra lateral | `--ic-lg` |
| círculo com ! | alerta e banner (§10.1), na cor `-700` da família | `--ic-md` |

A cor vai no próprio ícone: `color` no `<svg>` que usa `currentColor`,
`stroke`/`fill`, ou a classe do ícone, nunca num contêiner que também tem
texto, que pintaria o texto junto (§3.2). O `lint_output.py` segue essa
divisão: em ícone cobra o piso de UI (3:1), em texto o de texto (4.5:1).

Os ícones ficam em `assets/icones.svg`, um `<symbol>` por nome, todos com
linha de 2px no grid de 24 e cor herdada:
`<Icon name="psif-calendario" />`, o componente descrito abaixo, que desenha
`<svg aria-hidden="true"><use href="#psif-calendario" /></svg>` com o tamanho
pedido.
Desenhe um ícone novo no mesmo traço e acrescente-o ao arquivo; um ícone
avulso na tela quebra o conjunto.

`<use href="icones.svg#…">` apontando para arquivo externo não renderiza em
alguns ambientes (pré-visualização, captura de tela, `file://`). Injete o
sprite inline uma vez no `<body>` (no Next.js, no layout raiz) e referencie
por `href="#psif-…"`. O `<svg>` do sprite leva tamanho zero
(`position: absolute; width: 0; height: 0`): sem isso ele ocupa 300×150px no
topo da página. `display: none` não serve, porque alguns navegadores deixam
de desenhar o `<use>`.

No projeto, o sprite vira um componente `Icon` em `src/shared/components`
(código em inglês, como pede a convenção do projeto), que recebe `name` e
`size`. O shadcn traz `lucide-react`; use lucide só para o
que o sprite não tem, no mesmo traço de 2px. Se o projeto já usar a fonte Material
Symbols Rounded, a coluna da direita dá o equivalente.

| Nome | Onde | Material Symbols |
|---|---|---|
| `psif-voltar` | voltar | `arrow_back` |
| `psif-avancar` · `psif-anterior` | chevron de linha; mês seguinte e anterior | `chevron_right` · `chevron_left` |
| `psif-abrir-lista` | seleção, filtro | `expand_more` |
| `psif-fechar` | limpar filtro, fechar folha | `close` |
| `psif-menu` · `psif-mais` | ☰ das telas-raiz no celular e recolher a barra lateral no web (§7.12); `psif-mais` sem uso na navegação | `menu` · `more_horiz` |
| `psif-inicio` · `psif-atendimentos` · `psif-alunos` · `psif-relatorios` | navegação; `-ativo` no destino atual | `home` · `assignment` · `group` · `find_in_page` |
| `psif-calendario` · `psif-perfil` · `psif-notificacoes` · `psif-termo` | Agenda, Meu perfil, Notificações, Termo | `calendar_today` · `person` · `notifications` · `description` |
| `psif-sair` | Sair | `logout` |
| `psif-alerta` | alerta (§10.1) | `error` |
| `psif-sucesso` | toast de sucesso (§10.2), confirmação | `check_circle` |
| `psif-busca` · `psif-email` · `psif-cadeado` · `psif-mostrar-senha` | busca e campos de login | `search` · `mail` · `lock` · `visibility` |

Ícone sozinho, sem texto, sempre tem nome acessível (§20.7). Emoji nunca é
ícone (§11.5).
