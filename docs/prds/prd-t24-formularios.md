# PRD da tela de Formulários

| Campo | Valor |
| --- | --- |
| Identificador | T24 |
| Situação | Rascunho |
| Perfis | Psicopedagoga |
| Telas relacionadas | [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T09 Dados de saúde](prd-t09-dados-de-saude.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md), [T12 Planejamento semanal](prd-t12-planejamento-semanal.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 5 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga imprima os documentos do atendimento, em branco ou preenchidos, a partir de um só lugar, para que os registros que ainda circulam no papel sigam o mesmo modelo.

## 2. Escopo

### O que entra no escopo

- Reunir os quatro modelos: ficha do aluno, teste inicial, relatório de acompanhamento e planejamento semanal.
- Imprimir um modelo em branco.
- Imprimir um modelo preenchido com os dados de um aluno e, quando o modelo exigir, de um registro dele.
- Preencher um modelo na tela e imprimir, sem salvar.

### O que não entra no escopo

- Impressão a partir da própria tela de origem: os botões "Imprimir" de [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T09 Dados de saúde](prd-t09-dados-de-saude.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md) e [T12 Planejamento semanal](prd-t12-planejamento-semanal.md) funcionam desde a fase de cada tela, sem depender desta tela.
- Laudo: não é um modelo, porque é emitido por um profissional de saúde fora do sistema. Ele é impresso a partir do arquivo anexado ao diagnóstico em [T09 Dados de saúde](prd-t09-dados-de-saude.md).
- Salvar o que foi preenchido na tela: o preenchimento na tela serve só para imprimir.
- Conteúdo de cada modelo: a sugestão está em 7.2.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Escolhe o modelo e imprime em branco, preenchido ou preenchido na tela. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui quando precisa de um documento em papel, por exemplo uma ficha em branco para um atendimento fora da sala ou um relatório preenchido para entregar.

**Origem da jornada:** Início → menu "Formulários" → Formulários.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Modelos | Os quatro modelos: ficha do aluno, teste inicial, relatório de acompanhamento e planejamento semanal. |
| Ações de cada modelo | "Imprimir em branco", "Imprimir preenchido" e "Preencher na tela e imprimir". |
| Escolha do aluno | Lista de alunos ativos e inativos (RN-04). |
| Escolha do registro | Aparece só para o modelo que exige um registro: qual relatório ou qual semana (RN-04). |
| Versão impressa | Nome do campus, nome do sistema e data de impressão. Documento com dados de saúde e a ficha do aluno têm a marcação "Documento confidencial" (RN-05, RN-06). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Modelo | Sim | Ficha do aluno, teste inicial, relatório de acompanhamento ou planejamento semanal. |
| Aluno | Sim, para imprimir preenchido | Alunos ativos e inativos (RG-07). Não é pedido para imprimir em branco nem para preencher na tela. |
| Registro | Só quando o modelo exigir | Para o relatório de acompanhamento, qual relatório. Para o planejamento semanal, qual semana. A ficha do aluno e o teste inicial pedem só o aluno (RN-04). |

### 5.2 Filtros

Não se aplica.

### 5.3 Ordenação e paginação

- Ordenação padrão: Não se aplica.
- Outras ordenações: Não se aplica.
- Paginação: Não se aplica.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre "Formulários".
2. O sistema mostra os quatro modelos.
3. A psicopedagoga escolhe um modelo e a ação "Imprimir preenchido".
4. O sistema pede o aluno e, quando o modelo exigir, o registro.
5. A psicopedagoga escolhe o aluno e o registro e confirma.
6. O sistema monta a versão impressa do documento preenchido, registra a impressão (RN-07) e a psicopedagoga imprime.

### 6.2 Fluxos alternativos

- Imprimir em branco: o sistema mostra a versão impressa do modelo vazio, sem pedir aluno.
- Preencher na tela e imprimir: o sistema mostra o modelo com os campos para digitar, a psicopedagoga preenche e imprime, e nada do que foi digitado fica salvo. A impressão não fica registrada (RN-08).
- Aluno sem registro do tipo que o modelo exige: o sistema avisa e continua oferecendo a impressão em branco (ver 7.2).
- Modelo com dados de saúde: a versão impressa leva a marcação "Documento confidencial" (RN-06).
- Falha ao gerar a impressão: o sistema mostra o aviso de erro de [T26 Estados do sistema](prd-t26-estados-do-sistema.md) na própria tela.
- Outro perfil tenta abrir a tela: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Imprimir em branco | Psicopedagoga | Mostra o modelo sem dados de aluno, com a versão impressa padrão (RN-05). |
| Imprimir preenchido | Psicopedagoga | Pede o aluno e, quando o modelo exigir, o registro. Mostra o documento com os dados do sistema e registra a impressão (RN-07). |
| Preencher na tela e imprimir | Psicopedagoga | Mostra o modelo com campos para digitar. Imprime o que foi digitado, sem salvar e sem registrar a impressão (RN-08). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Não se aplica à lista de modelos, que é fixa. Para o aluno sem registro do tipo exigido, ver a mensagem na seção 9. |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Professor, aluno e responsável abrem "Acesso negado" (RG-13), de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado", de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |

### 6.5 Informações exigidas por modelo

| Modelo | Aluno | Registro | Documento confidencial |
| --- | --- | --- | --- |
| Ficha do aluno | Sim | Não | Sim (RN-06) |
| Teste inicial | Sim | Não, porque cada aluno tem um teste inicial | Sim (RN-06) |
| Relatório de acompanhamento | Sim | Sim, qual relatório | Sim (RN-06) |
| Planejamento semanal | Sim | Sim, qual semana | Não |

### 6.6 Entrega por fase

| Fase | O que está disponível |
| --- | --- |
| 1 | Botão "Imprimir" da ficha do aluno em [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md). |
| 3 | Impressão do teste inicial, em branco e preenchido, em [T09 Dados de saúde](prd-t09-dados-de-saude.md). Impressão do acompanhamento em [T10 Acompanhamentos](prd-t10-acompanhamentos.md). Impressão do planejamento em [T12 Planejamento semanal](prd-t12-planejamento-semanal.md). |
| 5 | Esta tela, que reúne os quatro modelos em um lugar. Todos os modelos já têm tela de origem entregue. |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-07, RG-10, RG-13, RG-18 e RG-30. |
| RN-02 | Os modelos são quatro: ficha do aluno, teste inicial, relatório de acompanhamento e planejamento semanal. |
| RN-03 | As ações são três: imprimir em branco, imprimir preenchido e preencher na tela e imprimir, sem salvar. |
| RN-04 | Imprimir preenchido exige escolher o aluno e, quando o modelo exigir, o registro, por exemplo qual relatório ou qual semana. A escolha do aluno inclui alunos inativos (RG-07). |
| RN-05 | Todo "Imprimir" usa a mesma versão impressa, desde a fase em que a tela é entregue. Ela tem o nome do campus, o nome do sistema e a data de impressão no formato dd/mm/aaaa (RG-30, RG-18). |
| RN-06 | Documento com dados de saúde tem a marcação "Documento confidencial": teste inicial e relatório de acompanhamento (RG-10, RG-30). A ficha do aluno também leva a marcação, por conter dados pessoais do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)). |
| RN-07 | Cada impressão de documento preenchido com os dados do sistema ("Imprimir preenchido") fica registrada com quem imprimiu, quando e o quê (RG-30). |
| RN-08 | Preencher na tela e imprimir não salva o que foi digitado e não registra a impressão (RG-30). |
| RN-09 | Esta tela reúne os modelos em um lugar. Os botões "Imprimir" das outras telas funcionam desde a fase de cada tela, sem depender desta. |
| RN-10 | O laudo não é um modelo. Ele é impresso a partir do arquivo anexado ao diagnóstico ([T09 Dados de saúde](prd-t09-dados-de-saude.md)). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Conteúdo de cada modelo | Cada modelo tem os mesmos campos da tela de origem: a ficha do aluno tem os dados do perfil, o teste inicial tem as perguntas e as respostas, o relatório de acompanhamento tem o texto do relatório e o planejamento semanal tem a grade de segunda a domingo. |
| Tipos de acompanhamento no relatório | O modelo de relatório de acompanhamento aceita só acompanhamentos do tipo Relatório. |
| Planejamento em rascunho | O planejamento semanal em Rascunho pode ser impresso, com a marcação "Rascunho" na versão impressa. |
| Aluno sem registro do tipo exigido | A tela avisa e mantém só a impressão em branco. |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Marcação na versão impressa de documento com dados de saúde e da ficha do aluno | Aviso | Documento confidencial |
| Aluno sem registro do tipo exigido pelo modelo | Aviso | Este aluno ainda não tem {registro} para imprimir. Você pode imprimir o modelo em branco. (proposta) |
| Antes de escolher o aluno | Aviso | Escolha o aluno para imprimir o documento preenchido. (proposta) |
| Imprimir preenchido sem aluno | Erro | Escolha o aluno antes de imprimir. (proposta) |
| Imprimir preenchido sem registro | Erro | Escolha {registro} antes de imprimir. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Imprimir em branco | Sim | Não | Não | Não |
| Imprimir preenchido | Sim | Não | Não | Não |
| Preencher na tela e imprimir | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga está logada, quando abre "Formulários", então o sistema mostra os quatro modelos: ficha do aluno, teste inicial, relatório de acompanhamento e planejamento semanal (RN-02).
- [ ] Dado que a psicopedagoga escolheu um modelo, quando escolhe "Imprimir em branco", então o sistema mostra o modelo sem dados de aluno, com nome do campus, nome do sistema e data de impressão (RN-05).
- [ ] Dado que a psicopedagoga escolheu a ficha do aluno, quando escolhe "Imprimir preenchido", então o sistema pede só o aluno (RN-04).
- [ ] Dado que a psicopedagoga escolheu o relatório de acompanhamento, quando escolhe "Imprimir preenchido", então o sistema pede o aluno e qual relatório (RN-04).
- [ ] Dado que a psicopedagoga escolheu o planejamento semanal, quando escolhe "Imprimir preenchido", então o sistema pede o aluno e qual semana (RN-04).
- [ ] Dado que existe um aluno inativo, quando a psicopedagoga escolhe o aluno para imprimir um documento preenchido, então o aluno inativo aparece na escolha (RG-07, RN-04).
- [ ] Dado que a psicopedagoga escolheu aluno e registro, quando imprime o documento preenchido, então o sistema registra quem imprimiu, quando e o quê (RN-07).
- [ ] Dado que a psicopedagoga imprime o teste inicial ou o relatório de acompanhamento, quando vê a versão impressa, então ela tem a marcação "Documento confidencial" (RN-06).
- [ ] Dado que a psicopedagoga imprime o planejamento semanal, quando vê a versão impressa, então ela não tem a marcação "Documento confidencial" (RN-06).
- [ ] Dado que a psicopedagoga escolheu "Preencher na tela e imprimir", quando digita os campos e imprime, então o sistema imprime o que foi digitado, não salva nada e não registra a impressão (RN-08).
- [ ] Dado que a psicopedagoga imprime a ficha do aluno, em branco ou preenchida, quando vê a versão impressa, então ela tem a marcação "Documento confidencial" (RN-06).
- [ ] Dado que a psicopedagoga preencheu um modelo na tela, quando fecha a tela e volta, então o que foi digitado não aparece mais (RN-08).
- [ ] Dado que a data de impressão aparece no documento, quando a psicopedagoga a vê, então ela está no formato dd/mm/aaaa, no horário de Brasília (RG-18).
- [ ] Dado que a psicopedagoga imprime a ficha do aluno pelo botão "Imprimir" do perfil do aluno, quando imprime pelo modelo desta tela, então a versão impressa é a mesma (RN-05).
- [ ] Dado que a fase de [T09 Dados de saúde](prd-t09-dados-de-saude.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md) ou [T12 Planejamento semanal](prd-t12-planejamento-semanal.md) já foi entregue, quando a psicopedagoga usa o botão "Imprimir" dessas telas, então ele funciona sem depender de "Formulários" (RN-09).
- [ ] Dado que a psicopedagoga quer imprimir um laudo, quando procura em "Formulários", então não encontra o laudo como modelo e o imprime a partir do arquivo anexado ao diagnóstico (RN-10).
- [ ] Dado que a psicopedagoga não escolheu o aluno, quando tenta imprimir preenchido, então o sistema não imprime e pede o aluno (RN-04).
- [ ] Dado que a conexão cai ou acontece um erro inesperado, quando a psicopedagoga tenta imprimir, então o sistema mostra o aviso de [T26 Estados do sistema](prd-t26-estados-do-sistema.md) na própria tela, sem trocar de tela.
- [ ] Dado que um professor, um aluno ou um responsável tenta abrir esta tela, quando a tela carrega, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
