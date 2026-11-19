## 11. LISTAS, TABELA E CALENDÁRIO

Sem gráfico: dado aparece em indicador (§9.2), lista, tabela e linha do tempo.

### 11.1 Lista de alunos

Tela estreita: cartões de aluno (§9.4) com `--sp-6` entre eles, sob busca e
filtros. A partir de `--bp-md`: tabela (§11.8). Ordem alfabética.

### 11.2 Lista de documentos

Agrupada por período, cada grupo com título de grupo ("Este mês",
"Anteriores", §4.3) e um cartão (raio de §3.6) com `--sp-1` de respiro
interno. Cada linha: `--list-row-pad` em volta, `--radius-md`, hover `--ink-100`;
quadro de ícone `--tile-icon` com `psif-termo`; nome em `--fs-body` 500
`--navy-700` com extensão ("Laudo médico.pdf"); embaixo, tamanho e data em
`--fs-caption` `--ink-700` ("12 MB · 10/08/2025") e, se for o caso, o selo
"Sigiloso" (§16.3); chevron à direita. Filtros por tipo acima (§7.6). O
arquivo só baixa ao abrir.

### 11.3 Indicador sem dado

Mostra "0", nunca vazio.

### 11.4 Filtros

Meus alunos: **Turma · Série · Período**, filtros com valor que abrem a
seleção (§7.6, §8.4). Documentos: por tipo, de escolha direta (Todos · Laudos
· Relatórios · Declarações).

### 11.5 Linha do tempo (Evolução)

Eventos em ordem cronológica, ligados por linha vertical de 1px `--ink-200`.
Cada evento: marcador de `--ic-sm` à esquerda, na cor do tipo; data em `--fs-body`
500 `--navy-700`; título em `--fs-body` 600 `--ink-900`; descrição em
`--fs-small` `--ink-700`.

| Tipo | Marcador |
|---|---|
| Atendimento (primeiro, encerramento) | `--navy-700` |
| Conversa com a família | `--navy-500` |
| Avanço ou mudança observada | `--success-700` |
| Relatório emitido | `--ink-600` |

`--warning-700` fica para pendência e alerta (§10.1), nunca para evento
comum.

O tipo vai escrito no título; a cor só repete (§20.2). Emoji nunca é
marcador.

### 11.6 Calendário

Cabeçalho "Junho 2026" com ‹ e › (`aria-label` "Mês anterior" e "Próximo
mês"), linha Dom … Sáb e a grade. Dia: círculo com 1/7 da linha, até
`--target-min`; na tela estreita fica menor, nunca abaixo de 24px (WCAG
2.5.8): em 320px, num cartão, dá uns 34px. Hoje com anel `--navy-700` e
`aria-current="date"`; selecionado com fundo `--navy-700`, número `--white` e
`aria-pressed="true"`; dia com atendimento com ponto `--navy-500` embaixo.
Abre em folha ou diálogo a partir do campo de data (§9.6), ou fica no topo da
Agenda.

A partir de `--bp-md`, divide a Agenda ao meio com a agenda do dia.

### 11.7 Agenda do dia

Cartão "Atendimentos de hoje": horário, nome, tipo (§9.3). Vazio: "Nenhum
atendimento hoje." e "+ Novo agendamento".

### 11.8 Tabela

A partir de `--bp-md`, as listagens principais (alunos, atendimentos,
relatórios, documentos, usuários) viram `DataTable` em `shared`, sobre
TanStack Table, com colunas da feature. É a mesma consulta da lista da tela
estreita; muda a apresentação.

- **Estado na URL** (nuqs): `?page=0&size=20&search=mar&sort=name,asc`.
  Busca com `--dur-debounce` (§7.7). Recarregar e compartilhar o link
  mantêm a lista.
- **Cartão**: dentro de um cartão (raio de §3.6); tabela que não cabe rola
  dentro dele.
- **Faixa intermediária**: só as colunas principais; as secundárias ("Enviado
  por", data) aparecem a partir de `--bp-lg`.
- **Cabeçalho** em `--fs-caption` 600 `--ink-700`; coluna ordenável é botão
  com `aria-sort`.
- **Linha**: altura mínima `--target-min`, separada por `--ink-200`, hover
  `--ink-100`.
- **Célula-chave**: quadro de ícone, nome em `--navy-700` 500 como link para
  o detalhe e, embaixo, tamanho e selo.
- **"Enviado por"**: avatar `--sp-8` de §12.1 e o nome.
- **Ações**: botão ⋯ com `aria-label` ("Ações de José Antonio"), menu com
  mouse ou folha no toque (§8.2); a coluna não tem rótulo visível.
  Destrutiva pede confirmação (§10.3).
- **Número** à direita, algarismos tabulares; data no formato de §19.3.
- **Seleção** com caixa só quando há ação em lote.
- **Rodapé**: "Mostrando 4 de 4" em `--fs-caption` `--ink-700` e, com mais
  de uma página, paginação ("Anterior", "Próxima", itens por página).
- **Estados**: esqueleto em formato de linha; "Nenhum aluno cadastrado." com a
  ação de criar; "Nenhum aluno encontrado para estes filtros." com "Limpar
  filtros".
- **Sigilo**: nome, turma e situação; nada clínico (§16.3).
