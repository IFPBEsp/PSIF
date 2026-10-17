# PRD da tela de Informações para a psicopedagoga

| Campo | Valor |
| --- | --- |
| Identificador | T18 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T03 Notificações](prd-t03-notificacoes.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md), [T14 Evento](prd-t14-evento.md), [T25 Busca no acervo](prd-t25-busca-no-acervo.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 4 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que o aluno e o responsável enviem informações à psicopedagoga, para que ela receba o que a família quer contar sem depender de outros canais.

## 2. Escopo

### O que entra no escopo

- Formulário "Enviar informação", para o aluno e o responsável.
- Aba "Informações enviadas" do perfil do aluno, para o autor e para a psicopedagoga.
- Lista "Informações recebidas", para a psicopedagoga, com detalhe, filtros e situação "Não lida" ou "Lida".
- Ações da psicopedagoga: marcar como lida ou não lida, abrir o perfil do aluno e "Registrar como acompanhamento".
- Anexos da informação.

### O que não entra no escopo

- Resposta da psicopedagoga pelo sistema: não existe. Se precisar conversar, ela marca um evento em [T14 Evento](prd-t14-evento.md) (RN-07).
- Conversa em tempo real entre usuários (seção 11 do índice).
- Registro de acompanhamento: é feito em [T10 Acompanhamentos](prd-t10-acompanhamentos.md). Aqui só se abre T10 com o texto da informação.
- Lista de notificações: fica em [T03 Notificações](prd-t03-notificacoes.md).
- Busca em todo o acervo: fica em [T25 Busca no acervo](prd-t25-busca-no-acervo.md).
- Edição e exclusão da informação depois de enviada: não existem (RN-06).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Recebe as informações. Lê o detalhe, marca como lida ou não lida, abre o perfil do aluno e registra como acompanhamento. Não envia nem responde pelo sistema. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Aluno | Envia informações sobre si e vê só as que ele mesmo enviou, com a situação "Enviada" ou "Lida pela psicopedagoga". Não vê as do responsável. |
| Responsável | Envia informações em nome do aluno vinculado e vê só as que ele mesmo enviou. Não vê as do aluno. Usa o aluno escolhido no Início. |

**Contexto:** o aluno ou o responsável chega aqui quando tem algo a contar à psicopedagoga, como uma mudança em casa ou na saúde, ou uma dificuldade nova. A psicopedagoga chega para ler o que chegou e decidir o que fazer.

**Origem da jornada:** Início → atalho "Enviar informação" (aluno e responsável). Menu → Enviar informação (aluno e responsável). Perfil do aluno → ação "Enviar informação" (aluno e responsável). Perfil do aluno → aba "Informações enviadas". Início → bloco de informações não lidas (psicopedagoga). Menu → Informações recebidas (psicopedagoga). Notificação "Informação enviada" (psicopedagoga).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Formulário "Enviar informação" | Campos da seção 5.1. Aparece para o aluno e o responsável (visão "Enviar", ver 6.5). |
| Aba "Informações enviadas" do perfil | Fica no perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). Colunas: data, assunto e situação. O aluno e o responsável veem só as que eles enviaram. A psicopedagoga vê todas, com o autor (RN-03). |
| Situação na aba "Informações enviadas" | "Enviada" ou "Lida pela psicopedagoga" (ver 6.6). |
| Lista "Informações recebidas" | Só para a psicopedagoga. Colunas: aluno, autor (aluno ou responsável), assunto, data e situação ("Não lida" ou "Lida"). |
| Detalhe da informação | Texto completo e anexos, com o aluno, o autor, o assunto e a data. Ao abrir, a informação vira "Lida" (RN-05). |
| Ações da psicopedagoga | "Marcar como lida", "Marcar como não lida", "Abrir o perfil do aluno" e "Registrar como acompanhamento". |
| Total de resultados | Quantidade de informações da lista, com 20 itens por página (RG-19). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Aluno | Sim | Preenchido para o aluno. O responsável escolhe entre os alunos vinculados. |
| Assunto | Sim | Até 100 caracteres. |
| Texto | Sim | Até 2.000 caracteres. |
| Anexos | Não | Segue RG-16. |

### 5.2 Filtros

Filtros da lista "Informações recebidas" (psicopedagoga):

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Situação | Ver "Opções do filtro de situação" em 7.2 | Não lidas |
| Aluno | Alunos que a psicopedagoga vê (RG-07) | Sem filtro |
| Período | Intervalo de datas | Sem filtro |

A aba "Informações enviadas" não tem filtros. Filtros ativos seguem RG-21.

### 5.3 Ordenação e paginação

- Ordenação padrão: informações mais recentes primeiro.
- Outras ordenações: Não se aplica.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O aluno ou o responsável abre "Enviar informação" no menu, pelo atalho do Início ou pelo perfil do aluno.
2. O sistema abre o formulário. Para o aluno, o campo Aluno vem preenchido. Para o responsável, vem o aluno escolhido no Início (RN-02).
3. O usuário informa o assunto e o texto e, se quiser, anexa arquivos.
4. O usuário escolhe "Enviar".
5. O sistema registra a informação com a situação "Não lida", mostra a mensagem de sucesso e notifica as psicopedagogas (seção 8).
6. A informação aparece na aba "Informações enviadas" do autor, com a situação "Enviada".
7. A psicopedagoga abre "Informações recebidas", vê a lista com o filtro "Não lidas" e abre o detalhe. A informação vira "Lida" (RN-05).
8. A psicopedagoga decide: registra como acompanhamento, abre o perfil do aluno ou marca um evento, se precisar conversar (RN-07).

### 6.2 Fluxos alternativos

- Campo obrigatório vazio ou fora do limite: o sistema não envia, mostra a mensagem de erro e mantém o que foi digitado (RG-29).
- Falha ao enviar: o sistema mostra a mensagem de erro e o que foi digitado continua no formulário (RG-29).
- Sair do formulário com alterações não enviadas: o sistema pede confirmação (RG-29).
- Anexo fora das regras de RG-16: o sistema não aceita o arquivo e mostra a mensagem de erro.
- Psicopedagoga marca como não lida: a informação volta para "Não lida" e aparece de novo no filtro padrão (RN-05).
- Informação de aluno inativo: a psicopedagoga continua vendo (RG-07).
- Informação que o usuário não pode ver: abre "Não encontrado" (RG-13).
- Lista vazia: mostra a mensagem. Em "Informações recebidas" não há ação principal, porque a psicopedagoga não envia informações. Na aba "Informações enviadas", o aluno e o responsável veem a ação "Enviar informação" (RG-22).
- Responsável com mais de um aluno: o campo Aluno vem com o aluno escolhido, e o responsável pode escolher outro aluno vinculado.

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Enviar informação | Aluno e responsável | Registra a informação, notifica as psicopedagogas e não permite editar nem apagar depois (RN-06). |
| Ver as informações enviadas | Aluno, responsável e psicopedagoga | Mostra a aba "Informações enviadas" (RN-03). |
| Abrir o detalhe | Psicopedagoga | Mostra texto e anexos e marca como "Lida" (RN-05). |
| Marcar como lida | Psicopedagoga | Muda a situação para "Lida" sem abrir o detalhe (RN-05). |
| Marcar como não lida | Psicopedagoga | Muda a situação para "Não lida" (RN-05). |
| Abrir o perfil do aluno | Psicopedagoga | Abre [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) do aluno da informação. |
| Registrar como acompanhamento | Psicopedagoga | Abre [T10 Acompanhamentos](prd-t10-acompanhamentos.md) com o texto da informação. O registro é concluído em T10. |
| Filtrar | Psicopedagoga | Aplica os filtros da seção 5.2. |
| Limpar filtros | Psicopedagoga | Remove todos os filtros de uma vez (RG-21). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra a mensagem de lista vazia (seção 9). Na aba "Informações enviadas", mostra também a ação "Enviar informação" (RG-22). |
| Vazio, por causa dos filtros | Mostra a mensagem e a opção "Limpar filtros" (RG-22). |
| Sem permissão | Professor abre "Acesso negado". Informação que o usuário não pode ver abre "Não encontrado" (RG-13). Conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Abre "Sem conexão" ou "Erro inesperado", conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Erro ao enviar mantém o formulário preenchido (RG-29). |

### 6.5 Visões da tela

| Visão | Perfis | Onde fica | Conteúdo |
| --- | --- | --- | --- |
| Enviar informação | Aluno e responsável | Menu "Enviar informação", atalho do Início e ação no cabeçalho do perfil do aluno | Formulário da seção 5.1. O responsável usa o aluno escolhido no Início ([T02 Início](prd-t02-inicio.md)). |
| Informações enviadas | Aluno, responsável e psicopedagoga | Aba "Informações enviadas" do perfil do aluno | Data, assunto e situação. Cada pessoa vê só as que enviou. A psicopedagoga vê todas, com o autor. |
| Informações recebidas | Psicopedagoga | Menu "Informações recebidas" | Lista com filtros, detalhe e ações de lida, perfil e acompanhamento. |

### 6.6 Situação exibida

A situação da informação é "Não lida" ou "Lida" (seção 6 do índice). Cada visão mostra um nome.

| Onde | Quem vê | Situação "Não lida" | Situação "Lida" |
| --- | --- | --- | --- |
| Lista "Informações recebidas" | Psicopedagoga | Não lida | Lida |
| Aba "Informações enviadas" | Todos que veem a aba (aluno, responsável e psicopedagoga) | Enviada | Lida pela psicopedagoga |

### 6.7 Onde a informação aparece e fase de entrega

Esta tela é da fase 4. As partes das outras telas que dependem dela só aparecem a partir dessa fase (seção 9 do índice).

| Onde | O que aparece | Fase |
| --- | --- | --- |
| [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) | Aba "Informações enviadas" e ação "Enviar informação" no cabeçalho (aluno e responsável). | 4 |
| [T02 Início](prd-t02-inicio.md) | Bloco de informações não lidas (psicopedagoga) e atalho "Enviar informação" (aluno e responsável). | 4 |
| [T03 Notificações](prd-t03-notificacoes.md) | Notificação "Informação enviada". | 4 |
| Menu | "Informações recebidas" (psicopedagoga) e "Enviar informação" (aluno e responsável). | 4 |
| [T10 Acompanhamentos](prd-t10-acompanhamentos.md) | Ação "Registrar como acompanhamento" abre T10 com o texto da informação. | 4 |
| [T25 Busca no acervo](prd-t25-busca-no-acervo.md) | Busca em "Informações recebidas". | 5 |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Só o aluno e o responsável enviam informações. A psicopedagoga recebe. O professor não acessa esta tela. |
| RN-02 | No campo Aluno, o aluno vê o próprio nome preenchido. O responsável escolhe entre os alunos vinculados a ele (RG-09), usando o aluno escolhido no Início como ponto de partida. Aluno com 18 anos ou mais só aparece para o responsável com autorização do aluno (RG-17). |
| RN-03 | O aluno e o responsável veem só as informações que eles mesmos enviaram: o aluno não vê o que o responsável mandou, e o responsável não vê o que o aluno mandou. A psicopedagoga vê todas, com o autor, inclusive as de alunos inativos (RG-07). |
| RN-04 | A aba "Informações enviadas" mostra data, assunto e a situação "Enviada" ou "Lida pela psicopedagoga", para todos que veem a aba (ver 6.6). |
| RN-05 | A informação nasce "Não lida". Vira "Lida" quando a psicopedagoga abre o detalhe. Ela pode marcar de novo como "Não lida". A situação vale para todas as psicopedagogas: quando uma abre a informação, ela fica "Lida" para todas (seção 6 do índice). |
| RN-06 | Depois de enviada, a informação não pode ser editada nem apagada. |
| RN-07 | A psicopedagoga não responde pelo sistema. Se precisar conversar, marca um evento ([T14 Evento](prd-t14-evento.md)). |
| RN-08 | "Registrar como acompanhamento" abre [T10 Acompanhamentos](prd-t10-acompanhamentos.md) com o texto da informação. |
| RN-09 | Ao enviar, as psicopedagogas recebem notificação (seção 7 do índice). Ninguém recebe notificação da própria ação (RG-25). |
| RN-10 | O anexo tem a mesma visibilidade da informação (RG-12) e segue RG-16. |
| RN-11 | O assunto tem até 100 caracteres e o texto tem até 2.000 caracteres. |
| RN-12 | A lista "Informações recebidas" tem o filtro de situação com padrão "Não lidas", e os filtros de aluno e período. Ordena pelas mais recentes primeiro. |
| RN-13 | O menu "Informações recebidas" é da psicopedagoga e o menu "Enviar informação" é do aluno e do responsável (seção 8 do índice). |
| RN-14 | Segue RG-09, RG-12, RG-13, RG-16, RG-17, RG-19 a RG-24 e RG-29. |
| RN-15 | O envio pede confirmação, porque a informação não pode ser editada nem apagada depois e as psicopedagogas são notificadas (RG-23). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Autor depois que a informação volta para "Não lida" | Quando a psicopedagoga marca como "Não lida", o autor volta a ver "Enviada". |
| Opções do filtro de situação | Não lidas, Lidas e Todas. |
| Ordem da aba "Informações enviadas" | Mais recentes primeiro, como em "Informações recebidas". |
| Detalhe para o autor | Ao escolher uma informação na aba "Informações enviadas", o autor lê o texto e os anexos que enviou, só para leitura. |
| Aluno do formulário do responsável | O campo Aluno vem com o aluno do cabeçalho. Se o responsável escolher outro aluno no campo, o aluno do cabeçalho muda também. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Informação enviada | Psicopedagogas. O autor não recebe (RG-25). | Avisa que o aluno ou o responsável enviou uma informação, com o nome do aluno e o assunto. |

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Situação na aba, informação não lida | Aviso | Enviada |
| Situação na aba, informação lida | Aviso | Lida pela psicopedagoga |
| Confirmação de envio | Confirmação | Enviar a informação à psicopedagoga. Depois de enviada, você não poderá editar nem apagar. (proposta) |
| Informação enviada | Sucesso | Informação enviada à psicopedagoga. (proposta) |
| Campo obrigatório vazio ou acima do limite | Erro | Preencha os campos obrigatórios e respeite os limites de caracteres para enviar a informação. (proposta) |
| Falha ao enviar | Erro | Não foi possível enviar a informação. O que você digitou foi mantido. Tente enviar de novo. (proposta) |
| Anexo fora das regras | Erro | Anexe só arquivos PDF, JPG ou PNG, com até 10 MB cada e no máximo 5 por informação. (proposta) |
| Sair com alterações não enviadas | Confirmação | Sair descarta o que você digitou e não enviou. (proposta) |
| Lista de informações recebidas vazia, sem nenhum registro | Aviso | Nenhuma informação recebida. (proposta) |
| Aba de informações enviadas vazia | Aviso | Nenhuma informação enviada. (proposta) |
| Lista vazia, por causa dos filtros | Aviso | Nenhuma informação encontrada com estes filtros. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Enviar informação | Não | Não | Sim, só para si | Sim, só para alunos vinculados |
| Ver a aba "Informações enviadas" | Sim, todas, com o autor | Não | Só as que ele enviou | Só as que ele enviou |
| Ver a lista "Informações recebidas" e o detalhe | Sim | Não | Não | Não |
| Marcar como lida ou não lida | Sim | Não | Não | Não |
| Abrir o perfil do aluno a partir da informação | Sim | Não | Não | Não |
| Registrar como acompanhamento | Sim | Não | Não | Não |
| Editar ou apagar uma informação enviada | Não | Não | Não | Não |
| Filtrar a lista "Informações recebidas" | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado um aluno, quando ele abre "Enviar informação", então o formulário abre com o campo Aluno preenchido com o nome dele, Assunto, Texto e Anexos (RN-02).
- [ ] Dado um responsável com um aluno escolhido, quando ele abre "Enviar informação", então o campo Aluno vem com o aluno escolhido e a lista de opções mostra só os alunos vinculados a ele (RN-02).
- [ ] Dado o formulário preenchido com assunto e texto, quando o usuário envia, então o sistema registra a informação com a situação "Não lida" e mostra a mensagem de sucesso (RN-05).
- [ ] Dado o campo Assunto, quando o usuário digita mais de 100 caracteres, então o sistema não envia e mostra a mensagem de erro (RN-11).
- [ ] Dado o campo Texto, quando o usuário digita mais de 2.000 caracteres, então o sistema não envia e mostra a mensagem de erro (RN-11).
- [ ] Dado um campo obrigatório vazio, quando o usuário envia, então o sistema não envia e mantém o que foi digitado (RG-29).
- [ ] Dado que o envio falhou, quando a mensagem de erro aparece, então o que o usuário digitou continua no formulário (RG-29).
- [ ] Dado o formulário preenchido, quando o usuário escolhe "Enviar", então o sistema pede confirmação dizendo que a informação não poderá ser editada nem apagada depois (RN-15, RG-23).
- [ ] Dado alterações não enviadas, quando o usuário tenta sair do formulário, então o sistema pede confirmação (RG-29).
- [ ] Dado um anexo em PDF, JPG ou PNG de até 10 MB, quando o usuário anexa até 5 arquivos, então o sistema aceita (RG-16).
- [ ] Dado um anexo fora das regras de RG-16, quando o usuário tenta anexar, então o sistema não aceita e mostra a mensagem de erro.
- [ ] Dado uma informação enviada, quando ela é registrada, então as psicopedagogas recebem a notificação "Informação enviada" (RN-09).
- [ ] Dado uma informação enviada pelo aluno ou pelo responsável, quando ela é registrada, então o autor não recebe notificação (RG-25).
- [ ] Dado uma informação enviada, quando o autor abre a aba "Informações enviadas", então vê a data, o assunto e a situação "Enviada" (RN-04).
- [ ] Dado uma informação enviada e ainda não aberta pela psicopedagoga, quando o autor abre a aba, então a situação mostra "Enviada", e não "Não lida" (6.6).
- [ ] Dado uma informação aberta pela psicopedagoga, quando o autor abre a aba, então a situação mostra "Lida pela psicopedagoga" (RN-04).
- [ ] Dado que o aluno e o responsável enviaram uma informação cada, quando o aluno abre a aba, então vê só a que ele enviou (RN-03).
- [ ] Dado que o aluno e o responsável enviaram uma informação cada, quando o responsável abre a aba, então vê só a que ele enviou (RN-03).
- [ ] Dado uma informação enviada, quando o aluno ou o responsável procura a ação de editar ou apagar, então ela não existe (RN-06).
- [ ] Dado a psicopedagoga, quando ela abre a aba "Informações enviadas" do perfil de um aluno, então vê todas as informações dele, com o autor, e a situação aparece como "Enviada" ou "Lida pela psicopedagoga" (RN-03, RN-04).
- [ ] Dado a psicopedagoga, quando ela abre "Informações recebidas", então vê a lista com aluno, autor, assunto, data e situação, com o filtro de situação em "Não lidas" (RN-12).
- [ ] Dado a lista "Informações recebidas", quando não há outros filtros, então as informações aparecem das mais recentes para as mais antigas (RN-12).
- [ ] Dado a psicopedagoga na lista, quando filtra por aluno ou por período, então a lista mostra só as informações que atendem aos filtros, e os filtros ativos ficam visíveis (RG-21).
- [ ] Dado mais de 20 informações, quando a lista abre, então mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado filtros que não retornam resultados, quando a lista abre, então mostra a opção de limpar os filtros (RG-22).
- [ ] Dado uma informação "Não lida", quando a psicopedagoga abre o detalhe, então o detalhe mostra o texto e os anexos e a situação passa para "Lida" (RN-05).
- [ ] Dado uma informação "Não lida" e duas psicopedagogas ativas, quando uma delas abre o detalhe, então a informação aparece como "Lida" também para a outra (RN-05).
- [ ] Dado uma informação "Lida", quando a psicopedagoga escolhe "Marcar como não lida", então a situação passa para "Não lida" (RN-05).
- [ ] Dado uma informação "Não lida", quando a psicopedagoga escolhe "Marcar como lida" sem abrir o detalhe, então a situação passa para "Lida" (RN-05).
- [ ] Dado o detalhe aberto, quando a psicopedagoga escolhe "Abrir o perfil do aluno", então o perfil do aluno abre ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)).
- [ ] Dado o detalhe aberto, quando a psicopedagoga escolhe "Registrar como acompanhamento", então [T10 Acompanhamentos](prd-t10-acompanhamentos.md) abre com o texto da informação (RN-08).
- [ ] Dado o detalhe aberto, quando a psicopedagoga procura uma ação para responder pelo sistema, então ela não existe (RN-07).
- [ ] Dado um aluno inativo com informações enviadas, quando a psicopedagoga abre a lista, então vê as informações dele (RN-03, RG-07).
- [ ] Dado um anexo da informação, quando quem vê a informação abre o anexo, então o anexo abre, e quem não vê a informação não acessa o anexo (RN-10).
- [ ] Dado um professor, quando ele tenta abrir "Informações recebidas" ou "Enviar informação", então o sistema mostra "Acesso negado" (RG-13).
- [ ] Dado a psicopedagoga, quando ela abre o menu, então vê "Informações recebidas" e não vê "Enviar informação" (RN-13).
- [ ] Dado um aluno ou um responsável, quando abre o menu, então vê "Enviar informação" e não vê "Informações recebidas" (RN-13).
- [ ] Dado um aluno ou um responsável, quando tenta abrir "Informações recebidas", então o sistema mostra "Acesso negado" (RG-13).
- [ ] Dado uma informação de outro usuário, quando o aluno ou o responsável tenta abri-la, então o sistema mostra "Não encontrado" (RG-13).
- [ ] Dado nenhuma informação enviada, quando o aluno abre a aba "Informações enviadas", então vê a mensagem de lista vazia e a ação "Enviar informação" (RG-22).
- [ ] Dado que a conexão caiu, quando a tela abre, então o sistema mostra "Sem conexão", conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md).
- [ ] Dado a tela aberta no celular, quando o usuário usa só o teclado, então consegue enviar, filtrar e marcar como lida (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
