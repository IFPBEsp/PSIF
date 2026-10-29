## 12. PESSOAS E SITUAÇÃO

### 12.1 Avatar

Círculo (`--radius-pill`): `--avatar-md` (80px) no cartão de aluno e no
perfil do celular (à esquerda do nome, com anel branco de 4px),
`--avatar-sm` (56px) no cabeçalho do aluno no web (§9.10), `--target-min` em
lista do Início e da busca, `--sp-8` na barra lateral. `--avatar-lg` (120px)
fica reservado.
Foto real do aluno, recortada no rosto, em miniatura carregada sob demanda.

- Sem foto: iniciais ("JA") em peso 600 `--navy-700` sobre `--sky-300`,
  `--fs-h2` no `--avatar-md`, `--fs-display` no `--avatar-lg`. O protótipo deixa o espaço vazio (José Antonio): vazio parece
  erro de carregamento.
- Nunca foto de banco de imagem: a imagem de exemplo do protótipo tem marca
  d'água de site de banco de imagem.
- `alt` com o nome do aluno.

### 12.2 Situação do aluno

No cabeçalho do perfil (celular e web) a situação é selo: pílula com fundo
`-100`, texto `-700` peso 600 `--fs-caption`, e um ponto de 6px na cor `-700`
antes do texto. O texto está sempre presente: a cor só repete o que ele diz
(§20.2). Em lista e tabela continua texto simples.

| Situação | Selo (cabeçalho) | Texto (lista e tabela) |
|---|---|---|
| Em acompanhamento | `--success-100` / `--success-700` | `--navy-700` |
| Acompanhamento pendente | `--warning-100` / `--warning-700` | `--warning-700` |
| Acompanhamento encerrado | `--ink-100` / `--ink-700` | `--ink-700` |

Os três pares do selo passam AA nos dois temas (§3.2, §26.5). Texto de
situação só sobre branco: `--success-700` reprova sobre o céu (§3.2).

### 12.3 Observações

Texto livre da psicopedagoga ou do professor sobre o aluno (§16.2). Cartão
branco, data e autor no topo em `--fs-caption`, texto em `--fs-body` `--lh-normal`. Conteúdo
sensível: nunca em lista, notificação ou pré-visualização (§16.3).
