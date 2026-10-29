## 7. NAVEGAÇÃO

### 7.1 Navegação principal

Uma navegação só, em dois formatos (seção 15 de
`docs/frontend/architecture-and-stack.md`, no projeto):

- **Web** (a partir de `--bp-md`): barra lateral fixa (§7.10).
- **Celular**: a mesma barra lateral, como gaveta que abre pelo ☰ (§7.9).

Não há barra inferior. Os destinos, nesta ordem: **Início · Atendimentos ·
Alunos · Relatórios**, depois **Agenda · Notificações · Meu perfil**,
e **Sair** no pé. "Termo", que o protótipo põe no menu e nos atalhos, fica
escondido até alguém decidir o que ele é (§28.4), porque hoje ele não leva a
tela nenhuma. A lista sai de uma configuração central de navegação, e cada
item aparece só para o perfil com permissão para ele (§16.2).

### 7.2 Menu (☰)

No celular, o ☰ fica à direita da barra superior das telas-raiz (Início e
listas) e abre a gaveta (§7.9). `aria-label="Abrir menu"`,
`aria-expanded` acompanhando a gaveta. Tela de tarefa e de detalhe não têm ☰:
ela tem ← (§7.4). No web o ☰ some, porque a barra lateral já está aberta.

### 7.3 Barra superior

**Celular.** A barra superior só tem ações, sobre `--surface-base`, sem
sombra, com `--sp-2` em cima:

- Esquerda: voltar (←), botão de ícone em `--radius-pill`, `--ic-sm` em alvo
  `--target-min`, cor `--ink-900`, com `aria-label` que diz o destino
  ("Voltar para Alunos").
- Direita: busca (§7.7), ⋯ ("Mais ações do aluno") ou o ☰ das telas-raiz
  (§7.2), também em `--radius-pill` e com `aria-label`.

O título não fica na barra: vem logo abaixo, à esquerda, em `--fs-display`
peso 600 `--navy-700`, seguido de uma linha de contexto em `--fs-body`
`--ink-700` ("José Antonio · 4 arquivos"). Regra completa em §4.3. Folha
modal e tela de autenticação mantêm o título centralizado.

O Início é a exceção: saudação à esquerda com o primeiro nome ("Olá, Ana!" em
`--fs-h1` `--ink-900`) e, embaixo, a data de hoje ("Segunda-feira, 15 de
junho" em `--fs-small` `--ink-700`), sem exclamação (§19.4), e ☰ à direita
(§7.2). Padding `--sp-2` `--page-pad` `--sp-6`: a saudação alinha com os
cartões (§5.7).

**Web** (a partir de `--bp-md`). No topo do conteúdo ficam os breadcrumbs à
esquerda e Notificações à direita (§7.13). Abaixo, o título em `--fs-display`
à esquerda, com ← antes dele só em tela abaixo de outra, como o perfil; à
direita do título, a ação primária da tela (§5.6).

### 7.4 Voltar

Sempre o mesmo ícone (←), sempre no mesmo lugar, sempre volta um nível. Em
formulário com conteúdo digitado, voltar pergunta antes de descartar
(§15.3).

### 7.5 Seções do aluno

**Celular**: grade de duas colunas de cartões (`--radius-xl`, altura mínima
84px, `--sp-3` de vão), sob o título de grupo "Prontuário" (§4.3). Cada
cartão: nome da seção em `--fs-body` peso 600 `--navy-700` e, embaixo, um
resumo em `--fs-caption` `--ink-700` vindo do backend ("12 registros", "4
arquivos", "Atualizada 22/10"); sem resumo, só o nome. Seções: Dados do aluno
· Atendimentos · Relatórios · Documentos · Observações · Evolução. A grade
fica sem ícone até Observações e Evolução terem o seu (§28.4).

**Web**: abas sob o cabeçalho do aluno (§9.10): Visão geral · Atendimentos ·
Documentos · Relatórios. Aba ativa em `--navy-700` peso 600, com sublinhado
de 3px e contador em pílula `--sky-100`; inativas em `--ink-700` peso 500.
Cada aba é um link (`aria-current="page"` na ativa), com alvo de
`--target-min`.

O resumo da seção Documentos mostra contagem ("2 sigilosos"), nunca nomes
(§16.3).

### 7.6 Filtros de lista

Linha de filtros sob a busca. Pílula (`--radius-pill`), altura
`--target-min`, `--chip-pad`, `--fs-small`. Inativo: transparente, borda 1px
`--line-on-sky`, texto `--navy-700` peso 500. Ativo: fundo `--navy-700`,
texto branco, peso 600. No celular a linha rola na horizontal, sem quebrar.

Dois tipos:

- **Escolha direta** (lista de documentos: Todos · Laudos · Relatórios ·
  Declarações): um ativo por vez, e cada pílula anuncia o estado. Botão solto
  leva `aria-pressed`; o `ToggleGroup type="single"` do shadcn já anuncia
  com `role="radio"` e `aria-checked`.
- **Filtro com valor** (Turma · Série · Período, em Meus alunos): abre folha
  de seleção (§11.4), com `aria-haspopup="dialog"`. Com valor escolhido, fica
  no estilo ativo, mostra o valor e um × para limpar.

O estado nunca está só na cor: o ativo muda fundo, peso e, no filtro com
valor, o próprio texto (§20.2).

### 7.7 Busca

Campo branco de largura total no topo da lista (no web, há também a busca
global da barra lateral, §7.13), lupa à esquerda, espera ~300ms depois da digitação antes de filtrar,
placeholder
"Pesquisar aluno" / "Pesquisar documento". Tem rótulo acessível mesmo sem
rótulo visível (é o único campo em que isso vale: a lupa e a posição dizem o
que ele é).

No celular, em tela com título grande (§4.3), a busca começa como botão de
lupa na barra superior e abre o campo no lugar do título. No web, a busca pode
ter fundo `--ink-100` sem borda: a lupa e a posição dizem o que ela é. Campo
de formulário continua com borda (§8.3): sem ela, o contorno fica abaixo de
3:1 (WCAG 1.4.11).

### 7.8 Ações rápidas

Cartão "Ações rápidas" no Início: até quatro atalhos por linha (quebram
linha em vez de encolher o quadrado), cada um um
quadrado `--sky-300` de 48px com ícone `--navy-700` `--ic-lg` e rótulo
`--fs-caption` `--ink-700` embaixo. Agenda · Meu perfil · Notificações. No protótipo os quadrados estão vazios: o
ícone é obrigatório
(§18).

### 7.9 Gaveta de navegação (celular)

Abaixo de `--bp-md`, a barra lateral (§7.10) vira gaveta: entra pela
esquerda, sobre o véu `--overlay` (`--z-overlay`), com `--z-modal`, largura
`--w-sidebar` e `--sh-md`. Mesmo conteúdo e mesma ordem do web. No projeto é o
`Sidebar` do shadcn, que já vira `Sheet` no celular.

- Fecha ao tocar num destino, no véu ou em Esc, e o foco volta para o ☰.
- Abre com o foco no item ativo; o foco fica preso dentro dela enquanto
  aberta.
- Movimento de entrada em `--dur-normal` (§17.3); com movimento reduzido, aparece sem
  deslizar (§17.5).
- Sair continua a dois toques: ☰ e Sair (§16.3).

### 7.10 Barra lateral (web)

A partir de `--bp-md`, fixa e sempre visível; no celular, vira a gaveta de
§7.9. Fixa à
esquerda, largura `--w-sidebar`, altura da janela, fundo `--surface-raised`
(é cartão, não marinho, §2.2), sem borda e sem sombra: o branco a separa do
céu. `<nav aria-label="Principal">`.

De cima para baixo, com `--sp-6` de padding:

1. Símbolo do PSIF (§1.1) em `--ic-xl` e, ao lado, **PSIF** em `--fs-h1`
   peso 600 `--navy-700`, com `--sp-3` de vão; à direita, o botão de
   recolher (§7.12).
2. Busca global "Pesquisar aluno" (§7.13).
3. Destinos principais: Início · Atendimentos · Alunos · Relatórios.
4. Linha `--ink-200`, depois Agenda · Notificações · Meu perfil.
5. No pé, um cartão `--ink-100` (`--radius-xl`) com as iniciais, o nome, o
   papel ("Psicopedagoga") e o botão "Sair".

Recolhível no web (§7.12). Item: ícone `--ic-lg` + rótulo `--fs-body` peso
500, `--sp-3` de vão, padding `--sp-3` `--sp-4`, `--radius-lg`, altura mínima
`--target-min`. Inativo: ícone e rótulo `--ink-700`. Ativo: fundo
`--sky-100`, ícone e rótulo `--navy-700`, peso 600, `aria-current="page"`.
Hover: fundo `--ink-100` (§17.2).

### 7.11 Breadcrumbs

Trilha derivada da rota ou da configuração de navegação, nunca escrita à mão
em cada página (seção 15 da doc de frontend do projeto): "Alunos › José
Antonio › Relatórios". No projeto, o `Breadcrumb` do shadcn.

- **Web**: no topo do conteúdo, à esquerda, na linha do botão de
  Notificações (§7.13), `--fs-small`. Itens anteriores em link
  `--ink-700`; o atual em `--ink-900`, sem link, com `aria-current="page"`.
  Separador › em `--ink-700`, `aria-hidden`. `<nav aria-label="Trilha">`.
- **Celular**: não aparece. O ← (§7.4) volta um nível e o título diz onde se
  está; uma trilha de três níveis não cabe em 390px sem quebrar.
- Só a partir do segundo nível. No Início e nas telas-raiz, a barra lateral já
  diz onde se está.
- Nome de aluno na trilha segue o sigilo: nome, nunca dado clínico (§16.3).

### 7.12 Barra lateral recolhível (web)

No web, a barra lateral (§7.10) recolhe para só ícones. No projeto, é o
`Sidebar` do shadcn com `collapsible="icon"`, e o botão é o `SidebarTrigger`.

- **Controle:** botão de ícone ☰ (`psif-menu`, `--ic-lg`, alvo
  `--target-min`, `--radius-pill`) no topo da barra lateral, à direita da
  marca. Recolhida, a barra mostra só o símbolo e o botão logo abaixo dele.
  `aria-label` "Recolher menu" ou "Expandir menu", conforme o estado, e
  `aria-expanded`.
- **Recolhida**: largura automática, padding
  `--sp-6` `--sp-3`; rótulos e o nome PSIF somem;
  símbolo centralizado; itens centralizados com padding `--sp-3`; a busca vira
  botão de lupa e o cartão do pé vira só as iniciais. Cada item mantém `title`
  e nome acessível.
- Ativo, hover e foco iguais aos de §7.10.
- A escolha é preferência do aparelho, como o tema (§26.4).
- No celular não muda: continua a gaveta de §7.9.

### 7.13 Busca global e topo do conteúdo (web)

Só a partir de `--bp-md`. Não há faixa de cabeçalho.

- **Busca global** fica na barra lateral, logo abaixo da marca (§7.10):
  fundo `--ink-100` sem borda (§7.7), lupa à esquerda, placeholder
  "Pesquisar aluno", `aria-label` igual, dentro de `role="search"`. A
  consulta passa pelo BFF e espera a digitação parar (debounce). No projeto,
  `Command` do shadcn num `Popover`.
- **Resultados:** ao digitar, cartão branco ancorado no campo (`--sh-md`,
  `--z-raised`) com linhas de aluno (avatar `--target-min`, nome, turma).
  Tocar abre o perfil. Enter leva a Meus alunos com a busca aplicada; Esc
  limpa. Sem resultado: estado vazio de §10.6 ("Nenhum aluno encontrado para
  "Mar".").
- **Topo do conteúdo:** os breadcrumbs à esquerda (§7.11) e, à direita, o
  botão de Notificações em pílula branca (`--surface-raised`,
  `--radius-pill`, alvo `--target-min`), com `aria-label` que diz quantas não
  lidas há ("Notificações, 2 não lidas").
- **Usuário:** iniciais, nome, papel e "Sair" no pé da barra lateral (§7.10).
- **Sigilo:** resultado mostra só nome e turma, nunca dado clínico (§16.3).
- **Perfil:** a busca só devolve os alunos que o perfil pode ver (§16.2).
- No celular não aparece: a busca fica nas telas de lista (§7.7).

O painel de resultados é exceção a §9.6, que pede sobreposição como folha:
vale só no web, onde o alvo de toque não é problema (§28.2).
