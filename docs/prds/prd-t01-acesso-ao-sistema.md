# PRD da tela de Acesso ao sistema

| Campo | Valor |
| --- | --- |
| Identificador | T01 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T02 Início](prd-t02-inicio.md), [T04 Minha conta](prd-t04-minha-conta.md), [T05 Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md), [T23 Equipe](prd-t23-equipe.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 e 5 (a recuperação de senha por e-mail é da fase 5) |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que usuários cadastrados entrem no sistema, definam a própria senha e recuperem o acesso, para que cada pessoa use o sistema só com a conta que a psicopedagoga criou para ela.

## 2. Escopo

### O que entra no escopo

- Login com e-mail e senha.
- Primeiro acesso: definir a nova senha e aceitar os termos de uso.
- Aceite da nova versão dos termos de uso depois do login.
- Bloqueio do login por excesso de tentativas erradas.
- "Esqueci a senha": orientação para procurar a psicopedagoga (fases 1 a 4).
- "Esqueci a senha" por e-mail e redefinição de senha pelo link recebido (fase 5).
- Destino do usuário depois do login.

### O que não entra no escopo

- Criar conta: não existe autocadastro (RG-01). Quem cria as contas é a psicopedagoga, no cadastro do usuário.
- Redefinir a senha de outro usuário: é feito pela psicopedagoga, no cadastro do usuário. A senha de quem tem o perfil Psicopedagoga segue RG-32 ([T23 Equipe](prd-t23-equipe.md)).
- Trocar a senha com o sistema aberto: fica em [T04 Minha conta](prd-t04-minha-conta.md).
- Texto e publicação dos termos de uso: ficam em [T05 Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md).
- Login institucional unificado: fica para depois (seção 11 do índice).
- Mensagens de sessão encerrada e de acesso desativado: ficam em [T26 Estados do sistema](prd-t26-estados-do-sistema.md).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Entra com e-mail do domínio @ifpb.edu.br, define a senha no primeiro acesso e aceita os termos. Para redefinir a senha, segue RG-32 e, a partir da fase 5, também pode usar o link por e-mail (RN-09). |
| Professor | Entra com e-mail do domínio @ifpb.edu.br, define a senha no primeiro acesso e aceita os termos. |
| Aluno | Entra com e-mail do domínio @academico.ifpb.edu.br, define a senha no primeiro acesso e aceita os termos. |
| Responsável | Entra com qualquer e-mail, define a senha no primeiro acesso e aceita os termos. Só entra se a conta não estiver "Inativo" (seção 6 do índice). |

**Contexto:** o usuário chega aqui antes de usar o sistema, na primeira vez que entra, quando a sessão foi encerrada, quando os termos de uso mudaram ou quando esqueceu a senha.

**Origem da jornada:** endereço do sistema → Acesso ao sistema. Também chegam aqui quem escolhe "Sair" em [T04 Minha conta](prd-t04-minha-conta.md) e quem escolhe "Entrar" em "Sessão encerrada" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). Esta tela não está no menu, porque aparece antes do login.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Login | Campos de e-mail e senha, botão "Entrar" e ação "Esqueci a senha". Não tem "Criar conta" (RG-01). |
| Aviso de bloqueio | Mostra a mensagem de bloqueio quando o e-mail passou das tentativas (RN-04). |
| Primeiro acesso | Campos de nova senha e confirmação da senha, aceite dos termos de uso e opção de ler os termos. Aparece para o usuário "Aguardando primeiro acesso". |
| Nova versão dos termos | Mostra o texto da nova versão e o botão "Aceitar". Aparece depois do login, quando os termos mudaram desde o último aceite. |
| Esqueci a senha, fases 1 a 4 | Mostra só a mensagem "Procure a psicopedagoga para redefinir sua senha". Não tem formulário. |
| Esqueci a senha, a partir da fase 5 | Campo de e-mail e botão "Enviar link". |
| Redefinir senha, a partir da fase 5 | Campos de nova senha e confirmação, abertos a partir do link recebido por e-mail. |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

**Login**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| E-mail | Sim | E-mail institucional (RG-02): @academico.ifpb.edu.br para aluno, @ifpb.edu.br para professor e equipe, qualquer e-mail para responsável. |
| Senha | Sim | A senha da conta. Na primeira vez, é a senha provisória definida no cadastro (RG-03). |

**Primeiro acesso**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nova senha | Sim | Mínimo de 8 caracteres, com letras e números (RG-03). |
| Confirmação da senha | Sim | Repete a nova senha. |
| Aceite dos termos de uso | Sim | O usuário marca que aceita. Tem a opção de ler os termos antes ([T05 Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md)). |

**Esqueci a senha (fase 5)**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| E-mail | Sim | O e-mail da conta. |

**Redefinir senha (fase 5)**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nova senha | Sim | Mínimo de 8 caracteres, com letras e números (RG-03). |
| Confirmação da senha | Sim | Repete a nova senha. |

### 5.2 Filtros

Não se aplica.

### 5.3 Ordenação e paginação

Não se aplica.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário informa e-mail e senha e escolhe "Entrar".
2. O sistema confere os dados.
3. Se o usuário está "Aguardando primeiro acesso", o sistema abre o primeiro acesso. O usuário define a nova senha, aceita os termos e passa a ser "Ativo".
4. Se os termos mudaram desde o último aceite, o sistema mostra a nova versão. O usuário escolhe "Aceitar".
5. O sistema leva o usuário ao Início ([T02 Início](prd-t02-inicio.md)) ou à tela em que ele estava quando a sessão foi encerrada (RN-03).

### 6.2 Fluxos alternativos

- E-mail inexistente, senha errada ou usuário inativo: o sistema mostra o mesmo erro de login (RN-06).
- Cinco tentativas erradas seguidas no mesmo e-mail: o sistema mostra a mensagem de bloqueio por 15 minutos (RN-04).
- Nova senha fora da regra ou confirmação diferente da nova senha: o sistema não grava a senha e mostra o erro no campo.
- Primeiro acesso sem aceitar os termos: o sistema não conclui o primeiro acesso (RN-05).
- Nova versão dos termos sem aceitar: o usuário só pode sair (RN-07).
- Usuário toca em "Esqueci a senha" nas fases 1 a 4: o sistema mostra a mensagem de orientação, sem formulário (RN-08).
- Usuário pede o link na fase 5: o sistema mostra sempre a mesma resposta, com e-mail cadastrado ou não (RN-10).
- Link expirado ou já usado (fase 5): o sistema não permite redefinir a senha (RN-11). O que a tela oferece está em "Link expirado ou já usado" na 7.2.
- Sessão encerrada depois de 2 horas sem uso: o usuário entra de novo e volta para a tela em que estava (RG-28).
- Falha de conexão ou erro do sistema: aparece o estado "Sem conexão" ou "Erro inesperado" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Entrar | Todos os perfis | Confere e-mail e senha e leva o usuário ao destino definido em RN-03. |
| Esqueci a senha | Todos os perfis | Fases 1 a 4: mostra a mensagem de orientação. Fase 5: abre o campo de e-mail. |
| Ler os termos de uso | Todos os perfis | Abre o texto dos termos, sem exigir login ([T05 Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md)). |
| Definir a senha e aceitar os termos | Usuário "Aguardando primeiro acesso" | Grava a nova senha e o aceite, com data, hora e versão (RG-06), e o usuário passa a "Ativo". |
| Aceitar | Usuário com nova versão dos termos para aceitar | Registra o aceite da nova versão, com data, hora e versão, e libera o uso do sistema. |
| Sair | Usuário com nova versão dos termos para aceitar | Encerra a sessão sem aceitar. O usuário não usa o sistema. |
| Enviar link (fase 5) | Todos os perfis | Envia o link de redefinição para o e-mail informado, se ele estiver cadastrado, e mostra a mesma resposta nos dois casos. |
| Redefinir a senha (fase 5) | Todos os perfis, a partir do link | Grava a nova senha e encerra as outras sessões do usuário (RN-12). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Não se aplica. |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Todos os perfis usam esta tela (matriz de permissões, seção 10 do índice). Usuário inativado com o sistema aberto vê "Acesso desativado" (RG-05, [T26 Estados do sistema](prd-t26-estados-do-sistema.md)). "Acesso negado" e "Não encontrado" (RG-13) não se aplicam. |
| Erro | "Sem conexão" e "Erro inesperado" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)) aparecem como aviso na própria tela. O que o usuário digitou continua nos campos. |

### 6.5 Entrega por fase

| Fase | O que aparece |
| --- | --- |
| 1 | Login, primeiro acesso, nova versão dos termos e "Esqueci a senha" com a mensagem "Procure a psicopedagoga para redefinir sua senha", sem formulário. |
| 5 | "Esqueci a senha" com e-mail e "Enviar link", no lugar da mensagem das fases 1 a 4, e "Redefinir senha" a partir do link recebido. |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A tela segue RG-02 a RG-06 e RG-28. |
| RN-02 | Não existe autocadastro nem opção "Criar conta" (RG-01). A primeira conta com o perfil Psicopedagoga é criada na implantação do sistema (RG-27). |
| RN-03 | Depois do login, o usuário "Aguardando primeiro acesso" vai para o primeiro acesso. Os outros vão para o Início ou para a tela em que estavam quando a sessão foi encerrada. |
| RN-04 | Cinco tentativas de login erradas seguidas bloqueiam o login daquele e-mail por 15 minutos (RG-04). Enquanto durar o bloqueio, a tela mostra "Login bloqueado por excesso de tentativas. Tente de novo em 15 minutos". |
| RN-05 | O usuário que não troca a senha e não aceita os termos não usa o sistema. Ele fica "Ativo" ao fazer as duas coisas (seção 6 do índice). |
| RN-06 | O erro de login é o mesmo para e-mail inexistente, senha errada e usuário inativo, para não revelar quem tem conta. Usuário inativo não entra (RG-05). Conta de responsável que ficou "Inativo" por não ter aluno ativo vinculado com acesso permitido também não entra. |
| RN-07 | Quando os termos mudaram desde o último aceite, a nova versão aparece depois do login (RG-06). O usuário só pode aceitar ou sair. O aceite fica registrado com data, hora e versão. |
| RN-08 | Nas fases 1 a 4, "Esqueci a senha" mostra "Procure a psicopedagoga para redefinir sua senha", sem formulário. Quando a psicopedagoga redefine a senha, o usuário volta para "Aguardando primeiro acesso" (seção 6 do índice). |
| RN-09 | A senha de quem tem o perfil Psicopedagoga é redefinida por outra pessoa com o mesmo perfil. Se só existir uma conta ativa com este perfil, a redefinição é feita pela equipe que opera o sistema (RG-32). A partir da fase 5, quem tem este perfil também pode usar o "Esqueci a senha" por e-mail, como os outros perfis, e a redefinição por outra pessoa continua possível. |
| RN-10 | A partir da fase 5, "Esqueci a senha" responde a mesma coisa para e-mail cadastrado e para e-mail não cadastrado. |
| RN-11 | O link de redefinição vale por 1 hora e só pode ser usado uma vez. |
| RN-12 | Depois de redefinir a senha, o sistema encerra as outras sessões do usuário. Quem estava nelas vê "Sessão encerrada" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |
| RN-13 | Os termos de uso podem ser lidos sem login, inclusive pela opção de ler no primeiro acesso ([T05 Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md)). |
| RN-14 | O único e-mail que o sistema envia é o link de redefinição de senha, a partir da fase 5 (seção 11 do índice). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Botões de senha | O botão do primeiro acesso e o da redefinição se chamam "Salvar senha". |
| E-mail fora do domínio do perfil | O sistema trata como e-mail inexistente e mostra o mesmo erro de login. |
| Nova senha igual à provisória | A nova senha do primeiro acesso não pode ser igual à senha provisória. |
| Contagem de tentativas | A contagem de tentativas erradas (RG-04) volta a zero depois de um login certo. |
| Link expirado ou já usado | A tela mostra a mensagem e a opção de pedir um novo link. |
| Depois de redefinir pelo link | O sistema leva o usuário ao login com a mensagem de sucesso. O usuário não precisa aceitar os termos de novo, a menos que a versão tenha mudado. |
| Situação depois de redefinir pelo link | A situação do usuário não muda. Só a redefinição feita pela psicopedagoga volta o usuário para "Aguardando primeiro acesso". |
| Usuário "Aguardando primeiro acesso" e o link | O usuário "Aguardando primeiro acesso" não recebe o link. Ele entra com a senha provisória e faz o primeiro acesso. |
| Aceite do primeiro acesso | O aceite feito no primeiro acesso vale como aceite da versão vigente dos termos. |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Login bloqueado por excesso de tentativas | Erro | Login bloqueado por excesso de tentativas. Tente de novo em 15 minutos |
| "Esqueci a senha", fases 1 a 4 | Aviso | Procure a psicopedagoga para redefinir sua senha |
| E-mail inexistente, senha errada ou usuário inativo | Erro | E-mail ou senha incorretos. Confira os dados e tente de novo. (proposta) |
| Resposta ao "Enviar link", com e-mail cadastrado ou não | Aviso | Se este e-mail estiver cadastrado, enviaremos um link para redefinir a senha. (proposta) |
| Link expirado ou já usado | Erro | Este link expirou ou já foi usado. Peça um novo link. (proposta) |
| Nova senha fora da regra | Erro | A senha precisa ter no mínimo 8 caracteres, com letras e números. (proposta) |
| Senha e confirmação diferentes | Erro | A senha e a confirmação são diferentes. Digite as duas de novo. (proposta) |
| Primeiro acesso sem aceitar os termos | Erro | Aceite os termos de uso para continuar. (proposta) |
| Senha redefinida pelo link | Sucesso | Senha redefinida. Entre com a nova senha. (proposta) |
| Sessão encerrada | Aviso | Sua sessão foi encerrada. Entre de novo para continuar. |
| Sem conexão | Erro | Sem conexão com a internet. O que você digitou não foi perdido. |
| Erro inesperado | Erro | Algo deu errado. Tente de novo em alguns minutos. |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Entrar | Sim, se a conta não estiver inativa | Sim, se a conta não estiver inativa | Sim, se a conta não estiver inativa | Sim, se a conta não estiver inativa |
| Fazer o primeiro acesso | Sim | Sim | Sim | Sim |
| Aceitar a nova versão dos termos | Sim | Sim | Sim | Sim |
| Ler os termos de uso sem login | Sim | Sim | Sim | Sim |
| "Esqueci a senha" | Sim, segue RG-32 e, a partir da fase 5, também pelo link (RN-09) | Sim | Sim | Sim |
| Redefinir a senha pelo link (fase 5) | Sim | Sim | Sim | Sim |

## 11. Critérios de aceite

- [ ] Dado um usuário "Ativo" com os termos em dia, quando ele informa e-mail e senha certos e escolhe "Entrar", então o sistema abre o Início.
- [ ] Dado um usuário "Ativo" cuja sessão foi encerrada em outra tela, quando ele entra de novo, então o sistema abre a tela em que ele estava (RG-28).
- [ ] Dado um usuário "Aguardando primeiro acesso", quando ele entra com a senha provisória, então o sistema abre o primeiro acesso, e não o Início.
- [ ] Dado o primeiro acesso, quando o usuário informa nova senha com 8 caracteres ou mais, com letras e números, confirma a senha e aceita os termos, então o sistema grava a senha, registra o aceite com data, hora e versão e a situação passa a "Ativo".
- [ ] Dado o primeiro acesso, quando o usuário não aceita os termos ou não troca a senha, então o sistema não libera o uso e ele não chega ao Início.
- [ ] Dado o primeiro acesso, quando o usuário escolhe ler os termos, então o texto dos termos abre sem pedir login.
- [ ] Dado um usuário "Ativo" e termos que mudaram desde o último aceite, quando ele entra, então o sistema mostra o texto da nova versão e o botão "Aceitar" antes de qualquer tela.
- [ ] Dado o aviso da nova versão dos termos, quando o usuário não aceita, então ele só pode sair.
- [ ] Dado o aviso da nova versão dos termos, quando o usuário escolhe "Aceitar", então o sistema registra o aceite com data, hora e versão e abre o Início ou a tela em que ele estava.
- [ ] Dado um e-mail que não existe, uma senha errada ou um usuário inativo, quando alguém tenta entrar, então o sistema mostra o mesmo erro nos três casos.
- [ ] Dado um e-mail com cinco tentativas erradas seguidas, quando alguém tenta entrar com ele, então o sistema mostra "Login bloqueado por excesso de tentativas. Tente de novo em 15 minutos" e não faz o login por 15 minutos, mesmo com a senha certa.
- [ ] Dada a tela de login, quando o usuário a abre, então ela não mostra opção "Criar conta" (RG-01).
- [ ] Dada a fase 1, 2, 3 ou 4, quando o usuário escolhe "Esqueci a senha", então o sistema mostra "Procure a psicopedagoga para redefinir sua senha" e nenhum formulário.
- [ ] Dado um usuário cuja senha a psicopedagoga redefiniu, quando ele entra, então ele cai no primeiro acesso, com a situação "Aguardando primeiro acesso".
- [ ] Dado um usuário com o perfil Psicopedagoga que esqueceu a senha, quando ele pede ajuda, então a redefinição é feita por outra pessoa com o mesmo perfil ou, se só houver uma conta ativa com o perfil, pela equipe que opera o sistema (RG-32).
- [ ] Dada a fase 5 e um usuário com o perfil Psicopedagoga, quando ele informa o e-mail em "Esqueci a senha" e escolhe "Enviar link", então recebe o link de redefinição como os outros perfis, e a redefinição por outra pessoa com o perfil continua possível (RN-09).
- [ ] Dada a fase 5, quando o usuário informa um e-mail e escolhe "Enviar link", então o sistema mostra a mesma resposta, com e-mail cadastrado ou não.
- [ ] Dada a fase 5, quando o e-mail está cadastrado, então o usuário recebe um link de redefinição, e esse é o único e-mail que o sistema envia.
- [ ] Dado um link de redefinição com mais de 1 hora, quando o usuário o abre, então o sistema não permite redefinir a senha.
- [ ] Dado um link de redefinição já usado, quando o usuário o abre de novo, então o sistema não permite redefinir a senha.
- [ ] Dado um link válido, quando o usuário informa nova senha dentro da regra RG-03 e a confirma, então o sistema grava a nova senha e encerra as outras sessões dele.
- [ ] Dado um usuário com outra sessão aberta, quando a senha é redefinida pelo link, então essa sessão mostra "Sessão encerrada" na próxima ação.
- [ ] Dado um aluno, quando ele entra, então ele usa e-mail do domínio @academico.ifpb.edu.br (RG-02).
- [ ] Dado um professor ou um membro da equipe, quando ele entra, então ele usa e-mail do domínio @ifpb.edu.br (RG-02).
- [ ] Dado um responsável, quando ele entra, então ele pode usar qualquer e-mail (RG-02).
- [ ] Dado um responsável cuja conta ficou "Inativo", quando ele tenta entrar, então o sistema mostra o mesmo erro de login.
- [ ] Dado um usuário sem login, quando ele abre os termos de uso, então o sistema os mostra sem pedir login.
- [ ] Dado qualquer perfil, quando abre esta tela, então ela funciona no computador e no celular e pode ser usada só com o teclado (RG-26).
- [ ] Dado que a conexão caiu ou houve erro do sistema, quando o usuário tenta entrar, então aparece "Sem conexão" ou "Erro inesperado" na própria tela e o que ele digitou continua nos campos.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
