## 26. INTEGRAÇÃO COM TAILWIND V4 E SHADCN/UI

O frontend do PSIF é Next.js com Tailwind CSS v4 e shadcn/ui (seção 15 de
`docs/frontend/architecture-and-stack.md`, no projeto). Os tokens do PSIF são
a fonte; o Tailwind e o shadcn recebem apelidos para eles.

### 26.1 As colisões de nome

`--radius-*`, `--shadow-*` e `--font-*` são também namespaces do Tailwind.
Os tokens do PSIF continuam com os nomes de `assets/tokens.css`; o Tailwind
recebe apelidos.

### 26.2 O padrão de repasse

- **Cor**: em `@theme inline`, um apelido por token: `--color-navy-700:
  var(--navy-700)`, `--color-sky-100: var(--sky-100)`. Nomes diferentes, sem
  colisão; gera `bg-navy-700`, `text-ink-700`. O `inline` mantém o `var()`
  na utilitária, e é isso que deixa o tema escuro (§25) trocar a cor.
- **Raio e fonte**: os nomes já coincidem (`--radius-md`, `--font-sans`).
  Não redeclare em `@theme`: importe `tokens.css` depois do Tailwind, e
  `rounded-md` e `font-sans` passam a valer o PSIF.
- **Fonte**: o `next/font` registra a família com nome gerado
  (`__Figtree_a1b2c3`), então `'Figtree'` literal não acha a fonte. Declare a
  variável e ponha a classe no `<html>`:

  ```ts
  const figtree = Figtree({ subsets: ["latin"], weight: ["400", "500", "600"], variable: "--font-figtree" });
  // <html className={figtree.variable}>
  ```

  `--font-sans` já começa por `var(--font-figtree, 'Figtree')`.

O `check_consumer.py` não acusa o bloco `@theme` como divergência.

### 26.3 Ponte para os tokens semânticos do shadcn

Cada papel do shadcn aponta para um token, no `:root` do `globals.css`. Como o
bloco `.dark` de `tokens.css` troca os tokens, a mesma ponte serve aos dois
temas: apague o bloco `.dark { --background: ... }` que o `shadcn init` gera.

O mapa completo está no `:root` de §26.8. Duas escolhas que o `shadcn init`
não faz: `--muted-foreground` é `--ink-700`, nunca `--ink-600`; `--input` é
`--ink-600`, a borda de campo de 3:1 (§3.2).

**Raio.** Apague a escala calculada a partir de `--radius` que o
`shadcn init` gera: `--radius-xs` … `--radius-2xl` vêm do `tokens.css`. O
shadcn não conhece o raio por papel de §3.6; ajuste a variante de `Card`,
`Button`, `Input` e `Textarea` uma vez em `shared/components/ui`.

### 26.4 O que o lint NÃO cobre em projeto Tailwind

`lint_output.py` lê CSS, `style` e as classes, inclusive dentro de `cn()` e
`cva()`. Em classe utilitária confere cor (família, palavra-chave, `dark:`,
`--dark-*`, azul da marca), a sombra preta do Tailwind (`shadow-sm` …
`shadow-2xl`), raio fora da escala (`rounded-3xl`), z-index, foco, alvo,
altura fixa a partir de 100px, `max-w` e valor entre colchetes, com as regras
do CSS; o papel de cada cor e o degrau de espaçamento ficam com a revisão. Em
projeto Tailwind, `check_checklist.py` e a revisão manual de §24 são o
instrumento principal.

### 26.5 Duas cópias dos tokens: como acusar divergência

`tokens.css` é copiado para o projeto sem edição. Rode
`check_consumer.py src/app/globals.css` (e na cópia dos tokens) no CI do
projeto: ele compara cada token colado com o `:root` do `assets/tokens.css`
da skill e acusa a escala de raio que o `shadcn init` deixa no `@theme`.

### 26.6 Tabela token → utilitária

| Token | Utilitária |
|---|---|
| `--surface-base` | `bg-background` |
| `--surface-raised` | `bg-card` |
| `--navy-700` | `bg-primary` · `text-primary` |
| `--ink-900` | `text-foreground` |
| `--ink-700` | `text-muted-foreground` |
| `--ink-200` | `border-border` |
| `--danger-700` | `text-destructive` |
| `--radius-xs` | `rounded-sm` · `rounded-xs` |
| `--radius-md` | `rounded-md` |
| `--radius-lg` | `rounded-lg` |
| `--radius-xl` · `--radius-2xl` | `rounded-xl` · `rounded-2xl` |
| `--radius-pill` | `rounded-full` |
| `--line-on-sky` · `--divider-on-sky` | `border-(--line-on-sky)` · `border-t border-(--divider-on-sky)` |
| `--tile-icon` · `--tile-icon-lg` | `size-(--tile-icon)` · `size-(--tile-icon-lg)` |
| `--avatar-sm` · `--avatar-md` · `--avatar-lg` | `size-(--avatar-sm)` · `size-(--avatar-md)` · `size-(--avatar-lg)` |
| `--fs-display` … `--fs-caption` | `text-display` · `text-h1` · `text-h2` · `text-h3` · `text-body` · `text-small` · `text-caption`, cada um com a altura de linha de §4.4 |
| `--sh-sm` · `--sh-md` | `shadow-acao` · `shadow-flutuante` |
| `--control-min` · `--target-min` | `min-h-(--control-min)` · `min-h-(--target-min)` |
| `--target-fine` | `mouse:size-(--target-fine)` |
| `--w-content` · `--w-auth` · `--w-form` | `max-w-(--w-content)` · `max-w-(--w-auth)` · `max-w-(--w-form)` |
| `--w-sidebar` · `--w-aside` | `w-(--w-sidebar)` · `w-(--w-aside)` |

Papel (`bg-primary`, `text-muted-foreground`) e token (`bg-navy-700`,
`text-ink-700`) valem o mesmo; em componente do shadcn, use o papel.

### 26.7 Um mecanismo de estilização por projeto

Componentes do shadcn e utilitárias com o repasse acima, e nada mais. A skill
não traz folha de componentes: uma folha de classes próprias ao lado do
Tailwind briga por especificidade e vira uma segunda versão de cada
componente. A tabela de §6 diz qual componente do shadcn e quais utilitárias
fazem cada peça do PSIF.

### 26.8 O `globals.css` de referência

```css
@import "tailwindcss";
@import "tw-animate-css";
@import "./tokens.css";

@custom-variant dark (&:is(.dark *));
@custom-variant mouse (@media (hover: hover) and (pointer: fine));

@theme {
  --breakpoint-md: 48rem;
  --breakpoint-lg: 75rem;
}

:root {
  --background: var(--surface-base);
  --foreground: var(--ink-900);
  --card: var(--surface-raised);
  --card-foreground: var(--ink-900);
  --popover: var(--surface-overlay);
  --popover-foreground: var(--ink-900);
  --primary: var(--navy-700);
  --primary-foreground: var(--white);
  --secondary: var(--ink-100);
  --secondary-foreground: var(--navy-700);
  --muted: var(--ink-100);
  --muted-foreground: var(--ink-700);
  --accent: var(--ink-100);
  --accent-foreground: var(--ink-900);
  --destructive: var(--danger-700);
  --border: var(--ink-200);
  --input: var(--ink-600);
  --ring: var(--navy-700);
  --radius: var(--radius-md);
  --sidebar: var(--surface-raised);
  --sidebar-foreground: var(--ink-900);
  --sidebar-primary: var(--navy-700);
  --sidebar-primary-foreground: var(--white);
  --sidebar-accent: var(--ink-100);
  --sidebar-accent-foreground: var(--navy-700);
  --sidebar-border: var(--ink-200);
  --sidebar-ring: var(--navy-700);
}

@theme inline {
  --radius-sm: var(--radius-xs);
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);
  --color-navy-900: var(--navy-900);
  --color-navy-800: var(--navy-800);
  --color-navy-700: var(--navy-700);
  --color-navy-500: var(--navy-500);
  --color-sky-300: var(--sky-300);
  --color-sky-100: var(--sky-100);
  --color-blue-700: var(--blue-700);
  --color-blue-300: var(--blue-300);
  --color-success-700: var(--success-700);
  --color-success-100: var(--success-100);
  --color-warning-700: var(--warning-700);
  --color-warning-100: var(--warning-100);
  --color-danger-700: var(--danger-700);
  --color-danger-100: var(--danger-100);
  --color-ink-900: var(--ink-900);
  --color-ink-700: var(--ink-700);
  --color-ink-600: var(--ink-600);
  --color-ink-500: var(--ink-500);
  --color-ink-200: var(--ink-200);
  --color-ink-100: var(--ink-100);
  --text-display: var(--fs-display);
  --text-h1: var(--fs-h1);
  --text-h2: var(--fs-h2);
  --text-h3: var(--fs-h3);
  --text-body: var(--fs-body);
  --text-small: var(--fs-small);
  --text-caption: var(--fs-caption);
  --text-display--line-height: var(--lh-tight);
  --text-h1--line-height: var(--lh-tight);
  --text-h2--line-height: var(--lh-tight);
  --text-h3--line-height: var(--lh-tight);
  --text-body--line-height: var(--lh-normal);
  --text-small--line-height: var(--lh-normal);
  --text-caption--line-height: var(--lh-snug);
  --shadow-acao: var(--sh-sm);
  --shadow-flutuante: var(--sh-md);
}
```

`--radius-xl` e `--radius-2xl` ficam fora do `@theme`: o `tokens.css` já os
declara com o mesmo nome, e repetir aqui criaria referência circular.

- `md:` e `lg:` valem `--bp-md` (768px) e `--bp-lg` (1200px). O `lg` padrão
  do Tailwind é 1024px e quebraria a faixa intermediária (§5.2). O bloco é
  `@theme` sem `inline`: media query não lê `var()`.
- `dark:` existe porque os componentes do shadcn o usam por dentro; o código
  do projeto não o escreve (§25.2).
- `mouse:` aplica só com mouse (§5.12): `mouse:size-(--target-fine)`. O
  `hover:` do Tailwind v4 já só vale em `(hover: hover)`. Para escolher entre
  `DropdownMenu` (mouse) e folha (`Drawer` na tela estreita, `Dialog` na
  larga, §9.6) no React, use `matchMedia("(hover: hover) and (pointer: fine)")`,
  com o toque como padrão na renderização do servidor.
- O `tokens.css` entra sem camada, para o `:root` dele vencer o
  `@layer theme` do Tailwind; as regras de elemento dele (fonte, anel de
  foco, seleção, movimento reduzido) já vêm em `@layer base`, e qualquer
  utilitária da tela vence elas.

### 26.9 O `cn()` do shadcn com os tamanhos do PSIF

O `cn()` usa o `tailwind-merge`, que não conhece `text-h1` … `text-caption` e
os trata como cor: `cn("text-h2", "text-primary")` apaga um dos dois. Ensine
os nomes a ele, em `src/shared/lib/cn.ts`:

```ts
import { clsx, type ClassValue } from "clsx";
import { extendTailwindMerge } from "tailwind-merge";

const twMerge = extendTailwindMerge({
  extend: {
    theme: {
      text: ["display", "h1", "h2", "h3", "body", "small", "caption"],
      shadow: ["acao", "flutuante"],
    },
  },
});

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

No `components.json`, aponte `utils` para `@/shared/lib/cn` e `ui` para
`@/shared/components/ui`, como pede a estrutura do frontend do projeto.

