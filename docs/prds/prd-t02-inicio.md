# PRD da tela de Início

| Campo | Valor |
| --- | --- |
| Identificador | T02 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md), [T03 Notificações](prd-t03-notificacoes.md), [T06 Lista de alunos](prd-t06-lista-de-alunos.md), [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T12 Planejamento semanal](prd-t12-planejamento-semanal.md), [T13 Agenda](prd-t13-agenda.md), [T14 Evento](prd-t14-evento.md), [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md), [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md), [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md), [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1. Cada bloco aparece na fase da tela de onde vêm os dados (ver 6.6). |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que cada perfil veja, logo depois de entrar, o que precisa da atenção dele hoje, para chegar mais rápido à tela onde resolve cada item.

## 2. Escopo

### O que entra no escopo

- Boas-vindas com o nome do usuário e uma frase de Paulo Freire.
- Blocos de resumo diferentes para cada perfil.
- Atalhos para as ações mais usadas do professor e do aluno.
- Escolha do aluno pelo responsável, com cartões quando há mais de um aluno vinculado.
- Aluno escolhido no cabeçalho de todas as telas, com a opção "Trocar aluno".

### O que não entra no escopo

- Lista completa de eventos, pedidos, informações, atividades adaptadas e observações: ficam nas telas de origem de cada bloco (ver 6.6).
- Notificações: ficam em [T03 Notificações](prd-t03-notificacoes.md).
- Criação de usuário, vínculo de responsável e autorização de acesso do responsável de aluno com 18 anos ou mais: ficam em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md).
- Filtros, busca e ordenação escolhidos pelo usuário: o Início não tem.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê pedidos de agendamento pendentes, eventos, eventos realizados sem presença registrada, informações não lidas, atividades adaptadas e observações dos professores dos últimos 7 dias e alunos que completam 18 anos. Abre cada item na tela correspondente. Não tem atalhos de registro. |
| Professor | Vê eventos dos próximos 7 dias, eventos que criou sem presença registrada e os alunos atendidos das suas turmas. Usa os atalhos "Registrar atividade adaptada" e "Registrar observação". Não vê blocos de pedidos, informações nem dados de saúde. |
| Aluno | Vê eventos dos próximos 7 dias, planejamento da semana atual e pedidos pendentes dele. Usa os atalhos "Pedir agendamento" e "Enviar informação". |
| Responsável | Escolhe o aluno e vê o mesmo conteúdo do aluno escolhido, com os mesmos atalhos. Troca de aluno pelo cabeçalho de qualquer tela. |

**Contexto:** o usuário chega aqui logo depois de entrar no sistema, ou quando quer voltar ao ponto de partida. Quer saber o que precisa fazer hoje e abrir o item certo.

**Origem da jornada:** Acesso ao sistema → Início (ou a tela em que estava, RG-28). Depois, Menu → Início, o primeiro item do menu de todos os perfis.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Boas-vindas | Nome do usuário e a frase "A inclusão acontece quando se aprende com as diferenças e com as igualdades!" (Paulo Freire). Aparece para todos os perfis (RN-01). |
| Cabeçalho com o aluno escolhido | Só para o responsável. Mostra o aluno escolhido em todas as telas, com a opção "Trocar aluno" (RN-14). |
| Cartões de alunos | Só para o responsável com mais de um aluno vinculado. Cada cartão mostra foto, nome e turma do aluno, a quantidade de eventos nos próximos 7 dias e a quantidade de pedidos de agendamento pendentes (RN-13). |
| Pedidos de agendamento pendentes (psicopedagoga) | Quantidade total de pedidos com a situação "Pendente" e os 5 mais antigos (RN-06). Origem: [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md). |
| Eventos de hoje e dos próximos 7 dias (psicopedagoga) | Todos os eventos da agenda de hoje e dos próximos 7 dias, não só os criados por ela (RN-19). Origem: [T13 Agenda](prd-t13-agenda.md) e [T14 Evento](prd-t14-evento.md). |
| Eventos realizados sem presença registrada (psicopedagoga) | Eventos com a situação "Realizado" em que há participante com presença "Não registrada". Origem: [T13 Agenda](prd-t13-agenda.md) e [T14 Evento](prd-t14-evento.md). |
| Informações não lidas (psicopedagoga) | Informações com a situação "Não lida". Origem: [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md). |
| Atividades adaptadas dos últimos 7 dias (psicopedagoga) | Atividades adaptadas registradas nos últimos 7 dias. Origem: [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md). |
| Observações dos professores dos últimos 7 dias (psicopedagoga) | Observações do professor registradas nos últimos 7 dias. Origem: [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md). |
| Alunos que completam 18 anos (psicopedagoga) | Alunos com responsável com acesso que completam 18 anos nos próximos 30 dias (RN-07). Origem: [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md). |
| Eventos dos próximos 7 dias (professor, aluno e responsável) | Eventos dos próximos 7 dias. Para o professor, os eventos da agenda dele. Para o aluno e o responsável, os eventos do aluno. Origem: [T13 Agenda](prd-t13-agenda.md) e [T14 Evento](prd-t14-evento.md). |
| Eventos que criou sem presença registrada (professor) | Eventos criados pelo professor, com a situação "Realizado" e participante com presença "Não registrada". Origem: [T13 Agenda](prd-t13-agenda.md) e [T14 Evento](prd-t14-evento.md). |
| Alunos atendidos das suas turmas (professor) | Alunos ativos das turmas em que o professor leciona (RG-08). Cada aluno abre o perfil. Origem: [T06 Lista de alunos](prd-t06-lista-de-alunos.md) e [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md). |
| Planejamento da semana atual (aluno e responsável) | Planejamento semanal confirmado da semana atual do aluno (RN-10). Origem: [T12 Planejamento semanal](prd-t12-planejamento-semanal.md). |
| Pedidos pendentes (aluno e responsável) | Pedidos de agendamento do aluno com a situação "Pendente". Origem: [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md). |
| Atalho "Registrar atividade adaptada" (professor) | Abre o formulário de [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md). |
| Atalho "Registrar observação" (professor) | Abre o formulário de [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md) para um aluno escolhido (ver "Aluno do atalho Registrar observação" em 7.2). |
| Atalho "Pedir agendamento" (aluno e responsável) | Abre o formulário de [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md). |
| Atalho "Enviar informação" (aluno e responsável) | Abre o formulário de [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

Não se aplica. O Início não tem formulário.

### 5.2 Filtros

Não se aplica. O Início não tem filtros (RG-21 não vale aqui).

### 5.3 Ordenação e paginação

- Ordenação padrão: pedidos de agendamento pendentes, do mais antigo para o mais recente. Os outros blocos seguem "Limite e ordem dos itens por bloco" em 7.2.
- Outras ordenações: Não se aplica.
- Paginação: Não se aplica. O Início não mostra listas paginadas (RG-19 não vale aqui).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário entra no sistema.
2. O sistema abre o Início com as boas-vindas e os blocos do perfil dele (RN-01 e RN-02).
3. Se o usuário é responsável, o sistema abre direto o conteúdo do aluno (um aluno vinculado) ou mostra os cartões dos alunos (mais de um). O responsável escolhe um cartão (ver 6.5).
4. O usuário lê os blocos. Cada bloco vazio mostra a própria mensagem (RN-04).
5. O usuário abre um item ou usa um atalho, e o sistema abre a tela correspondente (RN-05).

### 6.2 Fluxos alternativos

- Bloco de uma tela ainda não entregue: o bloco não aparece (RN-03).
- Bloco sem dados: mostra a mensagem própria do bloco (seção 9).
- Acesso encerrado por inatividade: o usuário entra de novo e volta para a tela em que estava (RG-28). O responsável volta com o mesmo aluno escolhido (RN-20).
- Item aberto que o usuário não pode mais ver: abre "Não encontrado" (RG-13).
- Responsável sem nenhum aluno com acesso permitido: a conta fica "Inativo" (seção 6 do índice) e o responsável não entra (RG-05).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Abrir um item de bloco | Todos | Abre a tela de origem do item (RN-05). |
| Usar atalho | Professor, aluno e responsável | Abre o formulário da tela do atalho (RN-09 e RN-10). |
| Escolher um cartão de aluno | Responsável | Abre o Início com o conteúdo do aluno escolhido e define o aluno do cabeçalho (RN-14). |
| Trocar aluno | Responsável com mais de um aluno | Volta para a escolha do aluno e muda o aluno do cabeçalho (RN-14). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Cada bloco vazio mostra a própria mensagem (seção 9). A tela continua mostrando as boas-vindas. |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Todos os perfis acessam esta tela. Item aberto que o usuário não pode ver abre "Não encontrado" (RG-13), conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Abre "Sem conexão" ou "Erro inesperado", conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |

### 6.5 Escolha do aluno pelo responsável

| Situação do responsável | O que acontece |
| --- | --- |
| Um aluno vinculado | O Início abre direto com o conteúdo do aluno (RN-12). |
| Mais de um aluno vinculado | O Início mostra um cartão por aluno (RN-13). Escolher um cartão abre o conteúdo daquele aluno. |
| Depois da escolha | O aluno aparece no cabeçalho de todas as telas, com "Trocar aluno" (RN-14). |
| Telas em que a escolha vale | Perfil do aluno, Agenda, Meus pedidos e Enviar informação (RN-14). |
| Próximo login | A escolha é guardada só até o próximo login. No próximo login, o responsável escolhe de novo (RN-14). |
| Acesso encerrado por inatividade | O responsável entra de novo e volta para a tela em que estava, com o mesmo aluno escolhido (RN-20). |

### 6.6 Entrega por fase

Cada bloco e cada atalho só aparece quando a tela de origem foi entregue (RN-03 e seção 9 do índice).

| Bloco ou atalho | Perfis | Tela de origem | Fase em que aparece |
| --- | --- | --- | --- |
| Boas-vindas | Todos | Esta tela | 1 |
| Cartões de alunos (foto, nome e turma) e escolha do aluno | Responsável | Esta tela | 1 |
| Aluno escolhido no cabeçalho, para o Perfil do aluno | Responsável | Esta tela e [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) | 1 |
| Alunos que completam 18 anos | Psicopedagoga | [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md) | 1 |
| Alunos atendidos das suas turmas | Professor | [T06 Lista de alunos](prd-t06-lista-de-alunos.md) e [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) | 1 |
| Pedidos de agendamento pendentes | Psicopedagoga, aluno e responsável | [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md) | 2 |
| Eventos de hoje e dos próximos 7 dias, ou dos próximos 7 dias | Todos | [T13 Agenda](prd-t13-agenda.md) e [T14 Evento](prd-t14-evento.md) | 2 |
| Eventos realizados sem presença registrada, ou que criou sem presença registrada | Psicopedagoga e professor | [T13 Agenda](prd-t13-agenda.md) e [T14 Evento](prd-t14-evento.md) | 2 |
| Quantidades de eventos e de pedidos pendentes nos cartões | Responsável | [T13 Agenda](prd-t13-agenda.md) e [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md) | 2 |
| Atalho "Pedir agendamento" | Aluno e responsável | [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md) | 2 |
| Aluno escolhido no cabeçalho, para Agenda e Meus pedidos | Responsável | [T13 Agenda](prd-t13-agenda.md) e [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md) | 2 |
| Atividades adaptadas dos últimos 7 dias | Psicopedagoga | [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md) | 3 |
| Observações dos professores dos últimos 7 dias | Psicopedagoga | [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md) | 3 |
| Planejamento da semana atual | Aluno e responsável | [T12 Planejamento semanal](prd-t12-planejamento-semanal.md) | 3 |
| Atalho "Registrar atividade adaptada" | Professor | [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md) | 3 |
| Atalho "Registrar observação" | Professor | [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md) | 3 |
| Informações não lidas | Psicopedagoga | [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) | 4 |
| Atalho "Enviar informação" | Aluno e responsável | [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) | 4 |
| Aluno escolhido no cabeçalho, para Enviar informação | Responsável | [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) | 4 |

O que cada perfil vê em cada fase:

| Fase | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| 1 | Boas-vindas e alunos que completam 18 anos | Boas-vindas e alunos atendidos das suas turmas | Boas-vindas | Boas-vindas, cartões de alunos (foto, nome e turma) e escolha do aluno |
| 2 | Acrescenta pedidos pendentes, eventos e eventos realizados sem presença registrada | Acrescenta eventos dos próximos 7 dias e eventos que criou sem presença registrada | Acrescenta eventos dos próximos 7 dias, pedidos pendentes e o atalho "Pedir agendamento" | Acrescenta o conteúdo do aluno da fase 2 e as quantidades nos cartões |
| 3 | Acrescenta atividades adaptadas e observações dos professores | Acrescenta os atalhos "Registrar atividade adaptada" e "Registrar observação" | Acrescenta planejamento da semana atual | Acrescenta planejamento da semana atual do aluno |
| 4 | Acrescenta informações não lidas | Sem mudança | Acrescenta o atalho "Enviar informação" | Acrescenta o atalho "Enviar informação" |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Todo perfil vê as boas-vindas com o nome do usuário e a frase "A inclusão acontece quando se aprende com as diferenças e com as igualdades!" (Paulo Freire). |
| RN-02 | Cada perfil vê só os blocos do seu perfil, como descrito na seção 4. |
| RN-03 | Cada bloco e cada atalho só aparece quando a tela de onde vêm os dados já foi entregue (ver 6.6). |
| RN-04 | Cada bloco vazio mostra uma mensagem própria, por exemplo "Nenhum evento nos próximos 7 dias" (seção 9). |
| RN-05 | Cada item de um bloco abre a tela correspondente, que é a tela de origem do bloco (ver 6.6). |
| RN-06 | O bloco de pedidos de agendamento pendentes da psicopedagoga mostra a quantidade de pedidos e os 5 mais antigos. |
| RN-07 | O bloco de 18 anos lista os alunos com responsável com acesso que completam 18 anos nos próximos 30 dias. Ele acompanha a notificação "Aluno com responsável com acesso completa 18 anos em 30 dias" (seção 7 do índice). O responsável de aluno com 18 anos ou mais só mantém acesso com a autorização do aluno, registrada pela psicopedagoga (RG-17). |
| RN-08 | O bloco de atividades adaptadas e o de observações dos professores da psicopedagoga mostram os registros dos últimos 7 dias. |
| RN-09 | O professor vê só os alunos ativos das suas turmas (RG-08) e só eventos que a agenda permite a ele ([T13 Agenda](prd-t13-agenda.md)). Os atalhos dele são "Registrar atividade adaptada" e "Registrar observação". |
| RN-10 | O aluno vê só o planejamento semanal confirmado (seção 6 do índice). Os atalhos dele são "Pedir agendamento" e "Enviar informação". |
| RN-11 | O Início do responsável mostra o conteúdo do aluno escolhido, o mesmo do aluno (RN-10), inclusive os atalhos "Pedir agendamento" e "Enviar informação". |
| RN-12 | Com um aluno vinculado, o Início do responsável abre direto com ele. |
| RN-13 | Com mais de um aluno vinculado, o Início do responsável mostra um cartão por aluno, com foto, nome, turma, quantidade de eventos nos próximos 7 dias e quantidade de pedidos pendentes. Escolher um cartão abre o conteúdo daquele aluno. |
| RN-14 | O aluno escolhido aparece no cabeçalho de todas as telas, com a opção "Trocar aluno". A escolha vale para Perfil do aluno, Agenda, Meus pedidos e Enviar informação e fica guardada até o próximo login. |
| RN-15 | O responsável vê só os alunos vinculados a ele (RG-09). Aluno com 18 anos ou mais só aparece para o responsável com autorização do aluno (RG-17). |
| RN-16 | Os eventos mostrados seguem RG-31: cada usuário vê pelo nome só os participantes que pode ver. |
| RN-17 | "Início" é o primeiro item do menu de todos os perfis. Depois de entrar, o usuário vai para o Início ou para a tela em que estava. |
| RN-18 | Segue RG-07, RG-13, RG-18, RG-26 e RG-28. A psicopedagoga vê todos os alunos, ativos e inativos (RG-07). |
| RN-19 | O bloco de eventos da psicopedagoga mostra todos os eventos da agenda, não só os que ela criou ou de que participa. |
| RN-20 | Quando o acesso do responsável é encerrado por inatividade (RG-28), ele entra de novo e volta para a tela em que estava, com o mesmo aluno escolhido. Nos outros logins, ele escolhe o aluno de novo (RN-14). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Alunos nos cartões do responsável | Os cartões mostram só alunos ativos e com acesso permitido ao responsável. |
| Limite e ordem dos itens por bloco | Cada bloco mostra até 5 itens. Eventos e planejamento do mais próximo ao mais distante. Eventos sem presença e informações não lidas do mais antigo para o mais recente. Atividades adaptadas e observações do mais recente para o mais antigo. |
| Aluno do atalho Registrar observação | O formulário de observação não tem campo "Aluno". Ao usar o atalho, o professor escolhe antes um aluno atendido das suas turmas. |
| Ordem dos blocos | Os blocos aparecem na ordem em que estão listados na seção 4 para cada perfil, abaixo das boas-vindas. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

Não se aplica. O Início não gera notificações. O bloco de alunos que completam 18 anos acompanha uma notificação definida na seção 7 do índice (RN-07).

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Frase de boas-vindas | Aviso | A inclusão acontece quando se aprende com as diferenças e com as igualdades! (Paulo Freire) |
| Boas-vindas ao usuário | Aviso | Boas-vindas, [nome do usuário] (proposta) |
| Bloco de eventos vazio | Aviso | Nenhum evento nos próximos 7 dias |
| Bloco de pedidos pendentes vazio | Aviso | Nenhum pedido de agendamento pendente (proposta) |
| Bloco de eventos sem presença vazio | Aviso | Nenhum evento sem presença registrada (proposta) |
| Bloco de informações não lidas vazio | Aviso | Nenhuma informação não lida (proposta) |
| Bloco de atividades adaptadas vazio | Aviso | Nenhuma atividade adaptada nos últimos 7 dias (proposta) |
| Bloco de observações dos professores vazio | Aviso | Nenhuma observação dos professores nos últimos 7 dias (proposta) |
| Bloco de 18 anos vazio | Aviso | Nenhum aluno completa 18 anos nos próximos 30 dias (proposta) |
| Bloco de alunos atendidos vazio | Aviso | Nenhum aluno atendido nas suas turmas (proposta) |
| Bloco de planejamento vazio | Aviso | Nenhum planejamento confirmado para esta semana (proposta) |
| Bloco de pedidos pendentes do aluno vazio | Aviso | Nenhum pedido pendente (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Abrir o Início | Sim | Sim | Sim | Sim |
| Ver pedidos de agendamento pendentes | Sim, de todos os alunos | Não | Só os do aluno | Só os do aluno escolhido |
| Ver eventos | Sim | Só os que a agenda permite | Só os próprios | Só os do aluno escolhido |
| Ver eventos realizados sem presença registrada | Sim | Só os que criou | Não | Não |
| Ver informações não lidas | Sim | Não | Não | Não |
| Ver atividades adaptadas e observações dos últimos 7 dias | Sim | Não | Não | Não |
| Ver alunos que completam 18 anos | Sim | Não | Não | Não |
| Ver alunos atendidos das suas turmas | Não | Só alunos das suas turmas | Não | Não |
| Ver planejamento da semana atual | Não | Não | Só o próprio, confirmado | Só o do aluno escolhido, confirmado |
| Usar os atalhos "Registrar atividade adaptada" e "Registrar observação" | Não | Sim | Não | Não |
| Usar os atalhos "Pedir agendamento" e "Enviar informação" | Não | Não | Sim | Sim, para o aluno escolhido |
| Escolher aluno e usar "Trocar aluno" | Não | Não | Não | Sim |

## 11. Critérios de aceite

- [ ] Dado que um usuário de qualquer perfil entrou no sistema, quando o Início abre, então ele vê as boas-vindas com o próprio nome e a frase "A inclusão acontece quando se aprende com as diferenças e com as igualdades!" (Paulo Freire) (RN-01).
- [ ] Dado que o usuário informou e-mail e senha corretos, quando o acesso termina, então ele vai para o Início, ou para a tela em que estava (RN-17, RG-28).
- [ ] Dado um usuário de qualquer perfil, quando abre o menu, então "Início" é o primeiro item (RN-17).
- [ ] Dado um perfil, quando o Início abre, então ele vê só os blocos do seu perfil (RN-02).
- [ ] Dado que a tela de origem de um bloco ainda não foi entregue, quando o Início abre, então o bloco e o atalho dessa tela não aparecem (RN-03).
- [ ] Dado um bloco sem dados, quando o Início abre, então o bloco mostra a própria mensagem, por exemplo "Nenhum evento nos próximos 7 dias" (RN-04).
- [ ] Dado um item em qualquer bloco, quando o usuário o abre, então o sistema abre a tela correspondente (RN-05).
- [ ] Dado que a psicopedagoga tem 8 pedidos pendentes, quando abre o Início, então vê a quantidade 8 e os 5 pedidos mais antigos (RN-06).
- [ ] Dado que a psicopedagoga abre o Início, quando há eventos hoje e nos próximos 7 dias, então vê esses eventos, e os participantes aparecem conforme RG-31 (RN-16).
- [ ] Dado um evento de amanhã criado por um professor, sem a psicopedagoga como participante, quando ela abre o Início, então o evento aparece no bloco de eventos (RN-19).
- [ ] Dado um evento "Realizado" com participante de presença "Não registrada", quando a psicopedagoga abre o Início, então o evento aparece no bloco de eventos realizados sem presença registrada.
- [ ] Dado uma informação "Não lida", quando a psicopedagoga abre o Início, então a informação aparece no bloco de informações não lidas.
- [ ] Dado atividades adaptadas e observações registradas nos últimos 7 dias, quando a psicopedagoga abre o Início, então os blocos mostram esses registros (RN-08).
- [ ] Dado um aluno com responsável com acesso que completa 18 anos em 05/11/2026, quando a psicopedagoga abre o Início em 17/10/2026, então o aluno aparece no bloco de 18 anos (RN-07).
- [ ] Dado um aluno inativo, quando a psicopedagoga abre o Início, então os dados dele aparecem nos blocos, porque a psicopedagoga vê alunos ativos e inativos (RN-18, RG-07).
- [ ] Dado um professor que leciona em duas turmas, quando abre o Início, então vê só os alunos ativos dessas turmas no bloco de alunos atendidos (RN-09, RG-08).
- [ ] Dado um evento criado pelo professor, com situação "Realizado" e presença "Não registrada", quando o professor abre o Início, então o evento aparece no bloco de eventos que criou sem presença registrada.
- [ ] Dado um evento criado por outra pessoa, com presença "Não registrada", quando o professor abre o Início, então o evento não aparece no bloco de eventos sem presença registrada (RN-09).
- [ ] Dado um professor, quando abre o Início, então vê os atalhos "Registrar atividade adaptada" e "Registrar observação", e não vê blocos de pedidos nem de informações (RN-09).
- [ ] Dado um aluno, quando abre o Início, então vê eventos dos próximos 7 dias, planejamento da semana atual, pedidos pendentes e os atalhos "Pedir agendamento" e "Enviar informação" (RN-10).
- [ ] Dado um planejamento semanal em "Rascunho", quando o aluno abre o Início, então o planejamento não aparece (RN-10).
- [ ] Dado um responsável com um aluno vinculado, quando abre o Início, então o Início abre direto com o conteúdo do aluno (RN-12).
- [ ] Dado um responsável com três alunos vinculados, quando abre o Início, então vê três cartões, cada um com foto, nome, turma, quantidade de eventos nos próximos 7 dias e quantidade de pedidos pendentes (RN-13).
- [ ] Dado os cartões dos alunos, quando o responsável escolhe um cartão, então o Início mostra o conteúdo do aluno escolhido (RN-11, RN-13).
- [ ] Dado um aluno escolhido, quando o responsável abre qualquer tela, então o cabeçalho mostra o aluno escolhido com a opção "Trocar aluno" (RN-14).
- [ ] Dado um aluno escolhido, quando o responsável abre Perfil do aluno, Agenda, Meus pedidos ou Enviar informação, então a tela mostra os dados do aluno escolhido (RN-14).
- [ ] Dado um aluno escolhido, quando o responsável entra no sistema no próximo login, então escolhe o aluno de novo (RN-14).
- [ ] Dado um responsável com o aluno escolhido aberto na Agenda, quando o acesso é encerrado por inatividade e ele entra de novo, então volta para a Agenda com o mesmo aluno escolhido, sem passar pelos cartões (RN-20, RG-28).
- [ ] Dado um aluno com 18 anos ou mais sem autorização para o responsável, quando o responsável abre o Início, então o aluno não aparece nos cartões (RN-15, RG-17).
- [ ] Dado um responsável com acesso a um aluno e sem vínculo com outro, quando abre o Início, então só o aluno vinculado aparece (RN-15, RG-09).
- [ ] Dado que a tela de origem de um bloco é da fase 3, quando só as fases 1 e 2 foram entregues, então o bloco não aparece para nenhum perfil (6.6).
- [ ] Dado um usuário que abre um item que não pode ver, quando o item abre, então o sistema mostra "Não encontrado" (RG-13).
- [ ] Dado um usuário que usa o Início no celular, quando abre a tela, então todos os blocos e atalhos funcionam também só com o teclado (RG-26).
- [ ] Dado que a conexão caiu, quando o Início abre, então o sistema mostra "Sem conexão", conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
