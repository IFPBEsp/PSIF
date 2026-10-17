# PRD da tela de Professores

| Campo | Valor |
| --- | --- |
| Identificador | T21 |
| Situação | Rascunho |
| Perfis | Psicopedagoga |
| Telas relacionadas | [T19 Turmas](prd-t19-turmas.md), [T04 Minha conta](prd-t04-minha-conta.md), [T14 Evento](prd-t14-evento.md), [T03 Notificações](prd-t03-notificacoes.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que a psicopedagoga cadastre professores e defina em quais turmas e disciplinas cada um leciona, para que cada professor veja só os alunos das suas turmas.

## 2. Escopo

### O que entra no escopo

- Listar professores com filtros e ordenação.
- Cadastrar e editar professor, com os pares de turma e disciplina.
- Redefinir a senha do professor.
- Inativar e reativar professor.
- Decidir, ao inativar, o que fazer com os eventos futuros criados pelo professor.

### O que não entra no escopo

- Criação e edição da turma, e vínculo feito pelo lado da turma: ficam em [T19 Turmas](prd-t19-turmas.md).
- Troca da própria senha pelo professor: fica em [T04 Minha conta](prd-t04-minha-conta.md).
- Gestão do evento em si: fica em [T14 Evento](prd-t14-evento.md).
- Exclusão de professor: o professor nunca é excluído (RG-14).
- Cadastro de pessoas da equipe psicopedagógica: fica em [T23 Equipe](prd-t23-equipe.md).

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Lista, cadastra, edita, redefine a senha, inativa e reativa professores. |
| Professor | Não acessa esta tela. Abre "Acesso negado" (RG-13). Vê as suas turmas e disciplinas em [T04 Minha conta](prd-t04-minha-conta.md), sem poder alterá-las. |
| Aluno | Não acessa esta tela. Abre "Acesso negado" (RG-13). |
| Responsável | Não acessa esta tela. Abre "Acesso negado" (RG-13). |

**Contexto:** a psicopedagoga chega aqui para dar acesso a um professor novo, para ajustar as turmas e disciplinas dele, para devolver o acesso depois de uma senha esquecida ou para retirar o acesso de quem saiu do campus.

**Origem da jornada:** Início → menu "Professores" → Professores.

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Nome (coluna da lista) | Nome e sobrenome do professor. |
| E-mail (coluna da lista) | E-mail institucional do professor. |
| Telefone (coluna da lista) | Telefone, quando informado (RG-18). |
| Turmas e disciplinas (coluna da lista) | Pares de turma e disciplina do professor. |
| Situação (coluna da lista) | Ativo ou Inativo (professor, seção 6 do índice). |
| Primeiro acesso (coluna da lista) | Mostra se o professor já fez o primeiro acesso. Enquanto não trocou a senha e aceitou os termos de uso, a situação do usuário é "Aguardando primeiro acesso" (seção 6 do índice). |
| Total de resultados | Total de professores encontrados, com 20 itens por página (RG-19). |
| Criação e edição | Quem criou e quando. Professor alterado mostra "Editado em" com data e autor da última alteração (RG-15). |
| Senha provisória | Aparece uma vez, logo depois de cadastrar ou redefinir, para a psicopedagoga repassar ao professor (RN-04). |
| Botões | "Cadastrar professor", "Editar", "Redefinir senha", "Inativar" e "Reativar". |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Nome | Sim | Nome e sobrenome. |
| E-mail institucional | Sim | Único no sistema. Domínio @ifpb.edu.br (RG-02). |
| Telefone | Não | Formato (00) 00000-0000 (RG-18). |
| Turmas e disciplinas | Não | Pares de turma e disciplina. A disciplina é texto, com sugestão das já usadas. |
| Senha provisória | Sim, no cadastro | Digitada ou gerada. Aparece uma vez. Segue RG-03. |

**Janela de confirmação da inativação, quando o professor tem eventos futuros**

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Motivo do cancelamento dos eventos | Não | Texto livre. Se ficar vazio, o motivo é "O professor responsável deixou de atuar no sistema" (RN-10). |

### 5.2 Filtros

| Filtro | Opções | Valor padrão |
| --- | --- | --- |
| Busca | Nome ou e-mail | Vazio |
| Turma | Turmas | Todas |
| Disciplina | Disciplinas já usadas | Todas |
| Situação | Ativos, Inativos, Todos | Ativos |

A busca segue RG-20.

### 5.3 Ordenação e paginação

- Ordenação padrão: nome, de A a Z.
- Outras ordenações: não definidas.
- Paginação: 20 itens por página, com o total de resultados (RG-19).

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. A psicopedagoga abre "Professores".
2. O sistema mostra os professores ativos em ordem alfabética.
3. A psicopedagoga escolhe "Cadastrar professor" e preenche nome, e-mail institucional, telefone (opcional), turmas e disciplinas (opcional) e a senha provisória, digitada ou gerada.
4. A psicopedagoga escolhe "Salvar".
5. O sistema cadastra o professor com a situação "Aguardando primeiro acesso", mostra a senha provisória uma vez e a psicopedagoga a repassa ao professor.

### 6.2 Fluxos alternativos

- E-mail já usado ou fora do domínio @ifpb.edu.br: o sistema não salva e indica o campo (RN-02).
- Senha provisória fora da regra RG-03: o sistema não salva e indica o campo.
- Redefinir a senha: o sistema pede confirmação, define a nova senha provisória e muda a situação do usuário para "Aguardando primeiro acesso" (RN-05).
- Inativar professor sem eventos futuros: o sistema pede confirmação e inativa (RN-06).
- Inativar professor com eventos futuros: o sistema mostra quantos eventos futuros ele criou, pergunta se devem ser cancelados e oferece o campo de motivo (RN-07, RN-10). Os eventos não cancelados continuam na agenda (RN-09).
- Sair do formulário com alterações não salvas: o sistema pede confirmação (RG-29).
- Falha ao salvar: o que foi digitado continua no formulário (RG-29).
- Outro perfil tenta abrir a tela: abre "Acesso negado" (RG-13).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Listar, buscar e filtrar professores | Psicopedagoga | Mostra a lista com os filtros ativos visíveis (RG-21). |
| Cadastrar professor | Psicopedagoga | Valida os campos, cria o usuário com a situação "Aguardando primeiro acesso" e o professor como Ativo, e mostra a senha provisória uma vez (RG-01, RG-03). |
| Editar professor | Psicopedagoga | Salva as alterações, inclusive os pares de turma e disciplina, e passa a mostrar "Editado em" (RG-15). Mudar os pares muda, na hora, quais alunos o professor vê (RG-08). |
| Redefinir senha | Psicopedagoga | Pede confirmação, define uma nova senha provisória, mostra-a uma vez e volta a situação do usuário para "Aguardando primeiro acesso" (RN-05). |
| Inativar professor | Psicopedagoga | Pede confirmação. Remove o acesso e mantém tudo o que o professor registrou (RN-06). Com eventos futuros, pergunta se devem ser cancelados e oferece o campo de motivo (RN-07, RN-10). |
| Reativar professor | Psicopedagoga | O professor volta para Ativo. |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Mostra uma mensagem e a ação principal "Cadastrar professor" (RG-22). |
| Vazio, por causa dos filtros | Mostra uma mensagem e a opção de limpar os filtros (RG-22). |
| Sem permissão | Professor, aluno e responsável abrem "Acesso negado" (RG-13), de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). |
| Erro | "Sem conexão" e "Erro inesperado", de [T26 Estados do sistema](prd-t26-estados-do-sistema.md). Falha ao salvar mantém o que foi digitado (RG-29). |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | Segue RG-01 a RG-03, RG-05, RG-13 a RG-15, RG-18 a RG-24 e RG-29. |
| RN-02 | O e-mail institucional é obrigatório, único no sistema e usa o domínio @ifpb.edu.br (RG-02). |
| RN-03 | A disciplina é texto, com sugestão das disciplinas já usadas. Os mesmos pares de turma e disciplina são editados também em [T19 Turmas](prd-t19-turmas.md). Só a psicopedagoga altera os pares. O professor os vê em [T04 Minha conta](prd-t04-minha-conta.md). |
| RN-04 | A senha provisória é obrigatória no cadastro, digitada ou gerada, e aparece uma vez. A senha definida no cadastro precisa ser trocada no primeiro acesso (RG-03). |
| RN-05 | O usuário nasce "Aguardando primeiro acesso" e fica "Ativo" ao trocar a senha e aceitar os termos de uso. Redefinir a senha volta o usuário para "Aguardando primeiro acesso" (seção 6 do índice). |
| RN-06 | Inativar remove o acesso (RG-05) e mantém tudo o que o professor registrou. O professor nunca é excluído (RG-14). |
| RN-07 | Ao inativar, o sistema mostra quantos eventos futuros o professor criou e pergunta se devem ser cancelados. Os eventos cancelados passam a "Cancelado", e os participantes recebem a notificação "Evento cancelado" com o motivo (seção 7 do índice). |
| RN-08 | Vincular ou desvincular o professor de uma turma muda, na hora, quais alunos ele vê (RG-08). |
| RN-09 | Os eventos futuros que não forem cancelados na inativação continuam na agenda e podem ser geridos por qualquer pessoa com o perfil Psicopedagoga. |
| RN-10 | Na janela de confirmação da inativação, a psicopedagoga pode escrever o motivo do cancelamento dos eventos. Se não escrever, o motivo é "O professor responsável deixou de atuar no sistema". |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Participação do professor inativado em eventos de outros | O professor inativado continua como participante dos eventos de outros, com a resposta e a presença que já tinha. |
| Reativar professor | Não pede nova senha. O professor volta com a senha que tinha, e a psicopedagoga pode redefinir a senha na mesma tela. |
| Senha na redefinição | Segue o cadastro: digitada ou gerada, e aparece uma vez. |
| Texto do primeiro acesso | A coluna "Primeiro acesso" mostra "Aguardando primeiro acesso" ou "Primeiro acesso feito". |
| Turmas para vincular | Só turmas ativas entram na escolha de turma. |

## 8. Notificações

| Acontecimento | Quem recebe | Conteúdo |
| --- | --- | --- |
| Evento cancelado porque o professor foi inativado e a psicopedagoga escolheu cancelar os eventos futuros dele | Participantes do evento, menos quem fez a ação (RG-25) | Aviso de evento cancelado, com o motivo (RN-07). |

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Professor cadastrado | Sucesso | Professor cadastrado. Repasse a senha provisória: ela aparece só desta vez. (proposta) |
| Professor atualizado | Sucesso | Professor atualizado. (proposta) |
| Senha redefinida | Sucesso | Senha redefinida. Repasse a nova senha provisória: ela aparece só desta vez. (proposta) |
| Professor inativado | Sucesso | Professor inativado. (proposta) |
| Professor reativado | Sucesso | Professor reativado. (proposta) |
| Campo obrigatório vazio | Erro | Preencha o campo {campo} para salvar o professor. (proposta) |
| Nome sem sobrenome | Erro | Informe o nome e o sobrenome do professor. (proposta) |
| E-mail fora do domínio | Erro | Use um e-mail institucional com o domínio @ifpb.edu.br. (proposta) |
| E-mail já cadastrado | Erro | Já existe uma conta com este e-mail. Use outro e-mail e salve de novo. (proposta) |
| Senha provisória fora da regra | Erro | A senha deve ter no mínimo 8 caracteres, com letras e números. Corrija e salve de novo. (proposta) |
| Redefinir senha | Confirmação | Redefinir a senha de {professor}? A senha atual deixa de valer e ele precisa trocar a nova senha no próximo acesso. (proposta) |
| Inativar professor sem eventos futuros | Confirmação | Inativar {professor}? Ele perde o acesso ao sistema e tudo o que registrou é mantido. (proposta) |
| Inativar professor com eventos futuros | Confirmação | {professor} criou {número} eventos futuros. Inativar o professor e cancelar esses eventos, ou inativar e manter os eventos? Os participantes dos eventos cancelados são avisados. (proposta) |
| Sair com alterações não salvas | Confirmação | Você tem alterações não salvas. Se sair agora, elas serão perdidas. (proposta) |
| Lista vazia, sem nenhum professor | Aviso | Nenhum professor cadastrado. (proposta) |
| Lista vazia, por causa dos filtros | Aviso | Nenhum professor encontrado com estes filtros. (proposta) |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Listar e buscar professores | Sim | Não | Não | Não |
| Cadastrar e editar professor | Sim | Não | Não | Não |
| Alterar turmas e disciplinas do professor | Sim | Não | Não | Não |
| Redefinir a senha do professor | Sim | Não | Não | Não |
| Inativar e reativar professor | Sim | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado que a psicopedagoga está logada, quando abre "Professores", então o sistema mostra os professores ativos em ordem alfabética de nome, com nome, e-mail, telefone, turmas e disciplinas, situação e primeiro acesso (seção 5.2 e 5.3).
- [ ] Dado que a lista tem mais de 20 professores, quando a psicopedagoga abre a tela, então o sistema mostra 20 por página e o total de resultados (RG-19).
- [ ] Dado que a psicopedagoga digitou "joao" na busca, quando a lista é filtrada, então aparecem os professores cujo nome ou e-mail contém "João" ou "joao", sem diferenciar maiúsculas e acentos (RG-20).
- [ ] Dado que a psicopedagoga filtrou por turma, disciplina ou situação, quando volta para a lista depois de abrir um professor, então os filtros continuam ativos e podem ser limpos de uma vez (RG-21).
- [ ] Dado que a psicopedagoga preencheu nome e sobrenome, e-mail @ifpb.edu.br único e senha provisória válida, quando escolhe "Salvar", então o professor é cadastrado, o sistema mostra a senha provisória uma vez e o usuário fica "Aguardando primeiro acesso" (RN-04, RN-05).
- [ ] Dado que o professor foi cadastrado, quando a psicopedagoga fecha a mensagem da senha provisória, então o sistema não mostra mais essa senha (RN-04).
- [ ] Dado que a psicopedagoga pede para gerar a senha, quando salva, então o sistema cadastra o professor com a senha gerada e a mostra uma vez (RN-04).
- [ ] Dado que o e-mail já existe no sistema ou não usa o domínio @ifpb.edu.br, quando a psicopedagoga tenta salvar, então o sistema não salva e mostra o erro do campo (RN-02).
- [ ] Dado que o nome não tem sobrenome, quando a psicopedagoga tenta salvar, então o sistema não salva e indica o campo.
- [ ] Dado que a senha provisória tem menos de 8 caracteres ou não tem letras e números, quando a psicopedagoga tenta salvar, então o sistema não salva e mostra o erro da senha (RG-03).
- [ ] Dado que o telefone não segue o formato (00) 00000-0000, quando a psicopedagoga tenta salvar, então o sistema não salva e indica o campo (RG-18).
- [ ] Dado que a psicopedagoga adicionou um par de turma e disciplina, quando digita a disciplina, então o sistema sugere as disciplinas já usadas e aceita um texto novo (RN-03).
- [ ] Dado que a psicopedagoga acrescentou ou removeu um par de turma e disciplina, quando salva, então o professor passa a ver ou deixa de ver na hora os alunos daquela turma (RN-08).
- [ ] Dado que a psicopedagoga escolhe "Redefinir senha" e confirma, quando o sistema define a nova senha provisória, então a senha aparece uma vez e o usuário volta para "Aguardando primeiro acesso" (RN-05).
- [ ] Dado que o professor não tem eventos futuros criados, quando a psicopedagoga escolhe "Inativar" e confirma, então o professor passa a Inativo, perde o acesso e tudo o que registrou continua no sistema (RN-06).
- [ ] Dado que o professor criou eventos futuros, quando a psicopedagoga escolhe "Inativar", então o sistema mostra quantos eventos futuros ele criou e pergunta se devem ser cancelados (RN-07).
- [ ] Dado que a psicopedagoga escolheu cancelar os eventos futuros, quando confirma, então os eventos passam a "Cancelado" e os participantes, menos a própria psicopedagoga, recebem a notificação "Evento cancelado" com o motivo (RN-07, RG-25).
- [ ] Dado que a psicopedagoga cancela os eventos futuros do professor sem escrever o motivo, quando confirma, então o motivo dos eventos cancelados é "O professor responsável deixou de atuar no sistema" (RN-10).
- [ ] Dado que a psicopedagoga escreve um motivo na janela de inativação, quando confirma o cancelamento dos eventos, então esse motivo aparece nos eventos e na notificação (RN-10).
- [ ] Dado que a psicopedagoga escolhe manter os eventos futuros do professor, quando confirma, então os eventos continuam "Agendado" na agenda e qualquer psicopedagoga pode geri-los (RN-09).
- [ ] Dado que o professor inativado estava com o sistema aberto, quando faz a próxima ação, então perde o acesso (RG-05).
- [ ] Dado que o professor está Inativo, quando a psicopedagoga escolhe "Reativar", então o professor volta para Ativo.
- [ ] Dado que o professor foi alterado, quando a psicopedagoga o abre, então vê "Editado em" com a data no formato dd/mm/aaaa e o autor da última alteração (RG-15, RG-18).
- [ ] Dado que a psicopedagoga alterou campos do formulário, quando tenta sair sem salvar, então o sistema pede confirmação (RG-29).
- [ ] Dado que o salvamento falhou, quando o formulário continua aberto, então o que foi digitado continua nos campos (RG-29).
- [ ] Dado que nenhum professor foi cadastrado, quando a psicopedagoga abre a tela, então vê a mensagem de lista vazia e a ação "Cadastrar professor" (RG-22).
- [ ] Dado que os filtros não retornam professores, quando a psicopedagoga vê a lista, então o sistema mostra a opção de limpar os filtros (RG-22).
- [ ] Dado que um professor, um aluno ou um responsável tenta abrir esta tela, quando a tela carrega, então o sistema abre "Acesso negado" (RG-13).
- [ ] Dado que a ação de salvar falha por falta de conexão ou erro inesperado, quando a psicopedagoga está no formulário, então o sistema mostra o aviso de [T26 Estados do sistema](prd-t26-estados-do-sistema.md) na própria tela, sem trocar de tela.
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
