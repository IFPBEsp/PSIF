# PRD da tela de Agenda

| Campo | Valor |
| --- | --- |
| Identificador | T13 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T12 Planejamento semanal](prd-t12-planejamento-semanal.md), [T14 Evento](prd-t14-evento.md), [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md), [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 2. Itens e filtros de atividade adaptada e de planejamento semanal só aparecem na fase 3 (ver 6.5). |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que cada perfil veja os compromissos que lhe dizem respeito e use a agenda como ponto de partida para marcar eventos ou pedir agendamentos, para que todo pedido de reunião passe pela agenda.

## 2. Escopo

### O que entra no escopo

- Ver os compromissos nas visões mês, semana e dia, com navegação para anterior, próximo e hoje.
- Ver, para cada perfil, só o que ele pode ver.
- Filtrar por tipo, aluno, situação, "Somente meus" e "Mostrar planejamento".
- Clicar em um horário vazio para abrir "Novo evento" ou "Pedir agendamento".
- Clicar em um item para abrir o evento, a atividade adaptada ou a semana do planejamento.
- Usar o botão "Novo" para começar um evento, uma atividade adaptada ou um pedido de agendamento.
- Mostrar a mesma agenda, filtrada pelo aluno, na aba "Agenda do aluno" do perfil ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)).

### O que não entra no escopo

- Criar, editar, remarcar, cancelar um evento e registrar resposta ou presença: ficam em [T14 Evento](prd-t14-evento.md).
- Pedir, analisar e acompanhar pedidos de agendamento: ficam em [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md).
- Registrar e editar atividades adaptadas: ficam em [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md).
- Montar e confirmar o planejamento semanal: fica em [T12 Planejamento semanal](prd-t12-planejamento-semanal.md).
- Notificações próprias da agenda: a agenda não gera notificação. As notificações dos eventos e dos pedidos estão em T14 e T15.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê a agenda conforme RN-06. Filtra por aluno e por "Somente meus". Abre "Novo evento" pelo horário vazio ou pelo botão "Novo". Não pede agendamento. |
| Professor | Vê a agenda conforme RN-07. Filtra por aluno. Abre "Novo evento" e registra atividade adaptada pelo botão "Novo". Não vê o planejamento semanal. |
| Aluno | Vê a agenda conforme RN-08. Abre "Pedir agendamento" pelo horário vazio ou pelo botão "Novo". Não cria evento. |
| Responsável | Vê a agenda conforme RN-09, do aluno escolhido. Abre "Pedir agendamento" pelo horário vazio ou pelo botão "Novo". Não cria evento. |

**Contexto:** o usuário chega aqui para saber o que está marcado, para ver o dia de um aluno ou para marcar um novo compromisso.

**Origem da jornada:** Início → menu "Agenda" (todos os perfis). Também pela aba "Agenda do aluno" no perfil do aluno. O responsável com mais de um aluno vinculado escolhe o aluno no Início e usa "Trocar aluno" no cabeçalho ([T02 Início](prd-t02-inicio.md)).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Visões | Mês (padrão), semana e dia. |
| Navegação | Anterior, próximo e hoje, em qualquer visão. |
| Item de evento | Horário, título, tipo (mostrado por cor) e situação (Agendado, Realizado ou Cancelado). |
| Item de pedido pendente | Para aluno e responsável, o pedido pendente do aluno aparece na agenda marcado como "Pendente". |
| Item de atividade adaptada | Aparece no dia, sem horário. Fase 3. |
| Item do planejamento semanal | Aparece com aparência própria, mais discreta que a dos eventos, e com a cor da prioridade. Fase 3. |
| Participantes | Os nomes de participantes que aparecem nos itens e nos detalhes seguem RG-31. |
| Filtros ativos | Ficam visíveis e podem ser limpos de uma vez (RG-21). |
| Botão "Novo" | Mostra as opções de cada perfil (RN-13). |
| Aluno escolhido | Para o responsável, o cabeçalho mostra o aluno escolhido, com a opção "Trocar aluno". |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

Não se aplica. A tela não tem formulário. "Novo evento" e "Pedir agendamento" abrem em [T14 Evento](prd-t14-evento.md) e [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md).

### 5.2 Filtros

| Filtro | Opções | Valor padrão | Perfis |
| --- | --- | --- | --- |
| Tipo | Reunião, Atendimento, Avaliação, Atividade adaptada, Outro | Todos | Todos |
| Aluno | Alunos visíveis ao usuário | Todos | Psicopedagoga, Professor |
| Situação | Agendado, Realizado, Cancelado | Agendado e Realizado | Todos |
| Somente meus | Sim ou não | Não | Psicopedagoga |
| Mostrar planejamento | Sim ou não | Sim | Aluno, Responsável e Psicopedagoga com um aluno filtrado |

A opção "Atividade adaptada" do filtro "Tipo" e o filtro "Mostrar planejamento" só aparecem na fase 3 (ver 6.5).

### 5.3 Ordenação e paginação

- Ordenação padrão: Não se aplica. Os itens aparecem no calendário, no dia e no horário a que pertencem.
- Outras ordenações: Não se aplica.
- Paginação: Não se aplica. A agenda é um calendário, não uma lista.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário abre "Agenda" no menu.
2. O sistema mostra a visão mês com os itens que o perfil pode ver (RN-06 a RN-09), com os filtros padrão (5.2).
3. O usuário muda a visão, navega com anterior, próximo e hoje, e aplica filtros.
4. O usuário clica em um item. O sistema abre o evento, a atividade adaptada ou a semana do planejamento (RN-12).
5. Ou o usuário clica em um horário vazio. Psicopedagoga e professor abrem "Novo evento" com a data e a hora preenchidas. Aluno e responsável abrem "Pedir agendamento" com a data e a hora sugeridas (RN-11).

### 6.2 Fluxos alternativos

- Filtros que não deixam nenhum item: o sistema mostra a mensagem de agenda vazia por causa dos filtros e a opção de limpar os filtros (RG-22).
- Agenda sem nenhum item no período: o sistema mostra a mensagem de agenda vazia e a ação principal do perfil (RN-13).
- Item que o usuário deixou de poder ver: o sistema abre "Não encontrado" (RG-13).
- Responsável que troca de aluno no cabeçalho: a agenda passa a mostrar o aluno escolhido (RN-09).
- Clique em horário passado ou em dia vazio da visão mês: ver 7.2.

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Mudar a visão (mês, semana, dia) | Todos | Mostra o mesmo período na visão escolhida. |
| Ir para anterior, próximo ou hoje | Todos | Mostra o período anterior, o seguinte ou o atual. |
| Aplicar e limpar filtros | Todos, conforme 5.2 | Atualiza os itens. Os filtros se mantêm ao voltar para a agenda, e um link copiado abre com os mesmos filtros (RG-21). |
| Clicar em um item | Todos | Abre o evento ([T14 Evento](prd-t14-evento.md)), a atividade adaptada ([T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md)) ou a semana do planejamento ([T12 Planejamento semanal](prd-t12-planejamento-semanal.md)). |
| Clicar em um horário vazio | Todos | Psicopedagoga e Professor: abre "Novo evento" com a data e a hora preenchidas. Aluno e Responsável: abre "Pedir agendamento" com a data e a hora sugeridas. |
| Botão "Novo": Evento | Psicopedagoga, Professor | Abre "Novo evento". |
| Botão "Novo": Atividade adaptada | Professor | Abre o registro de atividade adaptada. Fase 3. |
| Botão "Novo": Pedir agendamento | Aluno, Responsável | Abre "Pedir agendamento". |
| Trocar aluno | Responsável com mais de um aluno | Troca o aluno cuja agenda aparece, no cabeçalho ([T02 Início](prd-t02-inicio.md)). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra a mensagem de agenda vazia e a ação principal do perfil: "Novo evento" para Psicopedagoga e Professor, "Pedir agendamento" para Aluno e Responsável (RG-22). |
| Vazio, por causa dos filtros | Mostra a mensagem de nenhum item com os filtros escolhidos e a opção de limpar os filtros (RG-22). |
| Sem permissão | Todos os perfis usam esta tela. Evento que o usuário não pode ver abre "Não encontrado" e RG-13 vale ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |
| Erro | "Sem conexão" e "Erro inesperado" aparecem como em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |

### 6.5 Entrega por fase

| Fase | O que aparece na agenda |
| --- | --- |
| 2 | Visões, navegação, itens de evento e de pedido pendente. Filtros "Tipo" (sem "Atividade adaptada"), "Aluno", "Situação" e "Somente meus". Clique em horário vazio e em item de evento. Botão "Novo" com Evento e Pedir agendamento. Aba "Agenda do aluno" no perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). |
| 3 | Itens de atividade adaptada e do planejamento semanal. Opção "Atividade adaptada" no filtro "Tipo". Filtro "Mostrar planejamento". Clique em atividade adaptada e em semana do planejamento. Opção "Atividade adaptada" no botão "Novo". |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A agenda tem as visões mês (padrão), semana e dia, com navegação para anterior, próximo e hoje. |
| RN-02 | Cada item de evento mostra horário, título, tipo (por cor) e situação. As situações do evento são as da seção 6 do índice. |
| RN-03 | Para aluno e responsável, os pedidos pendentes do aluno aparecem na agenda marcados como "Pendente". |
| RN-04 | As atividades adaptadas aparecem no dia, sem horário. Fase 3. |
| RN-05 | As atividades do planejamento semanal aparecem com aparência própria, mais discreta que a dos eventos, e com a cor da prioridade. Aluno e responsável só veem planejamentos confirmados ([T12 Planejamento semanal](prd-t12-planejamento-semanal.md)). Fase 3. |
| RN-06 | Psicopedagoga: vê todos os eventos. O planejamento semanal aparece só quando ela filtra um aluno. Vê também as atividades adaptadas de todos os alunos (T16 define que ela vê todas). |
| RN-07 | Professor: vê os eventos em que participa, mais as avaliações e as atividades adaptadas dos alunos das suas turmas. Não vê os atendimentos dos quais não participa nem o planejamento semanal. |
| RN-08 | Aluno: vê os eventos em que participa, o próprio planejamento semanal confirmado e as próprias atividades adaptadas. |
| RN-09 | Responsável: vê, para o aluno escolhido, os eventos em que o aluno participa, o planejamento confirmado e as atividades adaptadas. Também vê os eventos em que ele próprio participa. |
| RN-10 | Cada filtro aparece só para os perfis indicados em 5.2. O filtro "Situação" começa com Agendado e Realizado. |
| RN-11 | Clicar em um horário vazio abre "Novo evento" com a data e a hora preenchidas (Psicopedagoga e Professor) ou "Pedir agendamento" com a data e a hora sugeridas (Aluno e Responsável). |
| RN-12 | Clicar em um item abre o evento, a atividade adaptada ou a semana do planejamento. |
| RN-13 | O botão "Novo" oferece: Evento (Psicopedagoga e Professor), Atividade adaptada (Professor) e Pedir agendamento (Aluno e Responsável). |
| RN-14 | A aba "Agenda do aluno" do perfil mostra esta agenda filtrada pelo aluno do perfil. |
| RN-15 | A agenda não gera notificação própria. As notificações dos eventos e dos pedidos estão em T14 e T15. |
| RN-16 | Segue RG-08, RG-09, RG-13, RG-17, RG-21, RG-22, RG-26 e RG-31. O responsável só vê a agenda de aluno a que tem acesso (RG-17). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Cores de cada tipo | Cada tipo tem uma cor fixa. O tipo também aparece escrito no item, para não depender só da cor. |
| Clique em dia vazio na visão mês | Abre a visão do dia clicado, para a pessoa escolher a hora. |
| Clique em horário passado | Não abre "Novo evento" nem "Pedir agendamento". A tela mostra um aviso pedindo para escolher um horário futuro. |
| Horário sugerido e as 24 horas do pedido | Se o horário clicado estiver a menos de 24 horas, "Pedir agendamento" abre com a data e a hora do clique e marca o horário como inválido, pedindo outro (regra do pedido em T15). |
| Avaliações de alunos das suas turmas em que o professor não participa | O professor vê o evento com todos os detalhes, porque a avaliação existe para orientar as adaptações. Os participantes seguem RG-31. |
| Eventos cancelados | Aparecem com o título riscado e a situação "Cancelado", quando o filtro "Situação" inclui Cancelado. |
| Eventos de que o responsável participa, de outro aluno vinculado | Aparecem na agenda de qualquer aluno escolhido, porque são compromissos do próprio responsável. Alunos que ele não vê aparecem só como quantidade (RG-31). |
| Significado de "Somente meus" | Mostra só os eventos que a psicopedagoga criou ou em que ela participa. |
| Clique em pedido pendente | Abre o detalhe do pedido em T15. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

Não se aplica. A agenda não gera notificação própria (RN-15). As notificações dos eventos estão em [T14 Evento](prd-t14-evento.md) e as dos pedidos estão em [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md).

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Agenda sem nenhum item no período | Aviso | Nenhum item na agenda neste período. (proposta) |
| Nenhum item com os filtros escolhidos | Aviso | Nenhum item encontrado com estes filtros. Limpe os filtros para ver todos os itens. (proposta) |
| Clique em horário passado | Aviso | Escolha um horário futuro. (proposta) |
| Evento que o usuário não pode ver | Erro | Não encontramos o que você procurou. |
| Falha de conexão | Erro | Sem conexão com a internet. O que você digitou não foi perdido. |
| Falha inesperada | Erro | Algo deu errado. Tente de novo em alguns minutos. |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Ver a agenda | Sim, todos os eventos | Sim, conforme RN-07 | Próprio | Próprio, do aluno escolhido |
| Filtrar por "Aluno" | Sim | Sim, só alunos das suas turmas | Não | Não |
| Usar "Somente meus" | Sim | Não | Não | Não |
| Usar "Mostrar planejamento" (fase 3) | Só com um aluno filtrado | Não | Sim | Sim |
| Abrir "Novo evento" (horário vazio ou botão "Novo") | Sim | Sim | Não | Não |
| Abrir "Pedir agendamento" (horário vazio ou botão "Novo") | Não | Não | Sim | Sim |
| Abrir o registro de atividade adaptada pelo botão "Novo" (fase 3) | Não | Sim, só alunos das suas turmas | Não | Não |

## 11. Critérios de aceite

- [ ] Dado um usuário de qualquer perfil, quando abre "Agenda" no menu, então a tela mostra a visão mês com os filtros padrão.
- [ ] Dado a agenda aberta, quando o usuário escolhe semana ou dia e usa anterior, próximo e hoje, então o sistema mostra o período correspondente.
- [ ] Dado um evento na agenda, quando o item é exibido, então mostra horário, título, tipo por cor e situação.
- [ ] Dado a psicopedagoga, quando abre a agenda sem filtrar aluno, então vê todos os eventos e não vê o planejamento semanal.
- [ ] Dado a psicopedagoga, quando filtra um aluno e "Mostrar planejamento" está em Sim, então vê também o planejamento semanal confirmado desse aluno na fase 3.
- [ ] Dado a psicopedagoga, quando marca "Somente meus" como Sim, então o filtro é aplicado e fica visível.
- [ ] Dado um professor, quando abre a agenda, então vê os eventos em que participa e as avaliações e atividades adaptadas dos alunos das suas turmas.
- [ ] Dado um professor, quando há um atendimento do qual ele não participa, então o atendimento não aparece na agenda dele.
- [ ] Dado um professor, quando abre a agenda, então não vê o planejamento semanal nem o filtro "Mostrar planejamento".
- [ ] Dado um professor, quando abre o filtro "Aluno", então só encontra alunos ativos das suas turmas (RG-08).
- [ ] Dado um aluno, quando abre a agenda, então vê os eventos em que participa, o próprio planejamento confirmado e as próprias atividades adaptadas, e não vê os filtros "Aluno" nem "Somente meus".
- [ ] Dado um aluno com pedido pendente, quando abre a agenda, então o pedido aparece marcado como "Pendente".
- [ ] Dado um responsável, quando abre a agenda, então vê os eventos do aluno escolhido, o planejamento confirmado, as atividades adaptadas e os eventos em que ele próprio participa.
- [ ] Dado um responsável com mais de um aluno, quando usa "Trocar aluno" no cabeçalho, então a agenda mostra o aluno escolhido.
- [ ] Dado um responsável com pedido pendente do aluno escolhido, quando abre a agenda, então o pedido aparece marcado como "Pendente".
- [ ] Dado um responsável de aluno com 18 anos ou mais sem autorização do aluno, quando tenta ver a agenda desse aluno, então não vê nenhum dado dele (RG-17).
- [ ] Dado o filtro "Situação" no padrão, quando a agenda abre, então mostra eventos Agendado e Realizado e não mostra Cancelado.
- [ ] Dado o filtro "Situação" com Cancelado marcado, quando a agenda atualiza, então os eventos cancelados aparecem.
- [ ] Dado filtros ativos, quando o usuário sai da agenda e volta, então os filtros continuam ativos (RG-21).
- [ ] Dado filtros ativos, quando o usuário copia o link da agenda e o abre, então a agenda abre com os mesmos filtros (RG-21).
- [ ] Dado filtros que não deixam nenhum item, quando a agenda atualiza, então mostra a mensagem de nenhum item e a opção de limpar os filtros (RG-22).
- [ ] Dado uma agenda sem nenhum item, quando a tela abre, então mostra a mensagem de agenda vazia e a ação principal do perfil.
- [ ] Dado a psicopedagoga ou o professor, quando clica em um horário vazio, então abre "Novo evento" com a data e a hora preenchidas.
- [ ] Dado um aluno ou um responsável, quando clica em um horário vazio, então abre "Pedir agendamento" com a data e a hora sugeridas.
- [ ] Dado um item de evento, quando o usuário clica nele, então abre o evento.
- [ ] Dado uma atividade adaptada na agenda na fase 3, quando o usuário clica nela, então abre a atividade adaptada.
- [ ] Dado uma atividade do planejamento semanal na fase 3, quando o usuário clica nela, então abre a semana do planejamento.
- [ ] Dado a atividade adaptada na agenda, quando é exibida, então aparece no dia, sem horário.
- [ ] Dado uma atividade do planejamento, quando é exibida, então aparece com aparência mais discreta que a dos eventos e com a cor da prioridade.
- [ ] Dado a fase 2, quando a agenda abre, então não mostra a opção "Atividade adaptada" no filtro "Tipo", o filtro "Mostrar planejamento" nem itens de atividade adaptada ou do planejamento.
- [ ] Dado a psicopedagoga ou o professor, quando abre o botão "Novo", então vê "Evento". O professor também vê "Atividade adaptada" na fase 3.
- [ ] Dado um aluno ou um responsável, quando abre o botão "Novo", então vê "Pedir agendamento" e não vê "Evento".
- [ ] Dado um evento com participantes que o usuário não pode ver, quando o evento aparece na agenda, então os nomes seguem RG-31 e os outros participantes aparecem só como quantidade.
- [ ] Dado a aba "Agenda do aluno" no perfil, quando o usuário a abre, então vê a agenda filtrada pelo aluno do perfil.
- [ ] Dado um evento que o usuário não pode ver, quando tenta abri-lo por um link, então vê "Não encontrado" (RG-13).
- [ ] Dado uma falha de conexão ou uma falha inesperada, quando a agenda é carregada, então o sistema mostra o estado "Sem conexão" ou "Erro inesperado".
- [ ] Dado a agenda em um celular ou usada só com o teclado, quando o usuário a percorre, então consegue usar todas as ações (RG-26).
- [ ] Dado qualquer acesso à agenda, quando o usuário abre, filtra ou navega, então nenhuma notificação é gerada.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
