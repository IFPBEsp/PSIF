## 12. PESSOAS E SITUAÇÃO

### 12.1 Avatar

Círculo (`--radius-pill`):

| Token | Onde |
|---|---|
| `--avatar-md` | cartão de aluno, cabeçalho do perfil na tela estreita (com anel branco de 4px) |
| `--avatar-sm` | cabeçalho do aluno na tela larga (§9.9) |
| `--target-min` | lista do Início e resultados da busca |
| `--sp-8` | barra lateral |
| `--avatar-lg` | reservado |

Foto real do aluno, recortada no rosto, em miniatura carregada sob demanda.

- Sem foto: iniciais ("JA") em peso 600 `--navy-700` sobre `--sky-300`,
  `--fs-h2` no `--avatar-md`, `--fs-display` no `--avatar-lg`. Nunca círculo
  vazio: parece erro de carregamento.
- Nunca foto de banco de imagem.
- `alt` com o nome do aluno.

### 12.2 Situação do aluno

No cabeçalho do perfil, a situação é selo: pílula com fundo `-100`, texto
`-700` peso 600 `--fs-caption` e um ponto de `--sp-2` na cor `-700` antes do
texto. O texto está sempre presente; a cor só repete o que ele diz (§20.2).
Em lista e tabela, texto simples.

| Situação | Selo (cabeçalho) | Texto (lista e tabela) |
|---|---|---|
| Em acompanhamento | `--success-100` / `--success-700` | `--navy-700` |
| Acompanhamento pendente | `--warning-100` / `--warning-700` | `--warning-700` |
| Acompanhamento encerrado | `--ink-100` / `--ink-700` | `--ink-700` |

Texto de situação só sobre branco: `--success-700` reprova sobre o céu
(§3.2).

### 12.3 Observações

Texto livre da psicopedagoga ou do professor sobre o aluno (§16.2). Cartão
branco, data e autor no topo em `--fs-caption`, texto em `--fs-body`
`--lh-normal`. Conteúdo sensível: nunca em lista, notificação ou
pré-visualização (§16.3).
