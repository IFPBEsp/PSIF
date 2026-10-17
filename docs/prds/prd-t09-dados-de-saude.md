# PRD da tela de Dados de saúde

| Campo | Valor |
| --- | --- |
| Identificador | T09 |
| Situação | Rascunho |
| Perfis | Psicopedagoga |
| Telas relacionadas | [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T10 Acompanhamentos](prd-t10-acompanhamentos.md), [T24 Formulários](prd-t24-formularios.md), [T25 Busca no acervo](prd-t25-busca-no-acervo.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 3 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga registre e consulte os diagnósticos, o teste inicial e os testes aplicados do aluno, para manter em um só lugar os registros de saúde que hoje ficam no papel.

## 2. Escopo

### O que entra no escopo

- Registrar, editar e consultar os diagnósticos do aluno, com data, descrição e laudo.
- Preencher, editar e consultar o teste inicial do aluno, com as 13 perguntas.
- Registrar, editar e consultar os testes aplicados ao aluno.
- Imprimir diagnósticos e o teste inicial, em branco ou preenchido.
- Anexar arquivos ao teste inicial e aos testes aplicados.

### O que não entra no escopo

- Acompanhamentos, que também são dados de saúde: ficam em [T10 Acompanhamentos](prd-t10-acompanhamentos.md).
- Cadastro e edição da identificação do aluno (nome, data de nascimento, telefone e curso): ficam em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md).
- Acesso por professor, aluno ou responsável: eles não usam esta tela (RG-10, RG-11).
- Busca por texto em diagnósticos, testes e anexos: fica em [T25 Busca no acervo](prd-t25-busca-no-acervo.md), na fase 5.
- Formulário "teste inicial" em [T24 Formulários](prd-t24-formularios.md), na fase 5. O laudo não é um formulário: ele é impresso a partir do arquivo anexado ao diagnóstico.
- Notificações: esta tela não gera nenhuma.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Registra, edita, consulta e imprime os dados de saúde dos alunos. Vê, registra e edita também os de alunos inativos (RG-07, RN-16). |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). Nunca vê dados de saúde (RG-11). |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui para registrar um laudo recebido, aplicar o teste inicial no começo do atendimento ou lançar o resultado de um teste, e depois para consultar esses registros.

**Origem da jornada:** Início → Alunos → Lista de alunos → Perfil do aluno → aba "Dados de saúde".

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Aluno | Nome do aluno ao qual os dados de saúde pertencem. |
| Seção Diagnósticos | Lista dos diagnósticos do aluno. Cada linha mostra data, descrição e laudo. O diagnóstico mais recente fica em destaque. |
| Laudo do diagnóstico | Indicação de que o diagnóstico tem laudo e ação para ver o arquivo. |
| Seção Teste inicial | Identificação do aluno (nome, idade, data de nascimento, telefone e curso), data de aplicação, as 13 perguntas com as respostas, observações e anexo. |
| Seção Testes aplicados | Lista dos testes aplicados. Cada linha mostra nome, data e resultado. |
| Autoria dos registros | Cada registro mostra quem criou e quando, e "Editado em" com data e autor da última alteração (RG-15). |
| Botões | Adicionar diagnóstico, Preencher teste inicial, Adicionar teste aplicado, Editar, Ver, Imprimir. |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

#### Seção Diagnósticos

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Data | Sim | Formato dd/mm/aaaa (RG-18). Não pode ser futura. |
| Descrição | Só se não houver laudo | Texto. É preciso informar a descrição ou o laudo (RN-05). |
| Laudo | Só se não houver descrição | Arquivo em PDF com até 10 MB (RG-16). É preciso informar a descrição ou o laudo (RN-05). |

#### Seção Teste inicial

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nome, idade, data de nascimento, telefone e curso | Não | Identificação preenchida a partir do cadastro do aluno. Ver "Identificação do teste inicial" e "Idade no teste inicial" em 7.2. |
| Data de aplicação | Sim | Formato dd/mm/aaaa (RG-18). |
| Resposta da pergunta 1 | Não | Texto. Pergunta: "Você consegue ter uma boa interação social na escola? Tem amigos dentro e fora da instituição?" |
| Resposta da pergunta 2 | Não | Texto. Pergunta: "Você gosta da instituição em que estuda?" |
| Resposta da pergunta 3 | Não | Texto. Pergunta: "Você tem rotina de estudos em casa?" |
| Resposta da pergunta 4 | Não | Texto. Pergunta: "Você gosta de atividades práticas?" |
| Resposta da pergunta 5 | Não | Texto. Pergunta: "Você gosta de atividades teóricas?" |
| Resposta da pergunta 6 | Não | Texto. Pergunta: "Você gosta de apresentar trabalhos? Se sente ansioso ou nervoso?" |
| Resposta da pergunta 7 | Não | Texto. Pergunta: "Em que tipo de prova você acha que se sairia melhor: objetiva, de múltipla escolha, ou com questões abertas?" |
| Resposta da pergunta 8 | Não | Texto. Pergunta: "Qual disciplina você mais gosta e qual menos gosta?" |
| Resposta da pergunta 9 | Não | Texto. Pergunta: "Qual é a sua maior dificuldade nos estudos?" |
| Resposta da pergunta 10 | Não | Texto. Pergunta: "Você conseguia acompanhar as aulas online? Quais dificuldades encontrava?" |
| Resposta da pergunta 11 | Não | Texto. Pergunta: "O que o professor poderia fazer para ajudar quando você não entende um assunto?" |
| Resposta da pergunta 12 | Não | Texto. Pergunta: "O que a instituição poderia fazer para melhorar a convivência e o ensino?" |
| Resposta da pergunta 13 | Não | Texto. Pergunta: "O que você mais gosta de fazer quando não está na escola?" |
| Observações | Não | Texto livre. |
| Anexo | Não | PDF, JPG ou PNG com até 10 MB (RG-16). Ver "Anexos do teste inicial" em 7.2. |

#### Seção Testes aplicados

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nome do teste | Sim | Texto. |
| Data | Sim | Formato dd/mm/aaaa (RG-18). Não pode ser futura. |
| Resultado ou observação | Sim | Texto. É preciso informar o resultado ou a observação. |
| Anexos | Não | PDF, JPG ou PNG com até 10 MB cada e até 5 por registro (RG-16). |

### 5.2 Filtros

Não se aplica.

### 5.3 Ordenação e paginação

- Ordenação padrão: ver "Ordem das listas" em 7.2.
- Outras ordenações: não se aplica.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre a aba "Dados de saúde" no perfil do aluno.
2. O sistema mostra as seções Diagnósticos, Teste inicial e Testes aplicados.
3. A psicopedagoga escolhe uma ação, por exemplo "Adicionar diagnóstico".
4. A psicopedagoga preenche os campos e salva.
5. O sistema valida os campos, guarda o registro com autor e data (RG-15) e mostra o registro na seção.

### 6.2 Fluxos alternativos

- Campo obrigatório vazio ou data futura: o sistema não salva, mostra a mensagem junto ao campo e mantém o que foi digitado.
- Diagnóstico sem descrição e sem laudo: o sistema não salva e pede uma das duas informações.
- Arquivo fora das regras de anexo (RG-16): o sistema não aceita o arquivo e explica o limite.
- Salvar falha: o que foi digitado continua no formulário (RG-29).
- Sair com alterações não salvas: o sistema pede confirmação (RG-29).
- Aluno que já tem teste inicial: a seção mostra o teste e a ação "Editar". Não existe segundo teste inicial (RN-07).
- Usuário que não é psicopedagoga: abre "Acesso negado" (RG-13).
- Aluno que não existe: abre "Não encontrado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Adicionar diagnóstico | Psicopedagoga | Abre o formulário de diagnóstico. Ao salvar, o diagnóstico entra na lista. |
| Editar diagnóstico | Psicopedagoga | Abre o formulário com os dados atuais. Ao salvar, mostra "Editado em" (RG-15). |
| Ver laudo | Psicopedagoga | Abre o arquivo do laudo anexado ao diagnóstico. |
| Imprimir diagnóstico | Psicopedagoga | Gera a versão impressa com "Documento confidencial" e registra quem imprimiu, quando e o quê (RG-30). Ver "Impressão do diagnóstico" em 7.2. |
| Preencher teste inicial | Psicopedagoga | Abre o formulário do teste inicial com a identificação preenchida. Só aparece se o aluno ainda não tem teste inicial. |
| Editar teste inicial | Psicopedagoga | Abre o formulário com as respostas atuais. |
| Imprimir teste inicial em branco | Psicopedagoga | Gera a versão impressa com as 13 perguntas e sem respostas (RG-30). |
| Imprimir teste inicial preenchido | Psicopedagoga | Gera a versão impressa com as respostas, com "Documento confidencial". Registra quem imprimiu, quando e o quê (RG-30). |
| Adicionar teste aplicado | Psicopedagoga | Abre o formulário de teste aplicado. Ao salvar, o teste entra na lista. |
| Editar teste aplicado | Psicopedagoga | Abre o formulário com os dados atuais. Ao salvar, mostra "Editado em" (RG-15). |
| Ver teste aplicado | Psicopedagoga | Mostra nome, data, resultado ou observação e anexos do teste. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Cada seção vazia mostra a mensagem da seção 9 e a ação principal: "Adicionar diagnóstico", "Preencher teste inicial" ou "Adicionar teste aplicado" (RG-22). |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Professor, aluno e responsável abrem "Acesso negado". Aluno que não existe abre "Não encontrado" (RG-13). Telas em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Sem conexão ou falha inesperada abrem "Sem conexão" ou "Erro inesperado" de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). O que foi digitado continua no formulário (RG-29). |

### 6.5 Entrega por fase

| Fase | O que aparece |
| --- | --- |
| 3 | Esta tela inteira. A aba "Dados de saúde" no perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)) só aparece a partir desta fase. O botão "Imprimir" usa a versão impressa padrão (RG-30). |
| 5 | Busca em diagnósticos, testes e anexos ([T25 Busca no acervo](prd-t25-busca-no-acervo.md)) e o formulário "teste inicial" em [T24 Formulários](prd-t24-formularios.md). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Só a psicopedagoga acessa esta tela. O professor nunca acessa. Aluno e responsável não veem os dados de saúde desta tela (RG-10, RG-11, RG-13). |
| RN-02 | Cada anexo tem a mesma visibilidade do registro ao qual pertence (RG-12). |
| RN-03 | O aluno pode ter vários diagnósticos. |
| RN-04 | A data do diagnóstico é obrigatória e não pode ser futura. |
| RN-05 | O diagnóstico precisa ter a descrição, o laudo ou os dois. |
| RN-06 | O laudo é um arquivo em PDF. Quando impresso, sai do arquivo anexado ao diagnóstico. |
| RN-07 | Cada aluno tem um único teste inicial. |
| RN-08 | A identificação do teste inicial é preenchida a partir do cadastro: nome, idade, data de nascimento, telefone e curso. |
| RN-09 | A data de aplicação do teste inicial é obrigatória. Cada uma das 13 perguntas tem um campo de resposta em texto. |
| RN-10 | O teste aplicado precisa de nome, data não futura e resultado ou observação. |
| RN-11 | A psicopedagoga vê os dados de saúde de alunos ativos e inativos (RG-07). |
| RN-12 | Toda impressão usa a versão impressa padrão. Documento com dados de saúde leva "Documento confidencial". A impressão de documento preenchido registra quem imprimiu, quando e o quê (RG-30). |
| RN-13 | Todo registro mostra quem criou e quando, e "Editado em" quando foi alterado (RG-15). |
| RN-14 | Sair do formulário com alterações não salvas pede confirmação. Se salvar falhar, o que foi digitado continua (RG-29). |
| RN-15 | Anexos seguem RG-16. Datas seguem RG-18. As listas seguem RG-19. Lista vazia segue RG-22. Confirmações seguem RG-23 e botões e erros seguem RG-24. A tela funciona no computador e no celular e só com o teclado (RG-26). |
| RN-16 | A psicopedagoga registra e edita dados de saúde de aluno inativo, como faz com aluno ativo. |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Exclusão de registros | Diagnóstico ou teste lançado por engano não pode ser excluído nesta tela. A psicopedagoga corrige pela edição. |
| Idade no teste inicial | A idade é calculada na data de aplicação e fica guardada com o teste. |
| Identificação do teste inicial | Os dados de identificação vêm do cadastro e não são editados nesta tela. Mudanças são feitas em [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md). |
| Perguntas sem resposta | O teste inicial pode ser salvo com perguntas sem resposta. Só a data de aplicação é obrigatória. |
| Limite de texto | Descrição do diagnóstico, respostas, observações e resultado aceitam até 5.000 caracteres cada. |
| Anexos do teste inicial | O teste inicial aceita até 5 anexos (RG-16), embora o campo seja opcional. |
| Impressão do diagnóstico | O botão "Imprimir" do diagnóstico imprime o registro (data e descrição). |
| Impressão dos testes aplicados | O teste aplicado também tem o botão "Imprimir", com as mesmas regras do diagnóstico. |
| Marcação na impressão em branco | O teste inicial em branco leva "Documento confidencial", para manter uma só versão impressa. |
| Destaque do diagnóstico mais recente | O diagnóstico de data mais recente aparece no topo da lista, com fundo diferente e o selo "Mais recente". |
| Ordem das listas | Diagnósticos e testes aplicados aparecem do mais recente para o mais antigo, pela data. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

Não se aplica. Esta tela não gera notificações (seção 7 do índice).

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Diagnóstico salvo | Sucesso | Diagnóstico salvo. (proposta) |
| Teste inicial salvo | Sucesso | Teste inicial salvo. (proposta) |
| Teste aplicado salvo | Sucesso | Teste aplicado salvo. (proposta) |
| Data futura | Erro | A data não pode ser futura. Informe a data de hoje ou uma data anterior. (proposta) |
| Diagnóstico sem descrição e sem laudo | Erro | Informe a descrição ou envie o laudo para salvar o diagnóstico. (proposta) |
| Data de aplicação vazia | Erro | Informe a data de aplicação para salvar o teste inicial. (proposta) |
| Nome do teste vazio | Erro | Informe o nome do teste para salvar. (proposta) |
| Teste aplicado sem resultado nem observação | Erro | Informe o resultado ou uma observação para salvar o teste. (proposta) |
| Laudo fora das regras | Erro | O laudo não foi aceito. Envie um arquivo em PDF com até 10 MB. (proposta) |
| Anexo fora das regras | Erro | O anexo não foi aceito. Envie um PDF, JPG ou PNG com até 10 MB. (proposta) |
| Limite de anexos | Erro | Cada registro aceita até 5 anexos. Remova um anexo para enviar outro. (proposta) |
| Falha ao salvar | Erro | Não foi possível salvar. Verifique a conexão e tente de novo. O que você digitou foi mantido. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Seção Diagnósticos vazia | Aviso | Nenhum diagnóstico registrado para este aluno. (proposta) |
| Seção Teste inicial vazia | Aviso | O teste inicial deste aluno ainda não foi preenchido. (proposta) |
| Seção Testes aplicados vazia | Aviso | Nenhum teste aplicado registrado para este aluno. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Abrir a tela | Sim | Não | Não | Não |
| Ver diagnósticos e laudo | Sim | Não | Não | Não |
| Adicionar e editar diagnóstico | Sim | Não | Não | Não |
| Imprimir diagnóstico | Sim | Não | Não | Não |
| Ver teste inicial | Sim | Não | Não | Não |
| Preencher e editar teste inicial | Sim | Não | Não | Não |
| Imprimir teste inicial, em branco ou preenchido | Sim | Não | Não | Não |
| Ver testes aplicados | Sim | Não | Não | Não |
| Adicionar e editar teste aplicado | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga abre o perfil de um aluno, quando escolhe a aba "Dados de saúde", então a tela mostra as seções Diagnósticos, Teste inicial e Testes aplicados.
- [ ] Dado que a psicopedagoga abre o perfil de um aluno inativo, quando abre a aba "Dados de saúde", então ela vê os registros (RG-07).
- [ ] Dado um aluno inativo, quando a psicopedagoga registra um teste aplicado ou edita um diagnóstico dele, então o sistema salva o registro como faria para um aluno ativo (RN-16).
- [ ] Dado um aluno com vários diagnósticos, quando a lista é exibida, então todos aparecem com data, descrição e laudo, e o mais recente fica em destaque.
- [ ] Dado o formulário de diagnóstico, quando a psicopedagoga informa uma data futura, então o sistema não salva e mostra a mensagem de data futura.
- [ ] Dado o formulário de diagnóstico, quando a psicopedagoga deixa a descrição e o laudo vazios, então o sistema não salva e pede uma das duas informações.
- [ ] Dado o formulário de diagnóstico, quando a psicopedagoga informa só a descrição, então o diagnóstico é salvo.
- [ ] Dado o formulário de diagnóstico, quando a psicopedagoga envia só o laudo em PDF, então o diagnóstico é salvo.
- [ ] Dado um laudo que não é PDF ou que passa de 10 MB, quando a psicopedagoga tenta enviar, então o sistema não aceita o arquivo e explica o limite.
- [ ] Dado um diagnóstico com laudo, quando a psicopedagoga escolhe "Ver laudo", então o arquivo anexado abre.
- [ ] Dado um diagnóstico editado, quando a lista é exibida, então o registro mostra "Editado em" com data e autor (RG-15).
- [ ] Dado um aluno sem teste inicial, quando a psicopedagoga escolhe "Preencher teste inicial", então o formulário abre com nome, idade, data de nascimento, telefone e curso preenchidos a partir do cadastro e com as 13 perguntas com o texto exato.
- [ ] Dado o formulário do teste inicial, quando a psicopedagoga deixa a data de aplicação vazia, então o sistema não salva e pede a data.
- [ ] Dado o formulário do teste inicial com a data de aplicação preenchida, quando a psicopedagoga salva, então o teste inicial é guardado com as respostas, as observações e o anexo informados.
- [ ] Dado um aluno que já tem teste inicial, quando a psicopedagoga abre a seção, então ela vê o teste e a ação "Editar", e não consegue criar um segundo teste inicial.
- [ ] Dado o teste inicial, quando a psicopedagoga escolhe imprimir em branco, então a versão impressa mostra as 13 perguntas sem respostas, o nome do campus, o nome do sistema e a data de impressão.
- [ ] Dado um teste inicial preenchido, quando a psicopedagoga escolhe imprimir preenchido, então a versão impressa mostra as respostas e "Documento confidencial", e o sistema registra quem imprimiu, quando e o quê.
- [ ] Dado o formulário de teste aplicado, quando a psicopedagoga deixa o nome, a data ou o resultado e a observação vazios, então o sistema não salva e indica o que falta.
- [ ] Dado o formulário de teste aplicado, quando a psicopedagoga informa uma data futura, então o sistema não salva e mostra a mensagem de data futura.
- [ ] Dado um teste aplicado salvo, quando a seção é exibida, então a lista mostra nome, data e resultado, e a psicopedagoga consegue editar e ver o teste.
- [ ] Dado um anexo de teste aplicado, quando a psicopedagoga tenta enviar um sexto anexo, então o sistema não aceita e mostra o limite de 5 anexos.
- [ ] Dado um formulário com alterações não salvas, quando a psicopedagoga tenta sair, então o sistema pede confirmação dizendo que as alterações serão perdidas (RG-29).
- [ ] Dado que salvar falhou, quando o formulário continua aberto, então o que foi digitado continua preenchido (RG-29).
- [ ] Dado que uma seção não tem registros, quando a tela é exibida, então a seção mostra a mensagem de vazio e a ação principal (RG-22).
- [ ] Dado um professor, quando tenta abrir esta tela, então o sistema abre "Acesso negado" e não mostra nenhum dado de saúde (RG-11, RG-13).
- [ ] Dado um aluno ou um responsável, quando tenta abrir esta tela, então o sistema abre "Acesso negado" (RG-10, RG-13).
- [ ] Dado um aluno que não existe, quando a psicopedagoga tenta abrir esta tela, então o sistema abre "Não encontrado" (RG-13).
- [ ] Dado um anexo de diagnóstico ou de teste, quando um usuário sem acesso ao registro tenta abri-lo, então o sistema não o mostra, porque o anexo tem a mesma visibilidade do registro (RG-12).
- [ ] Dado que a conexão caiu, quando a psicopedagoga abre a tela, então o sistema mostra "Sem conexão" e, se a falha for outra, "Erro inesperado".
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
