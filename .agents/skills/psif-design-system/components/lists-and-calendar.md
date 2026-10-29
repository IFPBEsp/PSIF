## 11. LISTAS, TABELA E CALENDÁRIO

O PSIF não tem gráfico. Dado aparece como número de indicador (§9.2), lista,
tabela (só no web, §11.8) e linha do tempo.

### 11.1 Lista de alunos

No celular, cartões de aluno (§9.4) empilhados com `--sp-6` entre eles, sob
busca e filtros. No web, tabela (§11.8). Ordem padrão: alfabética.

### 11.2 Lista de documentos

Documentos agrupados por período, cada grupo com título em `--fs-caption`
600 `--navy-700` ("Este mês", "Anteriores") e um cartão branco
(`--radius-xl`, `--sp-1` de respiro interno). Cada linha: altura mínima
56px, `--radius-md`, hover `--ink-100`; à esquerda, quadro de ícone
`--tile-icon` em `--sky-100` com `psif-termo` em `--navy-700`; nome em
`--fs-body` 500 `--navy-700` com extensão ("Laudo médico.pdf"); embaixo,
tamanho e data em `--fs-caption` `--ink-700` ("12 MB · 10/08/2025") e, se for
o caso, o selo "Sigiloso" (§16.3); chevron à direita. Filtros por tipo acima
da lista (§7.6). "+ Adicionar documento" na barra de ação (§8.1). O arquivo só
baixa ao abrir.

### 11.3 Indicadores

Ver §9.2. Indicador sem dado mostra "0", nunca vazio.

### 11.4 Filtros

Filtros de "Meus alunos": **Turma · Série · Período**. Cada filtro é uma
pílula (§7.6) que abre folha de seleção; com valor escolhido, fica no estilo
ativo (fundo `--navy-700`, texto branco, peso 600), mostra o valor ("3º ano")
e um × para limpar. Na lista de documentos o filtro é por tipo, de escolha
direta: Todos · Laudos · Relatórios · Declarações.

### 11.5 Linha do tempo (Evolução do aluno)

Eventos em ordem cronológica, ligados por linha vertical de 1px
`--ink-900` (medido). Cada evento:

- **Marcador**: círculo de 16px à esquerda, cor pelo tipo de evento.
- Data em `--fs-body` peso 500 `--navy-700` ("15/03/2026").
- Título em `--fs-body` peso 600 `--ink-900` ("Primeiro atendimento").
- Descrição em `--fs-small` `--ink-700`.

Tipos e cores (proposta: o protótipo usa emoji sem legenda, §28):

| Tipo | Marcador |
|---|---|
| Atendimento (primeiro, encerramento) | `--success-700` |
| Conversa com a família | `--success-700` |
| Avanço / mudança observada | `--warning-700` |
| Relatório emitido | `--navy-500` |

O tipo vai escrito no título do evento; a cor só repete (§20.2). Nunca use
emoji como marcador: a renderização muda por sistema e o leitor de tela lê
"círculo verde grande".

### 11.6 Calendário

Seletor de mês: cabeçalho "Junho 2026" com setas ‹ › nos lados, linha de dias
da semana (Dom … Sáb) e a grade do mês. Dia de hoje com anel `--navy-700`;
dia selecionado com fundo `--navy-700` e número branco; dia com atendimento
com ponto `--navy-500` embaixo. Abre em folha (§9.6) a partir do campo de
data, ou fica no topo da Agenda. A imagem do protótipo é uma captura de
calendário do sistema: o componente é o descrito aqui, com os tokens do
PSIF.

Cabeçalho do mês: título de cartão (§9.1) centralizado entre as setas, que
são botões só de ícone (`--ic-md` em alvo `--target-min`, `--ink-900`,
§18), com `aria-label` "Mês anterior" e "Próximo mês". Dia: círculo de
`--target-min`; o de hoje leva `aria-current="date"`, o selecionado
`aria-pressed="true"`.

No web, o calendário divide a Agenda ao meio com a agenda do dia (§11.7).
Nunca numa coluna mais estreita que sete alvos de toque (7 ×
`--target-min`): o dia viraria alvo pequeno.

### 11.7 Agenda do dia

Cartão "Atendimentos de hoje" sob o calendário: horário em destaque, nome,
tipo (§9.3). Vazio: "Nenhum atendimento hoje" com o botão "+ Novo
agendamento".

### 11.8 Listagem no web (tabela)

As listagens principais (alunos, atendimentos, relatórios, documentos,
usuários) seguem a seção 13 de `docs/frontend/architecture-and-stack.md`, no
projeto: `DataTable` genérico em `shared`, com colunas e barra de ferramentas
da feature, sobre TanStack Table.

**Formato por largura.** A partir de `--bp-md`, tabela. No celular, os mesmos
dados como cartões (§11.1) ou linhas de lista (§11.2). É a mesma consulta e o
mesmo estado de URL; muda só a apresentação.

**Estado na URL.** Paginação no servidor, ordenação, filtros e busca ficam na
URL, com nuqs: `?page=0&size=20&search=mar&sort=name,asc`. A busca espera a
digitação parar (debounce) antes de consultar. Recarregar, voltar e
compartilhar o link mantêm a lista como estava.

**Visual** (`Table` do shadcn, classes em §6):

- A tabela fica dentro de um cartão branco (§9.1), `--radius-2xl`, sem borda e
  sem sombra. Rolagem horizontal, se houver, é dentro do cartão, nunca na
  página.
- Cabeçalho em `--fs-caption` peso 600 `--ink-700`.
- Linha com altura mínima `--target-min`, padding `--sp-3` `--sp-4`, separada
  por `--ink-100`, hover `--ink-100`.
- A célula-chave leva o quadro de ícone (`--tile-icon`), o nome e, embaixo, o
  tamanho e o selo ("Sigiloso", §16.3).
- Coluna "Enviado por": iniciais num círculo `--ink-100` de 28px e o nome.
- A coluna de ações não tem rótulo visível; o cabeçalho dela existe só para
  leitor de tela.
- A coluna-chave (nome do aluno, título do relatório) em `--navy-700` peso 500
  e é o link para o detalhe. Número alinhado à direita, com algarismos
  tabulares; data no formato de §19.3.
- Ações da linha num botão de ícone (⋯) com `aria-label` ("Ações de José
  Antonio") que abre menu. Ação destrutiva pede confirmação (§10.3).
- Coluna ordenável: o cabeçalho é botão, com ícone de direção e `aria-sort`.
- Seleção com caixa só quando existe ação em lote.

**Em volta da tabela.** Acima: busca (§7.7) e filtros (§11.4); a ação
primária fica na barra superior (§7.3). Abaixo: o rodapé "Mostrando 4 de 4"
em `--fs-caption` `--ink-700` e, quando há mais de uma página, a paginação, botões "Anterior" e "Próxima" de `--target-min` e
seletor de itens por página.

**Estados** (§10):

- Carregando: esqueleto em formato de linha de tabela, não spinner.
- Vazio sem registro: "Nenhum aluno cadastrado." com a ação de criar.
- Vazio por filtro: "Nenhum aluno encontrado para estes filtros." com
  "Limpar filtros". Os dois casos têm texto diferente.

**Sigilo.** Coluna de tabela segue a regra de lista: nome, turma e situação;
nada clínico (§16.3).

