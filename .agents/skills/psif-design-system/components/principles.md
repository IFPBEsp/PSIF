## 6. PRINCÍPIOS DE COMPONENTES E REUTILIZAÇÃO

1. **Todo componente do PSIF é um cartão branco, um campo, um botão, uma
   linha de lista, um selo (§12.2), um filtro em pílula (§7.6), uma aba
   (§7.5) ou uma área de envio (§8.5).** Antes de criar outro, monte com
   essas peças.
2. **Raio pelo papel da peça**, na tabela de §3.6.
3. **Sem borda decorativa.** Borda existe em campo (`--ink-600`, 1px) e em
   botão secundário (`--navy-700`, 1px). Filtro inativo e área de envio usam
   `--line-on-sky`. Cartão não tem borda.
4. **Um primário por tela** (§5.6); o resto é secundário ou link.
5. **Componente novo entra na tabela abaixo**: se a tela precisou de um, ele
   ganha uma linha aqui e vai para `src/shared/components` do projeto quando
   uma segunda tela o usar.
6. **Todo componente interativo tem todos os estados** da tabela abaixo.
   Componente com metade deles não está pronto.

| Estado | Botão primário | Campo | Linha, cartão ou item clicável |
|---|---|---|---|
| normal | `--navy-700` | branco, borda `--ink-600` | branco ou transparente |
| hover (mouse, §5.12) | `--navy-800` | não se aplica | fundo `--ink-100` |
| foco | anel de §20.5 | anel de §20.5 | anel de §20.5 |
| pressionado | `--navy-900` | não se aplica | fundo `--ink-100` |
| selecionado | não se aplica | não se aplica | filtro: `--navy-700` e texto branco; navegação: `--sky-100` e `--navy-700` |
| desabilitado | `--o-disabled`, sem hover | `--o-disabled` | `--o-disabled` |
| carregando | "Salvando…", bloqueado | não se aplica | esqueleto (§10.5) |
| erro | alerta (§10.7) | borda `--danger-700` e texto | não se aplica |

7. **Monte com o shadcn/ui e as utilitárias de §26.** O catálogo do PSIF
   são os componentes do projeto. A variante do PSIF se define uma vez no
   componente, com o `cva` do shadcn, não em `className` repetido em cada
   tela.

As classes abaixo dependem do `globals.css` de §26.8. A escala de espaçamento
do Tailwind coincide com `--sp-*` (`p-4` é `--sp-4`). `mouse:` é a variante
de §5.12.

| Componente do PSIF | No projeto | Classes e variante | § |
|---|---|---|---|
| Estrutura da tela | `SidebarProvider` com `SidebarInset`; `<main id="conteudo">`; link "Pular para o conteúdo" | `bg-background`; conteúdo `px-6 md:px-8`; texto só para leitor de tela `sr-only` | §5.1, §20.4 |
| Barra superior | `<header>` só com ações: `Button variant="ghost" size="icon"` para ←, busca, ⋯ ou ☰ | botões `rounded-full` com `aria-label` do destino; título abaixo da barra (§4.3): `text-display font-semibold text-primary`, linha de contexto `text-body text-ink-700` | §7.3, §4.3 |
| Navegação | `Sidebar collapsible="icon"`, `SidebarTrigger` no topo da barra, `SidebarMenuButton` | item `rounded-lg`; ativo (`isActive`) `bg-sky-100 text-primary font-semibold`; inativo `text-ink-700`; pé com cartão `bg-ink-100 rounded-xl` (iniciais, nome, papel, Sair); recolhida por padrão até `lg:`; na tela estreita o `Sidebar` vira gaveta sozinho | §7.1, §7.9, §7.10, §7.12 |
| Breadcrumbs | `Breadcrumb` | `hidden md:flex text-small`, no topo do conteúdo; item atual sem link, com `aria-current="page"` | §7.11 |
| Busca global (tela larga) | `Command` na barra lateral sob a marca; resultados em `Popover` com mouse e na folha de §9.6 no toque | campo `bg-ink-100 border-0 rounded-lg`; resultados `shadow-flutuante` | §7.13 |
| Topo do conteúdo (tela larga) | breadcrumbs e `Button` de Notificações | Notificações `rounded-full bg-card min-h-(--target-min)`, `aria-label` com as não lidas | §7.13 |
| Botão primário | `Button` (variante padrão) | `w-full min-h-(--control-min) text-h2 font-semibold rounded-lg shadow-acao transition-colors duration-(--dur-fast)`; botão de tela a partir de `md:` com `md:w-auto md:min-h-(--target-min) md:text-small` (§5.6) | §8.1, §5.6 |
| Botão secundário | `Button variant="outline"` | `rounded-lg border-primary bg-card text-primary` | §8.1 |
| Ação destrutiva em texto ("Descartar") | `Button variant="ghost"` | `text-destructive` | §10.3 |
| Link | `Button variant="link"` ou `Link` do Next | `text-primary underline` | §8.1 |
| Campo | `Label` e `Input` ou `Textarea` | `min-h-(--control-min) text-h3 font-medium text-primary rounded-lg border-input`, sobre o céu ou sobre cartão; no `Textarea`, `leading-normal` (texto longo, §8.3); erro com `aria-invalid` e mensagem `text-small text-destructive` embaixo | §8.3 |
| Campo com ícone (busca, e-mail, senha) | `Input` num contêiner com o ícone à esquerda; "Mostrar senha" é `Button variant="ghost" size="icon"` com `aria-pressed` | ícone `size-(--ic-md) text-ink-600` | §8.3, §20.7 |
| Seleção (aluno, tipo) | `Select`; `Popover` com `Command` quando a lista tem busca | mesmo visual do campo; a lista abre como em §8.2 | §8.4 |
| Data | `Calendar` em `Popover` com mouse, na folha de §9.6 no toque | dia `aspect-square w-full max-w-(--target-min) min-w-6 rounded-full`; hoje `ring-1 ring-primary`; selecionado `bg-primary text-primary-foreground` | §8.6, §11.6 |
| Caixa de seleção | `Checkbox` com `Label` | `size-4 rounded-xs border-ink-600 data-[state=checked]:bg-primary`; a linha toda `min-h-(--target-min)` | §8.7 |
| Filtro em pílula | escolha direta: `ToggleGroup type="single"` com `ToggleGroupItem`; filtro com valor: `Button` que abre a seleção de §8.4, com o `aria-haspopup` de lá | `rounded-full min-h-(--target-min) px-4 text-small font-medium text-primary border border-(--line-on-sky) bg-transparent`; ativo `bg-primary text-primary-foreground font-semibold` (`data-[state=on]:` no `ToggleGroupItem`); na tela estreita a linha rola na horizontal (`overflow-x-auto`) | §7.6, §11.4 |
| Selo | `Badge` | `rounded-full bg-<família>-100 text-<família>-700 font-semibold text-caption`, ponto `size-2 rounded-full bg-<família>-700` antes do texto; sempre com texto | §12.2, §16.3 |
| Abas do aluno (tela larga) | `Tabs`, com cada gatilho como link | ativa `text-primary font-semibold` com sublinhado de 3px `border-b-3 border-primary`; contador `rounded-full bg-sky-100`; inativa `text-ink-700 font-medium`; alvo `min-h-(--target-min)` | §7.5 |
| Área de envio | componente próprio: `<button>` que abre o seletor e aceita arrastar; sem equivalente no shadcn | `rounded-2xl border-2 border-dashed border-(--line-on-sky) bg-card hover:bg-ink-100`; quadro `size-(--tile-icon-lg) rounded-md bg-sky-100` | §8.5 |
| Cartão | `Card` | `rounded-xl md:rounded-2xl border-0 shadow-none p-4 bg-card`; título `text-body font-semibold text-primary` | §9.1 |
| Quadro de ícone | `<span>` com o `Icon` | `size-(--tile-icon) rounded-md bg-sky-100 text-primary` (lista e tabela) ou `size-(--tile-icon-lg)` (destaque) | §3.8 |
| Linha de lista | `<ul>` com `<li>` | linha clicável `rounded-md hover:bg-ink-100 p-(--list-row-pad)` com quadro de ícone à esquerda e chevron `size-(--ic-sm) text-ink-600` à direita; cartão com `p-1` de respiro | §9.3, §11.2 |
| Indicadores | `Card` com grade | `grid grid-cols-2 md:grid-cols-4`; número `text-display font-semibold text-primary` | §9.2 |
| Ações rápidas | `Link` com ícone | quadrado `size-12 rounded-md bg-sky-300 text-primary`; rótulo `text-caption text-ink-700` | §7.8 |
| Avatar | `Avatar` com `AvatarFallback` | `size-(--avatar-md)` no cartão e no perfil em tela estreita (anel de 4px, `ring-4 ring-card`), `size-(--avatar-sm)` no cabeçalho do aluno em tela larga, `size-(--target-min)` em lista, `size-8` na barra lateral; iniciais `bg-sky-300 text-primary font-semibold` | §12.1 |
| Situação do aluno | no cabeçalho do perfil, `Badge` (selo); em lista e tabela, texto | selo: ver linha Selo; texto: `text-primary`, pendente `text-warning-700`, encerrado `text-ink-700` | §12.2 |
| Tabela (a partir de `md:`) | `Table` do shadcn com TanStack Table (`DataTable` em `shared`) | dentro de `Card`; cabeçalho `text-caption font-semibold text-ink-700`; célula-chave com quadro de ícone, nome e, embaixo, tamanho e selo; linha `h-(--target-min) hover:bg-ink-100`, separada por `border-ink-200`; colunas secundárias `hidden lg:table-cell`; ações sem rótulo visível (`sr-only`), com `mouse:size-(--target-fine)`; número `text-right tabular-nums` | §11.8 |
| Folha e diálogo | tela estreita: `Drawer`, que sobe da base e fecha arrastando; a partir de `md:`: `Dialog` centralizado | `Drawer` com `rounded-t-lg`; `Dialog` com `rounded-lg max-w-(--w-form)`; os dois com `shadow-flutuante`; ações em coluna, primário primeiro | §9.6, §10.3 |
| Menu de opções | mouse: `DropdownMenu`; toque: a folha de §9.6 (`Drawer` ou `Dialog`) | itens `min-h-(--target-min)`, com mouse `mouse:min-h-(--target-fine)`, `rounded-md` | §8.2, §5.12 |
| Toast | `Toaster` do Sonner, com as cores da ponte | ícone na cor do tipo | §10.2 |
| Alerta fixo | `Alert` | `bg-warning-100 text-warning-700` ou `bg-danger-100 text-danger-700` | §10.1, §20.2 |
| Carregando | `Skeleton` | `bg-ink-200 rounded-md`, no formato do componente; na lista, quadro `size-(--tile-icon)` | §10.5 |
| Notificação | lista dentro de `Card` | ponto `size-2 rounded-full bg-primary` (não lida) ou `bg-warning-700` (pendente) | §9.5 |
| Linha do tempo | lista ordenada da feature | marcador `size-4 rounded-full` na cor do tipo; linha `border-l border-ink-200` | §11.5 |
| Autenticação | `Card` centralizado | `max-w-(--w-auth) rounded-lg shadow-acao p-8` sobre `bg-background` | §9.8, §13.4 |
| Página pública | `Card` de funcionalidade | ícone num círculo `size-(--control-min) rounded-full bg-primary text-primary-foreground` | §9.7, §13.6 |
| Grades | utilitárias | painel `grid lg:grid-cols-3` com o principal em `lg:col-span-2`; formulário `md:grid-cols-2 lg:grid-cols-3` com texto longo em `col-span-full`; conteúdo `mx-auto w-full max-w-(--w-content)`; pilha `flex flex-col gap-6` | §5.2, §5.3, §15.1 |
