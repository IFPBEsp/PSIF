# PRD da tela de Notificações

| Campo | Valor |
| --- | --- |
| Identificador | T03 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md), [T14 Evento](prd-t14-evento.md), [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md), [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md), [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md), [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md), [T12 Planejamento semanal](prd-t12-planejamento-semanal.md), [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) |
| Fase de entrega | 1 (cada tipo de notificação aparece quando a tela de origem for entregue) |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que cada usuário veja o que mudou e o que depende dele, para agir sem precisar procurar as mudanças nas outras telas.

## 2. Escopo

### O que entra no escopo

- Sino no topo com a quantidade de notificações não lidas.
- Painel rápido com as 10 notificações mais recentes.
- Tela completa com todas as notificações.
- Filtros por situação e por tipo.
- Abrir o item relacionado, marcar como lida e marcar todas como lidas.
- Os 18 acontecimentos que geram notificação e quem recebe cada um (seção 7 do índice).

### O que não entra no escopo

- Notificações por e-mail, SMS ou celular: as notificações ficam só dentro do sistema (seção 11 do índice).
- Criar ou alterar o item que gerou a notificação: fica na tela de origem de cada tipo (ver 6.5).
- Mensagem de item removido ou sem acesso: o texto fica em [T26 Estados do sistema](prd-t26-estados-do-sistema.md).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê as próprias notificações, como pedidos de agendamento, atividades adaptadas, observações dos professores, informações e alunos prestes a completar 18 anos. Abre o item, marca como lida e marca todas como lidas. |
| Professor | Vê as próprias notificações, como eventos em que é participante e características ou orientações atualizadas dos seus alunos. Abre o item, marca como lida e marca todas como lidas. |
| Aluno | Vê as próprias notificações, como eventos, respostas a pedidos de agendamento, atividades adaptadas, acompanhamentos visíveis e planejamento semanal. Abre o item, marca como lida e marca todas como lidas. |
| Responsável | Se tiver conta ativa, vê as próprias notificações, com os tipos que a seção 7 do índice destina ao responsável. Abre o item, marca como lida e marca todas como lidas. |

**Contexto:** o usuário vê no sino que há novidades e quer saber o que mudou, ou quer rever o que já foi avisado.

**Origem da jornada:** qualquer tela → sino no topo → painel rápido → tela completa. A tela também é o destino de "Voltar às notificações" em "Item indisponível" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Sino | Fica no topo de todas as telas. Mostra a quantidade de notificações não lidas. Acima de 99, mostra "99+". |
| Painel rápido | Lista as 10 notificações mais recentes. Ver "Conteúdo do painel rápido" em 7.2. |
| Tela completa | Lista todas as notificações do usuário, com filtros, paginação e o total de resultados (RG-19). |
| Tipo | Categoria da notificação, que vem do acontecimento que a gerou (seção 8). |
| Título | Nome do acontecimento que gerou a notificação (RN-18). |
| Texto | Uma frase com o nome do evento, do pedido ou do aluno e, quando houver, a data e a hora (RN-18). |
| Quem gerou | Quem fez a ação que originou a notificação, ou "Sistema" nas notificações automáticas (RN-19). |
| Data e hora | Quando a notificação foi gerada, no formato dd/mm/aaaa hh:mm (RG-18). |
| Situação | "Não lida" ou "Lida" (seção 6 do índice). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

Não se aplica.

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Situação | Todas, Não lidas | Todas |
| Tipo | Todos os tipos, Eventos, Pedidos de agendamento, Atividades adaptadas, Observações dos professores, Informações, Acompanhamentos, Características e orientações, Planejamento semanal e Maioridade do aluno (RN-17) | Todos os tipos |

Os filtros ativos ficam visíveis, podem ser limpos de uma vez e se mantêm ao voltar para a lista (RG-21).

### 5.3 Ordenação e paginação

- Ordenação padrão: mais recentes primeiro.
- Outras ordenações: não há.
- Paginação: 20 itens por página e total de resultados na tela completa (RG-19). O painel rápido mostra as 10 mais recentes.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário vê no sino a quantidade de notificações não lidas.
2. O usuário abre o painel rápido e vê as 10 mais recentes.
3. O usuário escolhe uma notificação.
4. O sistema abre o item relacionado e muda a notificação para "Lida" (RN-12).

### 6.2 Fluxos alternativos

- Item removido ou sem acesso: ao abrir a notificação, aparece "Item indisponível" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)) (RN-13).
- Marcar como lida sem abrir o item: o usuário usa "Marcar como lida" e a notificação passa para "Lida".
- Marcar todas como lidas: as notificações não lidas passam para "Lida" (alcance em 7.2).
- Filtro sem resultado: a lista mostra a mensagem de lista vazia com a opção de limpar os filtros (RG-22).
- Notificação com mais de 90 dias: deixa de estar disponível (RN-14).
- Responsável sem conta ativa: não recebe notificações (RN-04).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Abrir o item relacionado | Todos os perfis, nas próprias notificações | Abre o item que gerou a notificação e marca a notificação como lida. Se o item não existe mais ou o usuário perdeu o acesso, abre "Item indisponível". |
| Marcar como lida | Todos os perfis, nas próprias notificações | Muda a situação para "Lida", sem abrir o item, e diminui a quantidade do sino. |
| Marcar todas como lidas | Todos os perfis, nas próprias notificações | Muda as notificações não lidas para "Lida" e atualiza a quantidade do sino (alcance em 7.2). |
| Filtrar por situação ou tipo | Todos os perfis | Mostra só as notificações que atendem ao filtro. |
| Limpar filtros | Todos os perfis | Volta para Todas e Todos os tipos (RG-21). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra a mensagem "Você não tem notificações. (proposta)". Como o usuário não cria notificações, não há ação principal (ver 7.2). |
| Vazio, por causa dos filtros | Mostra a mensagem "Nenhuma notificação encontrada com estes filtros. (proposta)" e a opção "Limpar filtros" (RG-22). |
| Sem permissão | Todos os perfis usam esta tela (matriz de permissões, seção 10 do índice), e cada um vê só as próprias notificações. Item sem acesso abre "Item indisponível". "Acesso negado" e "Não encontrado" (RG-13) não se aplicam à lista. |
| Erro | "Sem conexão" e "Erro inesperado" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |

### 6.5 Entrega por fase

A tela é entregue na fase 1. Cada tipo de notificação só aparece quando a tela de origem do acontecimento for entregue (seção 9 do índice).

| Fase | Tela de origem | Tipos de notificação que passam a aparecer |
| --- | --- | --- |
| 1 | [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md) | Características ou orientações atualizadas. |
| 1 | [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md) | Aluno com responsável com acesso completa 18 anos em 30 dias (ver 7.2). |
| 2 | [T14 Evento](prd-t14-evento.md) | Evento criado, evento alterado ou remarcado, participante retirado do evento, evento cancelado, lembrete 24 horas antes e participante recusa presença. |
| 2 | [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md) | Pedido criado, aceito ou recusado, cancelado pelo autor, cancelado automaticamente e expirado. |
| 3 | [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md) | Atividade adaptada registrada. |
| 3 | [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md) | Observação do professor registrada. |
| 3 | [T10 Acompanhamentos](prd-t10-acompanhamentos.md) | Acompanhamento visível para a família registrado ou alterado. |
| 3 | [T12 Planejamento semanal](prd-t12-planejamento-semanal.md) | Planejamento semanal confirmado ou alterado depois de confirmado. |
| 4 | [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) | Informação enviada. |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A tela segue RG-13, RG-19, RG-21 e RG-22. |
| RN-02 | As notificações aparecem só dentro do sistema, no sino e nesta tela. O sistema não envia notificação por e-mail, SMS ou celular (seção 11 do índice). |
| RN-03 | Os acontecimentos que geram notificação, e quem recebe cada um, são os da seção 7 do índice. A seção 8 desta tela os reproduz por tipo. |
| RN-04 | O responsável só recebe notificação se tiver conta ativa. |
| RN-05 | Ninguém recebe notificação da própria ação (RG-25). |
| RN-06 | Cada usuário vê só as próprias notificações. |
| RN-07 | Cada notificação mostra tipo, título, quem gerou, data e hora e situação. |
| RN-08 | O sino mostra a quantidade de notificações não lidas. Acima de 99, mostra "99+". |
| RN-09 | O painel rápido mostra as 10 notificações mais recentes. |
| RN-10 | A tela completa tem os filtros Situação (Todas ou Não lidas, padrão Todas) e Tipo. A ordenação é das mais recentes para as mais antigas. |
| RN-11 | A notificação tem a situação "Não lida" ou "Lida" (seção 6 do índice). |
| RN-12 | A notificação vira "Lida" quando o usuário abre o item relacionado ou escolhe "Marcar como lida". "Marcar todas como lidas" muda todas de uma vez. |
| RN-13 | Se o item foi removido ou o usuário perdeu o acesso a ele, a notificação abre o estado "Item indisponível" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). O sistema nunca revela que o item existe para quem não pode vê-lo (RG-13). |
| RN-14 | As notificações ficam disponíveis por 90 dias. |
| RN-15 | Cada tipo de notificação só aparece quando a tela de origem do acontecimento for entregue (seção 9 do índice e subseção 6.5). |
| RN-16 | Datas e horários seguem RG-18. |
| RN-17 | O filtro Tipo tem as opções Todos os tipos (padrão), Eventos, Pedidos de agendamento, Atividades adaptadas, Observações dos professores, Informações, Acompanhamentos, Características e orientações, Planejamento semanal e Maioridade do aluno. Cada opção agrupa os acontecimentos da seção 7 do índice que vêm da tela correspondente e só aparece quando essa tela for entregue (RN-15). |
| RN-18 | O título da notificação repete o nome do acontecimento, por exemplo "Evento criado". O texto é uma frase com o nome do evento, do pedido ou do aluno e, quando houver, a data e a hora. Nas notificações de evento e de pedido, o texto segue RG-31. |
| RN-19 | Nas notificações que o sistema gera sozinho, como o lembrete de evento, o pedido expirado, o pedido cancelado automaticamente e o aluno prestes a completar 18 anos, "Quem gerou" mostra "Sistema". |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Conteúdo do painel rápido | Cada item mostra as mesmas informações da tela completa. O painel rápido mostra as 10 mais recentes, lidas e não lidas, sem filtros, e tem a ação "Ver todas as notificações" para abrir a tela completa. |
| Sino sem não lidas | Quando não há notificações não lidas, o sino aparece sem quantidade. |
| Marcar todas como lidas | A ação vale para todas as notificações não lidas do usuário, mesmo as de outras páginas ou fora do filtro, e não pede confirmação. |
| Depois de 90 dias | A notificação some da lista, do painel e da quantidade do sino. |
| Atualização do sino | O sino atualiza a quantidade sem o usuário recarregar a tela. |
| Destino de cada tipo | Cada notificação abre a tela do item que a gerou: o evento, o pedido de agendamento, a atividade adaptada, a observação, a informação, o acompanhamento, as características e orientações, o planejamento semanal ou o perfil do aluno. |
| Item indisponível | Abrir uma notificação de item indisponível também marca a notificação como lida. |
| Lista vazia sem ação principal | A lista vazia mostra só a mensagem, sem ação principal, porque o usuário não cria notificações. |
| Abrir o aviso de retirada do evento | O aviso "Participante retirado do evento" não abre o evento, porque a pessoa não é mais participante. Abrir o aviso só o marca como lido. |
| Fase do aviso de maioridade | O aviso de aluno com responsável com acesso que completa 18 anos em 30 dias aparece desde a fase 1, com o cadastro de aluno. |

## 8. Notificações

Esta tela mostra as notificações de todos os acontecimentos abaixo (seção 7 do índice). O título e o texto de cada tipo seguem RN-18.

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Evento criado | Participantes, e quem é incluído depois numa edição | Avisa que o evento foi criado ou que a pessoa foi incluída nele. |
| Evento alterado ou remarcado | Participantes que continuam no evento | Avisa que o evento mudou ou foi remarcado. |
| Participante retirado do evento | Quem foi retirado | Avisa que a pessoa saiu do evento, com o nome, a data e a hora. |
| Evento cancelado | Participantes, com o motivo | Avisa o cancelamento e mostra o motivo. |
| Lembrete, 24 horas antes do evento | Participantes que não recusaram | Lembra o evento do dia seguinte. |
| Participante recusa presença | Quem criou o evento | Avisa que um participante recusou. |
| Pedido de agendamento criado | Psicopedagogas | Avisa que há um pedido novo. |
| Pedido de agendamento aceito ou recusado | Quem pediu, o aluno e os responsáveis do aluno | Avisa a decisão sobre o pedido. |
| Pedido de agendamento cancelado pelo autor | Psicopedagogas | Avisa que o autor cancelou o pedido. |
| Pedido de agendamento cancelado automaticamente, porque o aluno foi inativado ou o autor perdeu o acesso ao aluno | Psicopedagogas, com o motivo | Avisa que o pedido foi cancelado e mostra o motivo. |
| Pedido de agendamento expirado | Quem pediu | Avisa que o pedido expirou. |
| Atividade adaptada registrada | Psicopedagogas, o aluno e os responsáveis do aluno | Avisa que há uma atividade adaptada nova. |
| Observação do professor registrada | Psicopedagogas | Avisa que há uma observação nova. |
| Informação enviada | Psicopedagogas | Avisa que chegou uma informação. |
| Acompanhamento visível para a família registrado ou alterado | Aluno e responsáveis | Avisa que há um acompanhamento novo ou alterado. |
| Características ou orientações atualizadas | Professores do aluno | Avisa que as características ou as orientações do aluno mudaram. |
| Planejamento semanal confirmado ou alterado depois de confirmado | Aluno e responsáveis | Avisa que o planejamento semanal está confirmado ou mudou. |
| Aluno com responsável com acesso completa 18 anos em 30 dias | Psicopedagogas | Avisa que o aluno completa 18 anos em até 30 dias. |

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Item removido ou sem acesso | Aviso | Este item não está mais disponível. |
| Nenhuma notificação | Aviso | Você não tem notificações. (proposta) |
| Nenhuma notificação com os filtros | Aviso | Nenhuma notificação encontrada com estes filtros. (proposta) |
| Todas marcadas como lidas | Sucesso | Todas as notificações foram marcadas como lidas. (proposta) |
| Falha de conexão | Erro | Sem conexão com a internet. O que você digitou não foi perdido. |
| Erro do sistema | Erro | Algo deu errado. Tente de novo em alguns minutos. |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Ver o sino e o painel rápido | Sim, só as próprias | Sim, só as próprias | Sim, só as próprias | Sim, só as próprias |
| Ver a tela completa | Sim, só as próprias | Sim, só as próprias | Sim, só as próprias | Sim, só as próprias |
| Abrir o item relacionado | Sim, se ainda tem acesso ao item | Sim, se ainda tem acesso ao item | Sim, se ainda tem acesso ao item | Sim, se ainda tem acesso ao item |
| Marcar como lida | Sim, só as próprias | Sim, só as próprias | Sim, só as próprias | Sim, só as próprias |
| Marcar todas como lidas | Sim, só as próprias | Sim, só as próprias | Sim, só as próprias | Sim, só as próprias |
| Filtrar por situação e tipo | Sim | Sim | Sim | Sim |
| Receber notificações | Sim | Sim | Sim | Sim, só com conta ativa |

## 11. Critérios de aceite

- [ ] Dado um usuário com notificações não lidas, quando ele abre qualquer tela, então o sino no topo mostra a quantidade de não lidas.
- [ ] Dado um usuário com mais de 99 notificações não lidas, quando ele olha o sino, então o sino mostra "99+".
- [ ] Dado um usuário com mais de 10 notificações, quando ele abre o painel rápido, então o painel mostra as 10 mais recentes.
- [ ] Dado um usuário com notificações, quando ele abre a tela completa, então cada notificação mostra tipo, título, quem gerou, data e hora (dd/mm/aaaa hh:mm) e situação.
- [ ] Dada a tela completa aberta pela primeira vez, quando ela carrega, então o filtro de situação está em "Todas" e as notificações aparecem das mais recentes para as mais antigas.
- [ ] Dado um usuário com mais de 20 notificações, quando ele abre a tela completa, então a tela mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado o filtro de situação, quando o usuário escolhe "Não lidas", então a lista mostra só as notificações "Não lida".
- [ ] Dado um filtro ativo, quando o usuário sai da lista e volta, então o filtro continua ativo e visível, e pode ser limpo de uma vez (RG-21).
- [ ] Dada uma notificação "Não lida", quando o usuário abre o item relacionado, então o sistema abre o item, a notificação passa para "Lida" e a quantidade do sino diminui em um.
- [ ] Dada uma notificação "Não lida", quando o usuário escolhe "Marcar como lida", então a notificação passa para "Lida" sem abrir o item.
- [ ] Dado um usuário com várias notificações não lidas, quando ele escolhe "Marcar todas como lidas", então as notificações não lidas passam para "Lida" (alcance em 7.2).
- [ ] Dada uma notificação cujo item foi removido, quando o usuário a abre, então o sistema mostra "Item indisponível" com a mensagem "Este item não está mais disponível." e a ação "Voltar às notificações".
- [ ] Dada uma notificação de um item que o usuário não pode mais ver, quando ele a abre, então o sistema mostra o mesmo estado "Item indisponível", sem revelar que o item existe (RG-13).
- [ ] Dada uma notificação com mais de 90 dias, quando o usuário abre a lista, então a notificação não está mais disponível.
- [ ] Dado um usuário sem nenhuma notificação, quando ele abre a tela completa, então a tela mostra a mensagem de lista vazia (RG-22).
- [ ] Dados filtros sem resultado, quando a lista fica vazia, então a tela mostra a mensagem de lista vazia e a opção de limpar os filtros (RG-22).
- [ ] Dado um usuário que fez uma ação que gera notificação, quando o sistema gera as notificações, então ele não recebe a notificação da própria ação (RG-25).
- [ ] Dado um responsável sem conta ativa, quando ocorre um acontecimento que o envolve, então ele não recebe notificação.
- [ ] Dados dois usuários com notificações, quando um deles abre a tela, então ele vê só as próprias notificações.
- [ ] Dado um evento criado na fase 2, quando o evento é salvo, então cada participante, exceto o criador, recebe a notificação "Evento criado".
- [ ] Dado um evento cancelado, quando os participantes abrem a notificação, então ela mostra o motivo do cancelamento.
- [ ] Dado um pedido de agendamento criado, quando as psicopedagogas abrem o sino, então todas recebem a notificação do pedido.
- [ ] Dado o filtro Tipo, quando o usuário o abre, então vê "Todos os tipos" escolhido e só as opções das telas já entregues (RN-17).
- [ ] Dado o filtro Tipo em "Eventos", quando a lista carrega, então mostra só as notificações de evento criado, alterado ou remarcado, participante retirado, cancelado, lembrete e recusa de presença (RN-17).
- [ ] Dado um evento criado, quando o participante vê a notificação, então o título é "Evento criado" e o texto tem o nome do evento, a data e a hora (RN-18).
- [ ] Dado um evento com um aluno que o responsável não vê, quando o responsável lê a notificação do evento, então o texto não mostra o nome desse aluno (RN-18, RG-31).
- [ ] Dado um lembrete de evento, quando o participante vê a notificação, então "Quem gerou" mostra "Sistema" (RN-19).
- [ ] Dado um participante retirado de um evento numa edição, quando a edição é salva, então ele recebe a notificação "Participante retirado do evento", com o nome, a data e a hora do evento.
- [ ] Dado um pedido pendente de um aluno que é inativado, quando o pedido é cancelado automaticamente, então as psicopedagogas recebem a notificação com o motivo, exceto quem inativou o aluno (RG-25).
- [ ] Dada uma fase de entrega em que a tela de origem ainda não existe, quando o usuário abre a tela, então ela não mostra o tipo de notificação dessa tela.
- [ ] Dados os perfis Psicopedagoga, Professor, Aluno e Responsável, quando qualquer um abre o sino, então a tela abre sem "Acesso negado".
- [ ] Dado qualquer perfil, quando usa esta tela no computador, no celular ou só com o teclado, então todas as ações funcionam (RG-26).
- [ ] Dado que a conexão caiu, quando o usuário tenta abrir ou marcar uma notificação, então aparece "Sem conexão" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)) na própria tela.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
