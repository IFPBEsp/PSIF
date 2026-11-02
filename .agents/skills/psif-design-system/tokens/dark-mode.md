## 25. MODO ESCURO

### 25.1 A regra

Tema claro, escuro e sistema (seção 15 de
`docs/frontend/architecture-and-stack.md`, no projeto). O claro é o padrão de
desenho; o escuro é a mesma hierarquia com outros valores: **fundo noite,
cartão um degrau acima, ação em céu claro**. O papel de cada token não muda,
e a regra de ouro (§2.2) vale igual.

### 25.2 Como funciona

`assets/tokens.css` traz os tokens `--dark-*` e o bloco
`:root.dark`, que troca cada token pelo par escuro
(`--navy-700: var(--dark-navy-700)`). Quem consome `var(--navy-700)`,
`var(--surface-base)` ou `bg-primary` recebe o valor do tema ativo.

- A classe fica no `<html>`, onde os aliases (`--surface-base`, a ponte de
  §26.3) são resolvidos.
- No Next.js: `next-themes` com `attribute="class"`, `defaultTheme="system"`,
  `enableSystem` e `disableTransitionOnChange`; `<html suppressHydrationWarning>`.
- `--dark-*` nunca aparece numa tela; só o bloco `.dark` aponta para ele.
- Sem `dark:` do Tailwind na tela: o token já troca.
- Apague o bloco `.dark { --background: ... }` que o shadcn gera no
  `globals.css`; a ponte de §26.3 serve aos dois temas.

### 25.3 O que muda além da cor

- **Sombra e véu** usam a tinta quase preta do escuro (pares `--dark-sh-*` e
  `--dark-overlay`). Cartão comum segue sem sombra e sem borda: separa do
  fundo pela luminosidade.
- **Texto do botão primário** é `var(--white)`, que no escuro vira a cor do
  cartão. Nunca `#fff`.
- **Símbolo** (`simbolo-psif.svg`) fica igual nos dois temas; o glifo
  (`simbolo-psif-glifo.svg`) usa `currentColor`.
- **Foto e anexo** não invertem: nenhum `filter: invert()`.

### 25.4 Troca de tema

Em Meu perfil (§7.1), com três opções escritas: "Claro", "Escuro" e
"Sistema" (padrão), no mesmo lugar em qualquer largura. Vale para o aparelho, em estado local, não para a conta. Ícone
sozinho (sol e lua) não basta.

### 25.5 Pares verificados

Combinação fora daqui passa por
`check_contrast.py dark-<texto> dark-<fundo>`.

```
--dark-ink-900 / --dark-sky-100       16.33:1 ✓ AAA   texto principal no fundo
--dark-ink-900 / --dark-white         13.89:1 ✓ AAA   texto principal no cartão
--dark-ink-900 / --dark-ink-100       11.81:1 ✓ AAA   texto em campo e área afundada
--dark-ink-900 / --dark-sky-300        9.65:1 ✓ AAA   rótulo sobre atalho
--dark-ink-700 / --dark-sky-100        9.39:1 ✓ AAA   texto secundário no fundo
--dark-ink-700 / --dark-white          7.99:1 ✓ AAA   texto secundário no cartão
--dark-navy-700 / --dark-sky-100      10.62:1 ✓ AAA   título e dado-chave no fundo
--dark-navy-700 / --dark-white         9.04:1 ✓ AAA   título e dado-chave no cartão
--dark-navy-700 / --dark-sky-300       6.28:1 ✓ AA    ícone e item ativo sobre céu
--dark-white / --dark-navy-700         9.04:1 ✓ AAA   rótulo do botão primário
--dark-white / --dark-navy-800        11.03:1 ✓ AAA   botão primário em hover
--dark-white / --dark-navy-900        12.80:1 ✓ AAA   botão primário pressionado
--dark-success-700 / --dark-white      8.34:1 ✓ AAA   sucesso no cartão
--dark-success-700 / --dark-success-100  8.00:1 ✓ AAA   sucesso no alerta
--dark-warning-700 / --dark-white      8.56:1 ✓ AAA   atenção no cartão
--dark-warning-700 / --dark-warning-100  8.20:1 ✓ AAA   atenção no alerta
--dark-danger-700 / --dark-white       7.26:1 ✓ AAA   erro de campo no cartão
--dark-danger-700 / --dark-danger-100  7.48:1 ✓ AAA   erro no alerta
--dark-ink-700 / --dark-ink-100        6.79:1 ✓ AA    selo "Encerrado" (§12.2)
```

Componente de interface (piso 3:1): `--dark-ink-600` sobre `--dark-white`
4.72:1 (borda de campo, ícone) e `--dark-navy-500` sobre `--dark-white`
4.50:1 (marcador, ícone de 24px ou mais). A banlist de §3.2 vale nos dois
temas.
