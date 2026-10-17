# PRD da tela de Cadastro de aluno

| Campo | Valor |
| --- | --- |
| Identificador | T07 |
| Situação | Rascunho |
| Perfis | Psicopedagoga |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T03 Notificações](prd-t03-notificacoes.md), [T04 Minha conta](prd-t04-minha-conta.md), [T06 Lista de alunos](prd-t06-lista-de-alunos.md), [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md), [T14 Evento](prd-t14-evento.md), [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md), [T19 Turmas](prd-t19-turmas.md), [T22 Dificuldades](prd-t22-dificuldades.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga cadastre e mantenha os dados dos alunos atendidos e dê acesso ao sistema a eles e aos responsáveis, para que o atendimento tenha uma base de dados única e correta.

## 2. Escopo

### O que entra no escopo

- Cadastrar um aluno novo e editar um aluno já cadastrado, em formulário dividido em etapas.
- Escolher a turma do aluno e as dificuldades dele.
- Cadastrar dificuldade nova sem sair do formulário.
- Cadastrar responsáveis, vincular responsável já cadastrado e desvincular responsável.
- Dar e retirar o acesso ao sistema de cada responsável.
- Definir e redefinir a senha provisória do aluno e dos responsáveis com acesso.
- Registrar e retirar a autorização do aluno com 18 anos ou mais para o acesso dos responsáveis.
- Inativar e reativar o aluno.

### O que não entra no escopo

- Listar e buscar alunos: ficam em [T06 Lista de alunos](prd-t06-lista-de-alunos.md).
- Ver o perfil completo e imprimir a ficha: ficam em [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md).
- Manter o catálogo de dificuldades: fica em [T22 Dificuldades](prd-t22-dificuldades.md). Aqui só se cadastra uma dificuldade nova, sem sair do formulário.
- Criar e manter turmas: ficam em [T19 Turmas](prd-t19-turmas.md).
- Alterar nome, e-mail e vínculos pelo próprio usuário: [T04 Minha conta](prd-t04-minha-conta.md) não altera esses dados (RN-31).
- Importar alunos do sistema institucional: fica para depois (seção 11 do índice).
- Limite de alunos por curso: não existe (RN-07).
- Excluir aluno ou responsável: nunca acontece. O aluno é inativado e o responsável é desvinculado (RG-14).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Cadastra e edita alunos e responsáveis, define e redefine senhas provisórias, dá e retira acesso dos responsáveis, registra e retira a autorização do aluno com 18 anos ou mais, inativa e reativa o aluno. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega para cadastrar um aluno que passou a ser atendido, para corrigir dados, para trocar a turma na virada do ano letivo, para dar ou retirar acesso e para inativar ou reativar o aluno.

**Origem da jornada:** [T06 Lista de alunos](prd-t06-lista-de-alunos.md) → "Cadastrar aluno". Para editar: [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) → "Editar" no cabeçalho do perfil. Esta tela não tem item próprio no menu. Também chega por avisos do [T02 Início](prd-t02-inicio.md), que lista os alunos com responsável com acesso que completam 18 anos nos próximos 30 dias, e pela notificação desse acontecimento.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Título | Identifica o formulário: cadastro de aluno novo ou edição de aluno já cadastrado. |
| Indicador de etapas | Mostra as 4 etapas do formulário e a etapa atual. A psicopedagoga pode ir a qualquer etapa (seção 6.5). |
| Dados pessoais e escolares | Campos de dados pessoais e a turma (seção 5.1). Curso e série aparecem a partir da turma escolhida. |
| Dificuldades | Campo de dificuldades do catálogo e a opção de cadastrar uma dificuldade nova (seção 5.1). |
| Responsáveis | Lista dos responsáveis do aluno. Cada responsável mostra nome, parentesco, telefone e se tem acesso ao sistema, com as ações da seção 6.3. |
| Aviso de responsável compartilhado | No responsável vinculado a mais de um aluno, mostra "Este responsável também está vinculado a: <nomes dos alunos>" (RN-18). |
| Acesso | E-mail acadêmico, senha provisória e, quando aplicável, a autorização do aluno para acesso dos responsáveis (seção 6.7). |
| Autorização registrada | Mostra a data e quem registrou a autorização. Aparece só para aluno com 18 anos ou mais, ou que completa 18 anos nos próximos 30 dias. |
| Situação do aluno | Na edição, mostra "Ativo" ou "Inativo" e a ação "Inativar" ou "Reativar". |
| Criado e editado | Na edição, mostra quem criou o cadastro e quando e, se foi alterado, "Editado em" com data e autor da última alteração (RG-15). |
| Botões | "Salvar" e "Cancelar". |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

**Dados pessoais**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nome completo | Sim | Nome e sobrenome. |
| Data de nascimento | Sim | Não pode ser futura. Formato dd/mm/aaaa (RG-18). |
| Foto | Não | Segue RG-16: JPG ou PNG com até 5 MB. |
| Telefone | Não | Segue RG-18: formato (00) 00000-0000. |
| Endereço | Não | Texto livre. |
| Cidade | Sim | Lista de cidades da Paraíba, com opção de outra cidade. |
| E-mail pessoal | Não | E-mail válido. |

**Dados escolares**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Turma | Sim | Turmas ativas. O curso e a série vêm da turma. |

**Dificuldades**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Dificuldades | Não | Uma ou mais, do catálogo. Permite cadastrar uma dificuldade nova sem sair do formulário. |

**Responsáveis** (os campos se repetem para cada responsável)

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nome | Sim, por responsável | Pelo menos um responsável para aluno menor de 18 anos (RG-17). |
| Parentesco | Sim, por responsável | Mãe, Pai, Avó ou Avô, Tia ou Tio, Outro. |
| Telefone | Sim, por responsável | Segue RG-18: formato (00) 00000-0000. |
| Dar acesso ao sistema | Não | Caixa de marcação. Cria a conta do responsável. |
| E-mail | Só se tiver acesso | E-mail válido e único entre as contas do sistema. Aceita qualquer domínio (RG-02). |
| Senha provisória | Só se tiver acesso | A psicopedagoga digita ou pede para gerar. A senha aparece uma vez para ser repassada ao responsável. |

**Acesso**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| E-mail acadêmico | Sim | Único no sistema. Domínio @academico.ifpb.edu.br (RG-02). |
| Senha provisória | Sim, no cadastro | A psicopedagoga digita ou pede para gerar. A senha aparece uma vez para ser repassada ao aluno. Segue RG-03. |
| Autorização do aluno para acesso dos responsáveis | Não | Aparece para aluno com 18 anos ou mais, ou que completa 18 anos nos próximos 30 dias. Guarda a data e quem registrou. |

**Janela de confirmação da inativação**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Motivo do cancelamento dos eventos | Não | Texto livre. Se ficar vazio, o motivo é "Aluno inativado" (RN-35). |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Busca de responsável já cadastrado | Nome ou e-mail do responsável (RG-20) | Vazio |

O formulário não tem outros filtros.

### 5.3 Ordenação e paginação

- Ordenação padrão: Não se aplica.
- Outras ordenações: Não se aplica.
- Paginação: Não se aplica.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre "Cadastrar aluno" na [T06 Lista de alunos](prd-t06-lista-de-alunos.md).
2. O sistema abre o formulário na primeira etapa (seção 6.5).
3. A psicopedagoga preenche os dados pessoais e escolhe a turma. O sistema mostra o curso e a série da turma.
4. Ela escolhe as dificuldades do aluno, se houver.
5. Ela adiciona os responsáveis. Para aluno menor de 18 anos, informa pelo menos um (RN-14).
6. Ela informa o e-mail acadêmico e a senha provisória do aluno, digitada ou gerada.
7. Ela escolhe "Salvar".
8. O sistema cria o cadastro, mostra uma vez as senhas provisórias para serem repassadas e abre o [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) (RN-02).

### 6.2 Fluxos alternativos

- Dado inválido ou campo obrigatório vazio: o sistema aponta o campo e diz o que corrigir (RG-24). Ver "Salvar entre etapas" em 7.2.
- Falha ao salvar: o que foi digitado continua no formulário (RG-29).
- Sair com alterações não salvas: o sistema pede confirmação (RG-29).
- Cancelar: o sistema não grava nada e volta para a tela de origem. Se houver alterações não salvas, pede confirmação (RG-29).
- Edição de aluno já cadastrado: a psicopedagoga abre o formulário pelo "Editar" do [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md). Os campos vêm preenchidos, e a senha do aluno só muda por "Redefinir senha".
- Responsável já cadastrado: a psicopedagoga busca por nome ou e-mail e vincula, sem criar outra conta (RN-17).
- Desvincular o único responsável de aluno menor de 18 anos: o sistema impede enquanto não houver outro responsável (RN-19).
- Inativar o aluno: o sistema mostra a janela de confirmação com a quantidade de eventos futuros e o campo de motivo (RN-05, RN-35). Se a psicopedagoga não cancela os eventos, eles continuam na agenda (RN-34).
- Acesso marcado para responsável de aluno com 18 anos ou mais, sem autorização registrada: o sistema cria a conta, guarda a senha provisória e avisa que o acesso depende da autorização (RN-36).
- Perfil sem permissão: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Salvar | Psicopedagoga | Grava o cadastro e abre o [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md). Mostra as senhas provisórias novas uma vez. Ver "Salvar entre etapas" em 7.2. |
| Cancelar | Psicopedagoga | Sai sem gravar. Pede confirmação se houver alterações não salvas (RG-29). |
| Voltar a uma etapa | Psicopedagoga | Abre qualquer etapa antes de salvar, sem perder o que foi digitado (seção 6.5). |
| Redefinir senha do aluno | Psicopedagoga | A psicopedagoga digita ou pede para gerar uma nova senha provisória, que aparece uma vez. O usuário volta para "Aguardando primeiro acesso" (RN-12). |
| Redefinir senha de um responsável | Psicopedagoga | Igual à redefinição do aluno, para o responsável com acesso. Vale para todos os alunos vinculados a ele. |
| Adicionar responsável | Psicopedagoga | Abre os campos de um novo responsável. |
| Vincular responsável já cadastrado | Psicopedagoga | Busca por nome ou e-mail e vincula o responsável a este aluno, sem criar outra conta (RN-17). |
| Desvincular responsável | Psicopedagoga | Remove o vínculo só com este aluno e guarda o vínculo no histórico (RN-19). Pede confirmação (RG-23). |
| Dar acesso a um responsável | Psicopedagoga | Cria a conta com e-mail e senha provisória. A conta nasce "Aguardando primeiro acesso". Quando o acesso foi retirado antes, pede uma nova senha provisória (RN-20). |
| Retirar o acesso de um responsável | Psicopedagoga | Inativa a conta. O responsável continua como contato (RN-20). Pede confirmação (RG-23). |
| Registrar a autorização do aluno | Psicopedagoga | Guarda a data e quem registrou (RN-26). Disponível para aluno com 18 anos ou mais, ou que completa 18 anos nos próximos 30 dias. |
| Retirar a autorização do aluno | Psicopedagoga | A pedido do aluno. A retirada vale na hora (RN-29). Pede confirmação (RG-23). |
| Cadastrar dificuldade nova | Psicopedagoga | Cadastra sem sair do formulário e mostra "Dificuldade cadastrada" (RN-09). |
| Inativar o aluno | Psicopedagoga | Mostra a quantidade de eventos futuros do aluno e pergunta se devem ser cancelados, com um campo opcional para o motivo (RN-35). Os eventos não cancelados continuam (RN-34). O aluno perde o acesso (RN-05). |
| Reativar o aluno | Psicopedagoga | Devolve o acesso ao aluno e aos responsáveis vinculados (RN-06). Pede confirmação (RG-23). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Não se aplica. O formulário novo abre sem dados por definição. |
| Vazio, por causa dos filtros | Não se aplica. A busca de responsável sem resultado mostra a mensagem da seção 9. |
| Sem permissão | Professor, aluno e responsável abrem "Acesso negado" (RG-13), em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | Aluno que não existe abre "Não encontrado" (RG-13). Falha de conexão abre "Sem conexão" e falha inesperada abre "Erro inesperado", em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Se salvar falhar, o que foi digitado continua no formulário (RG-29). |

### 6.5 Etapas do formulário

O formulário é dividido em 4 etapas. A psicopedagoga pode voltar a qualquer etapa antes de salvar (RN-03).

| Etapa | Conteúdo | Observação |
| --- | --- | --- |
| 1. Dados pessoais e escolares | Nome completo, data de nascimento, foto, telefone, endereço, cidade, e-mail pessoal e turma. | Curso e série vêm da turma. |
| 2. Dificuldades | Dificuldades do catálogo e cadastro de dificuldade nova. | Etapa sem campo obrigatório. |
| 3. Responsáveis | Responsáveis do aluno, vínculo de responsável já cadastrado e acesso de cada responsável. | Obrigatória para aluno menor de 18 anos (RN-14). |
| 4. Acesso | E-mail acadêmico, senha provisória e autorização do aluno. | A autorização só aparece nos casos da seção 6.7. |

### 6.6 Acesso dos responsáveis

O quadro lista o que acontece quando o responsável perde o acesso. Em todos os casos vale RN-23 para os eventos e pedidos.

| Causa | Quem perde o acesso | Efeito na conta | Contato |
| --- | --- | --- | --- |
| A psicopedagoga retira o acesso | Esse responsável, em todos os alunos | Conta "Inativo" (RN-20) | Continua no cadastro |
| A psicopedagoga desvincula o responsável | Esse responsável, só neste aluno | Conta "Inativo" só se não restar aluno ativo vinculado com acesso permitido (RN-21) | O vínculo vai para o histórico (RN-19) |
| O aluno é inativado | Responsáveis deste aluno | Conta "Inativo" só se não restar outro aluno ativo vinculado com acesso permitido (RN-05, RN-21) | Continua no cadastro |
| O aluno completa 18 anos sem autorização registrada | Responsáveis deste aluno | Conta "Inativo" só se não restar outro aluno ativo vinculado com acesso permitido (RN-27, RN-21) | Continua no cadastro |
| O aluno retira a autorização | Responsáveis deste aluno | Conta "Inativo" só se não restar outro aluno ativo vinculado com acesso permitido (RN-29, RN-21) | Continua no cadastro |

Quando o responsável volta a ter um aluno ativo vinculado com acesso permitido, a conta volta ao estado anterior (RN-21).

### 6.7 Aluno com 18 anos ou mais

| Momento | O que o sistema faz |
| --- | --- |
| 30 dias antes de o aluno completar 18 anos | Mostra o campo de autorização no cadastro. Se o aluno tem responsável com acesso, notifica as psicopedagogas para colher a autorização (RN-25) e mostra o aluno no bloco do [T02 Início](prd-t02-inicio.md). |
| Aluno cadastrado já com 18 anos ou mais | Os responsáveis só têm acesso se a autorização for registrada no cadastro (RN-28). |
| A psicopedagoga registra a autorização | Guarda a data e quem registrou (RN-26). Os responsáveis com acesso permitido mantêm ou recebem o acesso. |
| Dia em que o aluno completa 18 anos, sem autorização registrada | Os responsáveis perdem o acesso a ele. Os contatos continuam no cadastro (RN-27). |
| O aluno pede para retirar a autorização | A psicopedagoga retira. A retirada vale na hora (RN-29). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-01 a RG-03, RG-05, RG-08, RG-13 a RG-18, RG-23 a RG-25 e RG-29. Só a psicopedagoga cadastra usuários (RG-01). |
| RN-02 | Depois de cadastrar, o sistema abre o perfil do aluno. |
| RN-03 | O formulário é dividido em etapas (dados pessoais e escolares, dificuldades, responsáveis, acesso). A psicopedagoga pode voltar a qualquer etapa antes de salvar. |
| RN-04 | Trocar a turma do aluno muda quais professores têm acesso a ele (RG-08). A turma anterior fica no histórico. Na virada do ano letivo, a psicopedagoga troca a turma de cada aluno nesta tela. |
| RN-05 | Inativar o aluno mostra quantos eventos futuros ele tem e pergunta se devem ser cancelados. O aluno perde o acesso. Responsáveis sem outro aluno ativo também perdem o acesso. Os pedidos de agendamento pendentes do aluno viram "Cancelado" automaticamente. |
| RN-06 | Reativar devolve o acesso ao aluno e aos responsáveis vinculados. |
| RN-07 | Não há limite de alunos por curso. |
| RN-08 | A turma do aluno só pode ser uma turma ativa. O curso e a série vêm da turma. |
| RN-09 | O campo Dificuldades aceita uma ou mais dificuldades do catálogo. Dificuldade nova pode ser cadastrada sem sair do formulário e mostra "Dificuldade cadastrada". Dificuldade inativa não aparece para novos vínculos. |
| RN-10 | O e-mail acadêmico é obrigatório, único no sistema e usa o domínio @academico.ifpb.edu.br (RG-02). |
| RN-11 | A senha provisória do aluno é obrigatória no cadastro. A psicopedagoga digita ou pede para gerar. A senha aparece uma vez para ser repassada. Segue RG-03: no mínimo 8 caracteres, com letras e números, e troca no primeiro acesso. |
| RN-12 | O usuário nasce "Aguardando primeiro acesso". Redefinir a senha do aluno ou de um responsável volta o usuário para "Aguardando primeiro acesso" (situações, seção 6 do índice). |
| RN-13 | A data de nascimento não pode ser futura. O nome completo precisa ter nome e sobrenome. A cidade é escolhida na lista de cidades da Paraíba ou como outra cidade. |
| RN-14 | Aluno menor de 18 anos precisa de pelo menos um responsável (RG-17). Cada responsável tem nome, parentesco e telefone. |
| RN-15 | Parentesco aceita só: Mãe, Pai, Avó ou Avô, Tia ou Tio, Outro. |
| RN-16 | Responsável sem "Dar acesso ao sistema" é só um contato: não tem conta e não recebe notificação. |
| RN-17 | Um responsável já cadastrado (mesmo e-mail) pode ser vinculado a outro aluno, sem criar outra conta. A busca para vincular é feita por nome ou e-mail. |
| RN-18 | Editar os dados de um responsável vinculado a mais de um aluno altera os dados em todos. O formulário avisa: "Este responsável também está vinculado a: <nomes dos alunos>". |
| RN-19 | Desvincular remove o vínculo só com este aluno e guarda o vínculo no histórico. O único responsável de aluno menor de 18 anos só pode ser desvinculado depois que outro for cadastrado (RG-17). |
| RN-20 | Retirar o acesso inativa a conta, e o responsável continua como contato. Dar o acesso de novo pede uma nova senha provisória. |
| RN-21 | Responsável sem nenhum aluno ativo vinculado com acesso permitido perde o acesso: a conta fica "Inativo" automaticamente. Quando passa a ter, a conta volta ao estado anterior (situações, seção 6 do índice). |
| RN-22 | O e-mail do responsável com acesso é obrigatório, válido e único entre as contas do sistema. A senha provisória do responsável com acesso é obrigatória e aparece uma vez para ser repassada. |
| RN-23 | Quando o responsável perde o acesso a um aluno, por qualquer motivo, ele sai dos eventos futuros daquele aluno, e os pedidos pendentes dele para aquele aluno são cancelados. |
| RN-24 | A foto segue RG-16. O telefone do aluno e dos responsáveis segue RG-18. O endereço é texto livre. O e-mail pessoal precisa ser válido. |
| RN-25 | 30 dias antes de o aluno completar 18 anos, as psicopedagogas recebem notificação para colher a autorização dele, quando ele tem responsável com acesso. |
| RN-26 | A autorização do aluno para acesso dos responsáveis não é obrigatória. Guarda a data e quem registrou. O campo aparece para aluno com 18 anos ou mais, ou que completa 18 anos nos próximos 30 dias. |
| RN-27 | No dia em que o aluno completa 18 anos, se a autorização não estiver registrada, os responsáveis perdem o acesso a ele. Os dados de contato dos responsáveis continuam no cadastro. |
| RN-28 | Aluno cadastrado já com 18 anos ou mais só dá acesso aos responsáveis se a autorização for registrada no cadastro. Até lá, a conta do responsável fica "Inativo" (RN-21). |
| RN-29 | O aluno pode retirar a autorização a qualquer momento, pedindo à psicopedagoga. A retirada vale na hora. |
| RN-30 | Aluno, responsável e dificuldade nunca são excluídos. São inativados ou desvinculados, e o histórico é mantido (RG-14). |
| RN-31 | Nome, e-mail e vínculos do aluno e do responsável só são alterados nesta tela. O usuário não os altera em [T04 Minha conta](prd-t04-minha-conta.md). |
| RN-32 | Cancelar eventos futuros ao inativar o aluno gera a notificação "Evento cancelado" para os participantes, com o motivo (seção 8). |
| RN-33 | Cadastro e edição do aluno mostram quem criou e quando, e "Editado em" com data e autor da última alteração (RG-15). |
| RN-34 | Se a psicopedagoga escolhe não cancelar os eventos futuros ao inativar o aluno, os eventos continuam na agenda e o aluno inativo segue como participante, só para consulta da psicopedagoga. |
| RN-35 | Na janela de confirmação da inativação, a psicopedagoga pode escrever o motivo do cancelamento dos eventos. Se não escrever, o motivo é "Aluno inativado". |
| RN-36 | Quando a psicopedagoga marca "Dar acesso ao sistema" para um responsável de aluno com 18 anos ou mais sem autorização registrada, a conta é criada e fica "Inativo" (RN-28). A senha provisória fica guardada até a autorização ser registrada, e a tela avisa que o acesso do responsável depende dela. |
| RN-37 | O pedido de agendamento cancelado automaticamente, pela inativação do aluno ou porque o autor perdeu o acesso ao aluno (RN-05, RN-23), gera notificação para as psicopedagogas, com o motivo (seção 7 do índice). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Reativar não reabre nada | Reativar o aluno não reabre pedidos nem eventos cancelados. Os responsáveis voltam a ter acesso. A psicopedagoga cria novos eventos se precisar. |
| Outra cidade | A opção "Outra cidade" abre um campo de texto livre, obrigatório quando escolhida. |
| Turma anterior no perfil | O histórico de turmas do aluno aparece só para a psicopedagoga, no [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md). |
| Aviso ao responsável removido dos eventos | O responsável que sai dos eventos futuros por perder o acesso ao aluno não recebe o aviso "Participante retirado do evento", porque perde o acesso ao mesmo tempo. |
| Cálculo da idade | A idade conta anos completos pela data de nascimento, no horário de Brasília. O aluno completa 18 anos no dia do aniversário de 18 anos. Os 30 dias contam a partir de 30 dias antes desse aniversário. |
| Mensagens de sucesso | Salvar mostra "Aluno cadastrado." no cadastro novo e "Alterações salvas." na edição. |
| Nome e sobrenome | O nome completo precisa ter pelo menos duas palavras, cada uma com pelo menos 2 letras. |
| Confirmação ao retirar a autorização | A janela de confirmação avisa que os responsáveis perdem o acesso na hora e que os contatos continuam no cadastro. |
| Salvar entre etapas | O botão "Salvar" fica disponível em todas as etapas. Se houver erro em outra etapa, o sistema leva a psicopedagoga até ela. |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Aluno com responsável com acesso completa 18 anos em 30 dias | Psicopedagogas | Informa o nome do aluno, a data em que ele completa 18 anos e que a autorização dele para o acesso dos responsáveis precisa ser colhida (RN-25). |
| Evento cancelado por inativação do aluno | Participantes do evento, menos quem inativou (RG-25) | Título "Evento cancelado", com o motivo do cancelamento escrito pela psicopedagoga ou "Aluno inativado" (RN-32, RN-35). |
| Pedido de agendamento cancelado automaticamente | Psicopedagogas, menos quem fez a ação (RG-25) | Informa o pedido, o aluno e o motivo do cancelamento: aluno inativado ou autor sem acesso ao aluno (RN-37). |

Reativar o aluno, redefinir senha, vincular, desvincular e dar ou retirar acesso não geram notificação, exceto pelo cancelamento automático dos pedidos pendentes (RN-37).

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Responsável vinculado a mais de um aluno | Aviso | Este responsável também está vinculado a: <nomes dos alunos> |
| Dificuldade nova cadastrada no formulário | Sucesso | Dificuldade cadastrada |
| Cadastro novo salvo | Sucesso | Aluno cadastrado. (proposta) |
| Edição salva | Sucesso | Alterações salvas. (proposta) |
| Senha provisória gerada ou redefinida | Aviso | Senha provisória: <senha>. Ela aparece só desta vez. Repasse ao usuário. (proposta) |
| Nome sem sobrenome | Erro | Informe nome e sobrenome. (proposta) |
| Data de nascimento futura | Erro | A data de nascimento não pode ser futura. Corrija a data. (proposta) |
| Campo obrigatório vazio | Erro | Preencha este campo para continuar. (proposta) |
| Foto fora do formato ou do tamanho | Erro | A foto deve ser JPG ou PNG com até 5 MB. Escolha outro arquivo. (proposta) |
| Telefone fora do formato | Erro | Digite o telefone no formato (00) 00000-0000. (proposta) |
| E-mail acadêmico fora do domínio | Erro | O e-mail acadêmico deve terminar com @academico.ifpb.edu.br. Corrija o e-mail. (proposta) |
| E-mail já usado em outra conta | Erro | Este e-mail já está em uso. Use outro e-mail. (proposta) |
| Senha fora da regra | Erro | A senha deve ter no mínimo 8 caracteres, com letras e números. Digite outra senha. (proposta) |
| Aluno menor de 18 anos sem responsável | Erro | Aluno menor de 18 anos precisa de pelo menos um responsável. Adicione um responsável para continuar. (proposta) |
| Desvincular o único responsável de aluno menor de 18 anos | Erro | Este é o único responsável do aluno. Cadastre outro responsável antes de desvincular. (proposta) |
| Busca de responsável sem resultado | Aviso | Nenhum responsável encontrado. Confira o nome ou o e-mail, ou adicione um responsável novo. (proposta) |
| Falha ao salvar | Erro | Não foi possível salvar. O que você digitou foi mantido. Tente salvar de novo. (proposta) |
| Sair com alterações não salvas | Confirmação | Há alterações não salvas. Se você sair agora, elas serão perdidas. (proposta) |
| Redefinir senha | Confirmação | Ao redefinir, a senha atual de <nome> deixa de valer e a pessoa volta para "Aguardando primeiro acesso". (proposta) |
| Desvincular responsável | Confirmação | Ao desvincular, <nome do responsável> deixa de ser responsável de <nome do aluno>, sai dos eventos futuros dele e tem os pedidos pendentes cancelados. O vínculo fica no histórico. (proposta) |
| Retirar o acesso de um responsável | Confirmação | Ao retirar o acesso, a conta de <nome do responsável> fica inativa para todos os alunos vinculados, ele sai dos eventos futuros e tem os pedidos pendentes cancelados. Ele continua como contato. (proposta) |
| Retirar a autorização do aluno | Confirmação | Ao retirar a autorização, os responsáveis perdem o acesso a <nome do aluno> agora. Os contatos continuam no cadastro. (proposta) |
| Inativar o aluno | Confirmação | <nome do aluno> tem <N> eventos futuros. Ao inativar, o aluno perde o acesso e os responsáveis sem outro aluno ativo também perdem. Cancelar os eventos futuros? (proposta) |
| Acesso marcado sem autorização do aluno com 18 anos ou mais | Aviso | O acesso de <nome do responsável> só começa quando a autorização de <nome do aluno> for registrada. (proposta) |
| Reativar o aluno | Confirmação | Ao reativar, <nome do aluno> e os responsáveis vinculados voltam a ter acesso. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Acessar a tela | Sim | Não | Não | Não |
| Cadastrar aluno | Sim | Não | Não | Não |
| Editar aluno | Sim | Não | Não | Não |
| Trocar a turma do aluno | Sim | Não | Não | Não |
| Redefinir a senha do aluno ou de um responsável | Sim | Não | Não | Não |
| Adicionar, vincular e desvincular responsável | Sim | Não | Não | Não |
| Dar e retirar o acesso de um responsável | Sim | Não | Não | Não |
| Registrar e retirar a autorização do aluno | Sim | Não | Não | Não |
| Cadastrar dificuldade nova pelo formulário | Sim | Não | Não | Não |
| Inativar e reativar o aluno | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga está na [T06 Lista de alunos](prd-t06-lista-de-alunos.md), quando escolhe "Cadastrar aluno", então o formulário abre na primeira etapa.
- [ ] Dado que a psicopedagoga preencheu todos os campos obrigatórios, quando escolhe "Salvar", então o aluno é cadastrado e o [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) dele abre (RN-02).
- [ ] Dado que o formulário tem 4 etapas, quando a psicopedagoga está na etapa de responsáveis, então pode voltar a qualquer etapa anterior sem perder o que digitou, antes de salvar (RN-03).
- [ ] Dado que o campo Nome completo tem só uma palavra, quando a psicopedagoga tenta salvar, então o sistema pede nome e sobrenome (RN-13).
- [ ] Dado que a data de nascimento é futura, quando a psicopedagoga tenta salvar, então o sistema rejeita a data e diz como corrigir (RN-13).
- [ ] Dado que a cidade não foi escolhida, quando a psicopedagoga tenta salvar, então o sistema aponta o campo obrigatório (RN-13).
- [ ] Dado que a psicopedagoga escolhe "outra cidade", quando salva, então a cidade informada fica no cadastro (RN-13).
- [ ] Dado que a foto enviada é um PDF ou tem mais de 5 MB, quando a psicopedagoga a escolhe, então o sistema rejeita o arquivo e diz o formato e o tamanho aceitos (RG-16, RN-24).
- [ ] Dado que o telefone não está no formato (00) 00000-0000, quando a psicopedagoga tenta salvar, então o sistema pede o formato correto (RG-18).
- [ ] Dado que o e-mail pessoal é inválido, quando a psicopedagoga tenta salvar, então o sistema rejeita o e-mail (RN-24).
- [ ] Dado que a psicopedagoga abre a lista de turmas, quando escolhe uma, então só aparecem turmas ativas e o curso e a série aparecem a partir da turma (RN-08).
- [ ] Dado que um aluno muda de turma, quando a psicopedagoga salva, então os professores da turma anterior perdem o acesso a ele e a turma anterior fica no histórico (RN-04, RG-08).
- [ ] Dado que a psicopedagoga está na etapa Dificuldades, quando escolhe uma ou mais dificuldades do catálogo, então todas ficam vinculadas ao aluno (RN-09).
- [ ] Dado que a dificuldade necessária não existe, quando a psicopedagoga a cadastra sem sair do formulário, então aparece "Dificuldade cadastrada" e ela pode ser escolhida na hora (RN-09).
- [ ] Dado que uma dificuldade está inativa, quando a psicopedagoga abre a lista de dificuldades, então ela não aparece para novo vínculo (RN-09).
- [ ] Dado que o aluno tem menos de 18 anos, quando a psicopedagoga tenta salvar sem responsável, então o sistema exige pelo menos um responsável (RN-14, RG-17).
- [ ] Dado que um responsável foi adicionado, quando falta nome, parentesco ou telefone, então o sistema aponta o campo obrigatório (RN-14).
- [ ] Dado que o campo Parentesco está aberto, quando a psicopedagoga vê as opções, então aparecem só Mãe, Pai, Avó ou Avô, Tia ou Tio e Outro (RN-15).
- [ ] Dado que "Dar acesso ao sistema" não está marcada, quando a psicopedagoga salva o responsável, então ele fica só como contato, sem conta e sem notificação (RN-16).
- [ ] Dado que "Dar acesso ao sistema" está marcada, quando a psicopedagoga salva sem e-mail ou sem senha provisória do responsável, então o sistema aponta os campos obrigatórios (RN-22).
- [ ] Dado que o e-mail do responsável já pertence a outra conta, quando a psicopedagoga tenta salvar um responsável novo com acesso, então o sistema rejeita o e-mail e diz para usar outro (RN-22).
- [ ] Dado que a psicopedagoga gerou a senha provisória do responsável, quando salva, então a senha aparece uma vez para ser repassada, e a conta nasce "Aguardando primeiro acesso" (RN-22, RN-12).
- [ ] Dado que o e-mail acadêmico não termina com @academico.ifpb.edu.br, quando a psicopedagoga tenta salvar, então o sistema rejeita o e-mail (RN-10).
- [ ] Dado que o e-mail acadêmico já existe no sistema, quando a psicopedagoga tenta salvar, então o sistema rejeita o e-mail e diz para usar outro (RN-10).
- [ ] Dado que a senha provisória do aluno tem menos de 8 caracteres ou não mistura letras e números, quando a psicopedagoga tenta salvar, então o sistema rejeita a senha (RN-11, RG-03).
- [ ] Dado que a psicopedagoga pede para gerar a senha do aluno, quando salva, então a senha aparece uma vez para ser repassada ao aluno, e o aluno nasce "Aguardando primeiro acesso" (RN-11, RN-12).
- [ ] Dado que a psicopedagoga redefine a senha do aluno, quando confirma, então o aluno volta para "Aguardando primeiro acesso" e a nova senha aparece uma vez (RN-12).
- [ ] Dado que a psicopedagoga redefine a senha de um responsável com acesso, quando confirma, então o responsável volta para "Aguardando primeiro acesso" (RN-12).
- [ ] Dado que um responsável já está cadastrado com um e-mail, quando a psicopedagoga busca por nome ou e-mail e o vincula a outro aluno, então ele é vinculado sem criar outra conta (RN-17).
- [ ] Dado que um responsável está vinculado a dois alunos, quando a psicopedagoga abre o formulário de um deles, então aparece "Este responsável também está vinculado a: <nomes dos alunos>" (RN-18).
- [ ] Dado que um responsável está vinculado a dois alunos, quando a psicopedagoga edita os dados dele em um aluno, então os dados mudam nos dois alunos (RN-18).
- [ ] Dado que a psicopedagoga desvincula um responsável, quando confirma, então o vínculo com este aluno é removido, os outros vínculos continuam e o vínculo antigo fica no histórico (RN-19, RG-14).
- [ ] Dado que o aluno tem menos de 18 anos e só um responsável, quando a psicopedagoga tenta desvincular esse responsável, então o sistema impede até que outro responsável seja cadastrado (RN-19, RG-17).
- [ ] Dado que um responsável tem acesso, quando a psicopedagoga retira o acesso e confirma, então a conta fica "Inativo" e o responsável continua como contato (RN-20).
- [ ] Dado que o acesso de um responsável foi retirado, quando a psicopedagoga dá o acesso de novo, então o sistema pede uma nova senha provisória (RN-20).
- [ ] Dado que um responsável não tem nenhum aluno ativo vinculado com acesso permitido, quando isso acontece, então a conta dele fica "Inativo" automaticamente (RN-21).
- [ ] Dado que a conta de um responsável ficou "Inativo" por falta de aluno com acesso permitido, quando ele passa a ter um aluno ativo vinculado com acesso permitido, então a conta volta ao estado anterior (RN-21).
- [ ] Dado que um responsável perde o acesso a um aluno, quando a perda acontece, então ele sai dos eventos futuros daquele aluno e os pedidos pendentes dele para aquele aluno são cancelados (RN-23).
- [ ] Dado que o aluno completa 18 anos em até 30 dias, quando a psicopedagoga abre a etapa Acesso, então o campo de autorização aparece (RN-26).
- [ ] Dado que o aluno tem 16 anos, quando a psicopedagoga abre a etapa Acesso, então o campo de autorização não aparece (RN-26).
- [ ] Dado que a psicopedagoga registra a autorização, quando salva, então o sistema guarda a data e quem registrou (RN-26).
- [ ] Dado que faltam 30 dias para um aluno com responsável com acesso completar 18 anos, quando chega esse dia, então as psicopedagogas recebem a notificação para colher a autorização (RN-25).
- [ ] Dado que o aluno completa 18 anos sem autorização registrada, quando chega o dia do aniversário, então os responsáveis perdem o acesso a ele e os contatos continuam no cadastro (RN-27).
- [ ] Dado que o aluno é cadastrado já com 18 anos ou mais, quando a psicopedagoga marca acesso para um responsável sem registrar a autorização, então o responsável não tem acesso a ele (RN-28).
- [ ] Dado que o aluno tem 19 anos e não tem autorização registrada, quando a psicopedagoga marca "Dar acesso ao sistema" para um responsável e salva, então a conta fica "Inativo", a senha provisória fica guardada e a tela avisa que o acesso depende da autorização (RN-36).
- [ ] Dado um responsável com conta criada à espera da autorização, quando a psicopedagoga registra a autorização do aluno, então o responsável passa a entrar com a senha provisória guardada (RN-36).
- [ ] Dado que o aluno pediu para retirar a autorização, quando a psicopedagoga a retira e confirma, então os responsáveis perdem o acesso na hora (RN-29).
- [ ] Dado que a psicopedagoga inativa um aluno com 3 eventos futuros, quando abre a confirmação, então ela mostra "3" eventos futuros e pergunta se devem ser cancelados (RN-05).
- [ ] Dado que a psicopedagoga escolhe cancelar os eventos ao inativar, quando confirma, então os eventos ficam "Cancelado" e os participantes, menos ela, recebem "Evento cancelado" com o motivo (RN-32, RG-25).
- [ ] Dado que a psicopedagoga cancela os eventos ao inativar sem escrever o motivo, quando confirma, então o motivo dos eventos cancelados é "Aluno inativado" (RN-35).
- [ ] Dado que a psicopedagoga escreve um motivo na janela de inativação, quando confirma, então esse motivo aparece nos eventos cancelados e na notificação (RN-35).
- [ ] Dado que a psicopedagoga escolhe não cancelar os eventos ao inativar, quando confirma, então os eventos continuam na agenda e o aluno inativo continua como participante, visível só para a psicopedagoga (RN-34).
- [ ] Dado um aluno com um pedido de agendamento pendente, quando a psicopedagoga o inativa, então o pedido vira "Cancelado" e as outras psicopedagogas recebem a notificação com o motivo (RN-37, RG-25).
- [ ] Dado que o aluno é inativado, quando a ação termina, então o aluno perde o acesso, os responsáveis sem outro aluno ativo perdem o acesso e os pedidos de agendamento pendentes do aluno viram "Cancelado" (RN-05).
- [ ] Dado que um aluno está inativo, quando a psicopedagoga o reativa e confirma, então o aluno e os responsáveis vinculados com acesso permitido voltam a ter acesso (RN-06).
- [ ] Dado que um curso já tem muitos alunos cadastrados, quando a psicopedagoga cadastra mais um aluno nele, então o cadastro é aceito, pois não há limite de alunos por curso (RN-07).
- [ ] Dado que um aluno ou responsável já foi cadastrado, quando a psicopedagoga procura a ação de excluir, então ela não existe, só inativar ou desvincular (RN-30, RG-14).
- [ ] Dado que um usuário abre [T04 Minha conta](prd-t04-minha-conta.md), quando procura alterar nome, e-mail ou vínculos, então não consegue (RN-31).
- [ ] Dado que a psicopedagoga alterou campos, quando tenta sair sem salvar, então aparece a confirmação de alterações não salvas (RG-29).
- [ ] Dado que salvar falhou, quando o formulário volta a aparecer, então o que foi digitado continua nos campos (RG-29).
- [ ] Dado que o cadastro foi alterado, quando a psicopedagoga abre a edição, então aparece quem criou e quando e "Editado em" com data e autor da última alteração (RN-33, RG-15).
- [ ] Dado que o usuário tem o perfil Professor, Aluno ou Responsável, quando tenta abrir esta tela, então abre "Acesso negado" (RG-13).
- [ ] Dado que a psicopedagoga abre a edição de um aluno que não existe, quando a tela abre, então aparece "Não encontrado" (RG-13).
- [ ] Dado que o sistema perdeu a conexão ou ocorreu uma falha inesperada, quando a tela é aberta, então abre "Sem conexão" ou "Erro inesperado", com orientação do que fazer (RG-24).
- [ ] Dado que a tela é aberta no celular, quando a psicopedagoga navega só com o teclado, então consegue preencher o formulário e salvar (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
