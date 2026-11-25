# PRD da tela de Atividades adaptadas

| Campo | Valor |
| --- | --- |
| Identificador | T16 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T03 Notificações](prd-t03-notificacoes.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T13 Agenda](prd-t13-agenda.md), [T19 Turmas](prd-t19-turmas.md), [T21 Professores](prd-t21-professores.md), [T25 Busca no acervo](prd-t25-busca-no-acervo.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 3 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que o professor registre as atividades adaptadas para cada aluno, para que a psicopedagoga acompanhe e o aluno e o responsável conheçam a adaptação.

## 2. Escopo

### O que entra no escopo

- Lista geral de atividades adaptadas, para a psicopedagoga e o professor.
- Aba "Atividades adaptadas" do perfil do aluno, para todos os perfis.
- Registro de atividade adaptada para um ou mais alunos.
- Ver, editar e excluir uma atividade adaptada.
- Anexos da atividade.
- Filtros por aluno, turma, disciplina, professor e período.

### O que não entra no escopo

- Registro de desempenho do aluno na disciplina: fica em [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md).
- Registro de acompanhamento da psicopedagoga: fica em [T10 Acompanhamentos](prd-t10-acompanhamentos.md).
- Cadastro das disciplinas do professor em cada turma: fica em [T19 Turmas](prd-t19-turmas.md) e [T21 Professores](prd-t21-professores.md).
- Lista de notificações: fica em [T03 Notificações](prd-t03-notificacoes.md).
- Busca em todo o acervo: fica em [T25 Busca no acervo](prd-t25-busca-no-acervo.md).
- Registro, edição e exclusão pela psicopedagoga, pelo aluno e pelo responsável: não existem (RN-04).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê todas as atividades adaptadas, na lista geral e na aba do perfil. Não registra, não edita e não exclui. |
| Professor | Registra atividades adaptadas e vê todas as dos alunos das suas turmas, inclusive as de outros professores. Edita e exclui só as que registrou. |
| Aluno | Lê as atividades adaptadas dele, pela aba do perfil. Não acessa a lista geral. Abre "Acesso negado" (RG-13). |
| Responsável | Lê as atividades adaptadas do aluno vinculado, pela aba do perfil. Não acessa a lista geral. Abre "Acesso negado" (RG-13). |

**Contexto:** o professor chega aqui depois de adaptar uma atividade para um ou mais alunos, ou quer ver o que os colegas adaptaram. A psicopedagoga chega para acompanhar as adaptações. O aluno e o responsável chegam para ler a atividade adaptada.

**Origem da jornada:** Início → atalho "Registrar atividade adaptada" (professor). Menu → Atividades adaptadas (psicopedagoga e professor). Perfil do aluno → aba "Atividades adaptadas" (todos os perfis). Perfil do aluno → ação "Registrar atividade adaptada" (professor). Agenda → "Novo" → "Atividade adaptada" (professor). Agenda → item da atividade. Notificação "Atividade adaptada registrada".

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Lista geral | Atividades adaptadas que o perfil pode ver (RN-03 e RN-05). Colunas: aluno, turma, disciplina, data, trecho da descrição, professor e anexos. |
| Aba "Atividades adaptadas" do perfil | Atividades adaptadas do aluno, com as mesmas colunas da lista geral. Aparece para todos os perfis que acessam o perfil ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). |
| Ação "Registrar atividade adaptada" | Abre o formulário. Aparece só para o professor, na lista geral e no cabeçalho do perfil do aluno. |
| Detalhe da atividade | Descrição completa, observações e anexos, com quem registrou e quando, e "Editado em" com data e autor quando houve alteração (RG-15). O aluno e os responsáveis veem a atividade inteira, inclusive as observações (RN-06). |
| Ações do autor | "Editar" e "Excluir" aparecem só para o professor autor. "Excluir" some depois de 24 horas do registro (RN-08). |
| Total de resultados | Quantidade de atividades da lista, com 20 itens por página (RG-19). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Alunos | Sim | Um ou mais, só das turmas do professor. Com mais de um aluno, o sistema cria um registro para cada. |
| Disciplina | Sim | Disciplinas do professor na turma do aluno. |
| Data | Sim | Qualquer data. |
| Descrição da atividade | Sim | Até 2.000 caracteres. |
| Observações | Não | Até 2.000 caracteres. |
| Anexos | Não | Segue RG-16. |

O formulário mostra o aviso "O aluno e os responsáveis veem esta atividade" (seção 9).

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Aluno | Alunos que o usuário pode ver | Sem filtro |
| Turma | Turmas dos alunos que o usuário pode ver | Sem filtro |
| Disciplina | Disciplinas das atividades que o usuário pode ver | Sem filtro |
| Professor | Professores que registraram atividades que o usuário pode ver | Sem filtro |
| Período | Intervalo de datas | Mês atual |

Os filtros da aba do perfil do aluno estão em "Filtros da aba para aluno e responsável" em 7.2. Filtros ativos seguem RG-21.

### 5.3 Ordenação e paginação

- Ordenação padrão: data da atividade, da mais recente para a mais antiga.
- Outras ordenações: Não se aplica.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O professor abre "Atividades adaptadas" no menu, o atalho do Início, o perfil do aluno ou a agenda.
2. O professor escolhe "Registrar atividade adaptada".
3. O sistema abre o formulário com o aviso "O aluno e os responsáveis veem esta atividade".
4. O professor escolhe um ou mais alunos das suas turmas, a disciplina, a data e a descrição. Se quiser, preenche observações e anexa arquivos.
5. O professor escolhe "Salvar".
6. O sistema cria um registro para cada aluno escolhido (RN-01) e mostra a mensagem de sucesso.
7. O sistema notifica as psicopedagogas, o aluno e os responsáveis do aluno (seção 8) e inclui a atividade na agenda do aluno, na data informada (RN-09).

### 6.2 Fluxos alternativos

- Campo obrigatório vazio ou inválido: o sistema não salva, mostra a mensagem de erro e mantém o que foi digitado (RG-29).
- Falha ao salvar: o sistema mostra a mensagem de erro e o que foi digitado continua no formulário (RG-29).
- Sair do formulário com alterações não salvas: o sistema pede confirmação (RG-29).
- Anexo fora das regras de RG-16: o sistema não aceita o arquivo e mostra a mensagem de erro.
- Atividade de outro professor: as ações "Editar" e "Excluir" não aparecem para quem não é o autor (RN-04).
- Atividade com mais de 24 horas: "Excluir" não aparece. "Editar" continua disponível para o autor (RN-08).
- Atividade ou aluno que o usuário não pode ver: abre "Não encontrado" (RG-13).
- Lista vazia: mostra a mensagem e, para o professor, a ação "Registrar atividade adaptada" (RG-22).
- Aluno que muda de turma: o professor da turma anterior perde o acesso ao aluno e às atividades dele, inclusive às que registrou (RN-16).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Registrar | Professor | Cria um registro para cada aluno escolhido, notifica e inclui na agenda do aluno (RN-01, RN-09 e RN-10). |
| Ver | Todos os perfis, conforme a seção 10 | Abre o detalhe da atividade, com observações e anexos (RN-06). |
| Editar | Professor autor | Abre o formulário preenchido. Ao salvar, o registro mostra "Editado em" (RG-15). |
| Excluir | Professor autor, até 24 horas depois de registrar | Pede confirmação (RG-23). Depois de confirmar, remove a atividade da lista e da agenda do aluno (RN-08). |
| Filtrar | Psicopedagoga e professor | Aplica os filtros da seção 5.2. |
| Limpar filtros | Psicopedagoga e professor | Remove todos os filtros de uma vez (RG-21). |
| Abrir a atividade pela agenda | Quem vê a atividade | Clicar no item da atividade na agenda abre o detalhe (RN-09). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra a mensagem de lista vazia e, para o professor, a ação "Registrar atividade adaptada" (RG-22). |
| Vazio, por causa dos filtros | Mostra a mensagem e a opção "Limpar filtros" (RG-22). |
| Sem permissão | Aluno e responsável na lista geral abrem "Acesso negado". Atividade que o usuário não pode ver abre "Não encontrado" (RG-13). Conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Abre "Sem conexão" ou "Erro inesperado", conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Erro ao salvar mantém o formulário preenchido (RG-29). |

### 6.5 Onde a atividade aparece e fase de entrega

Esta tela é da fase 3. As partes das outras telas que dependem dela só aparecem a partir dessa fase (seção 9 do índice).

| Onde | O que aparece | Fase |
| --- | --- | --- |
| [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) | Aba "Atividades adaptadas" (todos os perfis) e ação "Registrar atividade adaptada" no cabeçalho (professor). | 3 |
| [T13 Agenda](prd-t13-agenda.md) | Item no dia da atividade, sem horário, filtro Tipo "Atividade adaptada" e botão "Novo" → "Atividade adaptada" (professor). | 3 |
| [T02 Início](prd-t02-inicio.md) | Bloco de atividades dos últimos 7 dias (psicopedagoga) e atalho "Registrar atividade adaptada" (professor). | 3 |
| [T03 Notificações](prd-t03-notificacoes.md) | Notificação "Atividade adaptada registrada". | 3 |
| [T25 Busca no acervo](prd-t25-busca-no-acervo.md) | Busca em "Atividades adaptadas". | 5 |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Ao registrar para mais de um aluno, o sistema cria um registro para cada aluno. |
| RN-02 | O professor escolhe só alunos das suas turmas e só disciplinas dele na turma do aluno. |
| RN-03 | O professor vê todas as atividades adaptadas dos alunos das suas turmas, inclusive as de outros professores. A psicopedagoga vê todas. |
| RN-04 | Só o professor autor edita e exclui a atividade. Os outros professores só leem. A psicopedagoga, o aluno e o responsável só leem. |
| RN-05 | O aluno e o responsável leem só as atividades do aluno (RG-09). Aluno com 18 anos ou mais segue RG-17 para o responsável. |
| RN-06 | O aluno e os responsáveis veem a atividade inteira, inclusive as observações. O formulário avisa o professor: "O aluno e os responsáveis veem esta atividade". |
| RN-07 | O anexo tem a mesma visibilidade da atividade (RG-12) e segue RG-16. |
| RN-08 | O autor exclui a atividade até 24 horas depois de registrar. O prazo de 24 horas vale só para excluir. A exclusão pede confirmação (RG-23). |
| RN-09 | A atividade aparece na agenda do aluno na data informada, no dia, sem horário. O filtro Tipo "Atividade adaptada" e o botão "Novo" → "Atividade adaptada" (professor) estão em [T13 Agenda](prd-t13-agenda.md). Clicar no item abre a atividade. |
| RN-10 | Ao registrar, as psicopedagogas, o aluno e os responsáveis do aluno recebem notificação (seção 7 do índice). O responsável só recebe com conta ativa. Ninguém recebe notificação da própria ação (RG-25). |
| RN-11 | "Disciplina" é um texto no vínculo entre professor e turma ([T19 Turmas](prd-t19-turmas.md) e [T21 Professores](prd-t21-professores.md)). |
| RN-12 | Todo registro mostra quem criou e quando. Registro alterado mostra "Editado em" com data e autor da última alteração (RG-15). |
| RN-13 | A lista geral aparece no menu "Atividades adaptadas" da psicopedagoga e do professor (seção 8 do índice). |
| RN-14 | O professor vê só alunos ativos das suas turmas (RG-08). A psicopedagoga vê alunos ativos e inativos (RG-07). |
| RN-15 | Segue RG-13, RG-18, RG-19 a RG-24 e RG-29. |
| RN-16 | Quando o aluno muda para uma turma em que o professor não leciona, o professor perde o acesso ao aluno (RG-08) e às atividades adaptadas dele, inclusive às que ele mesmo registrou. A psicopedagoga continua vendo todas. |
| RN-17 | Editar ou excluir uma atividade adaptada não gera notificação. A atividade editada mostra "Editado em" ao aluno e aos responsáveis (RG-15). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Filtros da aba para aluno e responsável | A aba do perfil mostra aos dois só o filtro de período, com o mesmo padrão (mês atual). |
| Disciplina quando o professor tem várias na mesma turma | O professor escolhe uma das disciplinas dele na turma do aluno. Cada registro guarda uma disciplina. |
| Registro para alunos de turmas diferentes | O formulário usa uma única disciplina. Só aparecem a escolher as disciplinas que o professor tem em todas as turmas dos alunos escolhidos. |
| Anexos no registro para vários alunos | Cada registro criado recebe os mesmos anexos. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Atividade adaptada registrada | Psicopedagogas, o aluno e os responsáveis do aluno (responsável só com conta ativa). O professor autor não recebe (RG-25). | Avisa que uma atividade adaptada foi registrada para o aluno, com disciplina e data. Com vários alunos, cada aluno e seus responsáveis recebem o aviso do próprio registro. |

Editar ou excluir uma atividade adaptada não gera notificação (RN-17).

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Aviso no formulário | Aviso | O aluno e os responsáveis veem esta atividade |
| Registro salvo para um aluno | Sucesso | Atividade adaptada registrada. (proposta) |
| Registro salvo para vários alunos | Sucesso | Atividades adaptadas registradas, uma para cada aluno. (proposta) |
| Edição salva | Sucesso | Atividade adaptada atualizada. (proposta) |
| Confirmação de exclusão | Confirmação | Excluir esta atividade adaptada. Ela deixa de aparecer para o aluno e os responsáveis e não pode ser recuperada. (proposta) |
| Exclusão feita | Sucesso | Atividade adaptada excluída. (proposta) |
| Campo obrigatório vazio ou acima do limite | Erro | Preencha os campos obrigatórios e respeite os limites de caracteres para salvar a atividade adaptada. (proposta) |
| Falha ao salvar | Erro | Não foi possível salvar a atividade adaptada. O que você digitou foi mantido. Tente salvar de novo. (proposta) |
| Anexo fora das regras | Erro | Anexe só arquivos PDF, JPG ou PNG, com até 10 MB cada e no máximo 5 por atividade. (proposta) |
| Sair com alterações não salvas | Confirmação | Sair descarta o que você digitou e não salvou. (proposta) |
| Lista vazia, sem nenhum registro | Aviso | Nenhuma atividade adaptada registrada. (proposta) |
| Lista vazia, por causa dos filtros | Aviso | Nenhuma atividade adaptada encontrada com estes filtros. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Ver a lista geral | Sim, todas | Só alunos das suas turmas | Não | Não |
| Ver a aba "Atividades adaptadas" do perfil | Sim, todas | Só alunos das suas turmas | Só as próprias | Só as do aluno vinculado |
| Ver o detalhe, com observações e anexos | Sim | Só alunos das suas turmas | Só as próprias | Só as do aluno vinculado |
| Registrar | Não | Só para alunos das suas turmas | Não | Não |
| Editar | Não | Só as que registrou | Não | Não |
| Excluir | Não | Só as que registrou, até 24 horas depois de registrar | Não | Não |
| Filtrar a lista geral | Sim | Sim | Não | Não |

## 11. Critérios de aceite

- [ ] Dado um professor com alunos nas suas turmas, quando ele escolhe "Registrar atividade adaptada", então o formulário abre com os campos Alunos, Disciplina, Data, Descrição da atividade, Observações e Anexos e com o aviso "O aluno e os responsáveis veem esta atividade".
- [ ] Dado o formulário aberto, quando o professor escolhe um aluno, a disciplina, a data e a descrição e salva, então o sistema registra a atividade com o nome do professor e a data do registro (RN-12).
- [ ] Dado o formulário aberto, quando o professor escolhe três alunos e salva, então o sistema cria três registros, um para cada aluno (RN-01).
- [ ] Dado o campo Alunos, quando o professor abre a lista de opções, então vê só alunos ativos das suas turmas (RN-02, RN-14).
- [ ] Dado um aluno escolhido, quando o professor abre o campo Disciplina, então vê só as disciplinas dele na turma desse aluno (RN-02).
- [ ] Dado o campo Data, quando o professor informa uma data passada ou futura, então o sistema aceita (campo Data).
- [ ] Dado o campo Descrição da atividade, quando o professor digita mais de 2.000 caracteres, então o sistema não salva e mostra a mensagem de erro (campo Descrição da atividade).
- [ ] Dado o campo Observações, quando o professor deixa vazio e salva, então o sistema registra a atividade sem observações.
- [ ] Dado um anexo em PDF, JPG ou PNG de até 10 MB, quando o professor anexa até 5 arquivos, então o sistema aceita (RG-16).
- [ ] Dado um anexo fora das regras de RG-16, quando o professor tenta anexar, então o sistema não aceita e mostra a mensagem de erro.
- [ ] Dado um campo obrigatório vazio, quando o professor salva, então o sistema não salva e mostra a mensagem de erro com o que foi digitado mantido (RG-29).
- [ ] Dado que salvar falhou, quando a mensagem de erro aparece, então o que o professor digitou continua no formulário (RG-29).
- [ ] Dado alterações não salvas, quando o professor tenta sair do formulário, então o sistema pede confirmação (RG-29).
- [ ] Dado uma atividade registrada, quando ela é salva, então as psicopedagogas, o aluno e os responsáveis com conta ativa recebem a notificação "Atividade adaptada registrada" (RN-10).
- [ ] Dado uma atividade registrada pelo professor, quando ela é salva, então o professor autor não recebe notificação (RG-25).
- [ ] Dado um responsável sem conta ativa, quando a atividade do aluno é registrada, então ele não recebe notificação (RN-10).
- [ ] Dado uma atividade com data 20/10/2026, quando o aluno abre a agenda em 20/10/2026, então a atividade aparece no dia, sem horário (RN-09).
- [ ] Dado uma atividade na agenda, quando o usuário clica no item, então a atividade abre (RN-09).
- [ ] Dado um professor que leciona em duas turmas, quando ele abre a lista geral, então vê as atividades dos alunos das duas turmas, inclusive as de outros professores (RN-03).
- [ ] Dado uma atividade de outro professor, quando o professor abre o detalhe, então não vê as ações "Editar" e "Excluir" (RN-04).
- [ ] Dado uma atividade de aluno de outra turma, quando o professor tenta abrir, então o sistema mostra "Não encontrado" (RG-13).
- [ ] Dado um professor que registrou uma atividade adaptada para um aluno, quando o aluno muda para uma turma em que ele não leciona, então o professor não vê mais o aluno nem essa atividade, e a psicopedagoga continua vendo a atividade (RN-16).
- [ ] Dado uma atividade adaptada registrada, quando o autor a edita ou a exclui, então ninguém recebe notificação, e a atividade editada mostra "Editado em" ao aluno e aos responsáveis (RN-17, RG-15).
- [ ] Dado a psicopedagoga, quando ela abre a lista geral, então vê todas as atividades e não vê a ação "Registrar atividade adaptada" (RN-03, RN-04).
- [ ] Dado um aluno, quando ele abre a aba "Atividades adaptadas" do perfil, então vê só as atividades dele, inteiras, com as observações (RN-05, RN-06).
- [ ] Dado um responsável, quando ele abre a aba "Atividades adaptadas" do perfil do aluno vinculado, então vê as atividades inteiras do aluno, com as observações (RN-05, RN-06).
- [ ] Dado um aluno ou um responsável, quando tenta abrir a lista geral de atividades adaptadas, então o sistema mostra "Acesso negado" (RG-13).
- [ ] Dado um aluno ou um responsável, quando abre a aba do perfil, então não vê as ações "Registrar atividade adaptada", "Editar" e "Excluir" (RN-04).
- [ ] Dado a lista geral aberta, quando não há filtros, então o período é o mês atual e as atividades vêm da mais recente para a mais antiga.
- [ ] Dado mais de 20 atividades, quando a lista abre, então mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado filtros que não retornam resultados, quando a lista abre, então mostra a opção de limpar os filtros (RG-22).
- [ ] Dado nenhuma atividade registrada, quando o professor abre a lista, então vê a mensagem de lista vazia e a ação "Registrar atividade adaptada" (RG-22).
- [ ] Dado uma atividade registrada há menos de 24 horas, quando o autor escolhe "Excluir", então o sistema pede confirmação dizendo a ação e a consequência (RN-08, RG-23).
- [ ] Dado a confirmação de exclusão, quando o autor confirma, então a atividade sai da lista e da agenda do aluno (RN-08).
- [ ] Dado uma atividade registrada há mais de 24 horas, quando o autor abre o detalhe, então não vê a ação "Excluir" e continua vendo "Editar" (RN-08).
- [ ] Dado uma atividade editada pelo autor, quando o detalhe abre, então mostra "Editado em" com a data e o autor da última alteração (RN-12).
- [ ] Dado um aluno inativo, quando a psicopedagoga abre a lista geral, então vê as atividades dele, e o professor não vê (RN-14).
- [ ] Dado um anexo da atividade, quando o usuário que vê a atividade abre o anexo, então o anexo abre; quem não vê a atividade não acessa o anexo (RN-07).
- [ ] Dado que a conexão caiu, quando a lista abre, então o sistema mostra "Sem conexão", conforme [T26 Estados do sistema](prd-t26-estados-do-sistema.md).
- [ ] Dado a tela aberta no celular, quando o usuário usa só o teclado, então consegue registrar, ver, filtrar e excluir (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
