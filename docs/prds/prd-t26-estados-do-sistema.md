# PRD da tela de Estados do sistema

| Campo | Valor |
| --- | --- |
| Identificador | T26 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md), [T02 Início](prd-t02-inicio.md), [T03 Notificações](prd-t03-notificacoes.md), [T04 Minha conta](prd-t04-minha-conta.md), [T05 Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Mostrar sempre do mesmo jeito o que aconteceu quando a tela pedida não pode ser exibida ou quando algo deu errado, para que o usuário saiba o que fazer em seguida. Esta tela é a referência de estados para todas as outras telas do sistema.

## 2. Escopo

### O que entra no escopo

- Os 7 estados: Não encontrado, Acesso negado, Item indisponível, Sessão encerrada, Acesso desativado, Sem conexão e Erro inesperado.
- A mensagem e as ações de cada estado.
- O modo de mostrar o estado com o usuário logado e sem login.
- O aviso na própria tela quando uma ação falha por falta de conexão ou por erro do sistema.

### O que não entra no escopo

- Mensagens de validação dos campos e mensagens de sucesso: ficam em cada tela.
- Tela de login e primeiro acesso: ficam em [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md).
- Lista de notificações e abertura do item relacionado: ficam em [T03 Notificações](prd-t03-notificacoes.md).
- Estado de carregamento: é uma regra comum às telas (RG-33).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Vê o estado que corresponde ao que aconteceu e escolhe uma das ações. |
| Professor | Vê o estado que corresponde ao que aconteceu e escolhe uma das ações. |
| Aluno | Vê o estado que corresponde ao que aconteceu e escolhe uma das ações. |
| Responsável | Vê o estado que corresponde ao que aconteceu e escolhe uma das ações. |

**Contexto:** o usuário tentou abrir uma tela ou fazer uma ação e o sistema não pôde atender. Ele não chega aqui por escolha, e não há item de menu para esta tela.

**Origem da jornada:** qualquer tela ou endereço do sistema → estado correspondente. A notificação com item removido leva a "Item indisponível".

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Mensagem | Frase curta que diz o que aconteceu, sem detalhe técnico (RG-24). |
| Ações | Botões do estado, com verbo no infinitivo. |
| Layout com o usuário logado | O estado aparece dentro do layout normal, com o topo e o menu. |
| Layout sem login | O estado aparece com a marca do sistema e o link "Entrar". |

Estados:

| Estado | Quando aparece | Mensagem | Ações |
| --- | --- | --- | --- |
| Não encontrado | O item não existe ou o usuário não pode vê-lo (RG-13). | Não encontramos o que você procurou. | Voltar ao Início |
| Acesso negado | O usuário abre uma tela que o perfil dele não usa, por exemplo pelo endereço copiado de outra pessoa (RG-13). | Você não tem acesso a esta tela. | Voltar ao Início |
| Item indisponível | Uma notificação aponta para um item removido ou que o usuário não pode mais ver ([T03 Notificações](prd-t03-notificacoes.md)). | Este item não está mais disponível. | Voltar às notificações |
| Sessão encerrada | A sessão expirou (RG-28) ou foi encerrada por troca ou redefinição de senha. | Sua sessão foi encerrada. Entre de novo para continuar. | Entrar, voltando depois para a tela em que estava |
| Acesso desativado | O usuário foi inativado ou perdeu o acesso com o sistema aberto (RG-05). | Seu acesso foi desativado. Procure a psicopedagoga. | Sair |
| Sem conexão | O aparelho perdeu a conexão com a internet. | Sem conexão com a internet. O que você digitou não foi perdido. | Tentar de novo |
| Erro inesperado | Uma falha que não depende do usuário. | Algo deu errado. Tente de novo em alguns minutos. | Tentar de novo, Voltar ao Início |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

Não se aplica.

### 5.2 Filtros

Não se aplica.

### 5.3 Ordenação e paginação

Não se aplica.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário tenta abrir uma tela ou fazer uma ação que o sistema não pode atender.
2. O sistema mostra o estado que corresponde ao motivo, com a mensagem e as ações dele.
3. O usuário escolhe uma das ações do estado.
4. O sistema leva o usuário ao destino da ação.

### 6.2 Fluxos alternativos

- Usuário sem login: o estado aparece com a marca do sistema e o link "Entrar" (RN-08).
- Falha ao salvar em um formulário: o que o usuário digitou continua no formulário (RG-29).
- "Sem conexão" ou "Erro inesperado" durante uma ação, como salvar: aparecem como aviso na própria tela, sem trocar de tela (RN-10).
- Troca ou redefinição de senha em outra sessão: esta sessão mostra "Sessão encerrada" na próxima ação (RN-05).
- Conta de responsável que ficou "Inativo" por não ter aluno ativo vinculado com acesso permitido: mostra "Acesso desativado" na próxima ação (RN-06).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Voltar ao Início | Todos os perfis | Abre o Início ([T02 Início](prd-t02-inicio.md)). Está em "Não encontrado", "Acesso negado" e "Erro inesperado". |
| Voltar às notificações | Todos os perfis | Abre a lista de notificações ([T03 Notificações](prd-t03-notificacoes.md)). Está em "Item indisponível". |
| Entrar | Todos os perfis | Abre o acesso ao sistema ([T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md)). Depois do login, volta para a tela em que o usuário estava. Está em "Sessão encerrada". Sem login, também aparece como link em todos os estados. |
| Sair | Todos os perfis | Encerra a sessão. Está em "Acesso desativado". O destino depois de sair está em 7.2. |
| Tentar de novo | Todos os perfis | Tenta de novo o que falhou. Está em "Sem conexão" e "Erro inesperado" (ver 7.2). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Não se aplica. |
| Vazio, por causa dos filtros | Não se aplica. |
| Sem permissão | Todos os perfis usam esta tela (matriz de permissões, seção 10 do índice). "Acesso negado" e "Não encontrado" são estados definidos na seção 4 deste PRD (RG-13). |
| Erro | Esta tela é onde os erros das outras telas aparecem. "Sem conexão" e "Erro inesperado" estão na seção 4 deste PRD. |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A tela segue RG-24: as mensagens não mostram detalhe técnico, e os botões usam verbo no infinitivo. Segue também RG-26. |
| RN-02 | "Não encontrado" aparece quando o item não existe e quando o usuário não pode vê-lo, sem diferenciar os dois casos. O sistema nunca revela que um item existe para quem não pode vê-lo (RG-13). |
| RN-03 | "Acesso negado" aparece quando o usuário abre uma tela que o perfil dele não usa, por exemplo pelo endereço copiado de outra pessoa (RG-13). |
| RN-04 | "Item indisponível" aparece quando uma notificação aponta para um item removido ou que o usuário não pode mais ver ([T03 Notificações](prd-t03-notificacoes.md)). |
| RN-05 | "Sessão encerrada" aparece quando a sessão expirou depois de 2 horas sem uso (RG-28) ou foi encerrada por troca de senha ([T04 Minha conta](prd-t04-minha-conta.md)) ou redefinição de senha ([T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md)). Ao entrar de novo, o usuário volta para a tela em que estava. |
| RN-06 | "Acesso desativado" aparece quando o usuário foi inativado ou perdeu o acesso com o sistema aberto, na próxima ação dele (RG-05). Vale também para a conta de responsável que fica "Inativo" automaticamente (seção 6 do índice). |
| RN-07 | "Sem conexão" aparece quando o aparelho perdeu a conexão com a internet. "Erro inesperado" aparece em uma falha que não depende do usuário. |
| RN-08 | Com o usuário logado, o estado aparece dentro do layout normal, com o topo e o menu. Sem login, aparece com a marca do sistema e o link "Entrar". |
| RN-09 | Em formulários, falha ao salvar mantém o que foi digitado (RG-29). |
| RN-10 | "Sem conexão" e "Erro inesperado" em uma ação, como salvar, aparecem como aviso na própria tela, sem trocar de tela. |
| RN-11 | Todas as telas usam as mensagens deste PRD para estes estados, sem mudar o texto. |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| "Tentar de novo" | A ação repete o que falhou: em uma ação, como salvar, tenta a ação de novo com o que o usuário digitou. Em uma tela, abre a tela de novo. |
| "Acesso desativado" e a sessão | Ao mostrar "Acesso desativado", o sistema encerra a sessão do usuário. A ação "Sair" leva ao login. |
| "Não encontrado" sem login | Sem login, o link "Entrar" aparece no lugar da ação "Voltar ao Início". |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Não encontrado | Erro | Não encontramos o que você procurou. |
| Acesso negado | Erro | Você não tem acesso a esta tela. |
| Item indisponível | Aviso | Este item não está mais disponível. |
| Sessão encerrada | Aviso | Sua sessão foi encerrada. Entre de novo para continuar. |
| Acesso desativado | Erro | Seu acesso foi desativado. Procure a psicopedagoga. |
| Sem conexão | Erro | Sem conexão com a internet. O que você digitou não foi perdido. |
| Erro inesperado | Erro | Algo deu errado. Tente de novo em alguns minutos. |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Ver os estados do sistema | Sim | Sim | Sim | Sim |
| Ver os estados sem login | Sim | Sim | Sim | Sim |
| Usar as ações de cada estado | Sim | Sim | Sim | Sim |

## 11. Critérios de aceite

- [ ] Dado um item que não existe, quando o usuário tenta abri-lo, então o sistema mostra "Não encontrado" com a mensagem "Não encontramos o que você procurou." e a ação "Voltar ao Início".
- [ ] Dado um item que existe mas que o usuário não pode ver, quando ele tenta abri-lo, então o sistema mostra o mesmo "Não encontrado", sem diferença em relação ao item que não existe (RG-13).
- [ ] Dada uma tela que o perfil do usuário não usa, quando ele a abre pelo endereço copiado de outra pessoa, então o sistema mostra "Acesso negado" com a mensagem "Você não tem acesso a esta tela." e a ação "Voltar ao Início".
- [ ] Dada uma notificação que aponta para um item removido, quando o usuário a abre, então o sistema mostra "Item indisponível" com a mensagem "Este item não está mais disponível." e a ação "Voltar às notificações".
- [ ] Dada uma notificação que aponta para um item que o usuário não pode mais ver, quando ele a abre, então o sistema mostra "Item indisponível", sem revelar que o item existe.
- [ ] Dado "Item indisponível", quando o usuário escolhe "Voltar às notificações", então o sistema abre a lista de notificações.
- [ ] Dada uma sessão com 2 horas sem uso, quando o usuário faz uma ação, então o sistema mostra "Sessão encerrada" com a mensagem "Sua sessão foi encerrada. Entre de novo para continuar." e a ação "Entrar".
- [ ] Dado "Sessão encerrada", quando o usuário escolhe "Entrar" e faz o login, então o sistema abre a tela em que ele estava.
- [ ] Dado um usuário que trocou ou redefiniu a senha, quando outra sessão dele faz uma ação, então essa sessão mostra "Sessão encerrada".
- [ ] Dado um usuário inativado com o sistema aberto, quando ele faz a próxima ação, então o sistema mostra "Acesso desativado" com a mensagem "Seu acesso foi desativado. Procure a psicopedagoga." e a ação "Sair".
- [ ] Dada uma conta de responsável que ficou "Inativo" por não ter aluno ativo vinculado com acesso permitido, quando o responsável faz a próxima ação, então o sistema mostra "Acesso desativado".
- [ ] Dado que o aparelho perdeu a conexão, quando o usuário tenta abrir uma tela, então o sistema mostra "Sem conexão" com a mensagem "Sem conexão com a internet. O que você digitou não foi perdido." e a ação "Tentar de novo".
- [ ] Dada uma falha que não depende do usuário, quando ele faz uma ação, então o sistema mostra "Erro inesperado" com a mensagem "Algo deu errado. Tente de novo em alguns minutos." e as ações "Tentar de novo" e "Voltar ao Início".
- [ ] Dado um erro em uma ação, como salvar, quando o sistema não consegue concluir, então "Sem conexão" ou "Erro inesperado" aparece como aviso na própria tela, sem trocar de tela.
- [ ] Dado um formulário preenchido, quando salvar falha, então o que o usuário digitou continua no formulário (RG-29).
- [ ] Dado um usuário logado, quando qualquer estado aparece, então ele aparece dentro do layout normal, com o topo e o menu.
- [ ] Dado um usuário sem login, quando qualquer estado aparece, então ele aparece com a marca do sistema e o link "Entrar".
- [ ] Dada qualquer mensagem dos estados, quando o usuário a lê, então ela não mostra detalhe técnico (RG-24).
- [ ] Dado qualquer perfil, quando vê um estado, então a tela funciona no computador e no celular e pode ser usada só com o teclado (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
