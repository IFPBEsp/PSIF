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

Barra superior de toda tela interna, sobre `--surface-base`, sem sombra,
com padding `--sp-2` em cima e `--sp-6` embaixo, logo abaixo do topo do shell (§5.1):

- Esquerda: voltar (←) `--ic-sm` em alvo `--target-min`, cor `--ink-900`.
- Centro: título da tela, `--fs-h1`, peso 600, `--navy-700`.
- Direita: vazio, uma ação de ícone, ou o ☰ nas telas-raiz (§7.2).

No web, o cabeçalho (§7.13) fica acima da barra superior.

O Início é a exceção: saudação à esquerda com o primeiro nome ("Olá, Ana!" em
`--fs-h1` `--ink-900`) e, embaixo, a data de hoje ("Segunda-feira, 15 de
junho" em `--fs-small` `--ink-700`), sem exclamação (§19.4)
e ☰ à direita (§7.2). Padding `--sp-2` `--page-pad` `--sp-6`: a saudação alinha com
os cartões (§5.7).

No web (a partir de `--bp-md`), a barra superior alinha com a coluna de
conteúdo: ← (só em tela abaixo de outra, como o perfil) e o título **à
esquerda**; à direita, a ação primária da tela, com largura automática: no
web ela sobe do rodapé para cá (§5.6). A barra lateral já diz onde se está, e
um título centralizado numa área larga fica solto.

### 7.4 Voltar

Sempre o mesmo ícone (←), sempre no mesmo lugar, sempre volta um nível. Em
formulário com conteúdo digitado, voltar pergunta antes de descartar
(§15.3).

### 7.5 Menu de seções do aluno

No perfil (§13.2), cartão branco com as seções do aluno, uma por linha,
separadas por `--ink-200`: Dados do aluno · Histórico de atendimentos ·
Relatórios · Documentos · Observações · Evolução. Cada linha leva à tela da
seção; acrescente chevron (›) para deixar isso visível: no protótipo ele
falta.

### 7.6 Filtros de lista

Linha de filtros sob a busca: cartões brancos pequenos, `--radius-md`,
`--fs-small` `--ink-700`, `--chip-pad`, altura mínima `--target-min`. Filtro
ativo: fundo
`--navy-700`, texto branco. Detalhe em §11.4.

### 7.7 Busca

Campo branco de largura total no topo da lista (no web, há também a busca
global do cabeçalho, §7.13), lupa à esquerda (`.psif-campo` com
`.psif-campo__entrada`), espera ~300ms depois da digitação antes de filtrar,
placeholder
"Pesquisar aluno" / "Pesquisar documento". Tem rótulo acessível mesmo sem
rótulo visível (é o único campo em que isso vale: a lupa e a posição dizem o
que ele é).

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
   peso 600 `--navy-700`, com `--sp-3` de vão.
2. Destinos principais: Início · Atendimentos · Alunos · Relatórios.
3. Linha `--ink-200`, depois Agenda · Notificações · Meu perfil.
4. **Sair**, no pé da barra.

Recolhível no web (§7.12). Item: ícone `--ic-lg` + rótulo (`.psif-item__rotulo`) `--fs-body` peso 500, `--sp-3` de vão, padding
`--sp-3` `--sp-4`, `--radius-md`, altura mínima `--target-min`. Inativo:
ícone e rótulo `--ink-700`. Ativo: fundo `--sky-100`, ícone e rótulo
`--navy-700`, peso 600, `aria-current="page"`. Hover: fundo `--ink-100`
(§17.2).

### 7.11 Breadcrumbs

Trilha derivada da rota ou da configuração de navegação, nunca escrita à mão
em cada página (seção 15 da doc de frontend do projeto): "Alunos › José
Antonio › Relatórios". No projeto, o `Breadcrumb` do shadcn.

- **Web**: acima do título da tela, `--fs-small`. Itens anteriores em link
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
  `--target-min`) no cabeçalho (§7.13), à esquerda da busca, encostado na
  barra lateral. `aria-label` "Recolher menu" ou "Expandir menu", conforme o
  estado, e `aria-expanded`.
- **Recolhida** (`.psif-lateral--recolhida`): largura automática, padding
  `--sp-6` `--sp-3`; rótulos (`.psif-item__rotulo`) e o nome PSIF somem;
  símbolo centralizado; itens centralizados com padding `--sp-3`. Cada item
  mantém `title` e nome acessível.
- Ativo, hover e foco iguais aos de §7.10.
- A escolha é preferência do aparelho, como o tema (§26.4).
- No celular não muda: continua a gaveta de §7.9.

### 7.13 Cabeçalho com busca global (web)

Só a partir de `--bp-md`. Faixa branca de ponta a ponta no topo de toda tela
autenticada, acima da barra superior, como primeiro filho de `.psif-coluna`
(fora de `.psif-area`). Entre faixa branca, cartão flutuante e faixa fixa com
sombra, a faixa separa o cabeçalho do conteúdo sem competir com os cartões.

- **Faixa** (`.psif-cabecalho--faixa`): fundo `--surface-raised`, divisória
  1px `--ink-200` embaixo, padding `--sp-3` `--sp-8` `--sp-3` `--sp-2`,
  `--sp-6` até o conteúdo. Encosta no topo, anulando o `--sp-4` do shell.
- **Ordem**, da esquerda para a direita: ☰ recolher menu (§7.12) · busca ·
  Notificações · Meu perfil.
- **Busca:** `.psif-campo--borda` (campo sobre branco, §8.3) com lupa à
  esquerda, placeholder "Pesquisar aluno", `aria-label` igual, dentro de
  `role="search"` só no `.psif-cabecalho__busca`: Notificações e Meu perfil
  ficam fora do landmark de busca. Largura flexível até `--w-form`. A consulta passa pelo BFF
  e espera a digitação parar (debounce). No projeto, `Command` do shadcn.
- **Resultados:** ao digitar, cartão branco logo abaixo do campo (`--sh-md`,
  `--z-raised`) com linhas de aluno (avatar `--target-min`, nome, turma).
  Tocar abre o perfil. Enter leva a Meus alunos com a busca aplicada; Esc
  limpa.
- **Sem resultado:** estado vazio de §10.6 ("Nenhum aluno encontrado para
  "Mar".").
- **Direita:** botões de ícone Notificações e Meu perfil (avatar com
  iniciais, `--sp-8`, `.psif-avatar--mini`), alvo `--target-min`.
- **Sigilo:** resultado mostra só nome e turma, nunca dado clínico (§16.3).
- **Perfil:** a busca só devolve os alunos que o perfil pode ver (§16.2).
- No celular não aparece: a busca fica nas telas de lista (§7.7).

O painel de resultados é exceção a §9.6, que pede sobreposição como folha:
vale só no web, onde o alvo de toque não é problema (§28.2).

