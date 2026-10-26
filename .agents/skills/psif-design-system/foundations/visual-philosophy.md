## 2. FILOSOFIA VISUAL

### 2.1 Princípios

- **Calmo.** Uma família de azul, fundo claro, nada que pisque. O PSIF é
  aberto entre um atendimento e outro, às vezes com o aluno na sala.
- **Institucional, não clínico.** Branco e marinho do IFPB-sério, sem o
  verde-hospital nem o tom infantil de app escolar.
- **Um assunto por cartão.** Cada cartão branco responde uma pergunta
  ("quem atendo hoje?", "o que falta?").
- **Dado primeiro.** Nome, horário e número em marinho; o resto em cinza.
- **Ferramenta, não vitrine.** O app é de trabalho: a marca vive na cor, na
  fonte e na densidade, e navegação e controles são os que todo mundo já sabe
  usar. Estranheza sem propósito: botão enfeitado, controle inventado,
  movimento gratuito: é defeito, não personalidade. Só a página pública
  (§13.7) pode chamar atenção.

### 2.2 Superfícies e camadas (modelo mental)

Três planos, sempre nesta ordem:

1. **Céu** (`--surface-base`): o chão. Nunca recebe texto longo direto,
   só título de tela, rótulo de campo e título de seção.
2. **Cartão branco** (`--surface-raised`): onde mora o conteúdo. Raio
   `--radius-md`, sem borda, sem sombra.
3. **Marinho** (`--navy-700`): a ação. Botão primário, e nada mais de área
   grande.

Folha modal (seletor de data, confirmação) é um cartão branco sobre
`--overlay`, com `--sh-md`.

### 2.3 Iluminação e gradiente

Sem gradiente. Sem glass. Sombra só no botão primário e no cartão de login
(`--sh-sm`), e na folha modal (`--sh-md`). A ilustração de "Recuperar
senha" (mancha `--navy-500` translúcida, envelope e cadeado em
`--navy-700`) é a única peça decorativa do sistema e só vale em tela de
autenticação.

### 2.4 Superfícies do navegador

O que a tela não desenha também é PSIF. O `assets/tokens.css` já aplica:

- seleção de texto em `--sky-300` com texto `--ink-900`;
- cursor de digitação e controle nativo (caixa de seleção, rádio) em
  `--navy-700`;
- sublinhado de link afastado do texto (`text-underline-offset: .2em`);
- número tabular em `<time>`, `<data>` e célula de tabela: horário, data,
  indicador, matrícula e tamanho de arquivo vão nessas tags, para que 09:00
  e 14:00 não dancem na coluna;
- campo com fonte de 16px (§8.3).

Barra de rolagem e anel de foco: os do sistema e o de §20.5. Nada de rolagem
customizada.
