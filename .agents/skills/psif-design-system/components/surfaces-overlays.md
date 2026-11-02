## 9. SUPERFÍCIES E SOBREPOSIÇÕES

### 9.1 Cartão

Fundo `--surface-raised`, raio de §3.6, `--card-pad`, sem borda e sem
sombra. Cartão não vai dentro de cartão: dentro dele, linha, quadro de ícone
ou célula. Título do cartão, quando há, em `--fs-body` 600 `--navy-700`
("Próximos atendimentos").

### 9.2 Indicadores

Um cartão só, com as células separadas por `--ink-200` (grade em §5.3). Cada
célula: número em `--fs-display` 600 `--navy-700`, sem zero à esquerda, e
rótulo em `--fs-body` `--ink-700`. Os quatro: "Atendimentos hoje", "Alunos
ativos", "Relatórios pendentes", "Alertas importantes". Cada célula é um link
para a lista filtrada, e o nome acessível é a frase inteira ("8 atendimentos
hoje").

### 9.3 Cartão de lista

Linhas separadas por `--ink-200`: dado-chave em `--navy-700` à esquerda, apoio
ao lado, chevron (›) `--ink-600` à direita.

- Próximos atendimentos: horário em `--fs-body` 600 e nome do aluno.
- Atendimentos do dia (Agenda): horário em `--fs-h1`, nome em `--fs-body`
  600, tipo em `--fs-caption` `--ink-700`.

### 9.4 Cartão de aluno

Avatar `--avatar-md` à esquerda (§12.1); à direita, nome em `--fs-h2` 600
`--navy-700`, curso e turma em `--fs-body` `--ink-700` e a situação (§12.2).
O cartão inteiro abre o perfil.

### 9.5 Notificação

Título em `--fs-body` 600 (`--navy-700` não lida, `--ink-900` lida), corpo em
`--fs-small` `--ink-700`, tempo relativo ("Há 15 min") em `--fs-caption`
`--ink-700` à direita. Não lida ganha ponto `--navy-700` de `--sp-2` antes do
título e "não lida" no nome acessível. Pendência ("Acompanhamento pendente")
ganha ponto `--warning-700` e "Pendente" no título.

### 9.6 Folha e diálogo

Só para o que não cabe na tela de onde se abriu: seletor de data, lista de
seleção, confirmação, menu no toque (§8.2). `--surface-overlay`,
`--sh-md`, véu `--overlay`, `--z-modal`, foco preso enquanto aberto.

- **Tela estreita:** folha que sobe da base (`Drawer`), cantos de cima em
  `--radius-lg`; fecha arrastando, em "Fechar" ou Esc.
- **A partir de `--bp-md`:** diálogo centralizado (`Dialog`), `--radius-lg`,
  até `--w-form`; fecha em "Fechar", no véu ou Esc.

Exceção: com mouse, os resultados da busca global abrem como cartão ancorado
no campo (§7.13). Folha, diálogo e lista são renderizados na raiz do
documento, senão o `overflow` do cartão os corta.

### 9.7 Cartão de funcionalidade (página pública)

Círculo `--navy-700` de `--control-min` com ícone `--white`, título em
`--fs-body` 600 `--ink-900` e descrição em `--fs-small` `--ink-700`.

### 9.8 Cartão de autenticação

Cartão central até `--w-auth`, `--radius-lg`, `--sh-sm`: símbolo e "PSIF",
nome por extenso, campos e botão primário. Login e Recuperar senha.

### 9.9 Cabeçalho do aluno (tela larga)

Cartão `--radius-2xl` no topo da área do aluno: avatar `--avatar-sm` em
`--sky-300`, nome em `--fs-display` 600 `--navy-700`, curso e turma em
`--fs-small` `--ink-700` e o selo de situação (§12.2). Embaixo, as abas
(§7.5).

### 9.10 Próximo atendimento

Quadro de ícone `--tile-icon-lg` (`psif-calendario`, `--sky-100`), rótulo
"Próximo atendimento" em `--fs-caption` 600 `--ink-700`, quando em `--fs-h3`
600 `--navy-700` ("Quinta, 05/11 · 10:00"), tipo em `--fs-small` `--ink-700`
e chevron para a agenda. Sem atendimento: "Nenhum atendimento marcado." e
"+ Novo agendamento".

### 9.11 Aviso de sigilo

Ícone `psif-cadeado` num círculo `--warning-100` com o ícone em
`--warning-700`, título "Documentos sigilosos" e o texto "Laudos e relatórios
psicológicos são da psicopedagoga. Outros perfis só abrem o que for liberado
para eles." Fica na coluna lateral da aba Documentos, na tela larga.
