## 2. FILOSOFIA VISUAL

### 2.1 Princípios

- **Calmo.** Uma família de azul, fundo claro, nada que pisque: a tela é lida
  entre um atendimento e outro, às vezes com o aluno na sala.
- **Institucional.** Branco e marinho do IFPB, sem o verde de hospital nem o
  tom infantil de app escolar.
- **Um assunto por cartão.** Cada cartão responde uma pergunta ("quem atendo
  hoje?", "o que falta?").
- **Dado primeiro.** Nome, horário e número em marinho; o resto em cinza.
- **Ferramenta de trabalho.** Controles que você já sabe usar. Botão
  enfeitado, controle inventado e movimento gratuito são defeito. Só a página
  pública (§13.6) chama atenção.

### 2.2 Camadas: a regra de ouro

**Fundo céu, cartão branco, ação em marinho.**

1. **Céu** (`--surface-base`): o chão. Recebe título de tela, rótulo de campo
   e título de grupo, nunca texto longo.
2. **Cartão** (`--surface-raised`): onde mora o conteúdo, raio por papel
   (§3.6), sem borda e sem sombra.
3. **Marinho** (`--navy-700`): o que se clica e o que se lê primeiro (título,
   número, nome, botão). O único bloco largo de marinho na tela é o botão
   primário; a medida está em §3.3.

Folha e diálogo (§9.6) são cartão sobre `--overlay`.

### 2.3 Iluminação

Sem gradiente, sem vidro. Onde vai sombra: §3.4. A ilustração de "Recuperar
senha" (mancha `--navy-500` translúcida, envelope e cadeado em `--navy-700`)
é a única peça decorativa e só vale em tela de autenticação.

### 2.4 Superfícies do navegador

O `assets/tokens.css` já aplica: seleção de texto em `--sky-300` com
`--ink-900`; cursor e controle nativo em `--navy-700`; sublinhado de link
afastado do texto; número tabular em `<time>`, `<data>` e célula de tabela;
campo em `--fs-h3`. Barra de rolagem e anel de foco: os do sistema e o de
§20.5.
