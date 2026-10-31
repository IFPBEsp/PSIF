## 26. MODO ESCURO

### 26.1 A regra

O PSIF tem tema claro, escuro e sistema (seção 15 de
`docs/frontend/architecture-and-stack.md`, no projeto). O claro é o do protótipo e continua o padrão de desenho. O
escuro é a mesma hierarquia com outros valores:

**Fundo noite, cartão um degrau acima, ação em céu.** O papel de cada token não
muda: `--navy-700` continua marcando o que se clica e o que se lê primeiro, só
que em céu claro sobre o escuro. O teste de cinco segundos (regra de ouro) vale
igual: o único bloco largo da cor de ação é o botão primário.

A paleta escura é a **"noturno"**: derivada, não medida, porque o protótipo
estático não desenha modo escuro. Foi validada no protótipo navegável contra
as variações escuro, marinho, grafite e suave: fundo profundo, cartão um pouco
mais azul e ação em céu claro, para as camadas céu e cartão se separarem no
escuro. Está registrada em §28.4.

### 26.2 Como funciona

`assets/tokens.css` traz os tokens `--dark-*` e um bloco gerado
`:root.dark, :root[data-theme="dark"]` que troca cada token pelo par escuro
(`--navy-700: var(--dark-navy-700)`). Quem consome `var(--navy-700)`,
`var(--surface-base)` ou `bg-primary` recebe o valor do tema ativo sem mudar
nada.

- A classe fica no `<html>`. Os aliases (`--surface-base: var(--sky-100)`, a
  ponte do shadcn em §27.3) são resolvidos no `<html>`; classe num elemento
  abaixo dele não troca esses aliases.
- No Next.js, `next-themes` com `attribute="class"`, `defaultTheme="system"`,
  `enableSystem` e `disableTransitionOnChange`. O `<html>` leva
  `suppressHydrationWarning`.
- Nunca use `--dark-*` direto numa tela. Ele só existe para o bloco `.dark`
  apontar para ele.
- Evite a variante `dark:` do Tailwind na tela. O token já troca; um `dark:`
  avulso vira a segunda versão da paleta.
- Apague o bloco `.dark { --background: ... }` que o shadcn gera no
  `globals.css`. A ponte de §27.3 serve aos dois temas.

### 26.3 O que muda além da cor

- **Sombra e véu trocam de tinta.** A sombra tingida de marinho some sobre o
  fundo escuro. No escuro, `--sh-sm` vira `0 4px 4px rgba(3,9,15,.35)`,
  `--sh-md` vira `0 12px 32px rgba(3,9,15,.45)` e o véu `--overlay` vira
  `rgba(3,9,15,.65)`, todos com a tinta quase preta do escuro (não preto puro,
  §3.4). O cartão comum continua sem sombra: ele se separa do fundo pela
  luminosidade (`--white` escuro sobre `--sky-100` escuro). Não troque a
  sombra por borda.
- **Texto do botão primário fica escuro.** `--white` vira a cor do cartão, e o
  texto sobre `--navy-700` continua `var(--white)`. Não escreva `#fff` no
  botão.
- **Símbolo do PSIF não inverte.** O quadrado azul com o cérebro branco
  (`simbolo-psif.svg`) tem cores próprias e fica igual nos dois temas. O glifo
  (`simbolo-psif-glifo.svg`) usa `currentColor` e acompanha o texto.
- **Foto e anexo não invertem.** Nenhum `filter: invert()` em imagem.
- **Banlist vale por papel.** `--ink-600`, `--ink-500`, `--navy-500`,
  `--sky-300` e `--blue-300` continuam proibidos como texto no escuro, mesmo
  quando o par escuro passaria.

### 26.4 Troca de tema

Fica no menu do usuário, com três opções escritas: "Claro", "Escuro" e
"Sistema". "Sistema" é o padrão. A escolha vale para o aparelho, não para a
conta: é uma das poucas preferências que cabem em estado local (seção 15
da doc de frontend do projeto). Ícone sozinho (sol e lua) não basta: o rótulo diz o tema.

### 26.5 Pares verificados

Conferidos por `test_contrast_table.py` contra `check_contrast.py`. Combinação
fora daqui passa por `check_contrast.py dark-<texto> dark-<fundo>`.

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
--dark-blue-700 / --dark-white         8.19:1 ✓ AAA   logo de login sobre cartão (só marca)
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
4.50:1 (marcador, ícone de 24px ou mais). Os dois continuam banidos como
texto.

A banlist não muda: `--ink-600`, `--ink-500`, `--navy-500`, `--sky-300` e
`--blue-300` nunca são cor de texto, em nenhum tema.
