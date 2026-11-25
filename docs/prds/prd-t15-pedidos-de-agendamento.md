# PRD da tela de Pedidos de agendamento

| Campo | Valor |
| --- | --- |
| Identificador | T15 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T13 Agenda](prd-t13-agenda.md), [T14 Evento](prd-t14-evento.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 2 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que o aluno e o responsável peçam para marcar, remarcar ou cancelar eventos, e que a psicopedagoga aceite ou recuse cada pedido, para que todo pedido de reunião passe pela agenda.

## 2. Escopo

### O que entra no escopo

- Pedir a marcação de uma Reunião ou de um Atendimento (Aluno e Responsável).
- Pedir a remarcação ou o cancelamento de um evento, a partir do evento (Aluno e Responsável).
- Acompanhar os pedidos do aluno em "Meus pedidos" (Aluno e Responsável).
- Analisar todos os pedidos, aceitando ou recusando (Psicopedagoga).
- Cancelar o próprio pedido enquanto ele está pendente (autor).
- Ver o detalhe de um pedido.

### O que não entra no escopo

- Criar, editar, remarcar e cancelar eventos diretamente: ficam em [T14 Evento](prd-t14-evento.md). O professor marca eventos por T14 e não faz pedido.
- Ver os pedidos pendentes no calendário: o pedido aparece como "Pendente" em [T13 Agenda](prd-t13-agenda.md).
- Ver a lista de notificações: fica em [T03 Notificações](prd-t03-notificacoes.md).
- Pedido de remarcação ou cancelamento de Avaliação e de evento do tipo Outro: não é aceito (RN-04).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Analisa todos os pedidos. Aceita, com ajuste de data, horário e participantes quando for marcação ou remarcação, ou recusa com motivo. Não pede agendamento e não cancela pedido de outra pessoa. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Aluno | Pede marcação, remarcação e cancelamento para si. Acompanha em "Meus pedidos" todos os pedidos dele, inclusive os feitos pelos responsáveis. Cancela os pedidos que fez, enquanto estão pendentes. |
| Responsável | Pede marcação, remarcação e cancelamento em nome do aluno escolhido. Acompanha em "Meus pedidos" todos os pedidos do aluno escolhido, inclusive os feitos pelo aluno e por outros responsáveis. Cancela só os pedidos que fez, enquanto estão pendentes. |

**Contexto:** o aluno ou o responsável chega aqui para pedir um horário ou acompanhar um pedido. A psicopedagoga chega para decidir os pedidos que aguardam resposta.

**Origem da jornada:** Início (a psicopedagoga vê a quantidade e os 5 pendentes mais antigos, o aluno vê os pedidos pendentes e o responsável vê a quantidade de pendentes por aluno nos cartões, [T02 Início](prd-t02-inicio.md)) → menu "Pedidos de agendamento" (Psicopedagoga) ou "Meus pedidos" (Aluno e Responsável). O pedido de marcação também começa por um horário vazio ou pelo botão "Novo" da agenda ([T13 Agenda](prd-t13-agenda.md)) e pelo botão "Pedir agendamento" no cabeçalho do perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). Os pedidos de remarcação e de cancelamento começam no evento ([T14 Evento](prd-t14-evento.md)).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Lista de pedidos | Uma linha por pedido, com aluno, quem pediu, tipo de pedido (marcação, remarcação ou cancelamento), data sugerida, data do pedido e situação. |
| Coluna "Quem pediu" | Mostra o autor do pedido: o aluno ou o responsável. |
| Quantidade de pendentes | Em "Meus pedidos", todos veem quantos pedidos pendentes o aluno já tem (RN-02). |
| Detalhe do pedido | Todos os campos, quem pediu, data do pedido, situação, motivo da recusa e link para o evento criado, remarcado ou cancelado. |
| Participantes | Os nomes seguem RG-31. Os outros aparecem só como quantidade, por exemplo "Mais 2 participantes". |
| Filtros ativos | Ficam visíveis e podem ser limpos de uma vez (RG-21). |
| Aluno escolhido | Para o responsável, o cabeçalho mostra o aluno escolhido, com a opção "Trocar aluno" ([T02 Início](prd-t02-inicio.md)). |
| Autoria | Quem criou o pedido e quando (RG-15). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

Campos do pedido de marcação:

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Tipo | Sim | Reunião ou Atendimento. |
| Aluno | Sim | O próprio aluno, ou um aluno vinculado, se quem pede é o responsável. |
| Data e horário sugeridos | Sim | Pelo menos 24 horas a partir do pedido. |
| Outro horário possível | Não | Segunda opção de data e horário. |
| Motivo | Sim | Até 1.000 caracteres. |
| Participantes sugeridos | Não | Responsáveis e professores do aluno. |
| Anexos | Não | Segue RG-16. |

Campos do pedido de remarcação (feito a partir do evento):

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nova data | Sim | Data sugerida para o evento. |
| Novo horário sugerido | Sim | Pelo menos 24 horas a partir do pedido. |
| Motivo | Sim | Ver "Tamanho dos motivos" em 7.2. |

Campo do pedido de cancelamento (feito a partir do evento):

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Motivo | Sim | Só o motivo. Ver "Tamanho dos motivos" em 7.2. |

Campo da recusa:

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Motivo da recusa | Sim | Texto livre. Ver "Tamanho dos motivos" em 7.2. |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Situação | Pendente, Aceito, Recusado, Cancelado, Expirado | Pendente |
| Tipo de pedido | Marcação, Remarcação, Cancelamento | Sem filtro |
| Aluno | Alunos visíveis ao usuário (Psicopedagoga). Ver "Filtro Aluno para o responsável" em 7.2. | Sem filtro |
| Período | Intervalo de datas | Ver "Período padrão" em 7.2. |

### 5.3 Ordenação e paginação

- Ordenação padrão: pendentes mais antigos primeiro.
- Outras ordenações: ver "Ordem dos pedidos que não estão pendentes" em 7.2.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O aluno ou o responsável abre "Pedir agendamento" (pelo horário vazio da agenda, pelo botão "Novo" ou pelo perfil do aluno).
2. O usuário preenche tipo, aluno, data e horário sugeridos, motivo e, se quiser, outro horário possível, participantes sugeridos e anexos.
3. O sistema cria o pedido "Pendente" e notifica as psicopedagogas (seção 8).
4. O pedido aparece na agenda do aluno como "Pendente" ([T13 Agenda](prd-t13-agenda.md)) e em "Meus pedidos".
5. A psicopedagoga abre "Pedidos de agendamento", que mostra os pendentes mais antigos primeiro, e abre o detalhe.
6. A psicopedagoga aceita, com ajuste se quiser, ou recusa com motivo.
7. O sistema muda a situação do pedido, executa o efeito do aceite (6.5) e notifica quem pediu, o aluno e os responsáveis do aluno.

### 6.2 Fluxos alternativos

- Aluno com 3 pedidos pendentes: o sistema não cria outro pedido e mostra a mensagem de erro (RN-02).
- Evento que já tem um pedido de remarcação ou cancelamento pendente: o sistema não cria outro pedido (RN-03).
- Data e horário sugeridos com menos de 24 horas: o sistema não salva e mostra a mensagem de erro (RN-05).
- Aceite com conflito de horário: o sistema avisa, mas não impede (RN-08).
- Recusa sem motivo: o sistema não recusa e mostra a mensagem de erro.
- Pedido que expira: o sistema muda a situação para "Expirado" e notifica quem pediu (RN-06).
- Aluno inativado ou autor que perde o acesso ao aluno: o pedido pendente vira "Cancelado" automaticamente, e as psicopedagogas recebem a notificação com o motivo (RN-07).
- Sair do formulário com alterações não salvas: o sistema pede confirmação (RG-29). Se salvar falhar, o que foi digitado continua no formulário.
- Pedido que o usuário não pode ver ou que não existe: o sistema abre "Não encontrado" (RG-13).
- Professor que tenta abrir a tela: o sistema abre "Acesso negado" (RG-13).
- Botão "Pedir agendamento" em "Meus pedidos" e anexos do pedido: ver 7.2.

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Pedir marcação | Aluno, Responsável | Abre o formulário de marcação (5.1). Ao salvar, cria o pedido "Pendente" e notifica as psicopedagogas. |
| Pedir remarcação | Aluno, Responsável | Feita a partir do evento ([T14 Evento](prd-t14-evento.md)). Cria o pedido de remarcação. |
| Pedir cancelamento | Aluno, Responsável | Feita a partir do evento ([T14 Evento](prd-t14-evento.md)). Cria o pedido de cancelamento. |
| Abrir o detalhe do pedido | Psicopedagoga, Aluno, Responsável | Mostra o detalhe (seção 4). |
| Aceitar | Psicopedagoga | Na marcação e na remarcação, pode ajustar data, horário e participantes. Cria o evento, remarca ou cancela o evento existente, conforme o tipo do pedido (6.5). No cancelamento, o motivo do pedido vira o motivo do cancelamento. Pede confirmação (RG-23). |
| Recusar | Psicopedagoga | Motivo obrigatório. Pede confirmação (RG-23). O motivo aparece no detalhe do pedido. |
| Cancelar pedido | Autor | Só enquanto está pendente. Pede confirmação (RG-23) e notifica as psicopedagogas. |
| Filtrar e limpar filtros | Psicopedagoga, Aluno, Responsável | Atualiza a lista. Os filtros se mantêm ao voltar e um link copiado abre com os mesmos filtros (RG-21). |
| Trocar aluno | Responsável com mais de um aluno | Troca o aluno cujos pedidos aparecem ([T02 Início](prd-t02-inicio.md)). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra a mensagem de lista vazia. Aluno e Responsável veem a ação principal "Pedir agendamento". A psicopedagoga vê só a mensagem (RG-22). |
| Vazio, por causa dos filtros | Mostra a mensagem de nenhum pedido com os filtros escolhidos e a opção de limpar os filtros (RG-22). |
| Sem permissão | O professor abre "Acesso negado". Pedido que não existe ou que o usuário não pode ver abre "Não encontrado" (RG-13). Os estados estão em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado" aparecem como aviso na própria tela, sem trocar de tela ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |

### 6.5 Tipos de pedido

| Tipo | Onde o pedido é feito | O que o autor informa | O que acontece ao aceitar |
| --- | --- | --- | --- |
| Marcação | Agenda, perfil do aluno ou "Pedir agendamento" | Os campos de marcação (5.1) | Cria o evento (RN-09). A psicopedagoga pode ajustar data, horário e participantes. |
| Remarcação | Evento ([T14 Evento](prd-t14-evento.md)) | Nova data, novo horário sugerido e motivo | Remarca o evento existente, com o histórico de remarcações. A psicopedagoga pode ajustar data, horário e participantes. |
| Cancelamento | Evento ([T14 Evento](prd-t14-evento.md)) | Só o motivo | Cancela o evento existente. O motivo do pedido vira o motivo do cancelamento. |

### 6.6 Situações e regras de mudança

As situações e as regras completas estão na seção 6 do índice (Pedido de agendamento). Este quadro diz qual ação ou momento provoca cada mudança nesta tela.

| Situação | O que provoca a mudança nesta tela |
| --- | --- |
| Pendente | O pedido nasce assim. |
| Aceito | A psicopedagoga usa "Aceitar". |
| Recusado | A psicopedagoga usa "Recusar". |
| Cancelado | O autor usa "Cancelar pedido" enquanto está pendente, ou o sistema cancela sozinho (RN-07). |
| Expirado | O sistema muda sozinho, conforme RN-06. |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Aluno e responsável fazem os pedidos e acompanham os pedidos do aluno. A psicopedagoga analisa todos. O professor não acessa a tela. O responsável só pede para aluno vinculado a que tem acesso (RG-17). |
| RN-02 | Cada aluno pode ter no máximo 3 pedidos pendentes. Todos veem quantos pedidos pendentes o aluno já tem. |
| RN-03 | Um evento só pode ter um pedido de remarcação ou cancelamento pendente por vez. |
| RN-04 | Remarcação e cancelamento só valem para Reunião e Atendimento. Avaliações e eventos do tipo Outro não aceitam pedido. |
| RN-05 | A data e o horário sugeridos, na marcação e na remarcação, ficam pelo menos 24 horas à frente do momento do pedido. |
| RN-06 | Pedido de marcação pendente vira "Expirado" quando passa a última data sugerida: o outro horário possível, se informado, ou a data sugerida. Pedido de remarcação ou cancelamento vira "Expirado" quando o evento começa. |
| RN-07 | O pedido pendente vira "Cancelado" automaticamente quando o aluno é inativado ou quando o autor perde o acesso ao aluno. O responsável que perde o acesso a um aluno tem os pedidos pendentes daquele aluno cancelados (T07). O cancelamento automático gera notificação para as psicopedagogas, com o motivo: aluno inativado ou autor sem acesso ao aluno (seção 7 do índice). |
| RN-08 | Ao aceitar com conflito de horário, o sistema avisa, mas não impede. |
| RN-09 | O evento criado ao aceitar uma marcação tem como criador a psicopedagoga que aceitou. São participantes: ela, o aluno, o autor do pedido e os participantes que ela mantiver. O autor do pedido começa com resposta "Confirmada" se a psicopedagoga aceitou uma das datas sugeridas, e com "Sem resposta" se ela mudou a data ou o horário. |
| RN-10 | Recusar exige motivo, que aparece no detalhe do pedido. |
| RN-11 | O autor cancela o pedido só enquanto ele está pendente. |
| RN-12 | "Meus pedidos" mostra todos os pedidos do aluno, feitos pelo próprio aluno ou por qualquer responsável dele, com a coluna "Quem pediu". O responsável vê os pedidos do aluno escolhido ([T02 Início](prd-t02-inicio.md)). |
| RN-13 | O filtro "Situação" começa em Pendente e a lista mostra os pendentes mais antigos primeiro. |
| RN-14 | Em todos os pedidos, os participantes seguem RG-31. |
| RN-15 | As notificações dos pedidos seguem a seção 7 do índice e RG-25. O responsável só recebe notificação com conta ativa. O texto das notificações segue RG-31. |
| RN-16 | Os pedidos pendentes aparecem na agenda do aluno marcados como "Pendente" ([T13 Agenda](prd-t13-agenda.md)). |
| RN-17 | Segue RG-09, RG-13, RG-16, RG-17, RG-18, RG-19 a RG-24, RG-29 e RG-31. |
| RN-18 | Ao aceitar uma remarcação, as respostas de todos os participantes, inclusive a do autor, voltam para "Sem resposta" (situações, seção 6 do índice). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Expiração de remarcação quando a nova data sugerida passa antes do evento começar | Se a nova data sugerida já passou e o evento ainda não começou, o pedido continua pendente, e a psicopedagoga aceita ajustando a data ou recusa. |
| Participantes sugeridos que são responsáveis sem conta | A lista só inclui responsáveis com conta ativa, porque participante é usuário ativo. |
| Filtro Aluno para o responsável | Não aparece. A lista usa o aluno escolhido no cabeçalho. |
| Período padrão | O filtro "Período" começa vazio, sem limite de datas. |
| Ordem dos pedidos que não estão pendentes | Aparecem depois dos pendentes, do mais recente para o mais antigo. |
| Tamanho dos motivos | Os motivos de remarcação, cancelamento e recusa aceitam até 1.000 caracteres, como o motivo da marcação. |
| Botão "Pedir agendamento" em "Meus pedidos" | A tela mostra o botão no topo da lista para Aluno e Responsável. |
| Anexos do pedido ao aceitar uma marcação | Os anexos passam para o evento criado. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Pedido de agendamento criado | Psicopedagogas | Avisa que há um novo pedido, com aluno, tipo de pedido e data sugerida. |
| Pedido de agendamento aceito | Quem pediu, o aluno e os responsáveis do aluno | Avisa que o pedido foi aceito e leva ao evento. |
| Pedido de agendamento recusado | Quem pediu, o aluno e os responsáveis do aluno | Avisa que o pedido foi recusado e informa o motivo. |
| Pedido de agendamento cancelado pelo autor | Psicopedagogas | Avisa que o autor cancelou o pedido, com aluno e tipo de pedido. |
| Pedido de agendamento cancelado automaticamente | Psicopedagogas, menos quem fez a ação que causou o cancelamento (RG-25) | Avisa que o pedido foi cancelado, com aluno, tipo de pedido e o motivo: aluno inativado ou autor sem acesso ao aluno (RN-07). |
| Pedido de agendamento expirado | Quem pediu | Avisa que o pedido expirou sem resposta. |
| Evento criado, remarcado ou cancelado ao aceitar | Participantes do evento | Seguem as notificações do evento em [T14 Evento](prd-t14-evento.md). |

Ninguém recebe notificação da própria ação (RG-25). O responsável só recebe notificação se tiver conta ativa. O texto das notificações segue RG-31 (RN-15).

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Pedido criado | Sucesso | Pedido enviado. A psicopedagoga vai analisar. (proposta) |
| Pedido aceito | Sucesso | Pedido aceito. O evento foi atualizado e os participantes foram avisados. (proposta) |
| Pedido recusado | Sucesso | Pedido recusado. O motivo foi enviado a quem pediu. (proposta) |
| Pedido cancelado pelo autor | Sucesso | Pedido cancelado. As psicopedagogas foram avisadas. (proposta) |
| Confirmar aceite de marcação | Confirmação | Aceitar este pedido? O evento será criado e os participantes serão avisados. (proposta) |
| Confirmar aceite de remarcação | Confirmação | Aceitar este pedido? O evento será remarcado e os participantes serão avisados. (proposta) |
| Confirmar aceite de cancelamento | Confirmação | Aceitar este pedido? O evento será cancelado e os participantes serão avisados com o motivo. (proposta) |
| Confirmar recusa | Confirmação | Recusar este pedido? Quem pediu será avisado com o motivo. (proposta) |
| Confirmar cancelamento do pedido | Confirmação | Cancelar este pedido? Ele deixará de ser analisado e as psicopedagogas serão avisadas. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Conflito de horário ao aceitar | Aviso | Algum participante já tem um evento neste horário. Você pode aceitar mesmo assim. (proposta) |
| Limite de 3 pedidos pendentes | Erro | Este aluno já tem 3 pedidos pendentes. Aguarde a resposta ou cancele um pedido para fazer outro. (proposta) |
| Evento já com pedido pendente | Erro | Este evento já tem um pedido de remarcação ou cancelamento pendente. Aguarde a resposta. (proposta) |
| Data e horário com menos de 24 horas | Erro | Escolha uma data e um horário com pelo menos 24 horas a partir de agora. (proposta) |
| Motivo não informado | Erro | Informe o motivo para continuar. (proposta) |
| Motivo da recusa não informado | Erro | Informe o motivo da recusa. (proposta) |
| Anexo fora das regras | Erro | O arquivo precisa ser PDF, JPG ou PNG, com até 10 MB, e cada pedido aceita até 5 anexos. Escolha outro arquivo. (proposta) |
| Pedido que não existe ou que o usuário não pode ver | Erro | Não encontramos o que você procurou. |
| Professor abre a tela | Erro | Você não tem acesso a esta tela. |
| Falha de conexão | Erro | Sem conexão com a internet. O que você digitou não foi perdido. |
| Falha inesperada | Erro | Algo deu errado. Tente de novo em alguns minutos. |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Acessar a tela | Sim | Não | Sim | Sim |
| Ver os pedidos | Sim, todos | Não | Só os do próprio aluno, de qualquer autor | Só os do aluno escolhido, de qualquer autor |
| Pedir marcação | Não | Não | Sim, para si | Sim, para aluno vinculado |
| Pedir remarcação ou cancelamento (a partir de T14) | Não | Não | Sim, em Reunião ou Atendimento agendado e futuro em que participa | Sim, em Reunião ou Atendimento agendado e futuro em que o aluno participa |
| Aceitar | Sim | Não | Não | Não |
| Ajustar data, horário e participantes ao aceitar | Sim | Não | Não | Não |
| Recusar | Sim | Não | Não | Não |
| Cancelar pedido | Não | Não | Só os que fez, enquanto pendentes | Só os que fez, enquanto pendentes |

## 11. Critérios de aceite

- [ ] Dado um aluno, quando preenche os campos obrigatórios com data e horário a pelo menos 24 horas à frente e salva, então o sistema cria o pedido "Pendente" e notifica as psicopedagogas.
- [ ] Dado um responsável com mais de um aluno, quando abre "Pedir agendamento", então pode escolher entre os alunos vinculados a ele.
- [ ] Dado um aluno, quando abre o campo "Aluno", então só vê a si mesmo.
- [ ] Dado o campo "Tipo", quando o usuário o abre, então vê Reunião e Atendimento.
- [ ] Dado um pedido sem tipo, aluno, data e horário ou motivo, quando o usuário salva, então o sistema não salva e mostra o erro dos campos.
- [ ] Dado um motivo com mais de 1.000 caracteres, quando o usuário salva, então o sistema não salva e mostra o erro do campo.
- [ ] Dado uma data e um horário sugeridos com menos de 24 horas, quando o usuário salva, então o sistema não salva e mostra a mensagem de erro.
- [ ] Dado um pedido com "Outro horário possível" informado, quando o usuário salva, então o pedido guarda as duas opções.
- [ ] Dado participantes sugeridos, quando o usuário busca, então encontra só responsáveis e professores do aluno.
- [ ] Dado anexos fora das regras de RG-16, quando o usuário os envia, então o sistema recusa o arquivo e mostra o erro.
- [ ] Dado um aluno com 3 pedidos pendentes, quando o aluno ou um responsável tenta criar outro pedido, então o sistema não cria e mostra a mensagem de erro.
- [ ] Dado um evento com um pedido de remarcação ou cancelamento pendente, quando o aluno ou o responsável tenta fazer outro pedido para o mesmo evento, então o sistema não cria.
- [ ] Dado uma Avaliação ou um evento do tipo Outro, quando o aluno ou o responsável abre o evento, então não pode pedir remarcação nem cancelamento.
- [ ] Dado uma Reunião ou um Atendimento agendado e futuro em que o aluno participa, quando o aluno ou o responsável pede remarcação com nova data, novo horário a pelo menos 24 horas à frente e motivo, então o sistema cria o pedido de remarcação "Pendente".
- [ ] Dado uma Reunião ou um Atendimento agendado e futuro em que o aluno participa, quando o aluno ou o responsável pede cancelamento só com o motivo, então o sistema cria o pedido de cancelamento "Pendente".
- [ ] Dado um aluno, quando abre "Meus pedidos", então vê todos os pedidos dele, feitos por ele ou por qualquer responsável, com a coluna "Quem pediu".
- [ ] Dado um responsável, quando abre "Meus pedidos", então vê os pedidos do aluno escolhido, feitos por qualquer autor, e troca de aluno em "Trocar aluno".
- [ ] Dado "Meus pedidos", quando o usuário abre a lista, então vê quantos pedidos pendentes o aluno já tem.
- [ ] Dado a psicopedagoga, quando abre "Pedidos de agendamento", então vê os pedidos de todos os alunos, com situação Pendente e os mais antigos primeiro.
- [ ] Dado a lista de pedidos, quando é exibida, então cada linha mostra aluno, quem pediu, tipo de pedido, data sugerida, data do pedido e situação.
- [ ] Dado a lista com mais de 20 pedidos, quando o usuário a abre, então vê 20 por página e o total de resultados (RG-19).
- [ ] Dado filtros de situação, tipo de pedido, aluno e período, quando o usuário os aplica, então a lista mostra só os pedidos que atendem aos filtros e os filtros ficam visíveis (RG-21).
- [ ] Dado filtros ativos, quando o usuário volta para a lista ou abre um link copiado, então os mesmos filtros estão ativos (RG-21).
- [ ] Dado filtros que não deixam nenhum pedido, quando a lista atualiza, então mostra a mensagem e a opção de limpar os filtros (RG-22).
- [ ] Dado um aluno ou um responsável sem nenhum pedido, quando abre "Meus pedidos", então vê a mensagem de lista vazia e a ação "Pedir agendamento".
- [ ] Dado um pedido, quando o usuário abre o detalhe, então vê todos os campos, quem pediu, a data do pedido, a situação, o motivo da recusa e o link para o evento criado, remarcado ou cancelado.
- [ ] Dado um pedido de marcação, quando a psicopedagoga o aceita, então o sistema cria o evento com a psicopedagoga como criadora.
- [ ] Dado um pedido de marcação aceito, quando o evento é criado, então os participantes são a psicopedagoga, o aluno, o autor do pedido e os que ela manteve.
- [ ] Dado um pedido de marcação aceito com uma das datas sugeridas, quando o evento é criado, então o autor do pedido tem a resposta "Confirmada".
- [ ] Dado um pedido de marcação aceito com data ou horário mudados, quando o evento é criado, então o autor do pedido tem a resposta "Sem resposta".
- [ ] Dado um pedido de marcação ou de remarcação, quando a psicopedagoga aceita, então pode ajustar data, horário e participantes.
- [ ] Dado um pedido de remarcação, quando a psicopedagoga o aceita, então o sistema remarca o evento existente e o pedido fica "Aceito".
- [ ] Dado um pedido de remarcação aceito, quando o evento é remarcado, então as respostas de todos os participantes, inclusive a do autor, voltam para "Sem resposta".
- [ ] Dado um pedido de cancelamento, quando a psicopedagoga o aceita, então o sistema cancela o evento existente e o motivo do pedido vira o motivo do cancelamento.
- [ ] Dado um aceite com conflito de horário, quando a psicopedagoga aceita, então o sistema avisa e não impede.
- [ ] Dado um aceite, quando a psicopedagoga confirma, então o sistema pede confirmação que diz a ação e a consequência, muda o pedido para "Aceito" e notifica quem pediu, o aluno e os responsáveis do aluno.
- [ ] Dado um pedido pendente, quando a psicopedagoga recusa com motivo, então o pedido fica "Recusado", o motivo aparece no detalhe e quem pediu, o aluno e os responsáveis do aluno são notificados.
- [ ] Dado um pedido pendente, quando a psicopedagoga tenta recusar sem motivo, então o sistema não recusa e mostra o erro do motivo.
- [ ] Dado um pedido pendente, quando o autor o cancela, então o pedido fica "Cancelado" e as psicopedagogas são notificadas.
- [ ] Dado um pedido que não está pendente, quando o autor abre o detalhe, então não vê "Cancelar pedido".
- [ ] Dado um pedido feito por outro responsável, quando o aluno ou outro responsável abre o detalhe, então não vê "Cancelar pedido".
- [ ] Dado um pedido de marcação pendente com outro horário possível informado, quando passa esse outro horário sem resposta, então o pedido fica "Expirado" e quem pediu é notificado.
- [ ] Dado um pedido de marcação pendente sem outro horário, quando passa a data sugerida sem resposta, então o pedido fica "Expirado" e quem pediu é notificado.
- [ ] Dado um pedido de remarcação ou de cancelamento pendente, quando o evento começa, então o pedido fica "Expirado" e quem pediu é notificado.
- [ ] Dado um aluno com pedidos pendentes, quando a psicopedagoga o inativa, então os pedidos pendentes ficam "Cancelados" automaticamente, e as outras psicopedagogas recebem a notificação com o motivo "aluno inativado" (RN-07, RG-25).
- [ ] Dado um responsável que perde o acesso a um aluno, quando o acesso é retirado, então os pedidos pendentes dele para esse aluno ficam "Cancelados" automaticamente, e as outras psicopedagogas recebem a notificação com o motivo (RN-07, RG-25).
- [ ] Dado um pedido pendente, quando o usuário abre a agenda do aluno, então o pedido aparece como "Pendente" (aluno e responsável).
- [ ] Dado um pedido com participantes que o usuário não pode ver, quando abre o detalhe, então vê os nomes que RG-31 permite e os outros só como quantidade.
- [ ] Dado um professor, quando tenta abrir a tela, então vê "Acesso negado" (RG-13).
- [ ] Dado um pedido que não existe ou que o usuário não pode ver, quando tenta abri-lo, então vê "Não encontrado" (RG-13).
- [ ] Dado um aluno ou um responsável, quando tenta aceitar ou recusar um pedido, então a ação não está disponível.
- [ ] Dado um formulário com alterações não salvas, quando o usuário tenta sair, então o sistema pede confirmação (RG-29).
- [ ] Dado uma falha ao salvar, quando o usuário tenta salvar, então o sistema mantém o que foi digitado e mostra "Sem conexão" ou "Erro inesperado".
- [ ] Dado qualquer notificação gerada por uma ação do próprio usuário, quando ela é enviada, então o usuário não a recebe (RG-25).
- [ ] Dado a tela em um celular ou usada só com o teclado, quando o usuário a percorre, então consegue usar todas as ações (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
