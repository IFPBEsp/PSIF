# PRD da tela de Cursos

| Campo | Valor |
| --- | --- |
| Identificador | T20 |
| Situação | Rascunho |
| Perfis | Psicopedagoga |
| Telas relacionadas | [T19 Turmas](prd-t19-turmas.md), [T06 Lista de alunos](prd-t06-lista-de-alunos.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga mantenha o catálogo de cursos, para que as turmas sejam criadas sempre com cursos válidos.

## 2. Escopo

### O que entra no escopo

- Listar os cursos com sigla, nome, número de séries e situação.
- Cadastrar e editar curso.
- Inativar e reativar curso.

### O que não entra no escopo

- Cadastro de turmas: fica em [T19 Turmas](prd-t19-turmas.md).
- Exclusão de curso: o curso nunca é excluído (RG-14).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Lista, cadastra, edita, inativa e reativa cursos. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui quando o campus passa a atender um curso novo, quando muda o número de séries de um curso ou quando um curso deixa de ser usado.

**Origem da jornada:** Início → menu "Cursos" → Cursos.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Sigla (coluna da lista) | Sigla do curso, por exemplo "TIN". |
| Nome (coluna da lista) | Nome do curso. |
| Número de séries (coluna da lista) | Quantidade de séries do curso, de 1 a 4. |
| Situação (coluna da lista) | Ativo ou Inativo (curso, seção 6 do índice). |
| Total de resultados | Total de cursos encontrados, com 20 itens por página (RG-19). |
| Criação e edição | Quem criou e quando. Curso alterado mostra "Editado em" com data e autor da última alteração (RG-15). |
| Botões | "Cadastrar curso", "Editar", "Inativar" e "Reativar". |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Sigla | Sim | Única entre os cursos. Até 10 caracteres. |
| Nome | Sim | Texto. |
| Número de séries | Sim | De 1 a 4. Não pode ficar menor que a maior série de uma turma ativa do curso (RN-04). |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Situação | Ativos, Inativos e Todos | Ativos |
| Busca | Sigla ou nome do curso (RG-20) | Vazio |

Os filtros ativos ficam visíveis, podem ser limpos de uma vez e se mantêm ao voltar para a lista (RG-21).

### 5.3 Ordenação e paginação

- Ordenação padrão: sigla, de A a Z (RN-09).
- Outras ordenações: não há.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre "Cursos".
2. O sistema mostra a lista de cursos.
3. A psicopedagoga escolhe "Cadastrar curso" e preenche sigla, nome e número de séries.
4. A psicopedagoga escolhe "Salvar".
5. O sistema cadastra o curso como Ativo, mostra a confirmação e volta para a lista com o curso novo.

### 6.2 Fluxos alternativos

- Sigla já usada por outro curso: o sistema não salva e pede outra sigla (RN-02).
- Campo obrigatório vazio, sigla com mais de 10 caracteres ou número de séries fora de 1 a 4: o sistema não salva e indica o campo.
- Reduzir o número de séries abaixo da maior série de uma turma ativa do curso: o sistema não salva e explica o que fazer (RN-04).
- Inativar curso com turmas ativas: o sistema não inativa e explica o que fazer (RN-03).
- Sair do formulário com alterações não salvas: o sistema pede confirmação (RG-29).
- Falha ao salvar: o que foi digitado continua no formulário (RG-29).
- Outro perfil tenta abrir a tela: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Listar cursos | Psicopedagoga | Mostra a lista de cursos, com o filtro "Situação" em Ativos e ordenada pela sigla (RN-09). |
| Filtrar e buscar | Psicopedagoga | Filtra por situação e busca por sigla ou nome (RN-09, RG-20, RG-21). |
| Cadastrar curso | Psicopedagoga | Valida os campos e a regra RN-02, cria o curso como Ativo e mostra a confirmação. |
| Editar curso | Psicopedagoga | Valida os campos e a regra RN-04, salva e passa a mostrar "Editado em" (RG-15). |
| Inativar curso | Psicopedagoga | Pede confirmação. Só inativa se não houver turmas ativas (RN-03). O curso deixa de aparecer para novas turmas (RN-05). |
| Reativar curso | Psicopedagoga | O curso volta para Ativo e passa a aparecer para novas turmas. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra uma mensagem e a ação principal "Cadastrar curso" (RG-22). |
| Vazio, por causa dos filtros | Mostra a mensagem da seção 9 e a opção de limpar os filtros (RG-22). |
| Sem permissão | Professor, aluno e responsável abrem "Acesso negado" (RG-13), de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado", de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Falha ao salvar mantém o que foi digitado (RG-29). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-13 a RG-15, RG-19, RG-22 a RG-24 e RG-29. |
| RN-02 | A sigla é obrigatória, única e tem até 10 caracteres. O nome é obrigatório. O número de séries é obrigatório e vai de 1 a 4. |
| RN-03 | Um curso só pode ser inativado se não tiver turmas ativas. |
| RN-04 | O número de séries não pode ficar menor que a maior série de uma turma ativa do curso. |
| RN-05 | Curso inativo não aparece para novas turmas ([T19 Turmas](prd-t19-turmas.md)). |
| RN-06 | O curso nunca é excluído. Ele é inativado e reativado, e o histórico é mantido (RG-14). |
| RN-07 | As turmas usam só cursos ativos ([T19 Turmas](prd-t19-turmas.md)), e o filtro "Curso" de [T06 Lista de alunos](prd-t06-lista-de-alunos.md) usa só cursos ativos. |
| RN-08 | A série é identificada de 1º a 4º, até o número de séries do curso (seção 4 do índice). |
| RN-09 | A lista tem o filtro "Situação" com Ativos, Inativos e Todos, com padrão Ativos, e a busca por sigla ou nome. A ordenação é pela sigla, de A a Z. |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Sigla única sem diferenciar maiúsculas | "tin" e "TIN" contam como a mesma sigla. |
| Nome único | O nome do curso também não se repete entre os cursos. |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Curso cadastrado | Sucesso | Curso cadastrado. (proposta) |
| Curso atualizado | Sucesso | Curso atualizado. (proposta) |
| Curso inativado | Sucesso | Curso inativado. (proposta) |
| Curso reativado | Sucesso | Curso reativado. (proposta) |
| Campo obrigatório vazio | Erro | Preencha o campo {campo} para salvar o curso. (proposta) |
| Sigla repetida | Erro | Já existe um curso com esta sigla. Use outra sigla e salve de novo. (proposta) |
| Sigla com mais de 10 caracteres | Erro | A sigla pode ter até 10 caracteres. Reduza a sigla e salve de novo. (proposta) |
| Número de séries fora do limite | Erro | O número de séries deve ser de 1 a 4. Corrija e salve de novo. (proposta) |
| Número de séries menor que a maior série de turma ativa | Erro | Este curso tem turma ativa na {série}. Informe pelo menos {série} séries ou inative a turma antes. (proposta) |
| Inativar curso com turmas ativas | Erro | Este curso tem turmas ativas. Inative as turmas antes de inativar o curso. (proposta) |
| Inativar curso | Confirmação | Inativar o curso {sigla}? Ele deixa de aparecer para novas turmas e o histórico é mantido. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Lista vazia, sem nenhum curso | Aviso | Nenhum curso cadastrado. (proposta) |
| Lista vazia por causa dos filtros | Aviso | Nenhum curso encontrado com estes filtros. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Listar cursos | Sim | Não | Não | Não |
| Filtrar e buscar cursos | Sim | Não | Não | Não |
| Cadastrar e editar curso | Sim | Não | Não | Não |
| Inativar e reativar curso | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga está logada, quando abre "Cursos", então o sistema mostra a lista com sigla, nome, número de séries e situação.
- [ ] Dado que a lista tem mais de 20 cursos, quando a psicopedagoga abre a tela, então o sistema mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado que a psicopedagoga abre "Cursos", quando a lista carrega, então o filtro "Situação" está em Ativos e os cursos aparecem pela sigla, de A a Z (RN-09).
- [ ] Dado que a psicopedagoga digita "inf" na busca, quando a lista é atualizada, então aparecem os cursos com "inf" na sigla ou no nome, ignorando maiúsculas e acentos (RN-09, RG-20).
- [ ] Dado que o filtro "Situação" está em Inativos e não há curso inativo, quando a lista carrega, então aparece a mensagem de lista vazia com a opção de limpar os filtros (RG-22).
- [ ] Dado que a psicopedagoga preencheu sigla, nome e número de séries válidos, quando escolhe "Salvar", então o curso é cadastrado como Ativo e o sistema mostra a confirmação.
- [ ] Dado que já existe um curso com a mesma sigla, quando a psicopedagoga tenta salvar outro com essa sigla, então o sistema não salva e mostra o erro de sigla repetida (RN-02).
- [ ] Dado que a sigla tem mais de 10 caracteres, quando a psicopedagoga tenta salvar, então o sistema não salva e mostra o erro do limite de caracteres (RN-02).
- [ ] Dado que o número de séries é 0 ou 5, quando a psicopedagoga tenta salvar, então o sistema não salva e mostra o erro do limite (RN-02).
- [ ] Dado que sigla ou nome estão vazios, quando a psicopedagoga tenta salvar, então o sistema não salva e indica o campo (RN-02).
- [ ] Dado que o curso tem turma ativa na 3ª série, quando a psicopedagoga tenta reduzir o número de séries para 2, então o sistema não salva e explica o que fazer (RN-04).
- [ ] Dado que o curso tem turmas ativas só até a 2ª série, quando a psicopedagoga reduz o número de séries para 2, então o sistema salva (RN-04).
- [ ] Dado que o curso tem turmas ativas, quando a psicopedagoga tenta inativar, então o sistema não inativa e mostra a mensagem de que é preciso inativar as turmas antes (RN-03).
- [ ] Dado que o curso não tem turmas ativas, quando a psicopedagoga escolhe "Inativar" e confirma, então o curso passa a Inativo (RN-03).
- [ ] Dado que a psicopedagoga vai cadastrar uma turma, quando abre a lista de cursos de [T19 Turmas](prd-t19-turmas.md), então o curso Inativo não aparece (RN-05).
- [ ] Dado que o curso está Inativo, quando a psicopedagoga escolhe "Reativar", então o curso volta para Ativo e aparece para novas turmas.
- [ ] Dado que o curso foi alterado, quando a psicopedagoga o vê na lista ou no formulário, então aparece "Editado em" com a data no formato dd/mm/aaaa e o autor da última alteração (RG-15, RG-18).
- [ ] Dado que a psicopedagoga alterou campos do formulário, quando tenta sair sem salvar, então o sistema pede confirmação (RG-29).
- [ ] Dado que o salvamento falhou, quando o formulário continua aberto, então o que foi digitado continua nos campos (RG-29).
- [ ] Dado que nenhum curso foi cadastrado, quando a psicopedagoga abre a tela, então vê a mensagem de lista vazia e a ação "Cadastrar curso" (RG-22).
- [ ] Dado que um professor, um aluno ou um responsável tenta abrir esta tela, quando a tela carrega, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado que a ação de salvar falha por falta de conexão ou erro inesperado, quando a psicopedagoga está no formulário, então o sistema mostra o aviso de [T26 Estados do sistema](prd-t26-estados-do-sistema.md) na própria tela, sem trocar de tela.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
