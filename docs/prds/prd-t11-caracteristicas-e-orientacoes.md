# PRD da tela de Características e orientações

| Campo | Valor |
| --- | --- |
| Identificador | T11 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor |
| Telas relacionadas | [T03 Notificações](prd-t03-notificacoes.md), [T06 Lista de alunos](prd-t06-lista-de-alunos.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T22 Dificuldades](prd-t22-dificuldades.md), [T25 Busca no acervo](prd-t25-busca-no-acervo.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga registre as características e as orientações de cada aluno, para que os professores saibam como o aluno aprende e como lidar com ele antes de adaptar atividades.

## 2. Escopo

### O que entra no escopo

- Escrever e editar as características do aluno, com formatação simples (negrito e listas).
- Escrever e editar as orientações para os professores, com a mesma formatação.
- Adicionar e remover anexos em cada seção.
- Mostrar a data e o autor da última atualização de cada seção.
- Guardar cada alteração salva como uma nova versão e permitir que a psicopedagoga veja as versões anteriores.
- Avisar os professores do aluno quando o conteúdo é atualizado.
- Deixar o professor ler o conteúdo do aluno ativo das suas turmas.

### O que não entra no escopo

- Acesso de aluno e responsável: eles não veem esta tela.
- Campo "Características" do catálogo de dificuldades: é outro conteúdo, mantido em [T22 Dificuldades](prd-t22-dificuldades.md). Não se confunde com a seção "Características" desta tela.
- Dados de saúde: ficam em [T09 Dados de saúde](prd-t09-dados-de-saude.md) e [T10 Acompanhamentos](prd-t10-acompanhamentos.md). O professor nunca os vê (RG-11).
- Busca por texto em características e orientações: fica em [T25 Busca no acervo](prd-t25-busca-no-acervo.md), na fase 5.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Edita características e orientações dos alunos, vê e edita também as de alunos inativos (RG-07, RN-16), gerencia anexos e vê as versões anteriores. |
| Professor | Só lê características, orientações e anexos dos alunos ativos das turmas em que leciona (RG-08). Não edita e não vê versões anteriores. |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui depois de conhecer o aluno, para registrar como ele aprende e o que os professores devem fazer. O professor chega aqui antes de planejar ou adaptar uma atividade para o aluno.

**Origem da jornada:** Início → Alunos → Lista de alunos → Perfil do aluno → aba "Características" ou aba "Orientações". O professor chega também pelo Início e pela lista de turmas até o perfil do aluno.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Aluno | Nome do aluno ao qual o conteúdo pertence. |
| Seção Características | Texto que descreve como o aluno se comporta e aprende, com anexos, data e autor da última atualização. |
| Seção Orientações | Texto que explica como o professor deve lidar com o aluno e adaptar atividades, com anexos, data e autor da última atualização. |
| Texto | Texto com negrito e listas. |
| Anexos | Arquivos da seção, com ação para abrir. A psicopedagoga também vê a ação de remover. |
| Última atualização | Data e autor da última alteração da seção (RG-15). |
| Versões anteriores | Lista das versões guardadas de cada seção, com data e autor. Só a psicopedagoga vê. |
| Botões | Editar, Salvar, Cancelar, Adicionar anexo, Remover anexo, Ver versões anteriores. Só a psicopedagoga vê estes botões. |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

Os campos valem para cada uma das duas seções, Características e Orientações.

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Texto | Não | Aceita negrito e listas. A seção pode ficar sem conteúdo. Ver "Limite de texto" em 7.2. |
| Anexos | Não | PDF, JPG ou PNG com até 10 MB cada e até 5 por registro (RG-16). |

### 5.2 Filtros

Não se aplica.

### 5.3 Ordenação e paginação

- Ordenação padrão: ver "Ordem das versões anteriores" em 7.2.
- Outras ordenações: não se aplica.
- Paginação: não se aplica.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre o perfil do aluno e escolhe a aba "Características" ou "Orientações".
2. A psicopedagoga escolhe "Editar".
3. A psicopedagoga escreve o texto, usa negrito e listas se quiser e adiciona ou remove anexos.
4. A psicopedagoga salva.
5. O sistema guarda o texto como uma nova versão e guarda a anterior, atualiza a data e o autor da última atualização (RG-15) e mostra o conteúdo.
6. O sistema avisa os professores do aluno (seção 8).

### 6.2 Fluxos alternativos

- Professor abre a aba: vê o conteúdo em leitura, sem botões de edição. Se a seção não tem conteúdo, vê a mensagem de vazio da seção 9.
- Arquivo fora das regras de anexo (RG-16): o sistema não aceita o arquivo e explica o limite.
- Remover anexo: o sistema pede confirmação antes de remover.
- Salvar falha: o que foi digitado continua no formulário (RG-29).
- Sair com alterações não salvas: o sistema pede confirmação (RG-29).
- Professor de uma turma anterior do aluno: perde o acesso e abre "Não encontrado" (RG-08, RG-13).
- Aluno ou responsável: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Ver características e orientações | Psicopedagoga, Professor | Mostra texto, anexos, data e autor da última atualização. O professor só vê alunos ativos das suas turmas. |
| Editar o texto | Psicopedagoga | Abre a seção para edição com negrito e listas. |
| Salvar | Psicopedagoga | Guarda uma nova versão, atualiza data e autor e avisa os professores do aluno. |
| Adicionar anexo | Psicopedagoga | Anexa o arquivo à seção, dentro das regras de RG-16. |
| Remover anexo | Psicopedagoga | Pede confirmação. Depois de confirmar, o anexo deixa de aparecer para os professores. |
| Abrir anexo | Psicopedagoga, Professor | Abre o arquivo. O anexo tem a mesma visibilidade da seção (RG-12). |
| Ver versões anteriores | Psicopedagoga | Mostra as versões guardadas de cada seção, com data e autor. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Professor: mostra a mensagem de vazio da seção 9. Psicopedagoga: mostra a mensagem de vazio da seção 9 e a ação principal "Editar" (RG-22). |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Aluno e responsável abrem "Acesso negado". Aluno que não existe ou que o professor não pode ver abre "Não encontrado" (RG-13). Telas em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Sem conexão ou falha inesperada abrem "Sem conexão" ou "Erro inesperado" de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). O que foi digitado continua no formulário (RG-29). |

### 6.5 Entrega por fase

| Fase | O que aparece |
| --- | --- |
| 1 | Esta tela inteira: as abas "Características" e "Orientações" no perfil do aluno ([T08 Perfil do aluno](prd-t08-perfil-do-aluno.md)), as versões anteriores e a notificação aos professores. |
| 5 | Busca em características e orientações ([T25 Busca no acervo](prd-t25-busca-no-acervo.md)). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A psicopedagoga edita. O professor só lê. Aluno e responsável não veem esta tela. |
| RN-02 | O professor vê características e orientações dos alunos ativos das turmas em que leciona (RG-08, RG-11). Se o aluno muda de turma, os professores da turma anterior perdem o acesso. |
| RN-03 | Características descrevem como o aluno se comporta e aprende. Orientações explicam como o professor deve lidar com o aluno e adaptar atividades. As duas seções funcionam do mesmo jeito. |
| RN-04 | Cada seção tem texto com formatação simples (negrito e listas), anexos, data e autor da última atualização (RG-15). |
| RN-05 | Cada alteração salva gera uma nova versão. As versões anteriores ficam guardadas. |
| RN-06 | Só a psicopedagoga vê as versões anteriores. |
| RN-07 | Ao salvar, os professores do aluno recebem a notificação "Características ou orientações atualizadas". A psicopedagoga que salvou não recebe (RG-25). |
| RN-08 | Sem conteúdo em Orientações, o professor vê "A psicopedagoga ainda não registrou orientações para este aluno". |
| RN-09 | Cada anexo tem a mesma visibilidade da seção (RG-12). |
| RN-10 | Anexos seguem RG-16: PDF, JPG e PNG, até 10 MB cada e até 5 por registro. |
| RN-11 | Remover anexo pede confirmação (RG-23). |
| RN-12 | Sair do formulário com alterações não salvas pede confirmação. Se salvar falhar, o que foi digitado continua (RG-29). |
| RN-13 | A psicopedagoga vê o conteúdo de alunos ativos e inativos (RG-07). |
| RN-14 | Item que não existe e item que o usuário não pode ver abrem "Não encontrado" (RG-13). |
| RN-15 | A tela funciona no computador e no celular e só com o teclado (RG-26). Botões e erros seguem RG-24. |
| RN-16 | A psicopedagoga edita características e orientações de aluno inativo, como faz com aluno ativo. |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagem de Características vazia | O professor vê "A psicopedagoga ainda não registrou características para este aluno". |
| Vazio para a psicopedagoga | A seção vazia mostra a mensagem da seção 9 e o botão "Editar". |
| Restaurar versão anterior | A psicopedagoga só consulta as versões anteriores. Para voltar a um texto antigo, ela copia o texto e salva como nova versão. |
| Remover anexo e versões | Remover ou adicionar anexo não gera nova versão do texto e não avisa os professores. |
| Limite de texto | O texto de cada seção aceita até 10.000 caracteres. |
| Salvamento por seção | Cada seção é salva separadamente. A notificação diz qual seção mudou. |
| Ordem das versões anteriores | As versões aparecem da mais recente para a mais antiga. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Características ou orientações atualizadas | Professores do aluno. A psicopedagoga que salvou não recebe (RG-25). | Avisa que o conteúdo do aluno foi atualizado. Texto na seção 9. |

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Orientações vazias, vistas pelo professor | Aviso | A psicopedagoga ainda não registrou orientações para este aluno |
| Características vazias, vistas pelo professor | Aviso | A psicopedagoga ainda não registrou características para este aluno (proposta) |
| Seção vazia, vista pela psicopedagoga | Aviso | Esta seção ainda não tem conteúdo. Escolha Editar para escrever. (proposta) |
| Texto salvo | Sucesso | Texto salvo. Os professores do aluno foram avisados. (proposta) |
| Notificação aos professores | Aviso | As características ou orientações de <nome do aluno> foram atualizadas. (proposta) |
| Anexo fora das regras | Erro | O anexo não foi aceito. Envie um PDF, JPG ou PNG com até 10 MB. (proposta) |
| Limite de anexos | Erro | Cada seção aceita até 5 anexos. Remova um anexo para enviar outro. (proposta) |
| Remover anexo | Confirmação | Remover o anexo "<nome do arquivo>"? Ele deixará de aparecer para os professores do aluno. (proposta) |
| Falha ao salvar | Erro | Não foi possível salvar. Verifique a conexão e tente de novo. O que você digitou foi mantido. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Ver características e orientações | Sim | Só alunos ativos das suas turmas | Não | Não |
| Editar o texto | Sim | Não | Não | Não |
| Adicionar e remover anexos | Sim | Não | Não | Não |
| Abrir anexos | Sim | Só alunos ativos das suas turmas | Não | Não |
| Ver versões anteriores | Sim | Não | Não | Não |
| Receber a notificação de atualização | Não | Sim, se for professor do aluno | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga abre o perfil de um aluno, quando escolhe a aba "Características" ou "Orientações", então ela vê o texto, os anexos, a data e o autor da última atualização.
- [ ] Dado que a psicopedagoga escolhe "Editar", quando escreve um texto com negrito e listas e salva, então o sistema mostra o texto com a formatação e atualiza a data e o autor da última atualização.
- [ ] Dado um texto salvo, quando a psicopedagoga salva uma nova alteração, então o sistema guarda uma nova versão e mantém a anterior.
- [ ] Dado uma seção com várias versões, quando a psicopedagoga escolhe "Ver versões anteriores", então vê as versões guardadas com data e autor.
- [ ] Dado um professor, quando abre a seção, então não vê o botão nem a lista de versões anteriores.
- [ ] Dado que a psicopedagoga salva uma seção, quando o salvamento termina, então todos os professores do aluno recebem a notificação "Características ou orientações atualizadas".
- [ ] Dado que a psicopedagoga salva uma seção, quando o salvamento termina, então ela não recebe a notificação da própria ação (RG-25).
- [ ] Dado um aluno que mudou de turma, quando um professor da turma anterior tenta abrir o conteúdo, então o sistema abre "Não encontrado" (RG-08, RG-13).
- [ ] Dado um professor de uma turma do aluno, quando abre o perfil do aluno ativo, então ele lê características, orientações e anexos, sem poder editar nem remover (RG-11).
- [ ] Dado um aluno inativo, quando um professor tenta abrir o conteúdo dele, então o sistema abre "Não encontrado", e a psicopedagoga continua vendo o conteúdo (RG-07, RG-08).
- [ ] Dado um aluno inativo, quando a psicopedagoga edita as orientações dele e salva, então o sistema guarda uma nova versão, como faria para um aluno ativo (RN-16, RN-05).
- [ ] Dado um aluno sem orientações, quando o professor abre a aba "Orientações", então vê "A psicopedagoga ainda não registrou orientações para este aluno".
- [ ] Dado um aluno sem conteúdo, quando a psicopedagoga abre a aba, então vê a mensagem de vazio da seção e o botão "Editar".
- [ ] Dado um anexo em PDF, JPG ou PNG com até 10 MB, quando a psicopedagoga o adiciona, então ele aparece na seção para a psicopedagoga e para os professores do aluno.
- [ ] Dado um arquivo de outro formato ou acima de 10 MB, quando a psicopedagoga tenta adicionar, então o sistema não aceita o arquivo e explica o limite (RG-16).
- [ ] Dado uma seção com 5 anexos, quando a psicopedagoga tenta adicionar outro, então o sistema não aceita e mostra o limite de 5 anexos.
- [ ] Dado um anexo, quando a psicopedagoga escolhe "Remover anexo", então o sistema pede confirmação dizendo que o anexo deixará de aparecer para os professores, e só remove depois da confirmação.
- [ ] Dado um formulário com alterações não salvas, quando a psicopedagoga tenta sair, então o sistema pede confirmação dizendo que as alterações serão perdidas (RG-29).
- [ ] Dado que salvar falhou, quando o formulário continua aberto, então o texto digitado continua preenchido (RG-29).
- [ ] Dado um aluno ou um responsável, quando tenta abrir esta tela, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado um aluno que não existe, quando a psicopedagoga tenta abrir esta tela, então o sistema abre "Não encontrado" (RG-13).
- [ ] Dado que a conexão caiu, quando um usuário abre a tela, então o sistema mostra "Sem conexão" e, se a falha for outra, "Erro inesperado".
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
