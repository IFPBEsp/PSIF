# PRD da tela de Equipe

| Campo | Valor |
| --- | --- |
| Identificador | T23 |
| Situação | Rascunho |
| Perfis | Psicopedagoga |
| Telas relacionadas | [T04 Minha conta](prd-t04-minha-conta.md), [T14 Evento](prd-t14-evento.md), [T03 Notificações](prd-t03-notificacoes.md), [T21 Professores](prd-t21-professores.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga cadastre e mantenha as pessoas da equipe com o perfil Psicopedagoga, para que mais de uma pessoa possa administrar o sistema.

## 2. Escopo

### O que entra no escopo

- Listar as pessoas da equipe, inclusive a primeira conta criada na implantação (RN-05).
- Cadastrar e editar pessoa da equipe.
- Redefinir a senha de outra pessoa da equipe.
- Inativar e reativar pessoa da equipe.
- Decidir, ao inativar, o que fazer com os eventos futuros criados pela pessoa.

### O que não entra no escopo

- Troca da própria senha: fica em [T04 Minha conta](prd-t04-minha-conta.md).
- Gestão do evento em si: fica em [T14 Evento](prd-t14-evento.md).
- Cadastro de professores: fica em [T21 Professores](prd-t21-professores.md).
- Exclusão de pessoa da equipe: ela nunca é excluída (RG-14).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Lista, cadastra, edita, redefine a senha de outra pessoa, inativa e reativa pessoas da equipe. O cargo não muda as permissões: todas as pessoas da equipe têm o perfil Psicopedagoga (seção 3 do índice). |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui quando uma pessoa nova entra na equipe, como a assistente estudantil, quando alguém esquece a senha ou quando uma pessoa deixa a equipe.

**Origem da jornada:** Início → menu "Equipe" → Equipe.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Nome (coluna da lista) | Nome da pessoa. |
| Cargo (coluna da lista) | Cargo da pessoa, por exemplo "Psicopedagoga" ou "Assistente estudantil". |
| E-mail (coluna da lista) | E-mail institucional da pessoa. |
| Situação (coluna da lista) | Aguardando primeiro acesso, Ativo ou Inativo (usuário, seção 6 do índice). |
| Total de resultados | Total de pessoas encontradas, com 20 itens por página (RG-19). |
| Criação e edição | Quem criou e quando. Registro alterado mostra "Editado em" com data e autor da última alteração (RG-15). |
| Senha provisória | Aparece uma vez, logo depois de cadastrar ou redefinir, para a psicopedagoga repassar à pessoa (RN-04). |
| Botões | "Cadastrar pessoa", "Editar", "Redefinir senha", "Inativar" e "Reativar". |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nome | Sim | Texto. |
| Cargo | Sim | Por exemplo "Psicopedagoga" ou "Assistente estudantil". Não muda as permissões. |
| E-mail institucional | Sim | Único no sistema. Domínio @ifpb.edu.br (RG-02). |
| Senha provisória | Sim, no cadastro | Segue RG-03. A pessoa precisa trocá-la no primeiro acesso. |

**Janela de confirmação da inativação, quando a pessoa tem eventos futuros**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Motivo do cancelamento dos eventos | Não | Texto livre. Se ficar vazio, o motivo é "A pessoa responsável deixou a equipe" (RN-12). |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Situação | Ativos, Inativos e Todos | Ativos |
| Busca | Nome ou e-mail (RG-20) | Vazio |

Os filtros ativos ficam visíveis, podem ser limpos de uma vez e se mantêm ao voltar para a lista (RG-21).

### 5.3 Ordenação e paginação

- Ordenação padrão: nome, de A a Z (RN-11).
- Outras ordenações: não há.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre "Equipe".
2. O sistema mostra as pessoas da equipe, inclusive a primeira conta criada na implantação.
3. A psicopedagoga escolhe "Cadastrar pessoa" e preenche nome, cargo, e-mail institucional e senha provisória.
4. A psicopedagoga escolhe "Salvar".
5. O sistema cadastra a pessoa com a situação "Aguardando primeiro acesso", mostra a senha provisória uma vez e a psicopedagoga a repassa à pessoa.

### 6.2 Fluxos alternativos

- E-mail já usado ou fora do domínio @ifpb.edu.br: o sistema não salva e indica o campo (RN-02).
- Campo obrigatório vazio ou senha fora da regra RG-03: o sistema não salva e indica o campo.
- Inativar a última pessoa ativa com o perfil: o sistema não inativa e explica o motivo (RN-06).
- Inativar a si mesma: o sistema não inativa e explica o motivo (RN-07).
- Inativar pessoa sem eventos futuros: o sistema pede confirmação e inativa.
- Inativar pessoa com eventos futuros: o sistema mostra quantos eventos futuros ela criou, pergunta se devem ser cancelados e oferece o campo de motivo (RN-10, RN-12).
- Redefinir a senha de outra pessoa: o sistema pede confirmação e define a nova senha provisória (RN-08). Se só existir uma conta ativa com o perfil, a redefinição é feita pela equipe que opera o sistema (RG-32).
- Sair do formulário com alterações não salvas: o sistema pede confirmação (RG-29).
- Falha ao salvar: o que foi digitado continua no formulário (RG-29).
- Outro perfil tenta abrir a tela: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Listar pessoas da equipe | Psicopedagoga | Mostra a lista com nome, cargo, e-mail e situação, com o filtro "Situação" em Ativos e ordenada por nome (RN-11). |
| Filtrar e buscar | Psicopedagoga | Filtra por situação e busca por nome ou e-mail (RN-11, RG-20, RG-21). |
| Cadastrar pessoa | Psicopedagoga | Valida os campos, cria a conta com o perfil Psicopedagoga e a situação "Aguardando primeiro acesso" e mostra a senha provisória uma vez (RG-01, RG-03). |
| Editar pessoa | Psicopedagoga | Salva as alterações e passa a mostrar "Editado em" (RG-15). |
| Redefinir senha de outra pessoa | Psicopedagoga | Pede confirmação, define uma nova senha provisória, mostra-a uma vez e volta a situação da pessoa para "Aguardando primeiro acesso" (RN-08). |
| Inativar pessoa | Psicopedagoga | Pede confirmação. Não vale para a última pessoa ativa nem para si mesma (RN-06, RN-07). Com eventos futuros, pergunta se devem ser cancelados e oferece o campo de motivo (RN-10, RN-12). |
| Reativar pessoa | Psicopedagoga | A pessoa volta a ter acesso. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra uma mensagem e a ação principal "Cadastrar pessoa" (RG-22). Na prática a lista nunca fica vazia, porque a primeira conta aparece nela (RN-05). |
| Vazio, por causa dos filtros | Mostra a mensagem da seção 9 e a opção de limpar os filtros (RG-22). |
| Sem permissão | Professor, aluno e responsável abrem "Acesso negado" (RG-13), de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado", de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Falha ao salvar mantém o que foi digitado (RG-29). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-01 a RG-03, RG-05, RG-13 a RG-15, RG-19, RG-22 a RG-24 e RG-29. |
| RN-02 | O e-mail institucional é obrigatório, único no sistema e usa o domínio @ifpb.edu.br, também para a equipe (RG-02). |
| RN-03 | Nome e cargo são obrigatórios. O cargo não muda as permissões: toda pessoa da equipe tem o perfil Psicopedagoga (seção 3 do índice). |
| RN-04 | A senha provisória é obrigatória no cadastro, e a pessoa precisa trocá-la no primeiro acesso (RG-03). A situação nasce "Aguardando primeiro acesso" e fica "Ativo" ao trocar a senha e aceitar os termos de uso (seção 6 do índice). |
| RN-05 | A primeira conta com o perfil Psicopedagoga é criada na implantação do sistema e aparece nesta lista (RG-27). Todas as outras contas são criadas a partir dela (RG-01). |
| RN-06 | Sempre existe pelo menos uma pessoa ativa com o perfil Psicopedagoga. A última não pode ser inativada. |
| RN-07 | Ninguém inativa a si mesmo. |
| RN-08 | Redefinir a senha de outra pessoa da equipe segue RG-32. A situação da pessoa volta para "Aguardando primeiro acesso" (seção 6 do índice). Ninguém redefine a própria senha nesta tela: a redefinição é feita por outra pessoa com o perfil (RG-32), e a pessoa troca a própria senha em [T04 Minha conta](prd-t04-minha-conta.md). A partir da fase 5, a pessoa também pode redefinir a própria senha pelo "Esqueci a senha" por e-mail ([T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md), RG-32). |
| RN-09 | Inativar remove o acesso da pessoa (RG-05). A pessoa nunca é excluída e o que ela registrou é mantido (RG-14). |
| RN-10 | Ao inativar, o sistema mostra quantos eventos futuros a pessoa criou e pergunta se devem ser cancelados. Os eventos cancelados passam a "Cancelado", e os participantes recebem a notificação "Evento cancelado" com o motivo (seção 7 do índice). Os eventos que não forem cancelados continuam e podem ser geridos por qualquer pessoa com o perfil Psicopedagoga. |
| RN-11 | A lista tem o filtro "Situação" com Ativos, Inativos e Todos, com padrão Ativos, e a busca por nome ou e-mail. A ordenação é por nome, de A a Z. |
| RN-12 | Na janela de confirmação da inativação, a psicopedagoga pode escrever o motivo do cancelamento dos eventos. Se não escrever, o motivo é "A pessoa responsável deixou a equipe". |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Cargo | Texto livre, com sugestão dos cargos já usados. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Evento cancelado porque a pessoa foi inativada e a psicopedagoga escolheu cancelar os eventos futuros dela | Participantes do evento, menos quem fez a ação (RG-25) | Aviso de evento cancelado, com o motivo (RN-10). |

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Pessoa cadastrada | Sucesso | Pessoa cadastrada. Repasse a senha provisória: ela aparece só desta vez. (proposta) |
| Pessoa atualizada | Sucesso | Pessoa atualizada. (proposta) |
| Senha redefinida | Sucesso | Senha redefinida. Repasse a nova senha provisória: ela aparece só desta vez. (proposta) |
| Pessoa inativada | Sucesso | Pessoa inativada. (proposta) |
| Pessoa reativada | Sucesso | Pessoa reativada. (proposta) |
| Campo obrigatório vazio | Erro | Preencha o campo {campo} para salvar a pessoa. (proposta) |
| E-mail fora do domínio | Erro | Use um e-mail institucional com o domínio @ifpb.edu.br. (proposta) |
| E-mail já cadastrado | Erro | Já existe uma conta com este e-mail. Use outro e-mail e salve de novo. (proposta) |
| Senha provisória fora da regra | Erro | A senha deve ter no mínimo 8 caracteres, com letras e números. Corrija e salve de novo. (proposta) |
| Inativar a última pessoa ativa | Erro | Esta é a última pessoa ativa com o perfil Psicopedagoga. Cadastre outra pessoa antes de inativar esta. (proposta) |
| Inativar a si mesma | Erro | Você não pode inativar a própria conta. Peça a outra pessoa da equipe. (proposta) |
| Redefinir senha | Confirmação | Redefinir a senha de {pessoa}? A senha atual deixa de valer e ela precisa trocar a nova senha no próximo acesso. (proposta) |
| Inativar pessoa sem eventos futuros | Confirmação | Inativar {pessoa}? Ela perde o acesso ao sistema e tudo o que registrou é mantido. (proposta) |
| Inativar pessoa com eventos futuros | Confirmação | {pessoa} criou {número} eventos futuros. Inativar a pessoa e cancelar esses eventos, ou inativar e manter os eventos? Os participantes dos eventos cancelados são avisados. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Lista vazia, sem nenhuma pessoa | Aviso | Nenhuma pessoa cadastrada. (proposta) |
| Lista vazia por causa dos filtros | Aviso | Nenhuma pessoa encontrada com estes filtros. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Listar pessoas da equipe | Sim | Não | Não | Não |
| Filtrar e buscar pessoas da equipe | Sim | Não | Não | Não |
| Cadastrar e editar pessoa da equipe | Sim | Não | Não | Não |
| Redefinir a senha de outra pessoa da equipe | Sim | Não | Não | Não |
| Inativar pessoa da equipe | Sim, menos a última pessoa ativa e menos a si mesma | Não | Não | Não |
| Reativar pessoa da equipe | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga está logada, quando abre "Equipe", então o sistema mostra nome, cargo, e-mail e situação de cada pessoa, inclusive da primeira conta criada na implantação (RN-05).
- [ ] Dado que a lista tem mais de 20 pessoas, quando a psicopedagoga abre a tela, então o sistema mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado que a psicopedagoga abre "Equipe", quando a lista carrega, então o filtro "Situação" está em Ativos e as pessoas aparecem por nome, de A a Z (RN-11).
- [ ] Dado que a psicopedagoga digita parte de um e-mail na busca, quando a lista é atualizada, então aparece a pessoa com esse e-mail (RN-11, RG-20).
- [ ] Dado que o filtro "Situação" está em Inativos e não há pessoa inativa, quando a lista carrega, então aparece a mensagem de lista vazia com a opção de limpar os filtros (RG-22).
- [ ] Dado que a psicopedagoga preencheu nome, cargo, e-mail @ifpb.edu.br único e senha provisória válida, quando escolhe "Salvar", então a pessoa é cadastrada com o perfil Psicopedagoga, o sistema mostra a senha provisória uma vez e a situação fica "Aguardando primeiro acesso" (RN-03, RN-04).
- [ ] Dado que a pessoa foi cadastrada, quando a psicopedagoga fecha a mensagem da senha provisória, então o sistema não mostra mais essa senha (RN-04).
- [ ] Dado que o cargo é "Assistente estudantil", quando a pessoa entra no sistema, então ela tem as mesmas permissões de quem tem o cargo "Psicopedagoga" (RN-03).
- [ ] Dado que o e-mail já existe no sistema ou não usa o domínio @ifpb.edu.br, quando a psicopedagoga tenta salvar, então o sistema não salva e mostra o erro do campo (RN-02).
- [ ] Dado que nome ou cargo estão vazios, quando a psicopedagoga tenta salvar, então o sistema não salva e indica o campo (RN-03).
- [ ] Dado que a senha provisória tem menos de 8 caracteres ou não tem letras e números, quando a psicopedagoga tenta salvar, então o sistema não salva e mostra o erro da senha (RG-03).
- [ ] Dado que há duas ou mais pessoas ativas, quando a psicopedagoga escolhe "Redefinir senha" de outra pessoa e confirma, então o sistema mostra a nova senha provisória uma vez e a situação da pessoa volta para "Aguardando primeiro acesso" (RN-08, RG-32).
- [ ] Dado que só existe uma conta ativa com o perfil, quando é preciso redefinir a senha dela, então a redefinição é feita pela equipe que opera o sistema (RG-32).
- [ ] Dado que a psicopedagoga está na própria linha da lista, quando tenta inativar a própria conta, então o sistema não inativa e mostra a mensagem de que ninguém inativa a si mesmo (RN-07).
- [ ] Dado que só existe uma pessoa ativa com o perfil, quando a psicopedagoga tenta inativá-la, então o sistema não inativa e mostra a mensagem de que é a última pessoa ativa (RN-06).
- [ ] Dado que existem outras pessoas ativas e a pessoa não tem eventos futuros, quando a psicopedagoga escolhe "Inativar" e confirma, então a pessoa passa a Inativo e perde o acesso (RN-09).
- [ ] Dado que a pessoa criou eventos futuros, quando a psicopedagoga escolhe "Inativar", então o sistema mostra quantos eventos futuros ela criou e pergunta se devem ser cancelados (RN-10).
- [ ] Dado que a psicopedagoga escolheu cancelar os eventos futuros, quando confirma, então os eventos passam a "Cancelado" e os participantes, menos a própria psicopedagoga, recebem a notificação "Evento cancelado" com o motivo (RN-10, RG-25).
- [ ] Dado que a psicopedagoga escolheu manter os eventos futuros, quando confirma, então os eventos continuam "Agendado" e qualquer pessoa com o perfil Psicopedagoga pode geri-los (RN-10).
- [ ] Dado que a psicopedagoga cancela os eventos futuros de quem está sendo inativado sem escrever o motivo, quando confirma, então o motivo dos eventos cancelados é "A pessoa responsável deixou a equipe" (RN-12).
- [ ] Dado que a psicopedagoga escreve um motivo na janela de inativação, quando confirma o cancelamento dos eventos, então esse motivo aparece nos eventos e na notificação (RN-12).
- [ ] Dado que a pessoa inativada estava com o sistema aberto, quando faz a próxima ação, então perde o acesso (RG-05).
- [ ] Dado que a pessoa está Inativo, quando a psicopedagoga escolhe "Reativar", então a pessoa volta a ter acesso.
- [ ] Dado que a pessoa foi alterada, quando a psicopedagoga a abre, então vê "Editado em" com a data no formato dd/mm/aaaa e o autor da última alteração (RG-15, RG-18).
- [ ] Dado que a psicopedagoga alterou campos do formulário, quando tenta sair sem salvar, então o sistema pede confirmação (RG-29).
- [ ] Dado que o salvamento falhou, quando o formulário continua aberto, então o que foi digitado continua nos campos (RG-29).
- [ ] Dado que um professor, um aluno ou um responsável tenta abrir esta tela, quando a tela carrega, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado que a ação de salvar falha por falta de conexão ou erro inesperado, quando a psicopedagoga está no formulário, então o sistema mostra o aviso de [T26 Estados do sistema](prd-t26-estados-do-sistema.md) na própria tela, sem trocar de tela.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
