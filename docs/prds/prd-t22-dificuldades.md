# PRD da tela de Dificuldades

| Campo | Valor |
| --- | --- |
| Identificador | T22 |
| Situação | Rascunho |
| Perfis | Psicopedagoga |
| Telas relacionadas | [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T06 Lista de alunos](prd-t06-lista-de-alunos.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga mantenha o catálogo de dificuldades, para que o cadastro dos alunos use sempre os mesmos nomes e descrições.

## 2. Escopo

### O que entra no escopo

- Listar as dificuldades com filtros e ordenação.
- Cadastrar e editar dificuldade.
- Inativar e reativar dificuldade.
- Cadastrar uma dificuldade nova a partir do cadastro de aluno, sem sair do formulário.

### O que não entra no escopo

- Vínculo da dificuldade com o aluno: fica em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md).
- Texto "Em avaliação" que a lista de alunos mostra para o aluno sem dificuldade: fica em [T06 Lista de alunos](prd-t06-lista-de-alunos.md). Ele não é uma dificuldade do catálogo.
- Características do aluno: o campo "Características" desta tela descreve a dificuldade e não é o mesmo que as características do aluno, que ficam em [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md).
- Exclusão de dificuldade: a dificuldade nunca é excluída (RG-14).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Lista, cadastra, edita, inativa e reativa dificuldades. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). Vê o nome e a descrição das dificuldades dos seus alunos no perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui para manter o catálogo antes de cadastrar alunos ou quando precisa corrigir uma descrição. Também pode cadastrar uma dificuldade nova durante o cadastro de um aluno, sem abrir esta tela.

**Origem da jornada:** Início → menu "Dificuldades" → Dificuldades. A outra entrada é o formulário de [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Nome (coluna da lista) | Nome da dificuldade. |
| Tipo (coluna da lista) | Deficiência, Transtorno, Dificuldade de aprendizagem ou Outro. |
| Alunos vinculados (coluna da lista) | Quantidade de alunos vinculados à dificuldade. |
| Situação (coluna da lista) | Ativo ou Inativo (dificuldade, seção 6 do índice). |
| Total de resultados | Total de dificuldades encontradas, com 20 itens por página (RG-19). |
| Criação e edição | Quem criou e quando. Dificuldade alterada mostra "Editado em" com data e autor da última alteração (RG-15). |
| Botões | "Cadastrar dificuldade", "Editar", "Inativar" e "Reativar". |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nome | Sim | Único no catálogo. |
| Tipo | Sim | Lista de opções: Deficiência, Transtorno, Dificuldade de aprendizagem ou Outro. |
| O que é | Sim | Descrição curta. |
| Características | Não | Como a dificuldade costuma se manifestar no aluno. |
| Mais informações | Não | Texto livre. |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Busca | Nome | Vazio |
| Tipo | Deficiência, Transtorno, Dificuldade de aprendizagem, Outro | Todos |
| Situação | Ativas, Inativas, Todas | Ativas |

A busca segue RG-20.

### 5.3 Ordenação e paginação

- Ordenação padrão: nome, de A a Z.
- Outras ordenações: não definidas.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre "Dificuldades".
2. O sistema mostra as dificuldades ativas em ordem alfabética.
3. A psicopedagoga escolhe "Cadastrar dificuldade" e preenche nome, tipo e "O que é". Se quiser, preenche também "Características" e "Mais informações".
4. A psicopedagoga escolhe "Salvar".
5. O sistema cadastra a dificuldade como Ativo, mostra "Dificuldade cadastrada" e passa a oferecê-la no cadastro de aluno (RN-04).

### 6.2 Fluxos alternativos

- Nome já usado por outra dificuldade: o sistema não salva e pede outro nome (RN-02).
- Campo obrigatório vazio: o sistema não salva e indica o campo.
- Cadastro a partir do cadastro de aluno: a psicopedagoga preenche os mesmos campos sem sair do formulário do aluno. Ao salvar, o que já foi digitado do aluno continua no formulário e a dificuldade nova fica disponível para escolha (RN-05).
- Sair do formulário com alterações não salvas: o sistema pede confirmação (RG-29).
- Falha ao salvar: o que foi digitado continua no formulário (RG-29).
- Outro perfil tenta abrir a tela: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Listar, buscar e filtrar dificuldades | Psicopedagoga | Mostra a lista com os filtros ativos visíveis (RG-21). |
| Cadastrar dificuldade | Psicopedagoga | Valida os campos e a regra RN-02, cria a dificuldade como Ativo e mostra "Dificuldade cadastrada". |
| Cadastrar dificuldade a partir do cadastro de aluno | Psicopedagoga | Mesmo comportamento, sem sair do formulário do aluno (RN-05). |
| Editar dificuldade | Psicopedagoga | Salva as alterações e passa a mostrar "Editado em" (RG-15). |
| Inativar dificuldade | Psicopedagoga | Pede confirmação. A dificuldade deixa de aparecer para novos vínculos e continua nos alunos que já a têm (RN-03). |
| Reativar dificuldade | Psicopedagoga | A dificuldade volta para Ativo e passa a aparecer para novos vínculos. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra uma mensagem e a ação principal "Cadastrar dificuldade" (RG-22). |
| Vazio, por causa dos filtros | Mostra uma mensagem e a opção de limpar os filtros (RG-22). |
| Sem permissão | Professor, aluno e responsável abrem "Acesso negado" (RG-13), de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado", de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Falha ao salvar mantém o que foi digitado (RG-29). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-13 a RG-15, RG-19 a RG-24 e RG-29. |
| RN-02 | O nome é obrigatório e único no catálogo. O tipo é obrigatório e é Deficiência, Transtorno, Dificuldade de aprendizagem ou Outro. O campo "O que é" é obrigatório. |
| RN-03 | A dificuldade inativa não aparece para novos vínculos e continua nos alunos que já a têm. |
| RN-04 | Ao cadastrar, o sistema mostra "Dificuldade cadastrada" e a dificuldade passa a aparecer no cadastro de aluno ([T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md)). |
| RN-05 | A dificuldade também pode ser cadastrada a partir do cadastro de aluno, sem sair do formulário. As regras são as mesmas desta tela. |
| RN-06 | A dificuldade nunca é excluída. Ela é inativada e reativada, e o histórico é mantido (RG-14). |
| RN-07 | O professor vê o nome e a descrição ("O que é") das dificuldades dos seus alunos no perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)), dentro do que RG-08 e RG-11 permitem. |
| RN-08 | A lista de alunos ([T06 Lista de alunos](prd-t06-lista-de-alunos.md)) usa as dificuldades do catálogo no filtro e na coluna "Dificuldade". |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Limite de "O que é" | Até 300 caracteres. |
| Quantidade de alunos vinculados | Conta só alunos ativos. |
| Nome único sem diferenciar maiúsculas e acentos | "Dislexia" e "dislexia" contam como o mesmo nome. |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Dificuldade cadastrada | Sucesso | Dificuldade cadastrada |
| Dificuldade atualizada | Sucesso | Dificuldade atualizada. (proposta) |
| Dificuldade inativada | Sucesso | Dificuldade inativada. (proposta) |
| Dificuldade reativada | Sucesso | Dificuldade reativada. (proposta) |
| Campo obrigatório vazio | Erro | Preencha o campo {campo} para salvar a dificuldade. (proposta) |
| Nome repetido | Erro | Já existe uma dificuldade com este nome. Use outro nome e salve de novo. (proposta) |
| Inativar dificuldade | Confirmação | Inativar a dificuldade {nome}? Ela deixa de aparecer para novos vínculos e continua nos alunos que já a têm. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Lista vazia, sem nenhuma dificuldade | Aviso | Nenhuma dificuldade cadastrada. (proposta) |
| Lista vazia, por causa dos filtros | Aviso | Nenhuma dificuldade encontrada com estes filtros. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Listar e buscar dificuldades | Sim | Não | Não | Não |
| Cadastrar e editar dificuldade | Sim | Não | Não | Não |
| Inativar e reativar dificuldade | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga está logada, quando abre "Dificuldades", então o sistema mostra as dificuldades ativas em ordem alfabética de nome, com nome, tipo, quantidade de alunos vinculados e situação.
- [ ] Dado que a lista tem mais de 20 dificuldades, quando a psicopedagoga abre a tela, então o sistema mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado que a psicopedagoga digitou "dislexia" na busca, quando a lista é filtrada, então aparecem as dificuldades cujo nome contém "Dislexia", sem diferenciar maiúsculas e acentos (RG-20).
- [ ] Dado que a psicopedagoga filtrou por tipo ou situação, quando volta para a lista depois de abrir uma dificuldade, então os filtros continuam ativos e podem ser limpos de uma vez (RG-21).
- [ ] Dado que a psicopedagoga preencheu nome, tipo e "O que é", quando escolhe "Salvar", então a dificuldade é cadastrada como Ativo e o sistema mostra "Dificuldade cadastrada" (RN-04).
- [ ] Dado que a dificuldade foi cadastrada, quando a psicopedagoga abre o cadastro de aluno, então a dificuldade aparece na lista de dificuldades para escolha (RN-04).
- [ ] Dado que a psicopedagoga está no formulário de aluno, quando cadastra uma dificuldade nova sem sair do formulário, então a dificuldade é cadastrada, o que já foi digitado do aluno continua no formulário e a dificuldade nova pode ser escolhida (RN-05).
- [ ] Dado que já existe uma dificuldade com o mesmo nome, quando a psicopedagoga tenta salvar outra com esse nome, então o sistema não salva e mostra o erro de nome repetido (RN-02).
- [ ] Dado que nome, tipo ou "O que é" estão vazios, quando a psicopedagoga tenta salvar, então o sistema não salva e indica o campo (RN-02).
- [ ] Dado que a psicopedagoga deixou "Características" e "Mais informações" vazios, quando salva, então a dificuldade é cadastrada, porque os dois campos não são obrigatórios.
- [ ] Dado que a dificuldade está Ativo, quando a psicopedagoga escolhe "Inativar" e confirma, então ela passa a Inativo, deixa de aparecer para novos vínculos e continua nos alunos que já a têm (RN-03).
- [ ] Dado que a dificuldade está Inativo, quando a psicopedagoga escolhe "Reativar", então ela volta para Ativo e aparece para novos vínculos.
- [ ] Dado que a dificuldade foi alterada, quando a psicopedagoga a abre, então vê "Editado em" com a data no formato dd/mm/aaaa e o autor da última alteração (RG-15, RG-18).
- [ ] Dado que a psicopedagoga alterou campos do formulário, quando tenta sair sem salvar, então o sistema pede confirmação (RG-29).
- [ ] Dado que o salvamento falhou, quando o formulário continua aberto, então o que foi digitado continua nos campos (RG-29).
- [ ] Dado que nenhuma dificuldade foi cadastrada, quando a psicopedagoga abre a tela, então vê a mensagem de lista vazia e a ação "Cadastrar dificuldade" (RG-22).
- [ ] Dado que os filtros não retornam dificuldades, quando a psicopedagoga vê a lista, então o sistema mostra a opção de limpar os filtros (RG-22).
- [ ] Dado que um professor abre o perfil de um aluno ativo da sua turma, quando vê as dificuldades, então aparecem o nome e a descrição de cada uma (RN-07).
- [ ] Dado que um professor, um aluno ou um responsável tenta abrir esta tela, quando a tela carrega, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado que a ação de salvar falha por falta de conexão ou erro inesperado, quando a psicopedagoga está no formulário, então o sistema mostra o aviso de [T26 Estados do sistema](prd-t26-estados-do-sistema.md) na própria tela, sem trocar de tela.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
