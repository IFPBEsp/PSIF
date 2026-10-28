## 27. INTEGRAÇÃO COM TAILWIND V4 E SHADCN/UI

O frontend do PSIF é Next.js com Tailwind CSS v4 e shadcn/ui (seção 15 de
`docs/frontend/architecture-and-stack.md`, no projeto). Este é o caminho padrão
de toda tela: os tokens do PSIF são a fonte, e o Tailwind e o shadcn recebem
apelidos para eles.

### 27.1 As colisões de nome

`--radius-*`, `--shadow-*` e `--font-*` são também namespaces do Tailwind.
Os tokens do PSIF continuam com os nomes de `assets/tokens.css`; o Tailwind
recebe apelidos.

### 27.2 O padrão de repasse

- **Cor**: em `@theme inline`, um apelido por token: `--color-navy-700:
  var(--navy-700)`, `--color-sky-100: var(--sky-100)`. Nomes diferentes, sem
  colisão; gera `bg-navy-700`, `text-ink-700`. O `inline` mantém o `var()`
  na utilitária, e é isso que deixa o tema escuro (§26) trocar a cor.
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

### 27.3 Ponte para os tokens semânticos do shadcn

Cada papel do shadcn aponta para um token, no `:root` do `globals.css`. Como o
bloco `.dark` de `tokens.css` troca os tokens, a mesma ponte serve aos dois
temas: apague o bloco `.dark { --background: ... }` que o `shadcn init` gera.

| Papel do shadcn | Token do PSIF |
|---|---|
| `--background` | `--surface-base` |
| `--foreground` | `--ink-900` |
| `--card` · `--card-foreground` | `--surface-raised` · `--ink-900` |
| `--popover` · `--popover-foreground` | `--surface-overlay` · `--ink-900` |
| `--primary` · `--primary-foreground` | `--navy-700` · `--white` |
| `--secondary` · `--secondary-foreground` | `--ink-100` · `--navy-700` |
| `--muted` · `--muted-foreground` | `--ink-100` · `--ink-700` (nunca `--ink-600`) |
| `--accent` · `--accent-foreground` | `--ink-100` · `--ink-900` |
| `--destructive` | `--danger-700` |
| `--border` | `--ink-200` |
| `--input` | `--ink-600` (borda de campo, 3:1) |
| `--ring` | `--navy-700` |
| `--radius` | `--radius-md` (8px) |
| `--sidebar` · `--sidebar-foreground` | `--surface-raised` · `--ink-900` |
| `--sidebar-primary` · `--sidebar-primary-foreground` | `--navy-700` · `--white` |
| `--sidebar-accent` · `--sidebar-accent-foreground` | `--ink-100` · `--navy-700` |
| `--sidebar-border` · `--sidebar-ring` | `--ink-200` · `--navy-700` |

**Raio.** O `shadcn init` gera uma escala calculada a partir de `--radius`
(`rounded-sm` = `--radius` - 4px, `rounded-xl` = `--radius` + 4px), e o
`Card` dele usa `rounded-xl`, o que daria 12px, fora da escala. Apague esse
bloco de cálculo e use o mapa de §27.8: `rounded-xl` e `rounded-2xl` caem em
`--radius-md`, então o `Card` já sai com 8px (regra de ouro) sem edição. Trocar
a classe dele para `rounded-md` é só reforço. 10px fica para `rounded-lg`, o
cartão de login.

### 27.4 O que o lint NÃO cobre em projeto Tailwind

`lint_output.py` lê CSS e `style`; classe utilitária só é checada em parte
(família de cor, valor entre colchetes). Em projeto Tailwind,
`check_checklist.py` e a revisão manual de §25 são o instrumento principal.

### 27.5 Duas cópias dos tokens: como acusar divergência

`tokens.css` é copiado para o projeto sem edição. Rode
`check_consumer.py src/app/globals.css` (e na cópia dos tokens) no CI do
projeto: ele compara cada token colado com `scripts/tokens.json`.

### 27.6 Tabela token → utilitária

| Token | Utilitária |
|---|---|
| `--surface-base` | `bg-background` |
| `--surface-raised` | `bg-card` |
| `--navy-700` | `bg-primary` · `text-primary` |
| `--ink-900` | `text-foreground` |
| `--ink-700` | `text-muted-foreground` |
| `--ink-200` | `border-border` |
| `--danger-700` | `text-destructive` |
| `--radius-md` | `rounded-md` · `rounded-xl` · `rounded-2xl` |
| `--radius-lg` | `rounded-lg` (cartão de login) |
| `--radius-xs` | `rounded-sm` |

Prefira o papel (`bg-primary`) ao token cru (`bg-navy-700`) quando os dois
existem: o componente do shadcn já fala a língua do papel.

### 27.7 Um mecanismo de estilização por projeto

Utilitárias com o repasse acima. `assets/components.css` é a referência de
medida e estado para as variantes do shadcn (`Button`, `Card`, `Input`), não
uma folha para importar ao lado do Tailwind: as duas brigam por especificidade.

### 27.8 O `globals.css` de referência

```css
@import "tailwindcss";
@import "tw-animate-css";
@import "./psif-tokens.css";

@custom-variant dark (&:is(.dark *));

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
  --radius-xl: var(--radius-md);
  --radius-2xl: var(--radius-md);
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
  --color-navy-700: var(--navy-700);
  --color-sky-100: var(--sky-100);
  --color-sky-300: var(--sky-300);
  --color-ink-700: var(--ink-700);
  --color-ink-900: var(--ink-900);
  --color-success-700: var(--success-700);
  --color-success-100: var(--success-100);
  --color-warning-700: var(--warning-700);
  --color-warning-100: var(--warning-100);
  --color-danger-100: var(--danger-100);
}
```

O `@custom-variant dark` existe porque os componentes do shadcn trazem `dark:`
por dentro. Código do projeto não escreve `dark:` (§26.2).
