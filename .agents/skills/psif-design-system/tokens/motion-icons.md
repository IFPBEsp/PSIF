## 17. MICROINTERAÇÕES E MOVIMENTO

O PSIF é ferramenta de trabalho usada entre atendimentos: movimento confirma
uma ação, nunca decora.

### 17.1 Durações e easing

`--dur-fast` em hover, pressionado e troca de cor; `--dur-normal` ao abrir e
fechar folha, diálogo, gaveta e item expansível (§3.9). Entrada com
`--ease-out`; o resto com `--ease-standard`.

Dois tempos não animam e são lidos no código: `--dur-debounce`, a espera da
busca depois da última tecla (§7.7), e `--dur-toast`, quanto o toast de
sucesso fica na tela (§10.2). No cliente,
`parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--dur-toast"))`
dá os milissegundos, para o `duration` do Sonner ou o `setTimeout`.

### 17.2 Estados por gatilho

Hover e pressionado de botão, campo, linha, indicador, cartão clicável e
item da barra lateral estão na tabela de estados de §6. Fora dela, o atalho
de Ações rápidas: pressionado e com hover, o fundo vai de `--sky-300` para
`--sky-100`; foco com o anel padrão (§20.5). Hover só com mouse (§5.12), e
nada aparece ou some só no hover.

### 17.3 Transições de layout

Troca de tela direta, sem deslize. Folha sobe da base, gaveta entra pela
esquerda e diálogo aparece no centro, com `--dur-normal` `--ease-out` e o véu
junto. `Drawer`, `Sheet` e `Dialog` do shadcn já animam; ajuste a duração em
vez de escrever a animação de novo.

### 17.4 Propriedades seguras

Anime só `opacity`, `transform` e cor. Nunca `width`, `height`, `top` ou
`margin`.

### 17.5 Movimento reduzido (obrigatório)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition: none !important; animation: none !important; }
}
```

## 18. ICONOGRAFIA

Ícones de linha, traço de 2px no grid de 24, cantos arredondados. A cor sai
do papel do ícone:

| Papel | Cor |
|---|---|
| botão só de ícone: ← e ☰ da barra de ações, calendário do campo de data | `--ink-900` |
| destino ativo da navegação, ícone de atalho (§7.8) | `--navy-700` |
| destino inativo da navegação | `--ink-700`, igual ao rótulo |
| indicação sem ação própria: chevron ›, ⌄ da seleção, ícone à esquerda do campo | `--ink-600`: passa 3:1 como ícone, nunca como texto |

Tamanhos: `--ic-sm` para ← e ›; `--ic-md` para ícone de campo, ⌄ e alerta;
`--ic-lg` para navegação, ☰ e atalhos. Botão só de ícone tem alvo
`--target-min` (§5.12).

A cor vai no próprio ícone (`currentColor` no `<svg>` ou a classe do ícone),
nunca num contêiner que também tem texto (§3.2). O `lint_output.py` cobra
3:1 de ícone e 4.5:1 de texto.

### 18.1 Sprite e componente `Icon`

Os ícones ficam em `assets/icones.svg`, um `<symbol>` por nome, com cor
herdada. Ícone novo segue o mesmo traço e entra no arquivo; ícone avulso
quebra o conjunto.

Injete o sprite inline uma vez no `<body>` (no Next.js, no layout raiz),
com tamanho zero (`position: absolute; width: 0; height: 0`), e referencie
por `href="#psif-…"`. `<use href="icones.svg#…">` em arquivo externo falha
em pré-visualização, captura e `file://`; `display: none` no sprite faz
alguns navegadores deixarem de desenhar o `<use>`.

No projeto, o sprite vira o componente `Icon` em `src/shared/components`
(`name` e `size`), que desenha `<svg aria-hidden="true"><use href="#psif-…"
/></svg>`. Use `lucide-react` só para o que o sprite não tem, no mesmo traço.

| Nome | Onde | Material Symbols |
|---|---|---|
| `psif-voltar` | voltar | `arrow_back` |
| `psif-avancar` · `psif-anterior` | chevron de linha; mês seguinte e anterior | `chevron_right` · `chevron_left` |
| `psif-abrir-lista` | seleção, filtro | `expand_more` |
| `psif-fechar` | limpar filtro, fechar folha | `close` |
| `psif-menu` · `psif-mais` | ☰ e recolher a barra lateral (§7.12); ⋯ de ações | `menu` · `more_horiz` |
| `psif-inicio` · `psif-atendimentos` · `psif-alunos` · `psif-relatorios` | navegação; `-ativo` no destino atual | `home` · `assignment` · `group` · `find_in_page` |
| `psif-calendario` · `psif-perfil` · `psif-notificacoes` · `psif-termo` | Agenda, Meu perfil, Notificações, documento | `calendar_today` · `person` · `notifications` · `description` |
| `psif-sair` | Sair | `logout` |
| `psif-alerta` | alerta (§10.1) | `error` |
| `psif-sucesso` | toast de sucesso, confirmação | `check_circle` |
| `psif-busca` · `psif-email` · `psif-cadeado` · `psif-mostrar-senha` | busca, campos de login, selo Sigiloso | `search` · `mail` · `lock` · `visibility` |

A coluna Material Symbols vale para quem já usa essa fonte. Ícone sem texto
tem nome acessível (§20.7). Emoji nunca é ícone.
