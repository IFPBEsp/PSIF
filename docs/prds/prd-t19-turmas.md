# PRD da tela de Turmas

| Campo | Valor |
| --- | --- |
| Identificador | T19 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor |
| Telas relacionadas | [T20 Cursos](prd-t20-cursos.md), [T21 Professores](prd-t21-professores.md), [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T06 Lista de alunos](prd-t06-lista-de-alunos.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T04 Minha conta](prd-t04-minha-conta.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga organize alunos e professores por curso, série e ano letivo, e que o professor consulte as suas turmas, para que cada professor veja os alunos certos.

## 2. Escopo

### O que entra no escopo

- Listar turmas com filtros por curso, ano letivo e situação.
- Ver o detalhe da turma: dados da turma, alunos atendidos e professores com as disciplinas.
- Cadastrar e editar turma.
- Vincular e desvincular professores, com a disciplina de cada um.
- Inativar e reativar turma.
- Consulta, só leitura, das turmas do professor.

### O que não entra no escopo

- Cadastro de curso e do número de séries: fica em [T20 Cursos](prd-t20-cursos.md).
- Cadastro de professor e dos pares de turma e disciplina pelo lado do professor: fica em [T21 Professores](prd-t21-professores.md).
- Escolha da turma do aluno e troca de turma na virada do ano letivo: ficam em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md).
- Dados do aluno além do acesso ao perfil: ficam em [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md).
- Exclusão de turma: a turma nunca é excluída (RG-14).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Gerencia todas as turmas: lista, vê o detalhe, cadastra, edita, vincula e desvincula professores, inativa e reativa. |
| Professor | Vê só as suas turmas, em leitura: lista e detalhe. Não cadastra, não edita, não vincula, não inativa e não reativa. No detalhe, vê os alunos ativos da turma só com os dados básicos (RN-09). |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui no início do ano letivo para montar as turmas e durante o ano para ajustar os professores de cada uma. O professor chega para conferir em quais turmas e disciplinas está vinculado e quais alunos atende.

**Origem da jornada:** Início → menu "Turmas" → Turmas. Do detalhe, o usuário abre o perfil de um aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Turma (coluna da lista) | Série, sigla do curso e ano letivo, por exemplo "2º TIN 2027". |
| Alunos atendidos (coluna da lista) | Quantidade de alunos atendidos da turma. |
| Professores (coluna da lista) | Quantidade de professores vinculados à turma. |
| Situação (coluna da lista) | Ativo ou Inativo (turma, seção 6 do índice). |
| Total de resultados | Total de turmas encontradas, com 20 itens por página (RG-19). |
| Dados da turma (detalhe) | Curso, série, ano letivo e situação. |
| Alunos atendidos (detalhe) | Lista dos alunos da turma. Cada nome dá acesso ao perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). |
| Professores e disciplinas (detalhe) | Lista dos pares de professor e disciplina vinculados à turma. |
| Criação e edição (detalhe, só psicopedagoga) | Quem criou e quando. Turma alterada mostra "Editado em" com data e autor da última alteração (RG-15). |
| Botões (só psicopedagoga) | "Cadastrar turma", "Editar", "Vincular professor", "Desvincular", "Inativar" e "Reativar". |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Curso | Sim | Lista de cursos ativos (RN-03). |
| Série | Sim | De 1 até o número de séries do curso escolhido. |
| Ano letivo | Sim | Ano com quatro dígitos. |
| Professores e disciplinas | Não | Um ou mais pares de professor e disciplina. A disciplina é texto. |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Curso | Cursos | Todos |
| Ano letivo | Anos letivos das turmas | O ano letivo atual (RN-10) |
| Situação | Ativas, Inativas, Todas | Ativas |

Os filtros valem para os dois perfis. A lista do professor só traz as turmas dele.

### 5.3 Ordenação e paginação

- Ordenação padrão: não definida. Ver "Ordenação e busca por texto" em 7.2.
- Outras ordenações: não definidas. Ver 7.2.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre "Turmas".
2. O sistema mostra as turmas ativas do ano letivo atual.
3. A psicopedagoga escolhe "Cadastrar turma", escolhe o curso, a série e o ano letivo e, se quiser, acrescenta pares de professor e disciplina.
4. A psicopedagoga escolhe "Salvar".
5. O sistema cadastra a turma, mostra a confirmação e abre o detalhe dela.

### 6.2 Fluxos alternativos

- Turma repetida: o sistema não salva e avisa que já existe turma com o mesmo curso, série e ano letivo (RN-02).
- Campo obrigatório vazio: o sistema não salva e indica o campo.
- Inativar turma com alunos ativos: o sistema não inativa e avisa o que fazer (RN-04).
- Vincular ou desvincular professor: o sistema pede confirmação e, depois de confirmado, muda na hora quais alunos o professor vê (RN-05).
- Sair do formulário com alterações não salvas: o sistema pede confirmação (RG-29).
- Falha ao salvar: o que foi digitado continua no formulário (RG-29).
- Professor abre uma turma que não é dele: abre "Não encontrado" (RG-13).
- Aluno ou responsável tenta abrir a tela: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Listar e filtrar turmas | Psicopedagoga, Professor (só as suas) | Mostra a lista com os filtros ativos visíveis (RG-21). |
| Abrir o detalhe da turma | Psicopedagoga, Professor (só as suas) | Mostra dados da turma, alunos atendidos e professores com as disciplinas. |
| Abrir o perfil de um aluno | Psicopedagoga, Professor (só alunos ativos das suas turmas) | Abre [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md). |
| Cadastrar turma | Psicopedagoga | Valida os campos e as regras RN-02 e RN-03, cria a turma como Ativo e mostra a confirmação. |
| Editar turma | Psicopedagoga | Salva as alterações e passa a mostrar "Editado em" (RG-15). |
| Vincular professor | Psicopedagoga | Pede confirmação, cria o par de professor e disciplina e atualiza na hora quais alunos o professor vê (RN-05). |
| Desvincular professor | Psicopedagoga | Pede confirmação, remove o par e atualiza na hora quais alunos o professor vê (RN-05). O histórico é mantido (RG-14). |
| Inativar turma | Psicopedagoga | Pede confirmação. Só inativa se não houver alunos ativos (RN-04). |
| Reativar turma | Psicopedagoga | A turma volta para Ativo e passa a aparecer para novos cadastros de aluno. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra uma mensagem e a ação principal "Cadastrar turma" para a psicopedagoga (RG-22). Para o professor, mostra só a mensagem. |
| Vazio, por causa dos filtros | Mostra uma mensagem e a opção de limpar os filtros (RG-22). |
| Sem permissão | Aluno e responsável abrem "Acesso negado" e turma que o professor não pode ver abre "Não encontrado" (RG-13), de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado", de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Falha ao salvar mantém o que foi digitado (RG-29). |

### 6.5 Virada do ano letivo

1. A psicopedagoga cadastra as turmas do novo ano letivo (RN-02, RN-03).
2. Em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), troca a turma de cada aluno para a turma do novo ano.
3. Quando uma turma do ano anterior fica sem alunos ativos, a psicopedagoga a inativa (RN-04).

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-08, RG-11, RG-13 a RG-15, RG-19 a RG-24 e RG-29. |
| RN-02 | Não pode haver duas turmas com o mesmo curso, série e ano letivo. |
| RN-03 | Só cursos ativos aparecem para novas turmas. A série vai de 1 até o número de séries do curso. O ano letivo tem quatro dígitos. Ver [T20 Cursos](prd-t20-cursos.md). |
| RN-04 | Uma turma só pode ser inativada se não tiver alunos ativos. |
| RN-05 | Vincular ou desvincular um professor muda, na hora, quais alunos ele vê (RG-08). |
| RN-06 | A disciplina é registrada como texto no vínculo entre professor e turma. Os mesmos pares são editados também em [T21 Professores](prd-t21-professores.md), com sugestão das disciplinas já usadas. |
| RN-07 | A turma nunca é excluída. Ela é inativada e reativada, e o histórico é mantido (RG-14). |
| RN-08 | O professor só vê as turmas em que leciona e só lê, como diz a matriz de permissões (seção 10 do índice). No detalhe, o professor vê os dados da turma, os alunos atendidos e os professores com as disciplinas. |
| RN-09 | O professor vê os alunos da turma só com os dados básicos: nome, foto, turma e dificuldades (RG-11). Não vê dados de saúde, contatos, endereço nem data de nascimento. |
| RN-10 | O ano letivo atual é o ano letivo mais recente que tem pelo menos uma turma ativa. É o padrão do filtro "Ano letivo" (seção 4 do índice). |
| RN-11 | O número de séries de um curso não pode ficar menor que a maior série de uma turma ativa dele (regra de [T20 Cursos](prd-t20-cursos.md)). |
| RN-12 | O filtro "Turma" de [T06 Lista de alunos](prd-t06-lista-de-alunos.md) usa as turmas do ano letivo atual. O professor vê em [T04 Minha conta](prd-t04-minha-conta.md) as suas turmas e disciplinas, e só a psicopedagoga altera. |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Ordenação e busca por texto | Sem busca por texto. Ordenação padrão por ano letivo do mais recente para o mais antigo, depois curso e série. |
| Vínculos ao inativar a turma | Os vínculos de professor continuam guardados com a turma inativa. O professor deixa de ver alunos por ela porque a turma não tem alunos ativos (RN-04). |
| Editar curso, série e ano de turma com alunos | Permite editar. Os alunos continuam na turma, e a regra RN-02 continua valendo. |
| Ano letivo atual sem turma ativa | O filtro "Ano letivo" mostra "Todos" até existir uma turma ativa. |
| Quantidade de alunos atendidos | Conta só alunos ativos, e o detalhe lista só alunos ativos. |
| Professores e turmas para vincular | Só professores ativos e só turmas ativas entram na escolha. |
| Par repetido | Não permite o mesmo professor e a mesma disciplina duas vezes na mesma turma. |
| Reativar turma de curso inativo | Pede reativar o curso antes, em [T20 Cursos](prd-t20-cursos.md). |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Turma cadastrada | Sucesso | Turma cadastrada. (proposta) |
| Turma atualizada | Sucesso | Turma atualizada. (proposta) |
| Turma reativada | Sucesso | Turma reativada. (proposta) |
| Turma inativada | Sucesso | Turma inativada. (proposta) |
| Campo obrigatório vazio | Erro | Preencha o campo {campo} para salvar a turma. (proposta) |
| Turma repetida | Erro | Já existe uma turma com este curso, série e ano letivo. Altere um deles e salve de novo. (proposta) |
| Inativar turma com alunos ativos | Erro | Esta turma tem alunos ativos. Troque a turma deles no cadastro de aluno e tente de novo. (proposta) |
| Inativar turma | Confirmação | Inativar a turma {turma}? Ela deixa de aparecer para novos cadastros de aluno e o histórico é mantido. (proposta) |
| Vincular professor | Confirmação | Vincular {professor} à turma {turma}? Ele passa a ver agora os alunos ativos desta turma. (proposta) |
| Desvincular professor | Confirmação | Desvincular {professor} da turma {turma}? Ele deixa de ver agora os alunos desta turma. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Lista vazia, sem nenhuma turma | Aviso | Nenhuma turma cadastrada. (proposta) |
| Lista vazia, por causa dos filtros | Aviso | Nenhuma turma encontrada com estes filtros. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Listar e ver o detalhe da turma | Sim | Só as suas turmas, em leitura | Não | Não |
| Cadastrar e editar turma | Sim | Não | Não | Não |
| Vincular e desvincular professores | Sim | Não | Não | Não |
| Inativar e reativar turma | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga está em "Turmas", quando abre a tela, então o sistema mostra as turmas ativas do ano letivo atual, com turma (por exemplo "2º TIN 2027"), quantidade de alunos atendidos, quantidade de professores e situação (RN-10).
- [ ] Dado que a lista tem mais de 20 turmas, quando a psicopedagoga abre a tela, então o sistema mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado que a psicopedagoga escolheu filtros, quando volta para a lista depois de abrir um detalhe, então os filtros continuam ativos e podem ser limpos de uma vez (RG-21).
- [ ] Dado que a psicopedagoga abre o formulário de cadastro, quando escolhe o curso, então a lista de cursos mostra só cursos ativos e a série vai de 1 até o número de séries do curso (RN-03).
- [ ] Dado que a psicopedagoga preencheu curso, série e ano letivo, quando escolhe "Salvar", então a turma é cadastrada como Ativo, o sistema mostra a confirmação e abre o detalhe.
- [ ] Dado que já existe uma turma com o mesmo curso, série e ano letivo, quando a psicopedagoga tenta salvar outra igual, então o sistema não salva e mostra o erro de turma repetida (RN-02).
- [ ] Dado que o ano letivo tem menos de quatro dígitos, quando a psicopedagoga tenta salvar, então o sistema não salva e indica o campo (RN-03).
- [ ] Dado que a psicopedagoga cadastra uma turma sem professores, quando salva, então a turma é cadastrada, porque "Professores e disciplinas" não é obrigatório.
- [ ] Dado que a psicopedagoga acrescentou dois pares de professor e disciplina, quando salva, então o detalhe mostra os dois professores com as disciplinas (RN-06).
- [ ] Dado que a psicopedagoga vai vincular um professor, quando confirma, então o professor passa a ver na hora os alunos ativos da turma (RN-05).
- [ ] Dado que a psicopedagoga vai desvincular um professor, quando confirma, então o professor deixa de ver na hora os alunos da turma (RN-05).
- [ ] Dado que a turma tem alunos ativos, quando a psicopedagoga tenta inativar, então o sistema não inativa e mostra a mensagem de que é preciso trocar a turma dos alunos (RN-04).
- [ ] Dado que a turma não tem alunos ativos, quando a psicopedagoga escolhe "Inativar" e confirma, então a turma passa a Inativo e deixa de aparecer para novos cadastros de aluno (RN-04).
- [ ] Dado que a turma está Inativo, quando a psicopedagoga escolhe "Reativar", então a turma volta para Ativo.
- [ ] Dado que a psicopedagoga abre o detalhe de uma turma, quando escolhe o nome de um aluno, então o sistema abre o perfil dele ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)).
- [ ] Dado que a turma foi alterada, quando a psicopedagoga abre o detalhe, então vê "Editado em" com a data no formato dd/mm/aaaa e o autor da última alteração (RG-15, RG-18).
- [ ] Dado que a psicopedagoga alterou campos do formulário, quando tenta sair sem salvar, então o sistema pede confirmação (RG-29).
- [ ] Dado que o salvamento falhou, quando o formulário continua aberto, então o que foi digitado continua nos campos (RG-29).
- [ ] Dado que ninguém tem turma cadastrada, quando a psicopedagoga abre a tela, então vê a mensagem de lista vazia e a ação "Cadastrar turma" (RG-22).
- [ ] Dado que os filtros não retornam turmas, quando a psicopedagoga vê a lista, então o sistema mostra a opção de limpar os filtros (RG-22).
- [ ] Dado que o professor está vinculado a duas turmas, quando abre "Turmas", então vê só essas duas, sem botões de cadastrar, editar, vincular, inativar e reativar.
- [ ] Dado que o professor abre o detalhe de uma turma sua, quando vê os alunos, então só aparecem alunos ativos e só com nome, foto, turma e dificuldades (RG-08, RG-11).
- [ ] Dado que o professor tenta abrir uma turma em que não leciona, quando a tela carrega, então o sistema abre "Não encontrado" (RG-13).
- [ ] Dado que um aluno ou um responsável tenta abrir esta tela, quando a tela carrega, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado que a ação de salvar falha por falta de conexão ou erro inesperado, quando a psicopedagoga está no formulário, então o sistema mostra o aviso de [T26 Estados do sistema](prd-t26-estados-do-sistema.md) na própria tela, sem trocar de tela.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
