## 7. NAVEGAÇÃO

### 7.1 Navegação principal

Uma navegação só: a barra lateral (§7.10), que vira gaveta na tela estreita
(§7.9). Sem barra inferior. Destinos, nesta ordem: **Início · Atendimentos ·
Alunos · Relatórios**, depois **Agenda · Notificações · Meu perfil**, e
**Sair** no pé. A lista sai de uma configuração central, e cada item aparece
só para o perfil com permissão para ele (§16.2). "Termo" fica fora até ter
destino (§27).

### 7.2 Menu (☰)

Na tela estreita, o ☰ fica à direita da barra de ações das telas-raiz (Início
e listas) e abre a gaveta: `aria-label="Abrir menu"`, `aria-expanded`
acompanhando a gaveta. Tela de tarefa e de detalhe têm ← no lugar (§7.4).

### 7.3 Barra de ações e título

A barra de ações fica sobre `--surface-base`, sem sombra, com o topo de
§5.1, e só tem botões de ícone em `--radius-pill`, cada um com `aria-label`
que diz o destino:

- Esquerda: voltar (←), `--ic-sm` em alvo `--target-min` ("Voltar para
  Alunos").
- Direita: busca (§7.7), ⋯ ("Mais ações do aluno") ou ☰ (§7.2).

O título vem logo abaixo da barra (§4.3). Na tela larga, o topo do conteúdo
tem os breadcrumbs e Notificações (§7.13), e a ação primária fica à direita
do título (§5.6).

O Início é a exceção: no lugar do título, a saudação (texto em §19.4) em
`--fs-h1` `--ink-900` e a data de hoje embaixo em `--fs-small` `--ink-700`.

### 7.4 Voltar

Mesmo ícone (←), mesmo lugar, volta um nível. Formulário com conteúdo
digitado pergunta antes de descartar (§10.3).

### 7.5 Seções do aluno

**Tela estreita**: grade de duas colunas de cartões (raio de §3.6, mesma
altura na linha, `--sp-3` de vão), sob o título de grupo "Prontuário". Cada
cartão: nome da seção em `--fs-body` 600 `--navy-700` e, embaixo, um resumo em
`--fs-caption` `--ink-700` vindo do backend ("12 registros", "4 arquivos");
sem resumo, só o nome. Seções: Dados do aluno · Atendimentos · Relatórios ·
Documentos · Observações · Evolução.

**Tela larga**: abas sob o cabeçalho do aluno (§9.9): Visão geral (com os
dados do aluno) · Atendimentos · Relatórios · Documentos · Observações ·
Evolução. Ativa em `--navy-700` 600, com sublinhado de 3px e contador em
pílula `--sky-100`; inativas em `--ink-700`
500. Cada aba é um link (`aria-current="page"` na ativa), com alvo
`--target-min`.

O resumo de Documentos mostra contagem ("2 sigilosos"), nunca nomes (§16.3).

### 7.6 Filtros de lista

Pílula (`--radius-pill`), altura `--target-min`, `--chip-pad`, `--fs-small`.
Inativo: transparente, borda `--line-on-sky`, texto `--navy-700` 500. Ativo:
fundo `--navy-700`, texto `--white`, 600. Na tela estreita a linha rola na
horizontal, sem quebrar.

- **Escolha direta** (documentos: Todos · Laudos · Relatórios ·
  Declarações): um ativo por vez. Botão solto leva `aria-pressed`; o
  `ToggleGroup type="single"` anuncia com `role="radio"` e `aria-checked`.
- **Filtro com valor** (Turma · Série · Período, em Meus alunos): abre a
  seleção (§11.4) com o `aria-haspopup` de §8.4; com valor, fica ativo, mostra
  o valor e um × para limpar.

### 7.7 Busca

Campo de largura total no topo da lista, lupa à esquerda, placeholder
"Pesquisar aluno" ou "Pesquisar documento", e espera `--dur-debounce` depois
da digitação. Rótulo só acessível: é o único campo sem rótulo visível, porque a
lupa e a posição dizem o que ele é.

Na tela estreita, em tela com título grande, a busca começa como botão de
lupa na barra de ações e abre o campo no lugar do título. A busca pode ter
fundo `--ink-100` sem borda; campo de formulário, não (§8.3).

### 7.8 Ações rápidas

Cartão "Ações rápidas" no Início: até quatro atalhos por linha, quebrando
linha em vez de encolher. Cada um: quadrado `--sky-300` de `--sp-12` com
ícone `--navy-700` `--ic-lg` e rótulo `--fs-caption` `--ink-700` embaixo.
Agenda · Meu perfil · Notificações.

### 7.9 Gaveta

Abaixo de `--bp-md`, a barra lateral vira gaveta: entra pela esquerda sobre
`--overlay`, com `--z-modal`, largura `--w-sidebar` e `--sh-md`; mesmo
conteúdo e ordem. No projeto, o `Sidebar` do shadcn monta a gaveta com o `Drawer`, que fecha arrastando.

- Fecha num destino, no véu, em Esc ou arrastando para a esquerda, e o foco volta ao ☰.
- Abre com o foco no item ativo e prende o foco enquanto aberta.
- Entra em `--dur-normal` (§17.3).

### 7.10 Barra lateral

A partir de `--bp-md`, fixa à esquerda, altura da janela, fundo
`--surface-raised`, sem borda e sem sombra, `<nav aria-label="Principal">`.
Entre `--bp-md` e `--bp-lg` começa recolhida (§7.12); a partir de `--bp-lg`,
aberta com `--w-sidebar`. O `Sidebar` do shadcn vem com 16rem: passe a largura
no `SidebarProvider`, com `style={{ "--sidebar-width": "var(--w-sidebar)" } as
React.CSSProperties}`.

De cima para baixo, com `--sp-6` de padding:

1. **PSIF** em `--fs-h1` 600 `--navy-700`, sem o símbolo; à
   direita, o botão de recolher.
2. Busca global "Pesquisar aluno" (§7.13).
3. Início · Atendimentos · Alunos · Relatórios.
4. Linha `--ink-200`, recuada dos dois lados, depois Agenda · Notificações · Meu perfil.
5. No pé, cartão `--ink-100` (raio de §3.6) com iniciais, nome, papel e
   "Sair".

Item: ícone `--ic-lg` e rótulo `--fs-body` 500, `--radius-lg`, alvo
`--target-min`. Inativo `--ink-700`; ativo fundo `--sky-100`, `--navy-700`,
600, `aria-current="page"`; hover com mouse `--ink-100`.

### 7.11 Breadcrumbs

Trilha derivada da rota ou da configuração de navegação ("Alunos › José
Antonio › Relatórios"), com o `Breadcrumb` do shadcn.

- A partir de `--bp-md`, no topo do conteúdo, à esquerda (§7.13),
  `--fs-small`. Anteriores em link `--ink-700`; o atual em `--ink-900`, sem
  link, `aria-current="page"`. Separador › `aria-hidden`.
  `<nav aria-label="Trilha">`.
- Na tela estreita não aparece: o ← volta um nível e o título diz onde se
  está.
- Só a partir do segundo nível.
- Nome de aluno sim; dado clínico nunca (§16.3).

### 7.12 Barra lateral recolhida

A barra recolhe para só ícones (`Sidebar collapsible="icon"`, com o
`SidebarTrigger`).

- **Controle:** ☰ (`psif-menu`, `--ic-lg`, alvo `--target-min`,
  `--radius-pill`) à direita da marca; recolhida, no topo da barra.
  `aria-label` "Recolher menu" ou "Expandir menu" e `aria-expanded`.
- **Recolhida:** rótulos e nome PSIF somem; itens centralizados; a busca vira
  botão de lupa, que abre a busca como em §7.13; o cartão do pé vira as
  iniciais. Cada item mantém `title` e nome acessível.
- Começa recolhida entre `--bp-md` e `--bp-lg`, e aberta depois. A escolha
  da pessoa vale para o aparelho, como o tema (§25.4).

### 7.13 Busca global e topo do conteúdo

A partir de `--bp-md`.

- **Busca global** na barra lateral, sob a marca: fundo `--ink-100` sem
  borda, lupa, placeholder e `aria-label` "Pesquisar aluno", dentro de
  `role="search"`. Passa pelo BFF, com `--dur-debounce`. No projeto, `Command`;
  resultados em `Popover` com mouse e na folha de §9.6 no toque.
- **Resultados:** com mouse, cartão branco ancorado no campo (`--sh-md`,
  `--z-overlay`); no toque, a folha de §9.6, em qualquer largura (§5.12).
  Linhas com avatar `--target-min`, nome e turma. Clicar abre o perfil; Enter
  leva a Meus alunos com a busca aplicada; Esc limpa. Sem resultado: §10.6.
  Só nome e turma, só alunos que o perfil pode ver (§16.2, §16.3).
- **Topo do conteúdo:** breadcrumbs à esquerda; à direita, Notificações em
  pílula `--surface-raised`, alvo `--target-min`: sino `--ic-md` e o texto
  "2 não lidas" em `--fs-small` 500 `--navy-700`, e `aria-label`
  "Notificações, 2 não lidas", que contém o texto visível. Sem não lida, só
  o sino, com `aria-label` "Notificações".
