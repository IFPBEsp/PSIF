# PRD da tela de Perfil do aluno

| Campo | Valor |
| --- | --- |
| Identificador | T08 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T03 Notificações](prd-t03-notificacoes.md), [T06 Lista de alunos](prd-t06-lista-de-alunos.md), [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T09 Dados de saúde](prd-t09-dados-de-saude.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md), [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md), [T12 Planejamento semanal](prd-t12-planejamento-semanal.md), [T13 Agenda](prd-t13-agenda.md), [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md), [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md), [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md), [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md), [T19 Turmas](prd-t19-turmas.md), [T22 Dificuldades](prd-t22-dificuldades.md), [T24 Formulários](prd-t24-formularios.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Reunir em um lugar tudo o que cada perfil pode ver sobre um aluno, para que a psicopedagoga, o professor, o aluno e o responsável consultem as informações certas sem procurar em várias telas.

## 2. Escopo

### O que entra no escopo

- Mostrar o cabeçalho do aluno em todas as abas.
- Mostrar as abas que o perfil pode ver e abrir a aba "Dados pessoais e escolares" por padrão.
- Mostrar, na aba "Dados pessoais e escolares", os dados pessoais, os dados escolares, as dificuldades com a descrição e os responsáveis.
- Oferecer as ações do cabeçalho de cada perfil.
- Mostrar o aviso "Aluno inativo" para a psicopedagoga.
- Servir de "Meu perfil" para o aluno e de "Perfil do aluno" para o responsável.

### O que não entra no escopo

- Editar os dados do aluno: fica em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md). O botão "Editar" só abre aquele formulário.
- O conteúdo das outras abas: cada aba abre o conteúdo da tela indicada no quadro de abas da seção 4.
- Registrar acompanhamento, atividade adaptada, observação, pedido de agendamento e informação: ficam nas telas de destino de cada ação (seção 6.3).
- Escolher o aluno, no caso do responsável com mais de um aluno: fica no [T02 Início](prd-t02-inicio.md). Aqui só existe a opção "Trocar aluno" no cabeçalho.
- Imprimir documentos em branco ou preenchidos do atendimento: fica em [T24 Formulários](prd-t24-formularios.md). O botão "Imprimir ficha" daqui funciona desde a fase 1, sem depender daquela tela (RG-30).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê o perfil de qualquer aluno, ativo ou inativo (RG-07), com todas as abas. Pode editar, imprimir a ficha e registrar acompanhamento. |
| Professor | Vê o perfil só de alunos ativos das suas turmas (RG-08). Na aba de dados vê só o básico (RG-11), sem a idade. Vê as abas Características, Orientações, Atividades adaptadas, Agenda do aluno (conforme [T13 Agenda](prd-t13-agenda.md)) e as próprias Observações dos professores. Pode registrar atividade adaptada e observação. |
| Aluno | Vê só o próprio perfil, chamado "Meu perfil" (RG-09). Pode pedir agendamento e enviar informação. |
| Responsável | Vê só o perfil dos alunos vinculados a ele (RG-09). Para aluno com 18 anos ou mais, só com autorização registrada (RG-17). Pode pedir agendamento e enviar informação em nome do aluno. |

**Contexto:** a psicopedagoga e o professor chegam para consultar o aluno antes de atender, adaptar uma atividade ou registrar algo. O aluno e o responsável chegam para conferir os dados e acompanhar o atendimento.

**Origem da jornada:** a psicopedagoga e o professor chegam por Menu "Alunos" → [T06 Lista de alunos](prd-t06-lista-de-alunos.md), por [T19 Turmas](prd-t19-turmas.md), pelo [T02 Início](prd-t02-inicio.md) ou por notificações ([T03 Notificações](prd-t03-notificacoes.md)). O aluno chega pelo item de menu "Meu perfil". O responsável chega pelo item de menu "Perfil do aluno", do aluno escolhido, e troca de aluno pelo "Trocar aluno" no cabeçalho.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Cabeçalho | Presente em todas as abas: foto, nome, idade, curso, série, turma, dificuldades e situação. O professor não vê a idade (RG-11). |
| Aviso "Aluno inativo" | Aparece no cabeçalho de aluno inativo. Só a psicopedagoga acessa o perfil de aluno inativo (RN-05). |
| Trocar aluno | Opção do cabeçalho para o responsável com mais de um aluno vinculado ([T02 Início](prd-t02-inicio.md)). |
| Ações do cabeçalho | Variam por perfil (seção 6.3). |
| Abas | Cada perfil vê só as abas permitidas, no quadro abaixo. Abas sem permissão não aparecem (RN-03). |
| Aba "Dados pessoais e escolares" | Dados pessoais, dados escolares, dificuldades com a descrição de cada uma e responsáveis (RN-07). É a aba aberta por padrão. |

**Abas e quem vê cada uma**

| Aba | Psicopedagoga | Professor | Aluno | Responsável | Tela |
| --- | --- | --- | --- | --- | --- |
| Dados pessoais e escolares | Sim | Só o básico (RG-11) | Sim | Sim | T08 |
| Dados de saúde | Sim | Não | Não | Não | [T09 Dados de saúde](prd-t09-dados-de-saude.md) |
| Acompanhamentos | Sim | Não | Só os marcados como visíveis | Só os marcados como visíveis | [T10 Acompanhamentos](prd-t10-acompanhamentos.md) |
| Características | Sim | Sim | Não | Não | [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md) |
| Orientações | Sim | Sim | Não | Não | [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md) |
| Planejamento semanal | Sim | Não | Sim | Sim | [T12 Planejamento semanal](prd-t12-planejamento-semanal.md) |
| Agenda do aluno | Sim | Conforme T13 | Sim | Sim | [T13 Agenda](prd-t13-agenda.md) |
| Atividades adaptadas | Sim | Sim | Sim | Sim | [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md) |
| Observações dos professores | Sim | Só as próprias | Não | Não | [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md) |
| Informações enviadas | Sim | Não | Só as que enviou | Só as que enviou | [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) |

Dados de saúde seguem RG-10. Os anexos de cada aba seguem a visibilidade do registro a que pertencem (RG-12).

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

Não se aplica. A tela só mostra dados. A edição é feita em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md).

### 5.2 Filtros

Não se aplica. A aba "Agenda do aluno" abre a agenda já filtrada para o aluno ([T13 Agenda](prd-t13-agenda.md)).

### 5.3 Ordenação e paginação

- Ordenação padrão: Não se aplica.
- Outras ordenações: Não se aplica.
- Paginação: Não se aplica. Listas dentro de cada aba seguem a tela da aba.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário abre o perfil de um aluno pela lista, por uma turma, pelo Início, por uma notificação ou pelo menu.
2. O sistema mostra o cabeçalho do aluno e as abas permitidas ao perfil do usuário.
3. O sistema abre a aba "Dados pessoais e escolares".
4. O usuário muda de aba. O cabeçalho continua visível em todas.
5. O usuário usa uma ação do cabeçalho. O sistema abre a tela de destino da ação (seção 6.3).

### 6.2 Fluxos alternativos

- Aluno inativo, usuário psicopedagoga: o perfil abre com o aviso "Aluno inativo".
- Aluno inativo, usuário de outro perfil: abre "Não encontrado" (RG-13).
- Aluno fora das turmas do professor, não vinculado ao responsável, ou que não é o próprio aluno: abre "Não encontrado" (RG-13).
- Responsável de aluno com 18 anos ou mais sem autorização registrada: abre "Não encontrado" (RG-13, RN-06).
- Aba cuja tela ainda não foi entregue: a aba não aparece (seção 6.5).
- Professor que perdeu o acesso por mudança de turma do aluno: abre "Não encontrado" (RG-08, RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Mudar de aba | Todos, nas abas permitidas | Abre o conteúdo da aba. O cabeçalho continua. |
| Editar | Psicopedagoga | Abre o [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md) com os dados do aluno. |
| Imprimir ficha | Psicopedagoga | Imprime a ficha do aluno na versão impressa padrão, com o conteúdo de RN-17 e a marcação "Documento confidencial" (RG-30). A impressão fica registrada com quem imprimiu, quando e o quê. |
| Registrar acompanhamento | Psicopedagoga | Abre o registro em [T10 Acompanhamentos](prd-t10-acompanhamentos.md) para este aluno. |
| Registrar atividade adaptada | Professor | Abre o registro em [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md) para este aluno. |
| Registrar observação | Professor | Abre o registro em [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md) para este aluno. |
| Pedir agendamento | Aluno, Responsável | Abre o pedido em [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md) para este aluno. |
| Enviar informação | Aluno, Responsável | Abre o envio em [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md). |
| Trocar aluno | Responsável com mais de um aluno | Troca o aluno mostrado, como em [T02 Início](prd-t02-inicio.md). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Não se aplica. O perfil sempre tem os dados do aluno. Aluno sem responsável e aba sem registros seguem 7.2 e a tela da aba. |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Aluno que o usuário não pode ver abre "Não encontrado" (RG-13). "Acesso negado" não se aplica, porque todos os perfis usam esta tela. As telas estão em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Falha de conexão abre "Sem conexão" e falha inesperada abre "Erro inesperado", em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). A mensagem diz o que aconteceu e o que fazer (RG-24). |

### 6.5 Entrega por fase

A aba ou a ação que depende de outra tela só aparece quando essa tela for entregue (seção 9 do índice). O perfil é entregue na fase 1 e ganha abas e ações nas fases seguintes.

| Fase | Abas que passam a aparecer | Ações que passam a aparecer |
| --- | --- | --- |
| 1 | Dados pessoais e escolares ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). Características e Orientações ([T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md)). | Editar ([T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md)). Imprimir ficha. Trocar aluno. |
| 2 | Agenda do aluno ([T13 Agenda](prd-t13-agenda.md)). | Pedir agendamento ([T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md)). |
| 3 | Dados de saúde ([T09 Dados de saúde](prd-t09-dados-de-saude.md)). Acompanhamentos ([T10 Acompanhamentos](prd-t10-acompanhamentos.md)). Planejamento semanal ([T12 Planejamento semanal](prd-t12-planejamento-semanal.md)). Atividades adaptadas ([T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md)). Observações dos professores ([T17 Observações dos professores](prd-t17-observacoes-dos-professores.md)). | Registrar acompanhamento. Registrar atividade adaptada. Registrar observação. |
| 4 | Informações enviadas ([T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md)). | Enviar informação. |

Efeito por perfil na fase 1:

| Perfil | O que vê na fase 1 |
| --- | --- |
| Psicopedagoga | Abas "Dados pessoais e escolares", "Características" e "Orientações". Ações "Editar" e "Imprimir ficha". |
| Professor | Abas "Dados pessoais e escolares" (só o básico), "Características" e "Orientações". Sem ações no cabeçalho, porque as telas das ações chegam na fase 3. |
| Aluno | Aba "Dados pessoais e escolares". Sem ações no cabeçalho. |
| Responsável | Aba "Dados pessoais e escolares". "Trocar aluno" quando tem mais de um aluno. Sem outras ações no cabeçalho. |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-07 a RG-13, RG-17 e RG-30. |
| RN-02 | O cabeçalho aparece em todas as abas e mostra foto, nome, idade, curso, série, turma, dificuldades e situação. O professor não vê a idade (RG-11). |
| RN-03 | A aba aberta por padrão é "Dados pessoais e escolares". Abas sem permissão não aparecem. |
| RN-04 | Cada aba só aparece quando a tela correspondente já foi entregue (seção 6.5). A ação do cabeçalho que depende de uma tela segue a mesma regra. |
| RN-05 | Aluno inativo mostra o aviso "Aluno inativo" e só a psicopedagoga acessa o perfil. Para os outros perfis, abre "Não encontrado" (RG-13). |
| RN-06 | O responsável só acessa o perfil de aluno com 18 anos ou mais se houver autorização registrada (RG-17). Sem a autorização, abre "Não encontrado" (RG-13). |
| RN-07 | A aba "Dados pessoais e escolares" mostra dados pessoais, dados escolares, dificuldades com a descrição de cada uma e responsáveis. |
| RN-08 | O professor vê na aba de dados só nome, foto, turma e dificuldades com o nome e a descrição de cada uma. Nunca vê dados de saúde, contatos, endereço ou data de nascimento (RG-11). As dificuldades e as descrições são as do catálogo ([T22 Dificuldades](prd-t22-dificuldades.md)). |
| RN-09 | Dados de saúde são vistos só pela psicopedagoga (RG-10). Acompanhamentos para aluno e responsável são só os marcados como visíveis. |
| RN-10 | A aba Observações dos professores mostra ao professor só as próprias observações. |
| RN-11 | Aluno e responsável veem na aba Informações enviadas só as informações que enviaram. |
| RN-12 | A aba Agenda do aluno é a agenda filtrada para o aluno, e o professor a vê conforme [T13 Agenda](prd-t13-agenda.md). |
| RN-13 | O professor perde o acesso ao aluno quando o aluno muda para uma turma em que ele não leciona (RG-08). |
| RN-14 | Imprimir ficha usa a versão impressa padrão desde a fase 1. Impressão de documento preenchido fica registrada com quem imprimiu, quando e o quê (RG-30). |
| RN-15 | Cada perfil tem as ações do cabeçalho da seção 6.3. Psicopedagoga: editar, imprimir ficha e registrar acompanhamento. Professor: registrar atividade adaptada e registrar observação. Aluno e responsável: pedir agendamento e enviar informação. |
| RN-16 | Para o aluno, a tela se chama "Meu perfil". Para o responsável, "Perfil do aluno", do aluno escolhido (menu, seção 8 do índice). |
| RN-17 | A ficha impressa traz o cabeçalho e o conteúdo da aba "Dados pessoais e escolares", na versão impressa padrão (nome do campus, nome do sistema e data de impressão). Não traz dados de saúde. A ficha leva a marcação "Documento confidencial", por conter dados pessoais do aluno (RG-30). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Dados da aba para aluno e responsável | O aluno vê todos os próprios dados pessoais e escolares, inclusive o e-mail acadêmico, e os responsáveis com nome, parentesco e telefone. O responsável vê os dados pessoais e escolares do aluno e, dos responsáveis, só nome e parentesco. Telefone e e-mail de outro responsável não aparecem para ele. |
| Histórico de turmas e de responsáveis | A psicopedagoga vê, na aba de dados, o histórico de turmas anteriores e dos responsáveis desvinculados. Os outros perfis não veem. |
| Responsável com aluno inativo ou sem autorização | O aluno não aparece nos cartões de escolha de aluno do responsável no Início. |
| Foto ausente | Aluno sem foto mostra um círculo com as iniciais do nome. |
| Dificuldades no cabeçalho | O cabeçalho mostra o nome de todas as dificuldades, separadas por vírgula. Aluno sem dificuldade mostra "Em avaliação", como na [T06 Lista de alunos](prd-t06-lista-de-alunos.md). |
| Aluno sem responsável | A seção "Responsáveis" mostra "Nenhum responsável cadastrado." |
| Cálculo da idade | A idade conta anos completos pela data de nascimento, no horário de Brasília. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

Não se aplica. Esta tela não gera notificações. As ações do cabeçalho levam a telas que geram as suas próprias notificações.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Aluno inativo (só a psicopedagoga vê o perfil) | Aviso | Aluno inativo |
| Aluno sem responsável | Aviso | Nenhum responsável cadastrado. (proposta) |
| Ficha impressa | Sucesso | Ficha enviada para impressão. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Abrir o perfil | Sim | Só alunos ativos das suas turmas | Só o próprio | Só os alunos vinculados, e os de 18 anos ou mais só com autorização |
| Abrir o perfil de aluno inativo | Sim | Não | Não | Não |
| Ver a idade no cabeçalho | Sim | Não | Sim | Sim |
| Aba Dados pessoais e escolares | Sim | Só o básico | Sim | Sim |
| Aba Dados de saúde | Sim | Não | Não | Não |
| Aba Acompanhamentos | Sim | Não | Só os marcados como visíveis | Só os marcados como visíveis |
| Abas Características e Orientações | Sim | Sim | Não | Não |
| Aba Planejamento semanal | Sim | Não | Sim | Sim |
| Aba Agenda do aluno | Sim | Conforme T13 | Sim | Sim |
| Aba Atividades adaptadas | Sim | Sim | Sim | Sim |
| Aba Observações dos professores | Sim | Só as próprias | Não | Não |
| Aba Informações enviadas | Sim | Não | Só as que enviou | Só as que enviou |
| Editar | Sim | Não | Não | Não |
| Imprimir ficha | Sim | Não | Não | Não |
| Registrar acompanhamento | Sim | Não | Não | Não |
| Registrar atividade adaptada | Não | Só alunos das suas turmas | Não | Não |
| Registrar observação | Não | Só alunos das suas turmas | Não | Não |
| Pedir agendamento | Não | Não | Só para si | Só para o aluno vinculado |
| Enviar informação | Não | Não | Só para si | Só para o aluno vinculado |

## 11. Critérios de aceite

- [ ] Dado que o usuário tem permissão para ver o aluno, quando abre o perfil, então o sistema mostra o cabeçalho com foto, nome, idade, curso, série, turma, dificuldades e situação (RN-02).
- [ ] Dado que o usuário está em qualquer aba, quando muda de aba, então o cabeçalho continua visível (RN-02).
- [ ] Dado que o usuário abre o perfil, quando a tela carrega, então a aba aberta é "Dados pessoais e escolares" (RN-03).
- [ ] Dado que a psicopedagoga abre o perfil, quando vê a aba "Dados pessoais e escolares", então aparecem dados pessoais, dados escolares, dificuldades com a descrição de cada uma e responsáveis (RN-07).
- [ ] Dado que o usuário abre o perfil, quando o perfil dele não tem permissão para uma aba, então a aba não aparece (RN-03).
- [ ] Dado que a fase 1 está entregue e a fase 3 não, quando o aluno abre "Meu perfil", então só vê a aba "Dados pessoais e escolares" (RN-04).
- [ ] Dado que a tela T12 foi entregue, quando o aluno abre "Meu perfil", então aparece a aba "Planejamento semanal" (RN-04).
- [ ] Dado que a fase 2 ainda não foi entregue, quando o aluno abre "Meu perfil", então a aba "Agenda do aluno" e a ação "Pedir agendamento" não aparecem (RN-04).
- [ ] Dado que a fase 4 ainda não foi entregue, quando o aluno abre o perfil, então a ação "Enviar informação" e a aba "Informações enviadas" não aparecem (RN-04).
- [ ] Dado que o professor abre o perfil de um aluno ativo da sua turma, quando vê o cabeçalho, então a idade não aparece (RN-02, RG-11).
- [ ] Dado que o professor abre a aba "Dados pessoais e escolares", quando vê o conteúdo, então aparecem só nome, foto, turma e dificuldades com nome e descrição, sem contatos, endereço nem data de nascimento (RN-08, RG-11).
- [ ] Dado que o professor abre o perfil, quando vê as abas, então aparecem "Dados pessoais e escolares", "Características", "Orientações", "Atividades adaptadas", "Agenda do aluno" conforme T13 e "Observações dos professores" só com as próprias, e não aparecem "Dados de saúde", "Acompanhamentos", "Planejamento semanal" nem "Informações enviadas" (seção 4).
- [ ] Dado que o professor abre a aba "Observações dos professores", quando a lista aparece, então mostra só as observações que ele registrou (RN-10).
- [ ] Dado que o aluno abre "Meu perfil", quando vê as abas, então aparecem "Dados pessoais e escolares", "Planejamento semanal", "Agenda do aluno", "Atividades adaptadas", "Acompanhamentos" só com os marcados como visíveis e "Informações enviadas" só com as que enviou (seção 4, RN-09, RN-11).
- [ ] Dado que o responsável abre o perfil de um aluno vinculado, quando vê as abas, então aparecem as mesmas abas do aluno (seção 4).
- [ ] Dado que o usuário é aluno ou responsável, quando abre a aba "Acompanhamentos", então vê só os acompanhamentos marcados como visíveis para a família (RN-09, RG-10).
- [ ] Dado que o usuário não é a psicopedagoga, quando abre o perfil, então a aba "Dados de saúde" não aparece (RN-09, RG-10).
- [ ] Dado que um aluno está inativo, quando a psicopedagoga abre o perfil, então ele abre com o aviso "Aluno inativo" (RN-05).
- [ ] Dado que um aluno está inativo, quando o professor ou o responsável tenta abrir o perfil, então abre "Não encontrado" (RN-05, RG-13).
- [ ] Dado que o aluno tem 18 anos ou mais e não há autorização registrada, quando o responsável tenta abrir o perfil, então abre "Não encontrado" (RN-06, RG-17).
- [ ] Dado que o aluno tem 18 anos ou mais e há autorização registrada, quando o responsável abre o perfil, então o perfil abre (RN-06).
- [ ] Dado que o aluno tem menos de 18 anos, quando o responsável vinculado abre o perfil, então o perfil abre (RG-17).
- [ ] Dado que o aluno mudou para uma turma em que o professor não leciona, quando o professor tenta abrir o perfil, então abre "Não encontrado" (RN-13, RG-08).
- [ ] Dado que o aluno não existe ou que o usuário não pode vê-lo, quando o usuário tenta abri-lo, então aparece a mesma tela "Não encontrado" nos dois casos (RG-13).
- [ ] Dado que o usuário tem o perfil Aluno, quando tenta abrir o perfil de outro aluno, então abre "Não encontrado" (RG-09, RG-13).
- [ ] Dado que o responsável tem dois alunos vinculados, quando escolhe "Trocar aluno" no cabeçalho, então o perfil mostra o outro aluno (RN-16).
- [ ] Dado que o usuário é aluno, quando abre o menu, então o item que leva ao perfil se chama "Meu perfil" (RN-16).
- [ ] Dado que o usuário é responsável, quando abre o menu, então o item que leva ao perfil se chama "Perfil do aluno" (RN-16).
- [ ] Dado que a psicopedagoga está no perfil, quando escolhe "Editar", então abre o [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md) com os dados do aluno (RN-15).
- [ ] Dado que a psicopedagoga está no perfil, quando escolhe "Imprimir ficha", então a ficha é impressa na versão impressa padrão e a impressão fica registrada com quem imprimiu, quando e o quê (RN-14, RG-30).
- [ ] Dado um aluno com diagnóstico registrado, quando a psicopedagoga imprime a ficha, então a ficha traz o cabeçalho e os dados pessoais e escolares, não traz dados de saúde e leva a marcação "Documento confidencial" (RN-17).
- [ ] Dado que a psicopedagoga está no perfil, quando escolhe "Registrar acompanhamento", então abre o registro de acompanhamento para o aluno (RN-15).
- [ ] Dado que o professor está no perfil de um aluno da sua turma, quando escolhe "Registrar atividade adaptada" ou "Registrar observação", então abre o registro correspondente para o aluno (RN-15).
- [ ] Dado que o aluno ou o responsável está no perfil, quando escolhe "Pedir agendamento" ou "Enviar informação", então abre a tela de destino para o aluno (RN-15).
- [ ] Dado que o usuário não tem permissão para uma ação, quando abre o perfil, então a ação não aparece no cabeçalho (RN-15).
- [ ] Dado que o sistema perdeu a conexão ou ocorreu uma falha inesperada, quando o perfil é aberto, então abre "Sem conexão" ou "Erro inesperado", com orientação do que fazer (RG-24).
- [ ] Dado que o perfil é aberto no celular, quando o usuário navega só com o teclado, então consegue trocar de aba e usar as ações do cabeçalho (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
