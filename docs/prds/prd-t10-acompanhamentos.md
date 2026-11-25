# PRD da tela de Acompanhamentos

| Campo | Valor |
| --- | --- |
| Identificador | T10 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Aluno, Responsável |
| Telas relacionadas | [T03 Notificações](prd-t03-notificacoes.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T09 Dados de saúde](prd-t09-dados-de-saude.md), [T14 Evento](prd-t14-evento.md), [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md), [T24 Formulários](prd-t24-formularios.md), [T25 Busca no acervo](prd-t25-busca-no-acervo.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 3 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga registre a evolução do aluno (observações semanais, atendimentos, reuniões e relatórios) e escolha quais registros a família pode ler, para que o histórico saia do papel e aluno e responsável acompanhem o que for liberado.

## 2. Escopo

### O que entra no escopo

- Listar os acompanhamentos do aluno, com filtros por tipo, período e professor envolvido.
- Registrar, editar, ver e imprimir acompanhamentos.
- Marcar cada acompanhamento como visível ou não para o aluno e os responsáveis.
- Abrir o formulário já preenchido a partir de um evento realizado ([T14 Evento](prd-t14-evento.md)) e de uma informação recebida ([T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md)).
- Mostrar o histórico de edições de cada registro.
- Mostrar ao aluno e aos responsáveis só os acompanhamentos visíveis.

### O que não entra no escopo

- Diagnósticos, teste inicial e testes aplicados: ficam em [T09 Dados de saúde](prd-t09-dados-de-saude.md).
- Acesso do professor: ele não vê acompanhamentos nem recebe notificação deles (RG-10, RG-11).
- Formulário "relatório de acompanhamento": fica em [T24 Formulários](prd-t24-formularios.md), na fase 5.
- Busca por texto em acompanhamentos: fica em [T25 Busca no acervo](prd-t25-busca-no-acervo.md), na fase 5.
- Envio de informações pela família: fica em [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê todos os acompanhamentos do aluno, registra, edita, imprime e define a visibilidade para a família. É a única que vê "Professores envolvidos". |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). Nunca vê dados de saúde (RG-11). |
| Aluno | Lê só os próprios acompanhamentos marcados como visíveis. Não registra nem edita. |
| Responsável | Lê só os acompanhamentos visíveis dos alunos vinculados a ele. Não registra nem edita. Responsável de aluno com 18 anos ou mais só tem acesso com a autorização registrada (RG-17). |

**Contexto:** a psicopedagoga chega aqui depois de um atendimento, de uma reunião ou de ler uma informação, para registrar o que aconteceu. Aluno e responsável chegam para ler o que a psicopedagoga liberou.

**Origem da jornada:** Início → Alunos → Perfil do aluno → aba "Acompanhamentos". Aluno: Meu perfil → aba "Acompanhamentos". Responsável: Perfil do aluno → aba "Acompanhamentos". A psicopedagoga também chega pela ação "Registrar acompanhamento" no cabeçalho do perfil, pelo evento realizado e pela informação recebida.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Data | Data do acompanhamento. |
| Tipo | Observação semanal, Atendimento, Reunião ou Relatório. |
| Resumo | Começo do texto do acompanhamento. Ver "Resumo na lista" em 7.2. |
| Anexos | Arquivos do registro. Ver "Anexos do acompanhamento" em 7.2. |
| Autor | Quem criou o registro (RG-15). |
| Visível para a família | Indica se aluno e responsáveis podem ler o registro. |
| Detalhe do registro | Data, tipo, texto, anexos, evento relacionado, autor, "Editado em" e histórico de edições (RG-15). Aluno e responsável veem só o que dizem RN-18 e RN-19. |
| Professores envolvidos | Professores que participaram do que foi tratado. Aparece só para a psicopedagoga. |
| Botões | Registrar acompanhamento, Editar, Ver, Imprimir. Só a psicopedagoga vê Registrar, Editar e Imprimir. Ver "Impressão pela família" em 7.2. |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Data | Sim | Formato dd/mm/aaaa (RG-18). Não pode ser futura. |
| Tipo | Sim | Observação semanal, Atendimento, Reunião ou Relatório. |
| Texto | Sim | Até 5.000 caracteres. |
| Relatório em PDF | Só no tipo Relatório | Aparece só quando o tipo é Relatório. Segue RG-16. |
| Evento relacionado | Não | Lista os eventos realizados do aluno. |
| Professores envolvidos | Não | Lista os professores do aluno. Só a psicopedagoga vê este campo. |
| Visível para aluno e responsáveis | Sim | Padrão: não. |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Tipo | Observação semanal, Atendimento, Reunião, Relatório | Sem filtro |
| Período | Data inicial e data final | Ver "Período padrão da lista" em 7.2 |
| Professor envolvido | Professores do aluno. Só a psicopedagoga usa este filtro. | Sem filtro |

Filtros ativos seguem RG-21.

### 5.3 Ordenação e paginação

- Ordenação padrão: data mais recente primeiro.
- Outras ordenações: não se aplica.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre a aba "Acompanhamentos" no perfil do aluno.
2. O sistema mostra a lista, com o registro mais recente primeiro.
3. A psicopedagoga escolhe "Registrar acompanhamento".
4. A psicopedagoga preenche data, tipo e texto, anexa o relatório se o tipo for Relatório e escolhe se o registro fica visível para a família.
5. A psicopedagoga salva. O sistema guarda o registro com autor e data (RG-15) e mostra o registro na lista.
6. Se o registro é visível para a família, o sistema avisa o aluno e os responsáveis (seção 8).

### 6.2 Fluxos alternativos

- Registrar a partir de um evento realizado: em [T14 Evento](prd-t14-evento.md), "Registrar atendimento" abre o formulário com data, tipo e evento preenchidos. O detalhe do evento passa a ter um acesso ao acompanhamento registrado.
- Registrar a partir de uma informação recebida: em [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md), "Registrar como acompanhamento" abre o formulário com o texto da informação.
- Campo obrigatório vazio, data futura ou texto acima de 5.000 caracteres: o sistema não salva, mostra a mensagem junto ao campo e mantém o que foi digitado.
- Tipo Relatório sem arquivo: o sistema não salva e pede o relatório em PDF.
- Arquivo fora das regras de anexo (RG-16): o sistema não aceita o arquivo e explica o limite.
- Salvar falha: o que foi digitado continua no formulário (RG-29).
- Sair com alterações não salvas: o sistema pede confirmação (RG-29).
- Lista vazia: o sistema mostra a mensagem de vazio (seção 6.4).
- Aluno ou responsável abre um registro não visível: abre "Não encontrado" (RG-13).
- Professor: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Registrar acompanhamento | Psicopedagoga | Abre o formulário vazio, ou preenchido quando vem de um evento ou de uma informação. Ao salvar, o registro entra na lista. |
| Editar acompanhamento | Psicopedagoga | Abre o formulário com os dados atuais. Ao salvar, guarda a edição no histórico e mostra "Editado em" (RG-15). Se o registro é visível, avisa aluno e responsáveis. |
| Ver acompanhamento | Psicopedagoga, Aluno, Responsável | Abre o detalhe do registro. Aluno e responsável só abrem registros visíveis. |
| Imprimir acompanhamento | Psicopedagoga | Gera a versão impressa com "Documento confidencial" e registra quem imprimiu, quando e o quê (RG-30). |
| Filtrar a lista | Psicopedagoga, Aluno, Responsável | Aplica tipo, período e, para a psicopedagoga, professor envolvido. Aluno e responsável filtram só entre os registros visíveis. |
| Abrir o relatório | Psicopedagoga, Aluno, Responsável | Abre o arquivo anexado ao registro. Tem a mesma visibilidade do registro (RG-12). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Psicopedagoga: mensagem da seção 9 e a ação principal "Registrar acompanhamento" (RG-22). Aluno e responsável: mensagem da seção 9, sem ação. |
| Vazio, por causa dos filtros | Mensagem da seção 9 e a opção de limpar os filtros (RG-22). |
| Sem permissão | Professor abre "Acesso negado". Registro ou aluno que o usuário não pode ver abre "Não encontrado" (RG-13, RG-17). Telas em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Sem conexão ou falha inesperada abrem "Sem conexão" ou "Erro inesperado" de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). O que foi digitado continua no formulário (RG-29). |

### 6.5 Entrega por fase

| Fase | O que aparece |
| --- | --- |
| 2 | Evento e agenda já existem, mas sem a ação "Registrar atendimento" nem o acesso ao acompanhamento no evento. |
| 3 | Esta tela inteira, a aba "Acompanhamentos" no perfil, a ação "Registrar acompanhamento" no cabeçalho do perfil, "Registrar atendimento" e o acesso ao acompanhamento em [T14 Evento](prd-t14-evento.md), e a notificação de acompanhamento visível. |
| 4 | "Registrar como acompanhamento" em [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md). |
| 5 | Busca em acompanhamentos ([T25 Busca no acervo](prd-t25-busca-no-acervo.md)) e o formulário "relatório de acompanhamento" em [T24 Formulários](prd-t24-formularios.md). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A psicopedagoga vê todos os acompanhamentos. Aluno e responsável veem só os marcados como visíveis para a família. O professor não vê nenhum (RG-10, RG-11). |
| RN-02 | Acompanhamento é dado de saúde. Cada anexo tem a mesma visibilidade do registro (RG-12). |
| RN-03 | O campo "Visível para aluno e responsáveis" é obrigatório e começa em "não". |
| RN-04 | A data é obrigatória e não pode ser futura. O tipo é Observação semanal, Atendimento, Reunião ou Relatório. |
| RN-05 | O texto é obrigatório e tem até 5.000 caracteres. |
| RN-06 | O relatório em PDF só existe no tipo Relatório e é obrigatório nele (RG-16). |
| RN-07 | "Evento relacionado" lista só eventos realizados do aluno. "Professores envolvidos" lista só professores do aluno. |
| RN-08 | "Professores envolvidos" registra quais professores participaram do que foi tratado, por exemplo numa reunião com a psicopedagoga. Serve só para consulta da psicopedagoga. Os professores não veem o acompanhamento nem recebem notificação. |
| RN-09 | "Registrar atendimento" em um evento realizado abre o formulário com data, tipo e evento preenchidos. |
| RN-10 | "Registrar como acompanhamento" em uma informação recebida abre o formulário com o texto da informação. |
| RN-11 | O registro mostra o histórico de edições (RG-15). |
| RN-12 | O aluno e os responsáveis são avisados quando um acompanhamento visível é registrado ou alterado (seção 8). Responsável só recebe aviso com conta ativa. |
| RN-13 | Responsável de aluno com 18 anos ou mais só vê acompanhamentos com a autorização do aluno registrada pela psicopedagoga (RG-17). |
| RN-14 | Toda impressão usa a versão impressa padrão, com "Documento confidencial", e registra quem imprimiu, quando e o quê (RG-30). |
| RN-15 | Sair do formulário com alterações não salvas pede confirmação. Se salvar falhar, o que foi digitado continua (RG-29). |
| RN-16 | Segue RG-19 a RG-22: 20 itens por página com o total, filtros visíveis e mantidos, e lista vazia com mensagem e ação. |
| RN-17 | Segue RG-07 (a psicopedagoga vê alunos ativos e inativos), RG-23 (confirmação de ações que afetam outras pessoas, como tornar o registro visível), RG-24 e RG-26. |
| RN-18 | No registro visível, aluno e responsável veem data, tipo, texto, anexos, autor e o evento relacionado, se puderem ver esse evento na agenda. Nunca veem "Professores envolvidos". |
| RN-19 | O histórico completo de edições fica só para a psicopedagoga. Aluno e responsável veem só "Editado em", com data e autor da última alteração (RG-15). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mudança de visibilidade | Tornar visível um registro que não era avisa aluno e responsáveis como se fosse novo. Deixar de ser visível não avisa ninguém. |
| Tipo preenchido pelo evento | "Registrar atendimento" em evento do tipo Atendimento preenche "Atendimento", e em evento do tipo Reunião preenche "Reunião". A psicopedagoga pode trocar o tipo. |
| Data e tipo vindos de uma informação | Ao registrar uma informação como acompanhamento, só o texto vem preenchido. Data e tipo ficam para a psicopedagoga escolher. |
| Resumo na lista | O resumo mostra os primeiros 150 caracteres do texto. |
| Anexos do acompanhamento | Só o tipo Relatório aceita arquivos, até 5 por registro (RG-16). Nos outros tipos a coluna Anexos fica vazia. |
| Período padrão da lista | A lista abre sem período aplicado e mostra todos os registros. |
| Impressão pela família | Só a psicopedagoga imprime acompanhamentos. Aluno e responsável apenas leem. |
| Exclusão de acompanhamento | Não existe exclusão. Registro feito por engano é corrigido pela edição, e o histórico guarda as versões. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Acompanhamento visível para a família registrado ou alterado | Aluno e responsáveis. O responsável só recebe com conta ativa (seção 7 do índice). A psicopedagoga que fez a ação não recebe (RG-25). | Avisa que há um acompanhamento novo ou alterado no perfil do aluno. Texto na seção 9. |

Acompanhamento não visível para a família não gera notificação. Professores nunca recebem notificação de acompanhamento (RN-08).

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Acompanhamento registrado | Sucesso | Acompanhamento registrado. (proposta) |
| Acompanhamento alterado | Sucesso | Acompanhamento alterado. (proposta) |
| Notificação de acompanhamento visível | Aviso | Há um acompanhamento novo ou alterado no perfil de <nome do aluno>. (proposta) |
| Data vazia | Erro | Informe a data do acompanhamento. (proposta) |
| Data futura | Erro | A data não pode ser futura. Informe a data de hoje ou uma data anterior. (proposta) |
| Tipo vazio | Erro | Escolha o tipo do acompanhamento. (proposta) |
| Texto vazio | Erro | Escreva o texto do acompanhamento para salvar. (proposta) |
| Texto acima do limite | Erro | O texto passa de 5.000 caracteres. Reduza o texto para salvar. (proposta) |
| Relatório sem arquivo | Erro | Envie o relatório em PDF para salvar um acompanhamento do tipo Relatório. (proposta) |
| Arquivo fora das regras | Erro | O relatório precisa ser um arquivo PDF com até 10 MB. Escolha outro arquivo. (proposta) |
| Limite de anexos | Erro | Cada registro aceita até 5 anexos. Remova um anexo para enviar outro. (proposta) |
| Falha ao salvar | Erro | Não foi possível salvar. Verifique a conexão e tente de novo. O que você digitou foi mantido. (proposta) |
| Tornar o registro visível | Confirmação | Ao salvar, o aluno e os responsáveis poderão ler este acompanhamento e serão avisados. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Lista vazia para a psicopedagoga | Aviso | Nenhum acompanhamento registrado para este aluno. (proposta) |
| Lista vazia para aluno e responsável | Aviso | Ainda não há acompanhamentos disponíveis para você. (proposta) |
| Lista vazia por causa dos filtros | Aviso | Nenhum acompanhamento encontrado com os filtros escolhidos. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Abrir a tela | Sim | Não | Só os próprios, visíveis | Só os dos alunos vinculados, visíveis |
| Ver a lista e o detalhe | Sim, todos | Não | Só os próprios, marcados como visíveis | Só os dos alunos vinculados, marcados como visíveis |
| Registrar acompanhamento | Sim | Não | Não | Não |
| Editar acompanhamento | Sim | Não | Não | Não |
| Definir a visibilidade para a família | Sim | Não | Não | Não |
| Ver "Professores envolvidos" | Sim | Não | Não | Não |
| Ver o histórico de edições | Sim | Não | Não, vê só "Editado em" (RN-19) | Não, vê só "Editado em" (RN-19) |
| Imprimir | Sim | Não | Ver "Impressão pela família" em 7.2 | Ver "Impressão pela família" em 7.2 |
| Usar o filtro "Professor envolvido" | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga abre a aba "Acompanhamentos" de um aluno, quando a lista carrega, então ela vê data, tipo, resumo, anexos, autor e se o registro está visível para a família, com o mais recente primeiro.
- [ ] Dado um aluno com mais de 20 acompanhamentos, quando a lista é exibida, então ela mostra 20 itens por página e o total de resultados (RG-19).
- [ ] Dado o formulário de acompanhamento aberto pelo perfil, quando a psicopedagoga o abre, então "Visível para aluno e responsáveis" começa em "não".
- [ ] Dado o formulário, quando a psicopedagoga informa data futura, então o sistema não salva e mostra a mensagem de data futura.
- [ ] Dado o formulário, quando a psicopedagoga deixa data, tipo ou texto vazios, então o sistema não salva e indica o que falta.
- [ ] Dado o formulário, quando o texto passa de 5.000 caracteres, então o sistema não salva e pede para reduzir o texto.
- [ ] Dado o tipo Relatório, quando a psicopedagoga tenta salvar sem o relatório em PDF, então o sistema não salva e pede o arquivo.
- [ ] Dado um tipo diferente de Relatório, quando a psicopedagoga abre o formulário, então o campo "Relatório em PDF" não aparece.
- [ ] Dado o campo "Evento relacionado", quando a psicopedagoga abre a lista, então ela mostra só eventos realizados do aluno.
- [ ] Dado o campo "Professores envolvidos", quando a psicopedagoga abre a lista, então ela mostra só professores do aluno.
- [ ] Dado um evento realizado em [T14 Evento](prd-t14-evento.md), quando a psicopedagoga escolhe "Registrar atendimento", então o formulário abre com data, tipo e evento preenchidos.
- [ ] Dado uma informação recebida em [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md), quando a psicopedagoga escolhe "Registrar como acompanhamento", então o formulário abre com o texto da informação.
- [ ] Dado um acompanhamento salvo a partir de um evento, quando a psicopedagoga abre o detalhe do evento, então ela encontra o acesso ao acompanhamento registrado.
- [ ] Dado um acompanhamento editado, quando a psicopedagoga abre o registro, então ele mostra o histórico de edições e "Editado em" com data e autor (RG-15).
- [ ] Dado um acompanhamento marcado como visível, quando a psicopedagoga salva, então aluno e responsáveis com conta ativa recebem a notificação "Acompanhamento visível para a família registrado ou alterado", e a psicopedagoga não recebe (RG-25).
- [ ] Dado um acompanhamento visível já salvo, quando a psicopedagoga o altera, então aluno e responsáveis com conta ativa recebem a notificação.
- [ ] Dado um acompanhamento não visível, quando a psicopedagoga o registra ou altera, então ninguém recebe notificação.
- [ ] Dado um acompanhamento com "Professores envolvidos", quando ele é salvo, então nenhum professor recebe notificação nem consegue vê-lo.
- [ ] Dado um aluno, quando ele abre a aba "Acompanhamentos", então vê só os próprios registros marcados como visíveis.
- [ ] Dado um responsável, quando abre a aba "Acompanhamentos" de um aluno vinculado, então vê só os registros visíveis desse aluno.
- [ ] Dado um responsável de aluno com 18 anos ou mais sem autorização registrada, quando tenta abrir os acompanhamentos, então o sistema abre "Não encontrado" (RG-13, RG-17).
- [ ] Dado um aluno ou responsável, quando tenta abrir um acompanhamento não visível, então o sistema abre "Não encontrado" (RG-13).
- [ ] Dado um acompanhamento visível ligado a um evento que o aluno vê na agenda, quando o aluno abre o registro, então vê data, tipo, texto, anexos, autor e o evento relacionado, e não vê "Professores envolvidos" (RN-18).
- [ ] Dado um acompanhamento visível ligado a um evento que o responsável não vê na agenda, quando o responsável abre o registro, então o evento relacionado não aparece (RN-18).
- [ ] Dado um acompanhamento visível editado duas vezes, quando o responsável abre o registro, então vê só "Editado em" com data e autor da última alteração, sem o histórico de edições (RN-19).
- [ ] Dado um aluno ou responsável, quando abre a tela, então não vê os botões Registrar e Editar nem "Professores envolvidos".
- [ ] Dado um professor, quando tenta abrir esta tela, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado um relatório anexado a um registro não visível, quando aluno ou responsável tenta abri-lo, então o sistema não o mostra (RG-12).
- [ ] Dado um acompanhamento, quando a psicopedagoga escolhe "Imprimir", então a versão impressa mostra o nome do campus, o nome do sistema, a data de impressão e "Documento confidencial", e o sistema registra quem imprimiu, quando e o quê (RG-30).
- [ ] Dado a lista com filtros por tipo, período e professor envolvido, quando a psicopedagoga os aplica, então a lista mostra só os registros que atendem aos filtros, os filtros ativos ficam visíveis e podem ser limpos de uma vez (RG-21).
- [ ] Dado um filtro sem resultados, quando a lista é exibida, então o sistema mostra a mensagem de vazio por causa dos filtros e a opção de limpar os filtros (RG-22).
- [ ] Dado um aluno sem acompanhamentos, quando a psicopedagoga abre a aba, então vê a mensagem de vazio e a ação "Registrar acompanhamento" (RG-22).
- [ ] Dado um formulário com alterações não salvas, quando a psicopedagoga tenta sair, então o sistema pede confirmação dizendo que as alterações serão perdidas (RG-29).
- [ ] Dado que salvar falhou, quando o formulário continua aberto, então o que foi digitado continua preenchido (RG-29).
- [ ] Dado que a conexão caiu, quando um usuário abre a tela, então o sistema mostra "Sem conexão" e, se a falha for outra, "Erro inesperado".
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
