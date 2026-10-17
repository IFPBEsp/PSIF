# PRD da tela de Planejamento semanal

| Campo | Valor |
| --- | --- |
| Identificador | T12 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T03 Notificações](prd-t03-notificacoes.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T13 Agenda](prd-t13-agenda.md), [T24 Formulários](prd-t24-formularios.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 3 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga organize a semana de atividades de cada aluno e que o aluno e os responsáveis consultem o planejamento confirmado, para que a rotina de estudos e compromissos fique clara para todos.

## 2. Escopo

### O que entra no escopo

- Listar os planejamentos semanais do aluno, com semana, situação e quantidade de atividades.
- Criar o planejamento de uma semana, escolhendo a segunda-feira.
- Montar a semana em uma grade de segunda a domingo, das 07:00 às 23:00.
- Adicionar, editar, mover, remover e duplicar atividades, com prioridade Alta, Média ou Baixa mostrada por cor.
- Escrever anotações gerais da semana.
- Salvar como "Rascunho", confirmar o planejamento e alterar um planejamento confirmado.
- Imprimir o planejamento.
- Mostrar ao aluno e aos responsáveis só os planejamentos confirmados.

### O que não entra no escopo

- Agenda de eventos: fica em [T13 Agenda](prd-t13-agenda.md). Esta tela só alimenta a agenda com as atividades do planejamento confirmado.
- Resumo do planejamento da semana atual no Início: fica em [T02 Início](prd-t02-inicio.md).
- Acesso do professor: ele não usa esta tela.
- Formulário "planejamento semanal": fica em [T24 Formulários](prd-t24-formularios.md), na fase 5.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Cria e edita o planejamento dos alunos e vê também o de alunos inativos (RG-07), sem criar planejamento novo para eles (RN-21), vê rascunhos e confirmados, confirma e imprime. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Aluno | Lê só os próprios planejamentos confirmados. Não cria nem edita. |
| Responsável | Lê só os planejamentos confirmados dos alunos vinculados a ele. Não cria nem edita. Responsável de aluno com 18 anos ou mais só tem acesso com a autorização registrada (RG-17). |

**Contexto:** a psicopedagoga monta o planejamento no começo de cada semana, em conversa com o aluno. Aluno e responsável chegam para ver o que está combinado para a semana.

**Origem da jornada:** psicopedagoga: Início → Alunos → Perfil do aluno → aba "Planejamento semanal". Aluno: Início ou Meu perfil → aba "Planejamento semanal". Responsável: Início ou Perfil do aluno → aba "Planejamento semanal". Quem usa a agenda também chega aqui ao clicar em uma atividade do planejamento.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Semana | Data inicial (segunda-feira) e data final (domingo) de cada planejamento da lista, por exemplo 12/10/2026 a 18/10/2026. |
| Situação | "Rascunho" ou "Confirmado" (seção 6 do índice). Aluno e responsável só veem "Confirmado". |
| Quantidade de atividades | Número de atividades do planejamento da semana. |
| Grade da semana | Colunas de segunda a domingo e linhas das 07:00 às 23:00. Cada atividade ocupa o espaço entre o início e o fim. |
| Atividade | Mostra descrição, horário de início e de fim e a prioridade pela cor. |
| Prioridade | Alta, Média ou Baixa, cada uma com uma cor. Ver "Prioridade além da cor" em 7.2. |
| Anotações gerais | Texto livre sobre a semana. Ver "Anotações para a família" em 7.2. |
| Autoria | Quem criou o planejamento e quando, e "Editado em" com data e autor da última alteração (RG-15). |
| Botões | Criar planejamento, Adicionar atividade, Duplicar semana anterior, Salvar rascunho (só em rascunho, RN-19), Salvar alterações (só em confirmado, RN-19), Confirmar planejamento, Imprimir. Só a psicopedagoga vê os botões de criação e edição. |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

#### Semana

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Segunda-feira da semana | Sim | A psicopedagoga escolhe uma segunda-feira. Formato dd/mm/aaaa (RG-18). Só pode haver um planejamento por aluno por semana (RN-02). |
| Domingo da semana | Não | Preenchido automaticamente com o domingo da semana escolhida. Não pode ser editado. |

#### Atividade

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Descrição | Sim | Texto. Ver "Limite de texto" em 7.2. |
| Dia | Sim | De segunda a domingo da semana do planejamento. |
| Horário de início | Sim | Formato de 24 horas (RG-18), a partir das 07:00. |
| Horário de fim | Sim | Formato de 24 horas (RG-18), depois do início e até as 23:00. |
| Prioridade | Sim | Alta, Média ou Baixa. Ver "Prioridade padrão" em 7.2. |

#### Planejamento

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Anotações gerais da semana | Não | Texto livre. Ver "Limite de texto" em 7.2. |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Período | Data inicial e data final. Mostra os planejamentos cuja semana cai dentro do período. | Ver "Período padrão da lista" em 7.2 |

Filtros ativos seguem RG-21.

### 5.3 Ordenação e paginação

- Ordenação padrão: semana mais recente primeiro.
- Outras ordenações: não se aplica.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre a aba "Planejamento semanal" no perfil do aluno.
2. O sistema mostra a lista de semanas, com a mais recente primeiro.
3. A psicopedagoga escolhe "Criar planejamento" e escolhe a segunda-feira. O sistema preenche o domingo.
4. A psicopedagoga clica em um horário da grade e preenche descrição, dia, início, fim e prioridade da atividade.
5. A psicopedagoga repete o passo 4, move ou edita atividades e escreve as anotações gerais.
6. A psicopedagoga escolhe "Salvar rascunho". O planejamento fica "Rascunho" e só ela o vê.
7. Quando o planejamento está pronto, a psicopedagoga escolhe "Confirmar planejamento" e confirma na janela.
8. O planejamento fica "Confirmado". O aluno e os responsáveis são avisados e passam a ver a semana. As atividades aparecem na agenda do aluno.

### 6.2 Fluxos alternativos

- Atividade que se sobrepõe a outra do mesmo dia: o sistema não salva a atividade e mostra a mensagem de sobreposição.
- Fim igual ou anterior ao início, ou horário fora de 07:00 a 23:00: o sistema não salva a atividade e mostra a mensagem do horário.
- Descrição vazia: o sistema não salva a atividade e pede a descrição.
- Semana que já tem planejamento para o aluno: o sistema não cria outro e abre o planejamento existente (RN-02).
- Duplicar a semana anterior sem semana anterior: ver "Duplicar a semana anterior" em 7.2.
- Semana que já terminou: o planejamento abre só para leitura (RN-08).
- Confirmar sem nenhuma atividade: o sistema não confirma e mostra a mensagem (RN-20).
- Aluno inativo: "Criar planejamento" não aparece, e a psicopedagoga consulta os planejamentos que já existem (RN-21).
- Salvar falha: o que foi digitado continua no editor (RG-29).
- Sair do editor com alterações não salvas: o sistema pede confirmação (RG-29).
- Lista vazia: o sistema mostra a mensagem de vazio (seção 6.4).
- Aluno ou responsável tenta abrir um rascunho: abre "Não encontrado" (RG-13).
- Professor: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Criar planejamento | Psicopedagoga | Pede a segunda-feira e abre o editor vazio. A semana não pode já ter planejamento para o aluno. Não aparece para aluno inativo (RN-21). |
| Adicionar atividade | Psicopedagoga | Clicar em um horário da grade abre o formulário da atividade com dia e início preenchidos. Ver "Uso da grade pelo teclado" em 7.2. |
| Editar atividade | Psicopedagoga | Abre o formulário com os dados atuais. |
| Mover atividade | Psicopedagoga | Muda o dia e o horário da atividade, respeitando as regras de horário (RN-03, RN-04). A ação também pode ser feita usando só o teclado (RG-26). |
| Remover atividade | Psicopedagoga | Tira a atividade da grade. |
| Duplicar a semana anterior | Psicopedagoga | Copia as atividades da semana anterior do aluno para a semana aberta. Ver "Duplicar a semana anterior" em 7.2. |
| Salvar rascunho | Psicopedagoga | Guarda o planejamento como "Rascunho". Não avisa ninguém. |
| Confirmar planejamento | Psicopedagoga | Exige pelo menos uma atividade (RN-20). Pede confirmação. Ao confirmar, o planejamento fica "Confirmado", avisa aluno e responsáveis e mostra as atividades na agenda do aluno. |
| Salvar alterações de um planejamento confirmado | Psicopedagoga | Guarda as alterações, mantém "Confirmado", pede confirmação e avisa aluno e responsáveis uma vez, ao salvar (RN-19). |
| Imprimir | Psicopedagoga | Gera a versão impressa do planejamento com nome do campus, nome do sistema e data de impressão, e registra quem imprimiu, quando e o quê (RG-30). Ver "Impressão pela família" em 7.2. |
| Ver planejamento | Psicopedagoga, Aluno, Responsável | Abre a semana em leitura. Aluno e responsável só abrem planejamentos confirmados. |
| Filtrar por período | Psicopedagoga, Aluno, Responsável | Mostra só as semanas dentro do período. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Psicopedagoga: mensagem da seção 9 e a ação principal "Criar planejamento" (RG-22). Aluno e responsável: mensagem da seção 9, sem ação. |
| Vazio, por causa dos filtros | Mensagem da seção 9 e a opção de limpar os filtros (RG-22). |
| Sem permissão | Professor abre "Acesso negado". Planejamento ou aluno que o usuário não pode ver abre "Não encontrado" (RG-13, RG-17). Telas em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Sem conexão ou falha inesperada abrem "Sem conexão" ou "Erro inesperado" de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). O que foi digitado continua no editor (RG-29). |

### 6.5 Regras de mudança de situação

O planejamento semanal tem duas situações: "Rascunho" e "Confirmado" (seção 6 do índice).

| De | Para | Quem muda | Quando | O que acontece |
| --- | --- | --- | --- | --- |
| Não existe | Rascunho | Psicopedagoga | Ao salvar o planejamento pela primeira vez com "Salvar rascunho". | Só a psicopedagoga vê. Aluno e responsável não veem, e a agenda não mostra as atividades. Ninguém é avisado. |
| Rascunho | Confirmado | Psicopedagoga | Ao escolher "Confirmar planejamento" e confirmar na janela, com pelo menos uma atividade (RN-20). | Aluno e responsáveis passam a ver o planejamento e recebem a notificação. As atividades aparecem na agenda do aluno ([T13 Agenda](prd-t13-agenda.md)). |
| Confirmado | Confirmado | Psicopedagoga | Ao alterar o planejamento já confirmado e escolher "Salvar alterações" (RN-19). | Mantém "Confirmado". Aluno e responsáveis recebem a notificação de alteração e a agenda mostra as atividades novas. |
| Rascunho ou Confirmado, semana encerrada | Só leitura | Sistema | Quando a semana termina. | Ninguém edita mais. A situação continua a mesma. |

Aluno e responsável só veem "Confirmado". Planejamento confirmado não volta para "Rascunho" (RN-19).

### 6.6 Entrega por fase

| Fase | O que aparece |
| --- | --- |
| 1 | O Início ([T02 Início](prd-t02-inicio.md)) e o perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)) existem, mas sem planejamento. |
| 2 | A agenda ([T13 Agenda](prd-t13-agenda.md)) existe, mas sem as atividades do planejamento nem o filtro "Mostrar planejamento". |
| 3 | Esta tela inteira, a aba "Planejamento semanal" no perfil do aluno, o planejamento da semana atual no Início do aluno e do responsável, as atividades do planejamento confirmado na agenda e a notificação. O botão "Imprimir" usa a versão impressa padrão (RG-30). |
| 5 | O formulário "planejamento semanal" em [T24 Formulários](prd-t24-formularios.md). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A psicopedagoga cria e edita. Aluno e responsável leem só os planejamentos confirmados. O professor não acessa a tela. |
| RN-02 | Cada aluno tem no máximo um planejamento por semana. |
| RN-03 | A psicopedagoga escolhe a segunda-feira da semana, e o domingo é preenchido automaticamente. |
| RN-04 | A grade vai de segunda a domingo, das 07:00 às 23:00. O fim da atividade é depois do início e fica dentro desse intervalo. |
| RN-05 | Atividades do mesmo dia não podem se sobrepor. |
| RN-06 | Cada atividade tem descrição obrigatória, dia, horário de início, horário de fim e prioridade Alta, Média ou Baixa, mostrada por cor. |
| RN-07 | O planejamento tem anotações gerais da semana. |
| RN-08 | Semana que já terminou fica só para leitura. |
| RN-09 | Aluno e responsável só veem planejamentos confirmados. O responsável vê só os alunos vinculados a ele (RG-09). |
| RN-10 | Confirmar um planejamento, ou alterar um já confirmado, notifica o aluno e os responsáveis (seção 8). |
| RN-11 | As atividades do planejamento confirmado aparecem na agenda do aluno ([T13 Agenda](prd-t13-agenda.md)). Professor não vê essas atividades. |
| RN-12 | Responsável de aluno com 18 anos ou mais só vê o planejamento com a autorização do aluno registrada pela psicopedagoga (RG-17). |
| RN-13 | Mover atividade também pode ser feito usando só o teclado (RG-26). |
| RN-14 | Todo registro mostra quem criou e quando, e "Editado em" quando foi alterado (RG-15). |
| RN-15 | Imprimir usa a versão impressa padrão e registra quem imprimiu, quando e o quê (RG-30). |
| RN-16 | Sair do editor com alterações não salvas pede confirmação. Se salvar falhar, o que foi digitado continua (RG-29). |
| RN-17 | Confirmar planejamento e salvar alterações de um planejamento confirmado afetam outras pessoas e pedem confirmação (RG-23). |
| RN-18 | Datas e horários seguem RG-18. A lista segue RG-19 a RG-22. Botões e erros seguem RG-24. |
| RN-19 | O botão "Salvar rascunho" não aparece em planejamento confirmado. A psicopedagoga salva as alterações com "Salvar alterações", que mantém "Confirmado". Planejamento confirmado não volta para "Rascunho" (seção 6 do índice). A notificação de alteração sai quando ela salva, não a cada atividade alterada. |
| RN-20 | Só é possível confirmar um planejamento com pelo menos uma atividade (seção 6 do índice). |
| RN-21 | A psicopedagoga não cria planejamento novo para aluno inativo. Ela consulta os planejamentos que já existem (RG-07). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Semana em curso | A psicopedagoga não cria planejamento para semana que já terminou. |
| Duplicar a semana anterior | Copia as atividades da semana anterior do mesmo aluno para a semana aberta, sem as anotações gerais. A semana aberta fica "Rascunho". Se a semana aberta já tem atividades, pede confirmação antes de substituí-las. Sem semana anterior, a ação fica indisponível e mostra um aviso. |
| Horários e duração | Os horários são em intervalos de 30 minutos, com duração mínima de 30 minutos. Uma atividade pode começar no minuto em que outra termina. |
| Excluir planejamento em rascunho | Não existe exclusão de planejamento. A psicopedagoga edita o rascunho até confirmar. |
| Limite de texto | A descrição da atividade aceita até 200 caracteres e as anotações gerais, até 2.000 caracteres. |
| Prioridade padrão | A atividade nova nasce com prioridade Média. |
| Prioridade além da cor | A atividade mostra também o nome da prioridade em texto, para que a informação não dependa só da cor. |
| Anotações para a família | Aluno e responsável veem as anotações gerais da semana no planejamento confirmado. |
| Uso da grade pelo teclado | Cada horário da grade recebe o foco pelo teclado e abre o formulário da atividade. Para mover, a pessoa escolhe a atividade, ativa "Mover" e usa as setas para mudar o dia e o horário, confirmando para soltar. A edição da atividade também permite mudar dia, início e fim. |
| Impressão pela família | Aluno e responsável imprimem os planejamentos confirmados que podem ver. |
| Período padrão da lista | A lista abre sem período aplicado e mostra todas as semanas. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Planejamento semanal confirmado ou alterado depois de confirmado | Aluno e responsáveis. O responsável só recebe com conta ativa (seção 7 do índice). A psicopedagoga que fez a ação não recebe (RG-25). | Avisa que o planejamento de uma semana foi confirmado ou alterado, com a semana. Texto na seção 9. |

Salvar como "Rascunho" não gera notificação. Professores não recebem notificação de planejamento.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Rascunho salvo | Sucesso | Rascunho salvo. Aluno e responsáveis ainda não veem este planejamento. (proposta) |
| Planejamento confirmado | Sucesso | Planejamento confirmado. Aluno e responsáveis foram avisados. (proposta) |
| Alterações salvas em planejamento confirmado | Sucesso | Alterações salvas. Aluno e responsáveis foram avisados. (proposta) |
| Notificação de planejamento confirmado | Aviso | O planejamento da semana de 12/10/2026 a 18/10/2026 foi confirmado. (proposta) |
| Notificação de planejamento alterado | Aviso | O planejamento da semana de 12/10/2026 a 18/10/2026 foi alterado. (proposta) |
| Confirmar planejamento | Confirmação | Confirmar o planejamento de 12/10/2026 a 18/10/2026? <nome do aluno> e os responsáveis passarão a ver a semana e serão avisados. (proposta) |
| Salvar alterações de um planejamento confirmado | Confirmação | Salvar as alterações? <nome do aluno> e os responsáveis verão a semana alterada e serão avisados. (proposta) |
| Duplicar com atividades na semana | Confirmação | Duplicar a semana anterior? As atividades desta semana serão substituídas pelas da semana anterior. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Descrição vazia | Erro | Escreva a descrição da atividade para salvar. (proposta) |
| Confirmar sem atividades | Erro | Adicione pelo menos uma atividade para confirmar o planejamento. (proposta) |
| Atividade sobreposta | Erro | Já existe uma atividade neste horário. Escolha um horário livre no mesmo dia. (proposta) |
| Horário inválido | Erro | O fim precisa ser depois do início, e os dois ficam entre 07:00 e 23:00. Corrija os horários. (proposta) |
| Semana já tem planejamento | Erro | Este aluno já tem um planejamento para esta semana. Abra o planejamento existente para editar. (proposta) |
| Escolha de data que não é segunda-feira | Erro | Escolha uma segunda-feira. (proposta) |
| Semana encerrada | Aviso | Esta semana já terminou. O planejamento só pode ser consultado. (proposta) |
| Sem semana anterior para duplicar | Aviso | Este aluno não tem planejamento na semana anterior. (proposta) |
| Falha ao salvar | Erro | Não foi possível salvar. Verifique a conexão e tente de novo. O que você digitou foi mantido. (proposta) |
| Lista vazia para a psicopedagoga | Aviso | Nenhum planejamento criado para este aluno. (proposta) |
| Lista vazia para aluno e responsável | Aviso | Ainda não há planejamento confirmado. (proposta) |
| Lista vazia por causa dos filtros | Aviso | Nenhum planejamento encontrado no período escolhido. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Abrir a tela | Sim | Não | Só o próprio | Só dos alunos vinculados |
| Ver planejamentos em "Rascunho" | Sim | Não | Não | Não |
| Ver planejamentos "Confirmado" | Sim | Não | Só os próprios | Só dos alunos vinculados |
| Criar planejamento | Sim | Não | Não | Não |
| Adicionar, editar, mover, remover e duplicar atividades | Sim | Não | Não | Não |
| Salvar rascunho | Sim | Não | Não | Não |
| Confirmar planejamento | Sim | Não | Não | Não |
| Alterar planejamento confirmado | Sim | Não | Não | Não |
| Imprimir | Sim | Não | Ver "Impressão pela família" em 7.2 | Ver "Impressão pela família" em 7.2 |
| Filtrar por período | Sim | Não | Sim, nos próprios | Sim, nos dos alunos vinculados |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga abre a aba "Planejamento semanal" de um aluno, quando a lista carrega, então ela vê semana (data inicial e final), situação e quantidade de atividades, com a semana mais recente primeiro.
- [ ] Dado um aluno com mais de 20 planejamentos, quando a lista é exibida, então ela mostra 20 itens por página e o total de resultados (RG-19).
- [ ] Dado um período escolhido no filtro, quando a lista é exibida, então só aparecem as semanas dentro do período, e o filtro fica visível e pode ser limpo (RG-21).
- [ ] Dado que a psicopedagoga escolhe uma segunda-feira, quando o editor abre, então o domingo da mesma semana vem preenchido e não pode ser editado.
- [ ] Dado o editor aberto, quando a psicopedagoga olha a grade, então ela mostra de segunda a domingo, das 07:00 às 23:00.
- [ ] Dado a grade, quando a psicopedagoga clica em um horário, então abre o formulário da atividade com o dia e o início preenchidos.
- [ ] Dado o formulário da atividade, quando a psicopedagoga deixa a descrição vazia, então o sistema não salva a atividade e pede a descrição.
- [ ] Dado uma atividade com prioridade Alta, Média ou Baixa, quando ela aparece na grade, então a cor corresponde à prioridade.
- [ ] Dado uma atividade das 09:00 às 10:00 em uma segunda-feira, quando a psicopedagoga tenta salvar outra atividade que se sobrepõe a esse horário no mesmo dia, então o sistema não salva e mostra a mensagem de sobreposição.
- [ ] Dado o formulário da atividade, quando o fim é igual ou anterior ao início, então o sistema não salva e mostra a mensagem do horário.
- [ ] Dado o formulário da atividade, quando o início é antes das 07:00 ou o fim é depois das 23:00, então o sistema não salva e mostra a mensagem do horário.
- [ ] Dado um aluno que já tem planejamento em uma semana, quando a psicopedagoga tenta criar outro para a mesma semana, então o sistema não cria e abre o planejamento existente.
- [ ] Dado uma atividade na grade, quando a psicopedagoga a move para outro dia e horário livres, então a atividade aparece no novo lugar.
- [ ] Dado uma atividade na grade, quando a pessoa usa só o teclado, então ela consegue mover a atividade (RG-26).
- [ ] Dado uma atividade, quando a psicopedagoga a remove e salva, então ela não aparece mais na grade.
- [ ] Dado um aluno com planejamento na semana anterior, quando a psicopedagoga escolhe "Duplicar semana anterior", então as atividades da semana anterior aparecem na semana aberta.
- [ ] Dado o editor, quando a psicopedagoga escolhe "Salvar rascunho", então o planejamento fica "Rascunho" e ninguém recebe notificação.
- [ ] Dado um planejamento em "Rascunho", quando o aluno ou o responsável abre a aba, então o planejamento não aparece na lista, e abrir o rascunho mostra "Não encontrado" (RG-13).
- [ ] Dado um planejamento em "Rascunho", quando a psicopedagoga escolhe "Confirmar planejamento", então o sistema pede confirmação dizendo que o aluno e os responsáveis passarão a ver a semana e serão avisados.
- [ ] Dado que a psicopedagoga confirmou o planejamento, quando a confirmação termina, então a situação passa para "Confirmado", e aluno e responsáveis com conta ativa recebem a notificação, e a psicopedagoga não recebe (RG-25).
- [ ] Dado um planejamento "Confirmado", quando a psicopedagoga o altera e salva, então o sistema pede confirmação, mantém "Confirmado" e notifica aluno e responsáveis.
- [ ] Dado um planejamento "Confirmado" aberto no editor, quando a psicopedagoga vê os botões, então "Salvar rascunho" não aparece, só "Salvar alterações", e não há como voltar o planejamento para "Rascunho" (RN-19).
- [ ] Dado um planejamento "Confirmado" em que a psicopedagoga move três atividades, quando ela escolhe "Salvar alterações" e confirma, então aluno e responsáveis recebem uma só notificação de alteração (RN-19).
- [ ] Dado um planejamento em "Rascunho" sem nenhuma atividade, quando a psicopedagoga escolhe "Confirmar planejamento", então o sistema não confirma e pede pelo menos uma atividade (RN-20).
- [ ] Dado um aluno inativo, quando a psicopedagoga abre a aba "Planejamento semanal" dele, então vê os planejamentos que já existem e não vê "Criar planejamento" (RN-21).
- [ ] Dado um planejamento "Confirmado", quando o aluno abre a agenda, então as atividades aparecem na agenda dele ([T13 Agenda](prd-t13-agenda.md)).
- [ ] Dado um planejamento em "Rascunho", quando o aluno abre a agenda, então as atividades não aparecem.
- [ ] Dado uma semana que já terminou, quando a psicopedagoga abre o planejamento, então ele abre só para leitura e não permite adicionar, editar, mover nem remover atividades.
- [ ] Dado um aluno, quando abre a aba "Planejamento semanal", então vê só os próprios planejamentos confirmados.
- [ ] Dado um responsável, quando abre a aba "Planejamento semanal", então vê só os planejamentos confirmados dos alunos vinculados a ele.
- [ ] Dado um responsável de aluno com 18 anos ou mais sem autorização registrada, quando tenta abrir o planejamento, então o sistema abre "Não encontrado" (RG-13, RG-17).
- [ ] Dado um aluno ou responsável, quando abre a tela, então não vê os botões de criar, editar, confirmar nem salvar rascunho.
- [ ] Dado um professor, quando tenta abrir esta tela, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado um planejamento, quando a psicopedagoga escolhe "Imprimir", então a versão impressa mostra o nome do campus, o nome do sistema e a data de impressão, e o sistema registra quem imprimiu, quando e o quê (RG-30).
- [ ] Dado um editor com alterações não salvas, quando a psicopedagoga tenta sair, então o sistema pede confirmação dizendo que as alterações serão perdidas (RG-29).
- [ ] Dado que salvar falhou, quando o editor continua aberto, então o que foi digitado continua preenchido (RG-29).
- [ ] Dado um aluno sem planejamentos, quando a psicopedagoga abre a aba, então vê a mensagem de vazio e a ação "Criar planejamento" (RG-22).
- [ ] Dado um filtro sem resultados, quando a lista é exibida, então o sistema mostra a mensagem de vazio por causa dos filtros e a opção de limpar os filtros (RG-22).
- [ ] Dado que a conexão caiu, quando um usuário abre a tela, então o sistema mostra "Sem conexão" e, se a falha for outra, "Erro inesperado".
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
