# PRD da tela de Observações dos professores

| Campo | Valor |
| --- | --- |
| Identificador | T17 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T03 Notificações](prd-t03-notificacoes.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md), [T19 Turmas](prd-t19-turmas.md), [T21 Professores](prd-t21-professores.md), [T25 Busca no acervo](prd-t25-busca-no-acervo.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 3 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que o professor registre como está o desempenho do aluno na disciplina dele, para que a psicopedagoga acompanhe o aluno com a visão de cada professor.

## 2. Escopo

### O que entra no escopo

- Aba "Observações dos professores" do perfil do aluno, com a lista de observações.
- Registro de observação do professor.
- Editar e excluir a própria observação.
- Filtros por período, professor e disciplina.

### O que não entra no escopo

- Registro de acompanhamento da psicopedagoga: fica em [T10 Acompanhamentos](prd-t10-acompanhamentos.md). A observação do professor é outro registro (RN-01).
- Atividade que o professor adaptou para o aluno: fica em [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md).
- Leitura pelo aluno e pelo responsável: não existe (RN-02).
- Lista de notificações: fica em [T03 Notificações](prd-t03-notificacoes.md).
- Busca em todo o acervo: fica em [T25 Busca no acervo](prd-t25-busca-no-acervo.md).
- Anexos: a observação não tem anexos (seção 5.1).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê todas as observações dos professores do aluno. Não registra, não edita e não exclui. |
| Professor | Registra observações dos alunos das suas turmas e vê só as próprias. Edita e exclui só as próprias. |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). A aba não aparece no perfil dele. |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). A aba não aparece no perfil do aluno vinculado. |

**Contexto:** o professor chega aqui quando quer registrar como o aluno está indo na disciplina dele. A psicopedagoga chega para ler o que os professores observaram.

**Origem da jornada:** Início → atalho "Registrar observação" (professor). Menu → Alunos → Perfil do aluno → aba "Observações dos professores". Perfil do aluno → ação "Registrar observação" (professor). Notificação "Observação do professor registrada" (psicopedagoga). Início → bloco de observações dos últimos 7 dias (psicopedagoga).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Aba "Observações dos professores" | Fica no perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). Aparece para a psicopedagoga (todas as observações) e para o professor (só as próprias). Não aparece para aluno nem responsável. |
| Lista de observações | Colunas: data, disciplina, assunto, professor e texto. |
| Ação "Registrar observação" | Abre o formulário para o aluno do perfil. Aparece só para o professor, no cabeçalho do perfil e na aba. |
| Autoria da observação | Mostra quem registrou e quando, e "Editado em" com data e autor da última alteração (RG-15). |
| Ações do autor | "Editar" e "Excluir" aparecem só para o professor autor. "Excluir" some depois de 24 horas do registro (RN-05). |
| Total de resultados | Quantidade de observações da lista, com 20 itens por página (RG-19). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Data | Sim | Não pode ser futura. |
| Disciplina | Sim | Disciplinas do professor na turma do aluno. |
| Assunto | Sim | Desempenho, Comportamento, Frequência ou Outro. |
| Observação | Sim | Até 2.000 caracteres. |

O formulário não tem campo "Aluno": a observação é do aluno do perfil (ou do aluno escolhido no atalho do Início, ver 7.2).

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Período | Intervalo de datas | Sem filtro |
| Professor | Professores que registraram observações do aluno | Sem filtro |
| Disciplina | Disciplinas das observações do aluno | Sem filtro |

Filtros ativos seguem RG-21. O filtro "Professor" para o professor está em "Filtro Professor para o professor" em 7.2.

### 5.3 Ordenação e paginação

- Ordenação padrão: data da observação, da mais recente para a mais antiga.
- Outras ordenações: Não se aplica.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O professor abre o perfil de um aluno atendido e escolhe a aba "Observações dos professores", ou usa o atalho "Registrar observação" do Início.
2. O professor escolhe "Registrar observação".
3. O sistema abre o formulário.
4. O professor informa a data, a disciplina, o assunto e a observação.
5. O professor escolhe "Salvar".
6. O sistema registra a observação com o nome do professor e a data do registro, e mostra a mensagem de sucesso.
7. O sistema notifica as psicopedagogas (seção 8). A observação aparece na lista só para o professor autor e para a psicopedagoga (RN-02).

### 6.2 Fluxos alternativos

- Campo obrigatório vazio ou inválido, como data futura: o sistema não salva, mostra a mensagem de erro e mantém o que foi digitado (RG-29).
- Falha ao salvar: o sistema mostra a mensagem de erro e o que foi digitado continua no formulário (RG-29).
- Sair do formulário com alterações não salvas: o sistema pede confirmação (RG-29).
- Observação de outro professor: o professor não a vê na lista (RN-02). Se tentar abrir uma observação que não é dele, o sistema mostra "Não encontrado" (RG-13).
- Observação com mais de 24 horas: "Excluir" não aparece. "Editar" continua disponível para o autor (RN-05).
- Aluno que muda de turma: o professor da turma anterior perde o acesso ao aluno e às observações dele, inclusive às que registrou (RN-10).
- Lista vazia: mostra a mensagem e, para o professor, a ação "Registrar observação" (RG-22).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Registrar | Professor | Cria a observação do aluno e notifica as psicopedagogas (RN-07). |
| Editar | Professor autor | Abre o formulário preenchido. Ao salvar, a observação mostra "Editado em" (RG-15). |
| Excluir | Professor autor, até 24 horas depois de registrar | Pede confirmação (RG-23). Depois de confirmar, remove a observação da lista (RN-05). |
| Filtrar | Psicopedagoga e professor | Aplica os filtros da seção 5.2. |
| Limpar filtros | Psicopedagoga e professor | Remove todos os filtros de uma vez (RG-21). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra a mensagem de lista vazia e, para o professor, a ação "Registrar observação" (RG-22). |
| Vazio, por causa dos filtros | Mostra a mensagem e a opção "Limpar filtros" (RG-22). |
| Sem permissão | Aluno e responsável abrem "Acesso negado". Observação ou aluno que o usuário não pode ver abre "Não encontrado" (RG-13). Conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Abre "Sem conexão" ou "Erro inesperado", conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Erro ao salvar mantém o formulário preenchido (RG-29). |

### 6.5 Onde a observação aparece e fase de entrega

Esta tela é da fase 3. As partes das outras telas que dependem dela só aparecem a partir dessa fase (seção 9 do índice).

| Onde | O que aparece | Fase |
| --- | --- | --- |
| [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) | Aba "Observações dos professores" (psicopedagoga: todas; professor: só as próprias) e ação "Registrar observação" no cabeçalho (professor). | 3 |
| [T02 Início](prd-t02-inicio.md) | Bloco de observações dos últimos 7 dias (psicopedagoga) e atalho "Registrar observação" (professor). | 3 |
| [T03 Notificações](prd-t03-notificacoes.md) | Notificação "Observação do professor registrada". | 3 |
| [T25 Busca no acervo](prd-t25-busca-no-acervo.md) | Busca em "Observações dos professores". | 5 |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A observação do professor é diferente do acompanhamento ([T10 Acompanhamentos](prd-t10-acompanhamentos.md)), que é registro da psicopedagoga. |
| RN-02 | O professor vê só as próprias observações e não vê as de outros professores. A psicopedagoga vê todas. Aluno e responsável não veem. |
| RN-03 | A aba "Observações dos professores" fica no perfil do aluno. O professor só chega a alunos ativos das suas turmas (RG-08) e não vê dados de saúde, contatos, endereço nem data de nascimento do aluno (RG-11). A psicopedagoga vê alunos ativos e inativos (RG-07). |
| RN-04 | A data da observação não pode ser futura. A disciplina é uma das disciplinas do professor na turma do aluno. O assunto é Desempenho, Comportamento, Frequência ou Outro. |
| RN-05 | O autor edita a observação e exclui até 24 horas depois de registrar. O prazo de 24 horas vale só para excluir. A exclusão pede confirmação (RG-23). Só o autor edita e exclui. |
| RN-06 | Todo registro mostra quem criou e quando. Registro alterado mostra "Editado em" com data e autor da última alteração (RG-15). |
| RN-07 | Ao registrar, as psicopedagogas recebem notificação (seção 7 do índice). Ninguém recebe notificação da própria ação (RG-25). |
| RN-08 | O professor registra observação só de aluno das suas turmas. |
| RN-09 | Segue RG-13, RG-18, RG-19 a RG-24 e RG-29. |
| RN-10 | Quando o aluno muda para uma turma em que o professor não leciona, o professor perde o acesso ao aluno (RG-08) e às observações dele, inclusive às que ele mesmo registrou. A psicopedagoga continua vendo todas. |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Escolha do aluno no atalho do Início | O atalho "Registrar observação" pede que o professor escolha antes um aluno atendido das suas turmas. Depois da escolha, abre o formulário do aluno. |
| Notificação na edição | Editar não gera notificação para as psicopedagogas. A observação mostra "Editado em" (RG-15). |
| Filtro Professor para o professor | O filtro "Professor" não aparece para o professor, que só vê as próprias observações. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Observação do professor registrada | Psicopedagogas. O professor autor não recebe (RG-25). | Avisa que um professor registrou uma observação sobre o aluno, com disciplina e assunto. |

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Observação salva | Sucesso | Observação registrada. (proposta) |
| Edição salva | Sucesso | Observação atualizada. (proposta) |
| Confirmação de exclusão | Confirmação | Excluir esta observação. Ela deixa de aparecer na lista do aluno e não pode ser recuperada. (proposta) |
| Exclusão feita | Sucesso | Observação excluída. (proposta) |
| Campo obrigatório vazio ou inválido | Erro | Preencha os campos obrigatórios, informe uma data que não seja futura e respeite o limite de caracteres para salvar a observação. (proposta) |
| Falha ao salvar | Erro | Não foi possível salvar a observação. O que você digitou foi mantido. Tente salvar de novo. (proposta) |
| Sair com alterações não salvas | Confirmação | Sair descarta o que você digitou e não salvou. (proposta) |
| Lista vazia, sem nenhum registro | Aviso | Nenhuma observação registrada. (proposta) |
| Lista vazia, por causa dos filtros | Aviso | Nenhuma observação encontrada com estes filtros. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Ver a aba "Observações dos professores" | Sim, todas | Só as próprias, de alunos das suas turmas | Não | Não |
| Registrar | Não | Só para alunos das suas turmas | Não | Não |
| Editar | Não | Só as que registrou | Não | Não |
| Excluir | Não | Só as que registrou, até 24 horas depois de registrar | Não | Não |
| Filtrar a lista | Sim | Sim, só entre as próprias | Não | Não |

## 11. Critérios de aceite

- [ ] Dado um professor que leciona na turma do aluno, quando ele abre o perfil do aluno e escolhe "Registrar observação", então o formulário abre com os campos Data, Disciplina, Assunto e Observação e sem campo "Aluno".
- [ ] Dado o formulário aberto, quando o professor informa a data, a disciplina, o assunto e a observação e salva, então o sistema registra a observação com o nome do professor e a data do registro (RN-06).
- [ ] Dado o campo Data, quando o professor informa uma data futura e salva, então o sistema não salva e mostra a mensagem de erro (RN-04).
- [ ] Dado o campo Disciplina, quando o professor abre a lista de opções, então vê só as disciplinas dele na turma do aluno (RN-04).
- [ ] Dado o campo Assunto, quando o professor abre a lista de opções, então vê Desempenho, Comportamento, Frequência e Outro (RN-04).
- [ ] Dado o campo Observação, quando o professor digita mais de 2.000 caracteres e salva, então o sistema não salva e mostra a mensagem de erro.
- [ ] Dado um campo obrigatório vazio, quando o professor salva, então o sistema não salva e mantém o que foi digitado (RG-29).
- [ ] Dado que salvar falhou, quando a mensagem de erro aparece, então o que o professor digitou continua no formulário (RG-29).
- [ ] Dado alterações não salvas, quando o professor tenta sair do formulário, então o sistema pede confirmação (RG-29).
- [ ] Dado uma observação registrada, quando ela é salva, então as psicopedagogas recebem a notificação "Observação do professor registrada" (RN-07).
- [ ] Dado uma observação registrada pelo professor, quando ela é salva, então o professor autor não recebe notificação (RG-25).
- [ ] Dado dois professores que registraram observações do mesmo aluno, quando um deles abre a aba, então vê só as próprias observações (RN-02).
- [ ] Dado uma observação de outro professor, quando o professor tenta abri-la, então o sistema mostra "Não encontrado" (RG-13).
- [ ] Dado a psicopedagoga, quando ela abre a aba "Observações dos professores" de um aluno, então vê as observações de todos os professores (RN-02).
- [ ] Dado a psicopedagoga, quando ela abre a aba, então não vê as ações "Registrar observação", "Editar" e "Excluir" (seção 10).
- [ ] Dado um aluno ou um responsável, quando abre o perfil, então a aba "Observações dos professores" não aparece (RN-02).
- [ ] Dado um aluno ou um responsável, quando tenta abrir a tela de observações, então o sistema mostra "Acesso negado" (RG-13).
- [ ] Dado um aluno inativo, quando o professor tenta abrir o perfil dele, então o sistema não o mostra (RN-03, RG-08).
- [ ] Dado um professor que registrou uma observação de um aluno, quando o aluno muda para uma turma em que ele não leciona, então o professor não vê mais o aluno nem essa observação, e a psicopedagoga continua vendo a observação (RN-10).
- [ ] Dado um aluno inativo, quando a psicopedagoga abre a aba, então vê as observações dele (RN-03, RG-07).
- [ ] Dado a aba aberta, quando não há filtros, então as observações aparecem da mais recente para a mais antiga, com data, disciplina, assunto, professor e texto.
- [ ] Dado a psicopedagoga na aba, quando filtra por professor, disciplina ou período, então a lista mostra só as observações que atendem aos filtros e os filtros ativos ficam visíveis (RG-21).
- [ ] Dado filtros que não retornam resultados, quando a lista abre, então mostra a opção de limpar os filtros (RG-22).
- [ ] Dado nenhuma observação registrada, quando o professor abre a aba, então vê a mensagem de lista vazia e a ação "Registrar observação" (RG-22).
- [ ] Dado mais de 20 observações, quando a lista abre, então mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado uma observação registrada há menos de 24 horas, quando o autor escolhe "Excluir", então o sistema pede confirmação dizendo a ação e a consequência (RN-05, RG-23).
- [ ] Dado a confirmação de exclusão, quando o autor confirma, então a observação sai da lista (RN-05).
- [ ] Dado uma observação registrada há mais de 24 horas, quando o autor abre a aba, então não vê a ação "Excluir" e continua vendo "Editar" (RN-05).
- [ ] Dado uma observação editada pelo autor, quando a lista abre, então ela mostra "Editado em" com a data e o autor da última alteração (RN-06).
- [ ] Dado uma observação de outro professor, quando o professor abre a lista, então não vê as ações "Editar" e "Excluir" nem a observação (RN-02, RN-05).
- [ ] Dado a observação do professor e o acompanhamento da psicopedagoga, quando o professor abre o perfil, então vê só a aba de observações dele e não vê acompanhamentos (RN-01).
- [ ] Dado que a conexão caiu, quando a aba abre, então o sistema mostra "Sem conexão", conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md).
- [ ] Dado a tela aberta no celular, quando o usuário usa só o teclado, então consegue registrar, filtrar e excluir (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
