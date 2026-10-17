# PRD da tela de Busca no acervo

| Campo | Valor |
| --- | --- |
| Identificador | T25 |
| Situação | Rascunho |
| Perfis | Psicopedagoga |
| Telas relacionadas | [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T09 Dados de saúde](prd-t09-dados-de-saude.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md), [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md), [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md), [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md), [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 5 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga encontre qualquer material registrado sobre os alunos a partir de um termo, para que ela não precise abrir aluno por aluno.

## 2. Escopo

### O que entra no escopo

- Buscar um termo em todo o material registrado sobre os alunos.
- Filtrar por tipo de material, aluno e período.
- Ver os resultados agrupados por tipo, com a quantidade de cada grupo.
- Abrir o item encontrado a partir do resultado.

### O que não entra no escopo

- Busca dentro do conteúdo dos arquivos PDF: fica para depois. Na primeira versão, a busca em anexos usa o nome do arquivo (RN-08).
- Edição ou cadastro de qualquer item: ficam nas telas de origem de cada tipo (seção 6.5).
- Busca de alunos com filtros de lista, como curso e série: fica em [T06 Lista de alunos](prd-t06-lista-de-alunos.md).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Busca um termo em todo o acervo, filtra e abre os itens encontrados. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui quando lembra de uma palavra, um nome ou um assunto, mas não lembra em qual aluno ou em qual registro ele está.

**Origem da jornada:** Início → menu "Busca no acervo" → Busca no acervo. Do resultado, ela abre o item na tela de origem (seção 6.5).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Campo de busca | Um campo de texto, com no mínimo 3 caracteres (RN-02). |
| Filtros ativos | Tipo de material, aluno e período, sempre visíveis, com opção de limpar todos de uma vez (RG-21). |
| Grupos de resultados | Um grupo por tipo de material, com o nome do tipo e a quantidade de resultados do grupo. |
| Resultado | Trecho do texto com o termo destacado, nome do aluno e data. Ao escolher o resultado, o sistema abre o item (RN-06). |
| Total de resultados | Total de resultados encontrados (RG-19). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Termo da busca | Sim | Texto com no mínimo 3 caracteres. Ignora maiúsculas, minúsculas e acentos (RN-02, RN-03). |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Tipo de material | Alunos, Diagnósticos, Testes, Acompanhamentos, Características, Orientações, Atividades adaptadas, Observações dos professores, Informações recebidas, Anexos (pelo nome do arquivo) | Todos os tipos |
| Aluno | Alunos ativos e inativos (RN-07) | Todos |
| Período | Data inicial e data final, no formato dd/mm/aaaa (RG-18) | Sem limite |

### 5.3 Ordenação e paginação

- Ordenação padrão: não definida. Ver "Ordenação dentro de cada grupo" em 7.2.
- Outras ordenações: não definidas. Ver 7.2.
- Paginação: segue RG-19, com 20 itens por página e o total de resultados. Como a paginação funciona nos grupos: ver "Paginação dos grupos" em 7.2.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre "Busca no acervo".
2. Ela digita um termo com pelo menos 3 caracteres e, se quiser, escolhe filtros de tipo de material, aluno e período.
3. O sistema mostra os resultados agrupados por tipo de material, com a quantidade de cada grupo.
4. Cada resultado mostra o trecho com o termo destacado, o aluno e a data.
5. A psicopedagoga escolhe um resultado, e o sistema abre o item na tela de origem.

### 6.2 Fluxos alternativos

- Termo com menos de 3 caracteres: o sistema não busca e avisa o mínimo (RN-02).
- Nenhum resultado: o sistema mostra uma mensagem e a opção de limpar os filtros (RG-22).
- Filtros mantidos ao voltar do item para a busca: os filtros continuam ativos (RG-21).
- Outro perfil tenta abrir a tela: abre "Acesso negado" (RG-13).
- Item aberto que não está mais disponível: abre "Não encontrado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Buscar um termo | Psicopedagoga | Mostra os resultados agrupados por tipo, com a quantidade de cada grupo (RN-05). |
| Filtrar por tipo, aluno e período | Psicopedagoga | Restringe os resultados e mantém os filtros visíveis (RG-21). |
| Limpar filtros | Psicopedagoga | Remove todos os filtros de uma vez (RG-21). |
| Abrir um resultado | Psicopedagoga | Abre o item na tela de origem (RN-06). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Antes da primeira busca, a tela mostra uma mensagem pedindo o termo. A tela não tem ação principal de cadastro (RG-22). |
| Vazio, por causa dos filtros | Mostra uma mensagem e a opção de limpar os filtros (RG-22). |
| Sem permissão | Professor, aluno e responsável abrem "Acesso negado" (RG-13), de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado", de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |

### 6.5 Tipos de material e tela de destino

| Tipo de material | Tela de destino |
| --- | --- |
| Alunos | [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) |
| Diagnósticos | [T09 Dados de saúde](prd-t09-dados-de-saude.md) |
| Testes | [T09 Dados de saúde](prd-t09-dados-de-saude.md) |
| Acompanhamentos | [T10 Acompanhamentos](prd-t10-acompanhamentos.md) |
| Características | [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md) |
| Orientações | [T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md) |
| Atividades adaptadas | [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md) |
| Observações dos professores | [T17 Observações dos professores](prd-t17-observacoes-dos-professores.md) |
| Informações recebidas | [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) |
| Anexos (pelo nome do arquivo) | Ver "Destino do anexo" em 7.2 |

### 6.6 Entrega por fase

| Fase | Tipos de material com resultados |
| --- | --- |
| 1 | Alunos ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)), Características e Orientações ([T11 Características e orientações](prd-t11-caracteristicas-e-orientacoes.md)). |
| 3 | Diagnósticos e Testes ([T09 Dados de saúde](prd-t09-dados-de-saude.md)), Acompanhamentos ([T10 Acompanhamentos](prd-t10-acompanhamentos.md)), Atividades adaptadas ([T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md)), Observações dos professores ([T17 Observações dos professores](prd-t17-observacoes-dos-professores.md)). |
| 4 | Informações recebidas ([T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md)). |
| 5 | Esta tela. Todos os tipos já têm tela de origem entregue. |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-07, RG-13, RG-19 e RG-20 a RG-22. |
| RN-02 | O termo da busca tem no mínimo 3 caracteres. É uma exceção à RG-20, porque a busca percorre textos longos de todos os alunos. |
| RN-03 | A busca ignora maiúsculas, minúsculas e acentos (RG-20). Só o mínimo de caracteres muda. |
| RN-04 | Os filtros são tipo de material, aluno e período. O tipo "Anexos" busca pelo nome do arquivo. |
| RN-05 | Os resultados são agrupados por tipo de material, com a quantidade de cada grupo. |
| RN-06 | Cada resultado mostra o trecho com o termo destacado, o aluno e a data, e abre o item ao ser escolhido. |
| RN-07 | A busca inclui alunos inativos (RG-07). |
| RN-08 | Buscar dentro do conteúdo dos PDFs fica para depois. Na primeira versão, a busca usa o nome do arquivo. |
| RN-09 | Cada tipo de material só tem resultados quando a tela de origem foi entregue (seção 6.6). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Ordenação dentro de cada grupo | Do resultado mais recente para o mais antigo. |
| Paginação dos grupos | Cada grupo mostra 20 resultados por vez, com opção de ver mais do mesmo grupo. |
| Data de cada tipo para o filtro de período | A data do registro: data do cadastro para Alunos, data do diagnóstico para Diagnósticos, data do teste para Testes, data do acompanhamento para Acompanhamentos, data da última atualização para Características e Orientações, data da atividade para Atividades adaptadas, data da observação para Observações dos professores, data de envio para Informações recebidas e data de envio do arquivo para Anexos. |
| Versões anteriores de características e orientações | A busca olha só o texto atual. |
| Tipo "Testes" | Inclui o teste inicial e os testes aplicados. |
| Destino do anexo | O resultado do anexo abre o registro ao qual o arquivo pertence (RG-12). |
| Escolha de mais de um tipo | O filtro de tipo aceita mais de uma opção ao mesmo tempo. |
| Texto pesquisado em Alunos | A busca em Alunos olha o nome e o e-mail acadêmico, como em [T06 Lista de alunos](prd-t06-lista-de-alunos.md). |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Antes da primeira busca | Aviso | Digite pelo menos 3 caracteres para buscar no acervo. (proposta) |
| Termo com menos de 3 caracteres | Erro | O termo precisa ter pelo menos 3 caracteres. Digite mais letras e busque de novo. (proposta) |
| Nenhum resultado, sem filtros | Aviso | Nenhum resultado para o termo buscado. (proposta) |
| Nenhum resultado, por causa dos filtros | Aviso | Nenhum resultado com estes filtros. Limpe os filtros para ampliar a busca. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Buscar no acervo e filtrar | Sim | Não | Não | Não |
| Abrir o item encontrado | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga está logada, quando abre "Busca no acervo", então o sistema mostra o campo de busca e os filtros de tipo de material, aluno e período.
- [ ] Dado que a psicopedagoga digitou um termo com 3 caracteres ou mais, quando busca, então o sistema mostra os resultados agrupados por tipo de material, com a quantidade de cada grupo (RN-05).
- [ ] Dado que a psicopedagoga digitou um termo com 2 caracteres, quando tenta buscar, então o sistema não busca e avisa que o mínimo é de 3 caracteres (RN-02).
- [ ] Dado que existe o texto "Dificuldade de atenção", quando a psicopedagoga busca "ATENCAO", então o sistema encontra o texto, sem diferenciar maiúsculas e acentos (RN-03).
- [ ] Dado que há resultados, quando a psicopedagoga vê um resultado, então ele mostra o trecho com o termo destacado, o aluno e a data no formato dd/mm/aaaa (RN-06, RG-18).
- [ ] Dado que a psicopedagoga vê um resultado, quando escolhe o resultado, então o sistema abre o item na tela de origem do tipo de material (RN-06).
- [ ] Dado que a psicopedagoga escolheu o tipo "Atividades adaptadas", quando busca, então só aparecem resultados desse tipo (RN-04).
- [ ] Dado que a psicopedagoga escolheu o tipo "Anexos", quando busca, então o sistema compara o termo com o nome do arquivo e não com o conteúdo do PDF (RN-04, RN-08).
- [ ] Dado que a psicopedagoga escolheu um aluno no filtro, quando busca, então só aparecem resultados desse aluno (RN-04).
- [ ] Dado que a psicopedagoga escolheu um período, quando busca, então só aparecem resultados dentro do período (RN-04).
- [ ] Dado que existe material de um aluno inativo, quando a psicopedagoga busca um termo desse material, então o resultado aparece (RN-07, RG-07).
- [ ] Dado que a busca tem mais de 20 resultados, quando a psicopedagoga vê a lista, então o sistema mostra 20 itens por página e o total de resultados (RG-19).
- [ ] Dado que a psicopedagoga aplicou filtros, quando abre um resultado e volta para a busca, então os filtros continuam ativos e podem ser limpos de uma vez (RG-21).
- [ ] Dado que a busca não encontra nada, quando a psicopedagoga vê a tela, então o sistema mostra a mensagem de nenhum resultado (RG-22).
- [ ] Dado que a busca com filtros não encontra nada, quando a psicopedagoga vê a tela, então o sistema mostra a opção de limpar os filtros (RG-22).
- [ ] Dado que a tela de origem de um tipo de material foi entregue, quando a psicopedagoga busca, então esse tipo pode aparecer nos resultados (RN-09).
- [ ] Dado que um professor, um aluno ou um responsável tenta abrir esta tela, quando a tela carrega, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado que a busca falha por falta de conexão ou erro inesperado, quando a psicopedagoga busca, então o sistema mostra o aviso de [T26 Estados do sistema](prd-t26-estados-do-sistema.md) na própria tela, sem trocar de tela.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
