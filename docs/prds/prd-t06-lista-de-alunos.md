# PRD da tela de Lista de alunos

| Campo | Valor |
| --- | --- |
| Identificador | T06 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T19 Turmas](prd-t19-turmas.md), [T20 Cursos](prd-t20-cursos.md), [T22 Dificuldades](prd-t22-dificuldades.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga e o professor encontrem um aluno e abram o perfil dele, para consultar e manter o atendimento sem procurar em papel.

## 2. Escopo

### O que entra no escopo

- Listar alunos com colunas diferentes para a psicopedagoga e para o professor.
- Buscar por nome ou e-mail acadêmico. O professor busca só pelo nome.
- Filtrar por curso, série, turma, dificuldade e, só para a psicopedagoga, situação.
- Ordenar por nome, por curso e série e por dificuldade.
- Abrir o perfil do aluno.
- Levar a psicopedagoga ao cadastro de aluno pela ação "Cadastrar aluno".

### O que não entra no escopo

- Cadastrar, editar, inativar e reativar aluno: ficam em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md).
- Ver os dados completos do aluno: ficam em [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md).
- Manter turmas, cursos e dificuldades: ficam em [T19 Turmas](prd-t19-turmas.md), [T20 Cursos](prd-t20-cursos.md) e [T22 Dificuldades](prd-t22-dificuldades.md). Esta tela só usa esses itens como opções de filtro.
- Importar alunos do sistema institucional: fica para depois (seção 11 do índice).
- Acesso do aluno e do responsável: eles não usam esta tela.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê todos os alunos, ativos e inativos (RG-07), com todas as colunas. Usa os seis filtros, ordena a lista, abre o perfil e cadastra aluno. |
| Professor | Vê só os alunos ativos das turmas em que leciona (RG-08), com as colunas foto, nome, turma e dificuldades. Usa os filtros, exceto Situação. Abre o perfil. Não cadastra aluno. |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega para achar um aluno antes de consultar ou registrar algo, ou para cadastrar um aluno novo. O professor chega para consultar os alunos atendidos das suas turmas.

**Origem da jornada:** Menu "Alunos" → Lista de alunos. O professor também chega pelo bloco "alunos atendidos das suas turmas" do [T02 Início](prd-t02-inicio.md), que leva a esta lista ou direto ao perfil.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Total de resultados | Mostra o total de alunos que atendem à busca e aos filtros (RG-19). Aparece para os dois perfis. |
| Filtros ativos | Ficam visíveis acima da lista, com a opção de limpar todos de uma vez (RG-21). |
| Foto | Foto do aluno. Aparece para os dois perfis. |
| Nome | Nome completo do aluno. Aparece para os dois perfis. Abrir a linha leva ao perfil. |
| Curso e série | Sigla do curso e série da turma do aluno. Só a psicopedagoga. |
| Turma | Turma do aluno. Só o professor. |
| Dificuldades | Primeira dificuldade em ordem alfabética, com "+N" quando há mais de uma (RN-04). Aluno sem dificuldade mostra "Em avaliação" (RN-03). Aparece para os dois perfis. |
| Data de nascimento | No formato dd/mm/aaaa (RG-18). Só a psicopedagoga. |
| Cidade | Cidade do aluno. Só a psicopedagoga. |
| E-mail acadêmico | E-mail de acesso do aluno. Só a psicopedagoga. |
| Responsável | Primeiro responsável cadastrado, com "+N" quando há mais de um (RN-05). Só a psicopedagoga. |
| Contato do responsável | Contato do primeiro responsável cadastrado, com "+N" quando há mais de um responsável (RN-05). Só a psicopedagoga. O dado mostrado está em "Contato do responsável" na 7.2. |
| Situação | "Ativo" ou "Inativo" (situações do aluno, seção 6 do índice). Só a psicopedagoga. |
| Paginação | 20 itens por página (RG-19). |
| Cadastrar aluno | Botão principal que abre [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md). Só a psicopedagoga. |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

Não se aplica. A tela não tem formulário.

### 5.2 Filtros

| Filtro | Opções | Valor padrão | Perfis |
| --- | --- | --- | --- |
| Busca | Psicopedagoga: nome ou e-mail acadêmico. Professor: só nome (RN-12). Segue RG-20. | Vazio | Psicopedagoga, Professor |
| Curso | Cursos ativos | Todos | Psicopedagoga, Professor |
| Série | Séries do curso | Todas | Psicopedagoga, Professor |
| Turma | Turmas do ano letivo atual. O professor vê só as suas. | Todas | Psicopedagoga, Professor |
| Dificuldade | Catálogo de dificuldades | Todas | Psicopedagoga, Professor |
| Situação | Ativos, Inativos, Todos | Ativos | Só a psicopedagoga |

### 5.3 Ordenação e paginação

- Ordenação padrão: nome, de A a Z.
- Outras ordenações: curso e série; dificuldade. A ordenação por dificuldade usa a dificuldade mostrada na lista (RN-06).
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário abre "Alunos" no menu.
2. O sistema mostra a lista com o filtro Situação em "Ativos" (psicopedagoga) ou só os alunos ativos das turmas do professor, ordenada por nome de A a Z, com o total de resultados.
3. O usuário digita na busca ou escolhe filtros. O sistema atualiza a lista e mostra os filtros ativos.
4. O usuário abre a linha de um aluno.
5. O sistema abre o [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md).

### 6.2 Fluxos alternativos

- Busca com menos de 2 caracteres: a busca não é aplicada (RG-20).
- Nenhum resultado por causa dos filtros: o sistema mostra a mensagem de lista vazia e a opção de limpar os filtros (RG-22).
- Voltar do perfil para a lista: a lista volta com os mesmos filtros (RG-21).
- Link da lista copiado e aberto por outro usuário: abre com os mesmos filtros, dentro das permissões de quem abre (RG-21).
- Aluno e responsável: abrem "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Buscar | Psicopedagoga, Professor | Filtra por nome ou e-mail acadêmico, para a psicopedagoga, e só por nome, para o professor (RN-12). Ignora maiúsculas, minúsculas e acentos e começa a partir de 2 caracteres (RG-20). |
| Filtrar | Psicopedagoga, Professor | Aplica os filtros da seção 5.2. O professor não tem o filtro Situação. |
| Limpar filtros | Psicopedagoga, Professor | Volta todos os filtros ao valor padrão de uma vez (RG-21). |
| Ordenar | Psicopedagoga, Professor | Ordena por nome, curso e série ou dificuldade. |
| Abrir o perfil | Psicopedagoga, Professor | Abre o [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md). O professor só abre alunos ativos das suas turmas. |
| Cadastrar aluno | Só a psicopedagoga | Abre o [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra a mensagem de lista vazia e, para a psicopedagoga, a ação "Cadastrar aluno" (RG-22). O professor vê só a mensagem. |
| Vazio, por causa dos filtros | Mostra a mensagem de lista vazia e a opção de limpar os filtros (RG-22). |
| Sem permissão | Aluno e responsável abrem "Acesso negado" (RG-13), em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Falha de conexão abre "Sem conexão" e falha inesperada abre "Erro inesperado", em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). A mensagem diz o que aconteceu e o que fazer (RG-24). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-07, RG-08, RG-11, RG-13 e RG-19 a RG-22. |
| RN-02 | O professor vê só alunos ativos das turmas em que leciona. A psicopedagoga vê ativos e inativos e usa o filtro Situação, que começa em "Ativos". |
| RN-03 | Aluno sem dificuldade cadastrada aparece como "Em avaliação". |
| RN-04 | Com mais de uma dificuldade, a lista mostra a primeira em ordem alfabética e "+N", em que N é a quantidade das outras. Exemplo: "Dislexia +2". |
| RN-05 | Com mais de um responsável, as colunas "Responsável" e "Contato do responsável" mostram o primeiro cadastrado e "+N". |
| RN-06 | A ordenação por dificuldade usa a dificuldade mostrada na lista. |
| RN-07 | O filtro Turma lista as turmas do ano letivo atual (ano letivo mais recente com pelo menos uma turma ativa). O professor vê só as suas turmas. |
| RN-08 | O filtro Curso lista só cursos ativos. O filtro Dificuldade lista o catálogo de dificuldades. |
| RN-09 | O professor não vê data de nascimento, cidade, e-mail acadêmico, responsável nem contato do responsável (RG-11). |
| RN-10 | Só a psicopedagoga vê e usa a ação "Cadastrar aluno". |
| RN-11 | Aluno e responsável não usam esta tela. O menu "Alunos" só existe para psicopedagoga e professor (seção 8 do índice). |
| RN-12 | A busca da psicopedagoga considera o nome e o e-mail acadêmico. A busca do professor considera só o nome, porque ele não vê o e-mail acadêmico (RG-11). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Foto ausente | Aluno sem foto mostra um círculo com as iniciais do nome. |
| Aluno sem responsável | Aluno com 18 anos ou mais pode não ter responsável. As colunas "Responsável" e "Contato do responsável" ficam com "Não informado". |
| Contato do responsável | A coluna mostra o telefone do primeiro responsável cadastrado. |
| Filtro Série | A lista de séries vai de 1º a 4º quando o filtro Curso está em "Todos". Com um curso escolhido, mostra só as séries do curso. Trocar o curso limpa a série escolhida. |
| Ordenação por curso e série | Ordena pela sigla do curso, de A a Z, e depois pela série, de 1º a 4º. Clicar de novo no título da coluna inverte o sentido. O professor usa a mesma ordenação, aplicada à turma. |
| Dificuldade "Em avaliação" na ordenação | Na ordenação por dificuldade, os alunos "Em avaliação" ficam no fim da lista, nos dois sentidos. |
| Dificuldades inativas no filtro | O filtro Dificuldade também lista dificuldades inativas, para encontrar alunos que ainda as têm. |
| Turmas inativas no filtro | O filtro Turma lista só turmas do ano letivo atual. Para ver alunos de turmas antigas, a psicopedagoga usa a busca e o perfil do aluno. |
| Aluno inativo em destaque | Aluno inativo mostra o selo "Inativo" na coluna Situação e a linha em cor mais fraca. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

Não se aplica. Esta tela não gera nem recebe notificações.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Aluno sem dificuldade cadastrada | Aviso | Em avaliação |
| Lista vazia, sem nenhum aluno, psicopedagoga | Aviso | Nenhum aluno cadastrado. Use "Cadastrar aluno" para incluir o primeiro. (proposta) |
| Lista vazia, sem nenhum aluno, professor | Aviso | Nenhum aluno ativo nas suas turmas. (proposta) |
| Lista vazia por causa dos filtros | Aviso | Nenhum aluno encontrado com estes filtros. Limpe os filtros para ver todos os alunos. (proposta) |
| Busca com 1 caractere | Aviso | Digite pelo menos 2 caracteres para buscar. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Acessar a lista | Sim | Só alunos ativos das suas turmas | Não | Não |
| Ver alunos inativos | Sim | Não | Não | Não |
| Ver data de nascimento, cidade, e-mail acadêmico, responsável e contato do responsável | Sim | Não | Não | Não |
| Usar o filtro Situação | Sim | Não | Não | Não |
| Buscar, filtrar e ordenar | Sim | Sim, dentro das suas turmas | Não | Não |
| Abrir o perfil | Sim | Só alunos ativos das suas turmas | Não | Não |
| Cadastrar aluno | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga entrou no sistema, quando abre "Alunos", então vê a lista com o filtro Situação em "Ativos", ordenada por nome de A a Z, com o total de resultados e as colunas foto, nome, curso e série, dificuldades, data de nascimento, cidade, e-mail acadêmico, responsável, contato do responsável e situação.
- [ ] Dado que o professor entrou no sistema, quando abre "Alunos", então vê só alunos ativos das suas turmas, com as colunas foto, nome, turma e dificuldades, e sem o filtro Situação (RN-02, RN-09).
- [ ] Dado que existem 45 alunos nos resultados, quando a lista é aberta, então mostra 20 itens na primeira página e o total de 45 resultados (RG-19).
- [ ] Dado que o professor leciona em duas turmas, quando abre o filtro Turma, então vê só essas duas turmas do ano letivo atual (RN-07).
- [ ] Dado que a psicopedagoga abre o filtro Curso, quando vê as opções, então aparecem só cursos ativos e a opção "Todos" (RN-08).
- [ ] Dado que a psicopedagoga abre o filtro Situação, quando escolhe "Inativos", então a lista mostra só alunos inativos, e com "Todos" mostra ativos e inativos.
- [ ] Dado que o usuário digita "jose" na busca, quando a lista é atualizada, então aparecem alunos com "José" no nome, ignorando maiúsculas e acentos (RG-20).
- [ ] Dado que o usuário digita 1 caractere na busca, quando a busca é feita, então a lista não muda (RG-20).
- [ ] Dado que a psicopedagoga busca por parte do e-mail acadêmico, quando a lista é atualizada, então aparece o aluno com esse e-mail.
- [ ] Dado que o professor busca por parte do e-mail acadêmico de um aluno da sua turma, quando a lista é atualizada, então o aluno não aparece por esse e-mail, porque a busca do professor considera só o nome (RN-12, RG-11).
- [ ] Dado que o usuário escolheu filtros, quando abre um perfil e volta para a lista, então os filtros continuam aplicados e visíveis (RG-21).
- [ ] Dado que há filtros ativos, quando o usuário escolhe limpar os filtros, então todos voltam ao valor padrão de uma vez (RG-21).
- [ ] Dado que a lista foi aberta com filtros, quando o usuário copia o link e abre em outra janela, então a lista abre com os mesmos filtros (RG-21).
- [ ] Dado que um aluno não tem dificuldade cadastrada, quando a lista é mostrada, então a coluna Dificuldades mostra "Em avaliação" (RN-03).
- [ ] Dado que um aluno tem as dificuldades "TDAH", "Dislexia" e "Autismo", quando a lista é mostrada, então a coluna mostra "Autismo +2" (RN-04).
- [ ] Dado que um aluno tem dois responsáveis, quando a psicopedagoga vê a lista, então as colunas de responsável mostram o primeiro cadastrado e "+1" (RN-05).
- [ ] Dado que a psicopedagoga ordena por dificuldade, quando a lista é atualizada, então a ordem usa a dificuldade mostrada na coluna (RN-06).
- [ ] Dado que a psicopedagoga ordena por curso e série, quando a lista é atualizada, então os alunos aparecem agrupados por curso e série.
- [ ] Dado que nenhum aluno atende aos filtros, quando a lista é mostrada, então aparece a mensagem de lista vazia e a opção de limpar os filtros (RG-22).
- [ ] Dado que a psicopedagoga abre a lista sem nenhum aluno cadastrado, quando a lista é mostrada, então aparece a mensagem de lista vazia e a ação "Cadastrar aluno" (RG-22).
- [ ] Dado que a psicopedagoga está na lista, quando escolhe "Cadastrar aluno", então abre o [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md).
- [ ] Dado que o professor está na lista, quando olha a tela, então a ação "Cadastrar aluno" não aparece (RN-10).
- [ ] Dado que o usuário abre a linha de um aluno, quando a abertura termina, então o [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) daquele aluno abre.
- [ ] Dado que um aluno tem a turma anterior de um professor, quando o professor abre a lista, então esse aluno não aparece (RG-08).
- [ ] Dado que um aluno foi inativado, quando o professor abre a lista, então esse aluno não aparece (RG-08).
- [ ] Dado que o usuário tem o perfil Aluno, quando tenta abrir a lista, então abre "Acesso negado" (RG-13, RN-11).
- [ ] Dado que o usuário tem o perfil Responsável, quando tenta abrir a lista, então abre "Acesso negado" (RG-13, RN-11).
- [ ] Dado que o sistema perdeu a conexão, quando a lista é aberta, então abre "Sem conexão" com orientação do que fazer (RG-24).
- [ ] Dado que ocorre uma falha inesperada, quando a lista é aberta, então abre "Erro inesperado" com orientação do que fazer (RG-24).
- [ ] Dado que a tela é aberta no celular, quando o usuário navega só com o teclado, então consegue buscar, filtrar, ordenar e abrir um perfil (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
