# PRD da tela de Minha conta

| Campo | Valor |
| --- | --- |
| Identificador | T04 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md), [T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md), [T21 Professores](prd-t21-professores.md), [T23 Equipe](prd-t23-equipe.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que o usuário veja os dados da própria conta e troque a senha, para manter o acesso seguro sem depender da psicopedagoga.

## 2. Escopo

### O que entra no escopo

- Ver nome, e-mail e perfil da conta.
- Ver a foto (aluno), as turmas e disciplinas (professor) e os alunos vinculados (responsável).
- Trocar a senha, informando a senha atual.
- Sair do sistema.

### O que não entra no escopo

- Alterar nome, e-mail e vínculos: só a psicopedagoga altera, no cadastro correspondente ([T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md) para aluno e responsável, [T21 Professores](prd-t21-professores.md) para professor e [T23 Equipe](prd-t23-equipe.md) para a equipe).
- Alterar a foto: só o aluno tem foto no sistema, e ela é mantida no cadastro do aluno ([T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md)).
- Recuperar a senha esquecida: fica em [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md).
- Mensagem das sessões encerradas: fica em [T26 Estados do sistema](prd-t26-estados-do-sistema.md).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê nome, e-mail e perfil. Troca a própria senha e sai. Não altera os próprios dados aqui: altera no cadastro da equipe ([T23 Equipe](prd-t23-equipe.md)). |
| Professor | Vê nome, e-mail, perfil, turmas e disciplinas. Troca a própria senha e sai. |
| Aluno | Vê nome, e-mail, perfil e foto. Troca a própria senha e sai. |
| Responsável | Vê nome, e-mail, perfil e os alunos vinculados. Troca a própria senha e sai. |

**Contexto:** o usuário quer conferir os dados da conta, trocar a senha ou encerrar a sessão.

**Origem da jornada:** qualquer tela → menu do usuário no topo → Minha conta.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Nome | Nome do usuário, só para leitura. |
| E-mail | E-mail de login do usuário, só para leitura. |
| Perfil | Perfil do usuário: Psicopedagoga, Professor, Aluno ou Responsável. Só para leitura. |
| Foto | Aparece só para o aluno. |
| Turmas e disciplinas | Aparecem só para o professor, com as turmas em que ele leciona e a disciplina de cada uma. |
| Alunos vinculados | Aparecem só para o responsável, com os alunos ligados a ele. |
| Trocar senha | Formulário com senha atual, nova senha e confirmação (seção 5.1). |
| Sair | Encerra a sessão do usuário (destino em 7.2). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Senha atual | Sim | A senha que o usuário usa hoje. |
| Nova senha | Sim | Mínimo de 8 caracteres, com letras e números (RG-03). Não pode ser igual à senha atual. |
| Confirmação da senha | Sim | Repete a nova senha. |

### 5.2 Filtros

Não se aplica.

### 5.3 Ordenação e paginação

Não se aplica.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário abre o menu do usuário no topo e escolhe "Minha conta".
2. O sistema mostra os dados da conta do usuário.
3. O usuário informa a senha atual, a nova senha e a confirmação, e escolhe "Trocar senha".
4. O sistema grava a nova senha e encerra as outras sessões do usuário.

### 6.2 Fluxos alternativos

- Senha atual errada: o sistema não troca a senha e mostra o erro.
- Nova senha fora da regra RG-03: o sistema não troca a senha e mostra o erro.
- Nova senha igual à atual: o sistema não troca a senha e mostra o erro.
- Confirmação diferente da nova senha: o sistema não troca a senha e mostra o erro.
- Sair da tela com a senha digitada e não salva: o sistema pede confirmação (RG-29).
- Falha ao salvar: o que o usuário digitou continua nos campos (RG-29).
- Outras sessões abertas depois da troca de senha: mostram "Sessão encerrada" na próxima ação ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)).
- Usuário inativado com o sistema aberto: vê "Acesso desativado" (RG-05, [T26 Estados do sistema](prd-t26-estados-do-sistema.md)).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Trocar senha | Todos os perfis, na própria conta | Confere a senha atual, grava a nova senha e encerra as outras sessões do usuário. |
| Sair | Todos os perfis | Encerra a sessão do usuário. O destino depois de sair está em 7.2. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Não se aplica. A tela sempre mostra nome, e-mail e perfil. O professor sem turmas e o responsável sem alunos vinculados são tratados em 7.2. |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Todos os perfis usam esta tela e cada um vê só a própria conta (matriz de permissões, seção 10 do índice). "Acesso negado" e "Não encontrado" (RG-13) não se aplicam. |
| Erro | "Sem conexão" e "Erro inesperado" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)) aparecem como aviso na própria tela, e o que foi digitado continua nos campos (RG-29). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A tela segue RG-03, RG-24 e RG-29. RG-15 não se aplica, porque a tela não mostra quem criou ou editou um registro. |
| RN-02 | A tela mostra nome, e-mail e perfil do usuário. O aluno vê também a foto, o professor vê as suas turmas e disciplinas, e o responsável vê os alunos vinculados. |
| RN-03 | Só o aluno tem foto no sistema ([T07 Cadastro de aluno](prd-t07-cadastro-de-aluno.md)). |
| RN-04 | Nome, e-mail e vínculos só são alterados pela psicopedagoga, no cadastro correspondente. Esta tela não tem edição desses dados. |
| RN-05 | A nova senha segue RG-03 (mínimo de 8 caracteres, com letras e números) e não pode ser igual à senha atual. |
| RN-06 | Ao trocar a senha, o sistema encerra as outras sessões do usuário. A sessão em que o usuário trocou a senha continua aberta. |
| RN-07 | Cada usuário vê só a própria conta. |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Cargo da psicopedagoga | Quem tem o perfil Psicopedagoga vê também o cargo (por exemplo, "Assistente estudantil"), só para leitura. |
| Erros de senha atual e o bloqueio | Os erros de senha atual nesta tela não contam para as cinco tentativas que bloqueiam o login (RG-04). |
| Alunos vinculados sem acesso ou inativos | O responsável vê todos os alunos vinculados, ativos ou não, com a indicação "Sem acesso" ou "Inativo" nos que ele não pode abrir. |
| Professor sem turmas e responsável sem alunos | A tela mostra "Nenhuma turma vinculada" para o professor e "Nenhum aluno vinculado" para o responsável. |
| Destino depois de "Sair" | Depois de "Sair", o sistema abre o login ([T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md)). |
| Turmas e disciplinas do professor | A tela mostra uma linha por vínculo, com turma e disciplina, só dos vínculos ativos. |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Senha trocada | Sucesso | Senha trocada. As outras sessões foram encerradas. (proposta) |
| Senha atual errada | Erro | A senha atual está incorreta. Digite de novo. (proposta) |
| Nova senha igual à atual | Erro | A nova senha precisa ser diferente da atual. Escolha outra. (proposta) |
| Nova senha fora da regra | Erro | A senha precisa ter no mínimo 8 caracteres, com letras e números. (proposta) |
| Senha e confirmação diferentes | Erro | A senha e a confirmação são diferentes. Digite as duas de novo. (proposta) |
| Sair com senha digitada e não salva | Confirmação | Você digitou uma nova senha que não foi salva. Se sair agora, ela será descartada. (proposta) |
| Sessão encerrada, nas outras sessões | Aviso | Sua sessão foi encerrada. Entre de novo para continuar. |
| Sem conexão | Erro | Sem conexão com a internet. O que você digitou não foi perdido. |
| Erro inesperado | Erro | Algo deu errado. Tente de novo em alguns minutos. |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Ver a própria conta | Sim | Sim | Sim | Sim |
| Trocar a própria senha | Sim | Sim | Sim | Sim |
| Sair | Sim | Sim | Sim | Sim |
| Alterar nome, e-mail e vínculos nesta tela | Não | Não | Não | Não |
| Alterar nome, e-mail e vínculos de um usuário, no cadastro correspondente | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado um usuário de qualquer perfil, quando ele escolhe "Minha conta" no menu do usuário, então o sistema mostra o nome, o e-mail e o perfil dele.
- [ ] Dado um aluno, quando ele abre Minha conta, então a tela mostra a foto dele.
- [ ] Dado um professor, quando ele abre Minha conta, então a tela mostra as turmas em que ele leciona e as disciplinas.
- [ ] Dado um responsável, quando ele abre Minha conta, então a tela mostra os alunos vinculados a ele.
- [ ] Dada a psicopedagoga, quando ela abre Minha conta, então a tela não mostra foto, turmas, disciplinas nem alunos vinculados.
- [ ] Dado qualquer perfil, quando abre Minha conta, então nome, e-mail e vínculos não podem ser editados na tela (só a psicopedagoga os altera, no cadastro correspondente).
- [ ] Dado um usuário com a senha atual certa, quando ele informa nova senha com 8 caracteres ou mais, com letras e números, diferente da atual, e a confirma, então o sistema grava a nova senha.
- [ ] Dada uma nova senha igual à atual, quando o usuário escolhe "Trocar senha", então o sistema não troca a senha e diz o que fazer.
- [ ] Dada uma nova senha com menos de 8 caracteres ou sem letras e números, quando o usuário escolhe "Trocar senha", então o sistema não troca a senha e diz o que fazer.
- [ ] Dada uma senha atual errada, quando o usuário escolhe "Trocar senha", então o sistema não troca a senha e diz o que fazer.
- [ ] Dada uma confirmação diferente da nova senha, quando o usuário escolhe "Trocar senha", então o sistema não troca a senha.
- [ ] Dado um usuário com outra sessão aberta em outro aparelho, quando ele troca a senha, então a outra sessão mostra "Sessão encerrada" na próxima ação.
- [ ] Dado um usuário com a senha digitada e não salva, quando ele tenta sair da tela, então o sistema pede confirmação dizendo o que será descartado (RG-29).
- [ ] Dada uma falha ao trocar a senha, quando a falha acontece, então o que o usuário digitou continua nos campos (RG-29).
- [ ] Dado qualquer perfil, quando escolhe "Sair", então o sistema encerra a sessão dele.
- [ ] Dado um usuário inativado com o sistema aberto, quando ele faz a próxima ação, então aparece "Acesso desativado" (RG-05).
- [ ] Dado que a conexão caiu, quando o usuário tenta trocar a senha, então aparece "Sem conexão" como aviso na própria tela e o que ele digitou continua nos campos.
- [ ] Dado qualquer perfil, quando usa a tela no computador, no celular ou só com o teclado, então todas as ações funcionam (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
