## 12. PESSOAS E SITUAÇÃO

### 12.1 Avatar

Círculo (`--radius-pill`): `--avatar-md` (80px) no cartão de aluno,
`--avatar-lg` (120px) no perfil, `.psif-avatar--pequeno` (`--target-min`)
em lista do Início e da busca, `.psif-avatar--mini` (`--sp-8`) no cabeçalho.
Foto real do aluno, recortada no rosto, em miniatura carregada sob demanda.

- Sem foto: iniciais ("JA") em peso 600 `--navy-700` sobre `--sky-300`,
  `--fs-h2` no `--avatar-md`, `--fs-display` no `--avatar-lg`. O protótipo deixa o espaço vazio (José Antonio): vazio parece
  erro de carregamento.
- Nunca foto de banco de imagem: a imagem de exemplo do protótipo tem marca
  d'água de site de banco de imagem.
- `alt` com o nome do aluno.

### 12.2 Situação do aluno

Texto, não etiqueta colorida solta:

| Situação | Cor do texto | Onde pode aparecer |
|---|---|---|
| Em acompanhamento | `--success-700` no perfil · `--navy-700` na lista | sempre sobre branco |
| Acompanhamento pendente | `--warning-700` | sobre branco |
| Acompanhamento encerrado | `--ink-700` | sobre branco |

A lista do protótipo usa marinho e o perfil usa verde para a mesma situação.
Mantido assim: no perfil a situação é destaque; na lista, o nome é.

### 12.3 Observações

Texto livre da psicopedagoga ou do professor sobre o aluno (§16.2). Cartão
branco, data e autor no topo em `--fs-caption`, texto em `--fs-body` `--lh-normal`. Conteúdo
sensível: nunca em lista, notificação ou pré-visualização (§16.3).
