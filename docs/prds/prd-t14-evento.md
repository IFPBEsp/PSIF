# PRD da tela de Evento

| Campo | Valor |
| --- | --- |
| Identificador | T14 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md), [T13 Agenda](prd-t13-agenda.md), [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md), [T21 Professores](prd-t21-professores.md), [T23 Equipe](prd-t23-equipe.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 2. A ação "Registrar atendimento" e o link para o acompanhamento registrado só aparecem na fase 3 (ver 6.6). |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga e o professor criem, consultem, remarquem e cancelem eventos, e que os participantes respondam e tenham a presença registrada, para que a agenda reflita o que realmente foi marcado e o que aconteceu.

## 2. Escopo

### O que entra no escopo

- Criar um evento (Psicopedagoga e Professor).
- Consultar os detalhes de um evento.
- Editar, remarcar e cancelar um evento.
- Confirmar ou recusar presença, como participante.
- Registrar a presença dos participantes depois do evento.
- Pedir remarcação ou cancelamento de um evento (Aluno e Responsável), que cria um pedido de agendamento.
- Registrar atendimento a partir de um evento realizado (fase 3).

### O que não entra no escopo

- Ver os eventos no calendário e filtrá-los: fica em [T13 Agenda](prd-t13-agenda.md).
- Analisar pedidos de agendamento e criar evento por um pedido de marcação: ficam em [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md).
- Aluno e responsável criarem eventos: eles fazem um pedido de agendamento (T15).
- Preencher o acompanhamento: fica em [T10 Acompanhamentos](prd-t10-acompanhamentos.md).
- Perguntar se cancela os eventos futuros ao inativar um aluno, um professor ou um membro da equipe: fica em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T21 Professores](prd-t21-professores.md) e [T23 Equipe](prd-t23-equipe.md). O efeito sobre os eventos está em RN-19.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Cria eventos de qualquer tipo. Edita, remarca e cancela qualquer evento. Registra a presença de qualquer evento realizado. Registra atendimento. Confirma ou recusa presença quando é participante e não é criadora. |
| Professor | Cria eventos dos tipos Reunião, Avaliação e Outro, com alunos das suas turmas. Edita, remarca e cancela os eventos que criou. Registra a presença dos eventos que criou. Confirma ou recusa presença quando é participante. Não registra atendimento. |
| Aluno | Consulta os eventos em que participa. Confirma ou recusa presença. Pede remarcação ou cancelamento de Reunião ou Atendimento. Não cria, edita, remarca nem cancela evento. |
| Responsável | Consulta os eventos em que o aluno escolhido ou ele próprio participa. Confirma ou recusa presença quando é participante. Pede remarcação ou cancelamento de Reunião ou Atendimento em que o aluno participa. Não cria, edita, remarca nem cancela evento. |

**Contexto:** o usuário chega aqui para marcar um compromisso, conferir os detalhes de um evento, responder a um convite ou registrar quem compareceu.

**Origem da jornada:** Início (blocos de eventos e de eventos realizados sem presença registrada, [T02 Início](prd-t02-inicio.md)) → menu "Agenda" → item ou horário vazio ([T13 Agenda](prd-t13-agenda.md)). Também pelo sino de notificações, pelo detalhe de um pedido de agendamento ([T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md)) e pelo acompanhamento registrado ([T10 Acompanhamentos](prd-t10-acompanhamentos.md)).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Dados do evento | Tipo, título, data, início e fim, local, alunos, descrição e anexos. |
| Situação do evento | Agendado, Realizado ou Cancelado (6.5). |
| Participantes | Cada participante com a resposta e a presença. Os nomes seguem RG-31. Os participantes que o usuário não pode ver aparecem só como quantidade, por exemplo "Mais 2 participantes". |
| Histórico de remarcações | Cada remarcação com o motivo. |
| Motivo do cancelamento | Aparece no evento cancelado. |
| Pedido de origem | Link para o pedido de agendamento que deu origem ao evento, quando houver ([T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md)). |
| Acompanhamento registrado | Link para o acompanhamento registrado a partir do evento, quando houver. Fase 3. |
| Autoria | Quem criou e quando. Evento alterado mostra "Editado em" com a data e o autor da última alteração (RG-15). |
| Aviso de conflito | Aparece ao salvar quando algum participante já tem evento no mesmo horário (RN-04). |
| Ações | As ações que o perfil pode fazer naquele momento (6.3). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Tipo | Sim | Psicopedagoga: Reunião, Atendimento, Avaliação ou Outro. Professor: Reunião, Avaliação ou Outro. |
| Título | Sim | Até 100 caracteres. |
| Data | Sim | Hoje ou depois. |
| Início e fim | Sim | O fim vem depois do início, no mesmo dia. |
| Local | Não | Por exemplo, sala ou link de reunião. |
| Alunos | Em Atendimento e Avaliação | Alunos atendidos e ativos. O professor só escolhe alunos das suas turmas. Os alunos escolhidos viram participantes. |
| Participantes | Não | Usuários cadastrados e ativos, buscados por nome ou e-mail. A psicopedagoga escolhe qualquer usuário. O professor escolhe pessoas com perfil Psicopedagoga, outros professores, alunos das suas turmas e os responsáveis com acesso desses alunos. Ao escolher um aluno, o sistema sugere os responsáveis com acesso. |
| Descrição | Não | Até 2.000 caracteres. |
| Anexos | Não | Segue RG-16. |

Campos das ações:

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nova data e novo horário (remarcar) | Sim | Ver "Regras da nova data e do novo horário" em 7.2. |
| Motivo da remarcação | Sim | Texto livre. Ver "Tamanho dos motivos" em 7.2. |
| Motivo do cancelamento | Sim | Texto livre. Ver "Tamanho dos motivos" em 7.2. |
| Motivo da recusa de presença | Não | Texto livre. Ver "Tamanho dos motivos" em 7.2. |
| Presença de cada participante | Sim, ao registrar | Presente ou Faltou. |

### 5.2 Filtros

Não se aplica. A tela mostra um evento só. Os filtros ficam em [T13 Agenda](prd-t13-agenda.md).

### 5.3 Ordenação e paginação

- Ordenação padrão: Não se aplica.
- Outras ordenações: Não se aplica.
- Paginação: Não se aplica.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga ou o professor clica em um horário vazio da agenda ou em "Novo" e abre "Novo evento", com a data e a hora preenchidas quando vierem do horário vazio.
2. O usuário preenche os campos (5.1) e escolhe os alunos e os participantes.
3. O usuário salva. Se algum participante já tem evento no mesmo horário, o sistema avisa e deixa salvar (RN-04).
4. O sistema cria o evento "Agendado", sem aprovação, com o criador como participante "Confirmada" (RN-01, RN-02).
5. O sistema notifica os participantes (seção 8).
6. Cada participante confirma ou recusa presença até o início do evento (RN-09).
7. Depois que o evento vira "Realizado", o criador ou a psicopedagoga registra a presença de cada participante (RN-10).

### 6.2 Fluxos alternativos

- Dado inválido ou campo obrigatório vazio: o sistema não salva, marca o campo e mostra a mensagem de erro. O que foi digitado continua no formulário (RG-29).
- Falha ao salvar: o sistema mostra o aviso na própria tela e mantém o que foi digitado (RG-29). Ver "Sem conexão" e "Erro inesperado" em [T26 Estados do sistema](prd-t26-estados-do-sistema.md).
- Sair com alterações não salvas: o sistema pede confirmação (RG-29).
- Conflito de horário: o sistema avisa, mas não impede (RN-04).
- Evento realizado ou cancelado: a tela fica só para leitura, salvo o registro de presença no evento realizado (RN-05).
- Anexo fora das regras: o sistema recusa o arquivo e mostra a mensagem de erro (RG-16).
- Aluno ou responsável que quer marcar, remarcar ou cancelar: faz um pedido de agendamento (RN-13).
- Evento que não existe ou que o usuário não pode ver: o sistema abre "Não encontrado" (RG-13).
- Participante incluído ou retirado numa edição: quem entra recebe "Evento criado", quem sai recebe "Participante retirado do evento" e quem continua recebe "Evento alterado ou remarcado" (RN-21).
- Horário de início no passado quando a data é hoje e limite de participantes: ver 7.2.

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Criar evento | Psicopedagoga, Professor | Abre "Novo evento". Ao salvar, cria o evento "Agendado" e notifica os participantes. |
| Consultar evento | Participantes e quem a agenda mostra ([T13 Agenda](prd-t13-agenda.md)) | Mostra os detalhes (seção 4). |
| Editar | Criador e psicopedagoga | Só em evento agendado e futuro. Mudar data ou horário segue a regra de remarcar. Ao salvar, notifica os participantes conforme RN-21. |
| Remarcar | Criador e psicopedagoga | Pede nova data, novo horário e motivo obrigatório. As respostas dos participantes voltam para "Sem resposta". Guarda o histórico e mantém "Agendado". Notifica os participantes. |
| Pedir remarcação | Aluno e responsável | Só em Reunião ou Atendimento agendado e futuro em que o aluno participa. Cria um pedido de remarcação (T15). |
| Pedir cancelamento | Aluno e responsável | Mesmas condições do pedido de remarcação. Cria um pedido de cancelamento (T15), com motivo obrigatório. |
| Cancelar | Criador e psicopedagoga | Motivo obrigatório. Só em evento futuro. Pede confirmação (RG-23), muda o evento para "Cancelado" e notifica os participantes com o motivo. |
| Confirmar ou recusar presença | Participantes, exceto o criador | A recusa aceita um motivo opcional e avisa o criador. Pode ser mudada até o início do evento. |
| Registrar presença | Criador e psicopedagoga | Só em evento realizado. Marca cada participante como "Presente" ou "Faltou". Pode ser corrigida depois. |
| Registrar atendimento | Psicopedagoga | Só em Atendimento ou Reunião realizados. Abre [T10 Acompanhamentos](prd-t10-acompanhamentos.md) já preenchido com a data, o tipo e o evento. Fase 3. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Não se aplica. A tela mostra sempre um evento ou o formulário de novo evento. |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Evento que não existe ou que o usuário não pode ver abre "Não encontrado" (RG-13). Todos os perfis usam esta tela, então "Acesso negado" não se aplica. Aluno e responsável não têm a ação "Criar evento". Os estados estão em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado" aparecem como aviso na própria tela, sem trocar de tela ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |

### 6.5 Situações e regras de mudança

As situações e as regras completas estão na seção 6 do índice (Evento, Resposta do participante e Presença do participante). Esta tela só aplica as regras abaixo. Este quadro diz qual ação ou momento provoca cada mudança.

| Item | Situações | O que provoca a mudança nesta tela |
| --- | --- | --- |
| Evento | Agendado, Realizado, Cancelado | "Agendado" nasce ao criar o evento, sem aprovação. "Realizado" vem sozinho no término do evento. "Cancelado" vem da ação "Cancelar" ou do aceite de um pedido de cancelamento ([T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md)). "Remarcar" não muda a situação e guarda o histórico. |
| Resposta do participante | Sem resposta, Confirmada, Recusada | O criador nasce "Confirmada". Os outros participantes mudam pela ação "Confirmar ou recusar presença". "Remarcar" devolve todas para "Sem resposta". |
| Presença do participante | Não registrada, Presente, Faltou | Muda só pela ação "Registrar presença", depois que o evento vira "Realizado". Pode ser corrigida. |

### 6.6 Entrega por fase

| Fase | O que aparece no evento |
| --- | --- |
| 2 | Criar, consultar, editar, remarcar, cancelar, pedir remarcação, pedir cancelamento, confirmar ou recusar presença e registrar presença. Link para o pedido de origem. |
| 3 | Ação "Registrar atendimento" e link para o acompanhamento registrado ([T10 Acompanhamentos](prd-t10-acompanhamentos.md)). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Evento criado pela psicopedagoga ou pelo professor nasce "Agendado", sem aprovação. |
| RN-02 | O criador é participante com resposta "Confirmada". Os alunos escolhidos no campo "Alunos" também viram participantes. |
| RN-03 | Só a psicopedagoga e o professor criam eventos. Aluno e responsável fazem um pedido de agendamento (T15). |
| RN-04 | Se algum participante já tiver evento no mesmo horário, o sistema avisa, mas não impede. |
| RN-05 | Evento realizado ou cancelado fica só para leitura. A única exceção é o registro de presença no evento realizado. |
| RN-06 | Editar só vale em evento agendado e futuro. Mudar data ou horário segue a regra de remarcar. |
| RN-07 | Remarcar exige nova data, novo horário e motivo. Todas as respostas voltam para "Sem resposta". O evento continua "Agendado" e o histórico de remarcações, com o motivo, é guardado. |
| RN-08 | Cancelar exige motivo e só vale em evento futuro. O motivo é mostrado no evento e enviado aos participantes. |
| RN-09 | Todo participante, exceto o criador, confirma ou recusa presença. A recusa aceita motivo opcional e avisa o criador. A resposta pode ser mudada até o início do evento. |
| RN-10 | A presença só é registrada em evento realizado, pelo criador ou pela psicopedagoga, e pode ser corrigida depois. |
| RN-11 | "Registrar atendimento" só vale em Atendimento ou Reunião realizados, só para a psicopedagoga, e abre o acompanhamento com data, tipo e evento preenchidos. Fase 3. |
| RN-12 | O tipo depende do perfil: a psicopedagoga escolhe entre Reunião, Atendimento, Avaliação e Outro. O professor escolhe entre Reunião, Avaliação e Outro. Alunos são obrigatórios em Atendimento e Avaliação. |
| RN-13 | Aluno e responsável só pedem remarcação ou cancelamento de Reunião ou Atendimento agendado e futuro em que o aluno participa. Cada evento só tem um pedido de remarcação ou cancelamento pendente por vez, e cada aluno só tem no máximo 3 pedidos pendentes (T15). |
| RN-14 | Participantes são usuários cadastrados e ativos. O professor só escolhe quem a regra do campo permite (5.1). |
| RN-15 | O evento criado ao aceitar um pedido de marcação tem como criador a psicopedagoga que aceitou (T15). |
| RN-16 | Os participantes aparecem pelo nome ou como quantidade, conforme RG-31, nos detalhes do evento. |
| RN-17 | As notificações do evento seguem a seção 7 do índice e RG-25. O texto delas segue RG-31: cita pelo nome só os participantes que o destinatário pode ver. |
| RN-18 | O detalhe do evento mostra o link para o pedido de origem e, na fase 3, o link para o acompanhamento registrado. |
| RN-19 | Inativar um aluno pergunta se cancela os eventos futuros dele (T07). O responsável que perde acesso a um aluno sai dos eventos futuros daquele aluno (T07). Inativar um professor ou um membro da equipe pergunta se cancela os eventos futuros que ele criou (T21 e T23). Os eventos não cancelados de um membro da equipe podem ser geridos por qualquer pessoa com o perfil Psicopedagoga. Os eventos não cancelados de um professor inativado continuam, e a psicopedagoga os gerencia, como qualquer evento. |
| RN-20 | Segue RG-08, RG-09, RG-13, RG-15, RG-16, RG-18, RG-23, RG-24, RG-29 e RG-31. |
| RN-21 | Quando uma edição muda os participantes, quem foi incluído recebe "Evento criado", quem foi retirado recebe "Participante retirado do evento", com o nome, a data e a hora do evento, e quem continua recebe "Evento alterado ou remarcado" (seção 7 do índice). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Horário de início no passado quando a data é hoje | O horário de início precisa ser depois do horário atual. Caso contrário, o sistema não salva e mostra a mensagem de erro. |
| Regras da nova data e do novo horário | A remarcação segue as mesmas regras dos campos "Data" e "Início e fim". |
| Tamanho dos motivos | Os motivos de remarcação, cancelamento e recusa de presença aceitam até 1.000 caracteres, como o motivo do pedido de agendamento. |
| Texto do aviso de conflito | "Algum participante já tem um evento neste horário. Você pode salvar mesmo assim." |
| Professor edita participantes incluídos pela psicopedagoga | O professor edita o evento que criou, mas só remove os participantes que ele mesmo incluiu. |
| Aluno participante e a descrição e os anexos | O aluno participante vê a descrição e os anexos do evento. |
| Limite de participantes | Até 50 participantes por evento. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Evento criado | Participantes, menos quem criou (RG-25). Também quem é incluído depois numa edição (RN-21). | Avisa que o evento foi criado, com título, data e horário. |
| Evento alterado ou remarcado | Participantes que continuam no evento, menos quem alterou (RG-25) | Avisa que o evento mudou, com título e os novos data e horário, quando for remarcação. |
| Participante retirado do evento | Quem foi retirado numa edição (RN-21) | Avisa que a pessoa saiu do evento, com título, data e horário. |
| Evento cancelado | Participantes, menos quem cancelou (RG-25) | Avisa que o evento foi cancelado e informa o motivo. |
| Lembrete, 24 horas antes do evento | Participantes que não recusaram | Lembra o título, a data e o horário do evento. |
| Participante recusa presença | Quem criou o evento | Avisa quem recusou e o motivo, se houver. |

O responsável só recebe notificação se tiver conta ativa. O texto das notificações segue RG-31 (RN-17).

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Evento criado | Sucesso | Evento criado. Os participantes foram avisados. (proposta) |
| Evento editado | Sucesso | Evento salvo. Os participantes foram avisados. (proposta) |
| Evento remarcado | Sucesso | Evento remarcado. Os participantes foram avisados e as respostas voltaram para "Sem resposta". (proposta) |
| Evento cancelado | Sucesso | Evento cancelado. Os participantes foram avisados. (proposta) |
| Confirmar remarcação | Confirmação | Remarcar o evento? Os participantes serão avisados e as respostas voltarão para "Sem resposta". (proposta) |
| Confirmar cancelamento | Confirmação | Cancelar o evento? Os participantes serão avisados com o motivo, e o evento ficará só para leitura. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Conflito de horário | Aviso | Algum participante já tem um evento neste horário. Você pode salvar mesmo assim. (proposta) |
| Presença confirmada | Sucesso | Presença confirmada. (proposta) |
| Presença recusada | Sucesso | Presença recusada. O criador foi avisado. (proposta) |
| Presença registrada | Sucesso | Presença registrada. (proposta) |
| Data no passado | Erro | A data do evento precisa ser hoje ou depois. Escolha outra data. (proposta) |
| Fim antes do início | Erro | O horário de término precisa ser depois do início, no mesmo dia. Ajuste os horários. (proposta) |
| Título acima do limite | Erro | O título aceita até 100 caracteres. Reduza o texto. (proposta) |
| Descrição acima do limite | Erro | A descrição aceita até 2.000 caracteres. Reduza o texto. (proposta) |
| Alunos não informados em Atendimento ou Avaliação | Erro | Escolha pelo menos um aluno para este tipo de evento. (proposta) |
| Motivo não informado | Erro | Informe o motivo para continuar. (proposta) |
| Anexo fora das regras | Erro | O arquivo precisa ser PDF, JPG ou PNG, com até 10 MB, e cada evento aceita até 5 anexos. Escolha outro arquivo. (proposta) |
| Alteração em evento realizado ou cancelado | Erro | Este evento já aconteceu ou foi cancelado e não pode mais ser alterado. (proposta) |
| Evento que não existe ou que o usuário não pode ver | Erro | Não encontramos o que você procurou. |
| Falha de conexão | Erro | Sem conexão com a internet. O que você digitou não foi perdido. |
| Falha inesperada | Erro | Algo deu errado. Tente de novo em alguns minutos. |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Criar evento | Sim, todos os tipos | Sim, Reunião, Avaliação e Outro, com alunos das suas turmas | Não | Não |
| Consultar evento | Sim | Só os que a agenda mostra (T13) | Só os em que participa | Só os em que o aluno escolhido ou ele próprio participa |
| Ver resposta e presença dos participantes | Sim, nomes conforme RG-31 | Sim, nomes conforme RG-31 | Sim, nomes conforme RG-31 | Sim, nomes conforme RG-31 |
| Editar | Sim, em evento agendado e futuro | Só os que criou, em evento agendado e futuro | Não | Não |
| Remarcar | Sim | Só os que criou | Não | Não |
| Cancelar | Sim, em evento futuro | Só os que criou, em evento futuro | Não | Não |
| Pedir remarcação | Não | Não | Sim, em Reunião ou Atendimento agendado e futuro em que participa | Sim, em Reunião ou Atendimento agendado e futuro em que o aluno participa |
| Pedir cancelamento | Não | Não | Sim, nas mesmas condições | Sim, nas mesmas condições |
| Confirmar ou recusar presença | Sim, se for participante e não criadora | Sim, se for participante e não criador | Sim, se for participante | Sim, se for participante |
| Registrar presença | Sim, em evento realizado | Só os que criou, em evento realizado | Não | Não |
| Registrar atendimento (fase 3) | Sim, em Atendimento ou Reunião realizados | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado a psicopedagoga, quando cria um evento com todos os campos válidos, então o evento nasce "Agendado", sem aprovação.
- [ ] Dado um professor, quando cria um evento com todos os campos válidos, então o evento nasce "Agendado", sem aprovação.
- [ ] Dado um evento recém-criado, quando o criador consulta os participantes, então ele aparece com a resposta "Confirmada" e os outros com "Sem resposta".
- [ ] Dado um evento criado com alunos no campo "Alunos", quando o criador consulta os participantes, então os alunos escolhidos são participantes.
- [ ] Dado a escolha de um aluno no campo "Participantes", quando o usuário a faz, então o sistema sugere os responsáveis com acesso a esse aluno.
- [ ] Dado a psicopedagoga, quando abre o campo "Tipo", então vê Reunião, Atendimento, Avaliação e Outro.
- [ ] Dado um professor, quando abre o campo "Tipo", então vê Reunião, Avaliação e Outro, e não vê Atendimento.
- [ ] Dado o tipo Atendimento ou Avaliação, quando o criador salva sem alunos, então o sistema não salva e mostra o erro do campo "Alunos".
- [ ] Dado o tipo Reunião ou Outro, quando o criador salva sem alunos, então o evento é salvo.
- [ ] Dado um professor, quando busca alunos para o evento, então só encontra alunos ativos das suas turmas (RG-08).
- [ ] Dado a psicopedagoga, quando busca participantes por nome ou e-mail, então encontra qualquer usuário ativo.
- [ ] Dado um professor, quando busca participantes, então encontra só pessoas com perfil Psicopedagoga, outros professores, alunos das suas turmas e os responsáveis com acesso desses alunos.
- [ ] Dado um título com mais de 100 caracteres, quando o usuário salva, então o sistema não salva e mostra o erro do campo.
- [ ] Dado uma descrição com mais de 2.000 caracteres, quando o usuário salva, então o sistema não salva e mostra o erro do campo.
- [ ] Dado uma data anterior a hoje, quando o usuário salva, então o sistema não salva e mostra o erro do campo.
- [ ] Dado um horário de fim igual ou anterior ao de início, quando o usuário salva, então o sistema não salva e mostra o erro dos horários.
- [ ] Dado anexos fora das regras de RG-16, quando o usuário os envia, então o sistema recusa o arquivo e mostra o erro.
- [ ] Dado um participante com outro evento no mesmo horário, quando o criador salva, então o sistema avisa o conflito e salva o evento.
- [ ] Dado um evento criado, quando o criador salva, então os participantes, menos o criador, recebem a notificação "Evento criado" (RG-25).
- [ ] Dado a psicopedagoga ou o criador, quando edita um evento agendado e futuro, então as alterações são salvas e os participantes são notificados.
- [ ] Dado um evento agendado, quando o criador muda a data ou o horário na edição, então o sistema segue a regra de remarcar e pede o motivo.
- [ ] Dado um evento realizado ou cancelado, quando o usuário o abre, então a tela fica só para leitura, salvo o registro de presença no evento realizado.
- [ ] Dado um professor, quando abre um evento criado por outra pessoa, então não vê as ações editar, remarcar e cancelar.
- [ ] Dado o criador ou a psicopedagoga, quando remarca sem motivo, então o sistema não remarca e mostra o erro do motivo.
- [ ] Dado o criador ou a psicopedagoga, quando remarca com nova data, novo horário e motivo, então o evento continua "Agendado", o histórico mostra a remarcação com o motivo e todas as respostas voltam para "Sem resposta".
- [ ] Dado um evento remarcado, quando a remarcação é salva, então os participantes são notificados com "Evento alterado ou remarcado".
- [ ] Dado um evento agendado com a psicopedagoga e os responsáveis A e B, quando o professor criador inclui o responsável C e retira o B e salva, então C recebe "Evento criado", B recebe "Participante retirado do evento" com título, data e horário, e a psicopedagoga e A recebem "Evento alterado ou remarcado" (RN-21).
- [ ] Dado um evento com dois alunos, quando o responsável de um deles recebe uma notificação do evento, então o texto não cita o nome do outro aluno (RN-17, RG-31).
- [ ] Dado o criador ou a psicopedagoga, quando cancela um evento futuro, então o sistema pede confirmação que diz a ação e a consequência.
- [ ] Dado o criador ou a psicopedagoga, quando confirma o cancelamento com motivo, então o evento fica "Cancelado", o motivo aparece no evento e os participantes recebem a notificação com o motivo.
- [ ] Dado o criador ou a psicopedagoga, quando tenta cancelar sem motivo, então o sistema não cancela e mostra o erro do motivo.
- [ ] Dado um evento que já começou, quando o criador tenta cancelá-lo, então a ação não está disponível.
- [ ] Dado um participante que não é o criador, quando confirma presença, então a resposta fica "Confirmada".
- [ ] Dado um participante que não é o criador, quando recusa presença com ou sem motivo, então a resposta fica "Recusada" e o criador recebe a notificação "Participante recusa presença".
- [ ] Dado um participante que respondeu, quando muda a resposta antes do início do evento, então a nova resposta é salva.
- [ ] Dado um evento que já começou, quando um participante tenta mudar a resposta, então a ação não está disponível.
- [ ] Dado o criador de um evento, quando consulta as ações, então não vê "Confirmar ou recusar presença".
- [ ] Dado um evento a menos de 24 horas do início, quando o sistema envia o lembrete, então só os participantes que não recusaram o recebem.
- [ ] Dado um evento que passou do horário de término, quando o sistema atualiza, então o evento fica "Realizado".
- [ ] Dado um evento realizado, quando o criador ou a psicopedagoga abre o registro de presença, então marca cada participante como "Presente" ou "Faltou".
- [ ] Dado uma presença já registrada, quando o criador ou a psicopedagoga a corrige, então a nova presença é salva.
- [ ] Dado um evento agendado, quando o criador tenta registrar a presença, então a ação não está disponível.
- [ ] Dado um professor que não criou o evento, quando abre o evento realizado, então não registra presença.
- [ ] Dado um Atendimento ou uma Reunião realizados na fase 3, quando a psicopedagoga usa "Registrar atendimento", então o acompanhamento abre com a data, o tipo e o evento preenchidos.
- [ ] Dado um evento do tipo Avaliação ou Outro, ou um evento que ainda não foi realizado, quando a psicopedagoga abre o evento, então não vê "Registrar atendimento".
- [ ] Dado um professor, quando abre um evento realizado, então não vê "Registrar atendimento".
- [ ] Dado a fase 2, quando um evento é aberto, então não aparecem "Registrar atendimento" nem o link para o acompanhamento.
- [ ] Dado um aluno ou um responsável, quando tenta criar, editar, remarcar ou cancelar um evento, então essas ações não estão disponíveis.
- [ ] Dado um aluno ou um responsável e uma Reunião ou um Atendimento agendado e futuro em que o aluno participa, quando abre o evento, então vê "Pedir remarcação" e "Pedir cancelamento".
- [ ] Dado uma Avaliação ou um evento do tipo Outro, ou um evento passado ou cancelado, quando o aluno ou o responsável abre o evento, então não vê "Pedir remarcação" nem "Pedir cancelamento".
- [ ] Dado um evento com um pedido de remarcação ou cancelamento pendente, ou um aluno com 3 pedidos pendentes, quando alguém tenta fazer outro pedido, então valem as regras de T15.
- [ ] Dado um evento criado a partir de um pedido, quando o usuário abre o evento, então vê o link para o pedido de origem.
- [ ] Dado um evento com participantes que o usuário não pode ver, quando abre o evento, então vê os nomes que RG-31 permite e os outros só como quantidade, por exemplo "Mais 2 participantes".
- [ ] Dado um evento alterado, quando o usuário o abre, então vê "Editado em" com a data e o autor da última alteração (RG-15).
- [ ] Dado um evento que não existe ou que o usuário não pode ver, quando tenta abri-lo, então vê "Não encontrado" (RG-13).
- [ ] Dado um formulário com alterações não salvas, quando o usuário tenta sair, então o sistema pede confirmação (RG-29).
- [ ] Dado uma falha ao salvar, quando o usuário tenta salvar, então o sistema mostra o aviso na própria tela e mantém o que foi digitado (RG-29).
- [ ] Dado um aluno inativado com eventos futuros, quando a psicopedagoga escolhe cancelar os eventos futuros, então esses eventos ficam "Cancelados" (T07).
- [ ] Dado um responsável que perde acesso a um aluno, quando o acesso é retirado, então ele sai dos eventos futuros daquele aluno (T07).
- [ ] Dado um evento criado por um membro da equipe inativado e não cancelado, quando qualquer pessoa com o perfil Psicopedagoga o abre, então pode geri-lo.
- [ ] Dado qualquer notificação gerada por uma ação do próprio usuário, quando ela é enviada, então o usuário não a recebe (RG-25).
- [ ] Dado a tela em um celular ou usada só com o teclado, quando o usuário percorre o evento, então consegue usar todas as ações (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
