# PRD de índice do Inclusion of Diversity

| Campo | Valor |
| --- | --- |
| Situação | Rascunho |
| Conteúdo | Telas do produto e regras que valem para mais de uma tela |

Este índice reúne as regras transversais do produto. Os PRDs de tela citam estas regras pelo identificador ou pelo número da seção deste índice, sem copiar o texto. Por exemplo: "ver RG-19 no índice" ou "ver seção 7 do índice".

## 1. Produto

### Problema

O IFPB Campus Esperança não tem um sistema para a área psicopedagógica. O sistema institucional atual, o SUAP, só registra diário de atividades, encaminhamentos e tipos de atendimento. Relatórios, laudos, protocolos e o planejamento de cada aluno ficam no papel. Professores não têm um canal para receber orientações sobre os alunos. Alunos e responsáveis não têm onde acompanhar o atendimento nem pedir reuniões.

### Solução

Um sistema web único, que funciona no computador e no celular, com uma visão por perfil. Ele reúne:

- o acompanhamento de cada aluno com necessidades específicas;
- a agenda de reuniões e atendimentos, que é o principal diferencial do produto.

### Sucesso

- A psicopedagoga deixa de manter em papel os registros que o sistema cobre.
- Todo pedido de reunião passa pela agenda, não por canais paralelos.
- Os professores consultam as orientações no sistema antes de adaptar atividades.

## 2. Telas

| Id | Tela | Perfis | Fase |
| --- | --- | --- | --- |
| T01 | [Acesso ao sistema](prd-t01-acesso-ao-sistema.md) | Todos | 1 e 5 |
| T02 | [Início](prd-t02-inicio.md) | Todos | 1 |
| T03 | [Notificações](prd-t03-notificacoes.md) | Todos | 1 |
| T04 | [Minha conta](prd-t04-minha-conta.md) | Todos | 1 |
| T05 | [Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md) | Todos | 1 e 5 |
| T06 | [Lista de alunos](prd-t06-lista-de-alunos.md) | Psicopedagoga, Professor | 1 |
| T07 | [Cadastro de aluno](prd-t07-cadastro-de-aluno.md) | Psicopedagoga | 1 |
| T08 | [Perfil do aluno](prd-t08-perfil-do-aluno.md) | Todos | 1 |
| T09 | [Dados de saúde](prd-t09-dados-de-saude.md) | Psicopedagoga | 3 |
| T10 | [Acompanhamentos](prd-t10-acompanhamentos.md) | Psicopedagoga | 3 |
| T11 | [Características e orientações](prd-t11-caracteristicas-e-orientacoes.md) | Psicopedagoga, Professor | 1 |
| T12 | [Planejamento semanal](prd-t12-planejamento-semanal.md) | Psicopedagoga, Aluno, Responsável | 3 |
| T13 | [Agenda](prd-t13-agenda.md) | Todos | 2 |
| T14 | [Evento](prd-t14-evento.md) | Todos | 2 |
| T15 | [Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md) | Psicopedagoga, Aluno, Responsável | 2 |
| T16 | [Atividades adaptadas](prd-t16-atividades-adaptadas.md) | Psicopedagoga, Professor | 3 |
| T17 | [Observações dos professores](prd-t17-observacoes-dos-professores.md) | Psicopedagoga, Professor | 3 |
| T18 | [Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) | Psicopedagoga, Aluno, Responsável | 4 |
| T19 | [Turmas](prd-t19-turmas.md) | Psicopedagoga, Professor | 1 |
| T20 | [Cursos](prd-t20-cursos.md) | Psicopedagoga | 1 |
| T21 | [Professores](prd-t21-professores.md) | Psicopedagoga | 1 |
| T22 | [Dificuldades](prd-t22-dificuldades.md) | Psicopedagoga | 1 |
| T23 | [Equipe](prd-t23-equipe.md) | Psicopedagoga | 1 |
| T24 | [Formulários](prd-t24-formularios.md) | Psicopedagoga | 5 |
| T25 | [Busca no acervo](prd-t25-busca-no-acervo.md) | Psicopedagoga | 5 |
| T26 | [Estados do sistema](prd-t26-estados-do-sistema.md) | Todos | 1 |

A coluna "Perfis" mostra os perfis principais de cada tela. O que cada perfil pode fazer em cada tela está na matriz de permissões (seção 10).

## 3. Perfis

| Perfil | Papel no produto |
| --- | --- |
| Psicopedagoga | Administra o sistema. Cadastra usuários, turmas e dificuldades, registra o acompanhamento dos alunos, gerencia a agenda e responde aos pedidos de agendamento. |
| Professor | Vê os alunos atendidos das turmas em que leciona, com características e orientações. Registra atividades adaptadas e observações de desempenho. Marca avaliações e reuniões. |
| Aluno | Vê os próprios dados, o planejamento semanal e a agenda. Pede agendamentos e envia informações à psicopedagoga. |
| Responsável | Acompanha o aluno vinculado: dados, planejamento, agenda e pedidos. Pode pedir agendamentos e enviar informações em nome do aluno. |

Cada usuário tem um único perfil.

O perfil Psicopedagoga também pode ser dado a outros membros da equipe psicopedagógica, como a assistente estudantil, com as mesmas permissões. O que diferencia essas pessoas é o cargo, não o perfil. Nas telas, "a psicopedagoga" quer dizer qualquer usuário com este perfil. "As psicopedagogas" quer dizer todos os usuários ativos com este perfil.

## 4. Glossário

O mesmo termo é usado em todas as telas.

| Termo | Significado |
| --- | --- |
| Aluno | Estudante atendido pela psicopedagoga. Só alunos com necessidade específica são cadastrados. |
| Responsável | Pessoa responsável pelo aluno. Pode estar vinculada a mais de um aluno, como no caso de irmãos. Pode ser só um contato ou ter conta no sistema. |
| Curso | Curso técnico do campus, identificado por sigla e nome. |
| Série | Ano do curso em que o aluno está: 1º, 2º, 3º ou 4º, até o número de séries do curso. |
| Ano letivo | Ano do calendário escolar, com quatro dígitos. |
| Ano letivo atual | O ano letivo mais recente que tem pelo menos uma turma ativa. É o padrão dos filtros de turma. |
| Turma | Combinação de curso, série e ano letivo. Todo aluno está em uma turma. |
| Disciplina | Matéria que o professor leciona em uma turma. É registrada como texto no vínculo entre professor e turma ([T19 Turmas](prd-t19-turmas.md) e [T21 Professores](prd-t21-professores.md)). |
| Cargo | Função de quem tem o perfil Psicopedagoga, por exemplo "Psicopedagoga" ou "Assistente estudantil". Não muda as permissões. |
| Dificuldade | Deficiência, transtorno ou dificuldade de aprendizagem, mantida em um catálogo. Um aluno pode ter várias. |
| Diagnóstico | Registro clínico do aluno, com descrição, data e laudo. |
| Laudo | Documento em PDF, emitido por um profissional de saúde, que comprova o diagnóstico. |
| Teste inicial | Questionário aplicado uma vez a cada aluno, no início do atendimento. |
| Teste aplicado | Qualquer outro teste aplicado ao aluno, com nome, data e resultado. |
| Acompanhamento | Registro feito pela psicopedagoga sobre o aluno: observação semanal, atendimento, reunião ou relatório. |
| Características | Texto da psicopedagoga que descreve como o aluno se comporta e aprende. Professores leem. |
| Orientações | Texto da psicopedagoga que explica aos professores como lidar com o aluno. |
| Planejamento semanal | Grade de atividades do aluno de segunda a domingo, montada pela psicopedagoga. |
| Evento | Compromisso na agenda: reunião, atendimento, avaliação ou outro. |
| Avaliação | Tipo de evento para uma prova, trabalho ou apresentação de um ou mais alunos atendidos. Fica na agenda para que a psicopedagoga acompanhe e oriente as adaptações. |
| Participante | Usuário incluído em um evento. O criador e os alunos escolhidos no campo "Alunos" são participantes automaticamente. |
| Resposta | O que o participante disse antes do evento: se vai ou não comparecer. |
| Presença | O que aconteceu no evento: se o participante compareceu ou faltou. É registrada depois do evento. |
| Pedido de agendamento | Pedido do aluno ou do responsável para marcar, remarcar ou cancelar um evento. Depende da aprovação da psicopedagoga. |
| Atividade adaptada | Atividade que o professor adaptou para um aluno, registrada com data, disciplina e descrição. |
| Observação do professor | Registro do professor sobre o desempenho do aluno na disciplina dele. |
| Informação | Mensagem que o aluno ou o responsável envia à psicopedagoga. |
| Dados de saúde | Diagnósticos, teste inicial, testes aplicados e acompanhamentos. |
| Anexo | Arquivo ligado a um registro, como laudo, relatório ou foto de atividade. |
| Termos de uso | Texto que explica como o sistema funciona e como os dados pessoais são tratados. Cada versão precisa ser aceita pelo usuário. |

## 5. Regras gerais

Valem para todas as telas. Os PRDs de tela citam estas regras pelo identificador, sem repetir o texto. Os identificadores não mudam quando uma regra é acrescentada, por isso algumas tabelas não estão em ordem numérica.

### Acesso

| Id | Regra |
| --- | --- |
| RG-01 | Não existe autocadastro. Só a psicopedagoga cadastra usuários. |
| RG-02 | O login usa e-mail institucional e senha. Alunos usam o domínio @academico.ifpb.edu.br. Professores e equipe usam o domínio @ifpb.edu.br. Responsáveis usam qualquer e-mail. |
| RG-03 | A senha tem no mínimo 8 caracteres, com letras e números. A senha definida no cadastro é provisória e precisa ser trocada no primeiro acesso. |
| RG-04 | Cinco tentativas de login erradas seguidas bloqueiam o login daquele e-mail por 15 minutos. |
| RG-05 | Usuário inativo não entra no sistema. Se for inativado com o sistema aberto, perde o acesso na próxima ação. |
| RG-06 | Quando os termos de uso mudam, o usuário precisa aceitar a nova versão no próximo login. |
| RG-27 | A primeira conta com o perfil Psicopedagoga é criada na implantação do sistema. Todas as outras contas são criadas a partir dela (RG-01). |
| RG-32 | A senha de quem tem o perfil Psicopedagoga é redefinida por outra pessoa com o mesmo perfil ([T23 Equipe](prd-t23-equipe.md)). Se só existir uma conta ativa com este perfil, a equipe que opera o sistema faz a redefinição, como na criação da primeira conta (RG-27). A partir da fase 5, quem tem este perfil também pode redefinir a própria senha pelo link enviado por e-mail ([T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md)). |
| RG-28 | A sessão é encerrada depois de 2 horas sem uso. Quando o usuário entra de novo, volta para a tela em que estava. |

### Visibilidade

| Id | Regra |
| --- | --- |
| RG-07 | A psicopedagoga vê todos os alunos, ativos e inativos. |
| RG-08 | O professor vê só os alunos ativos das turmas em que leciona. Se o aluno muda de turma, os professores da turma anterior perdem o acesso a ele. |
| RG-09 | O aluno vê só os próprios dados. O responsável vê só os alunos vinculados a ele. |
| RG-10 | Dados de saúde são vistos só pela psicopedagoga, salvo os acompanhamentos que ela marcar como visíveis para a família. |
| RG-11 | O professor nunca vê dados de saúde, contatos, endereço ou data de nascimento do aluno. Vê nome, foto, turma, dificuldades, características e orientações. |
| RG-12 | Um anexo tem a mesma visibilidade do registro ao qual pertence. |
| RG-13 | Item que não existe e item que o usuário não pode ver abrem a mesma tela "Não encontrado", sem diferenciar os dois casos. Tela que o perfil não usa abre "Acesso negado". As duas telas estão em [T26 Estados do sistema](prd-t26-estados-do-sistema.md). O sistema nunca revela que um item existe para quem não pode vê-lo. |
| RG-31 | Em eventos e pedidos, cada usuário vê pelo nome só os participantes que pode ver: as pessoas com perfil Psicopedagoga, os professores, os alunos que ele vê pelas regras RG-07 a RG-09 e os responsáveis desses alunos. Os outros participantes aparecem só como quantidade, por exemplo "Mais 2 participantes". Assim, ninguém descobre por um evento que outro aluno é atendido. O texto das notificações de evento e de pedido segue a mesma regra. |

### Registros

| Id | Regra |
| --- | --- |
| RG-14 | Aluno, responsável, professor, turma, curso, dificuldade e membro da equipe nunca são excluídos. São inativados ou desvinculados, e o histórico é mantido. |
| RG-15 | Todo registro mostra quem criou e quando. Registro alterado mostra "Editado em" com data e autor da última alteração. |
| RG-16 | Anexos aceitos: PDF, JPG e PNG, com até 10 MB cada e até 5 por registro. Fotos de perfil: JPG ou PNG com até 5 MB. |
| RG-17 | Responsável é obrigatório para aluno menor de 18 anos. Para aluno com 18 anos ou mais, o responsável só tem acesso ao sistema com autorização do aluno, registrada pela psicopedagoga. |
| RG-18 | Datas no formato dd/mm/aaaa, horários no formato 24 horas, telefone no formato (00) 00000-0000. Datas e horários seguem o horário de Brasília. |
| RG-30 | Todo botão "Imprimir" usa a mesma versão impressa, desde a fase em que a tela é entregue. A versão impressa tem o nome do campus, o nome do sistema e a data de impressão. Documento com dados de saúde e a ficha do aluno têm a marcação "Documento confidencial". Cada impressão de documento preenchido com os dados do sistema fica registrada com quem imprimiu, quando e o quê. O modelo preenchido à mão na tela, em [T24 Formulários](prd-t24-formularios.md), não fica registrado. |

### Listas, ações e mensagens

| Id | Regra |
| --- | --- |
| RG-19 | Listas mostram 20 itens por página e o total de resultados. |
| RG-20 | A busca por texto ignora maiúsculas, minúsculas e acentos, e começa a partir de 2 caracteres. |
| RG-21 | Filtros ativos ficam visíveis, podem ser limpos de uma vez e se mantêm ao voltar para a lista. Um link copiado da lista abre com os mesmos filtros. |
| RG-22 | Lista vazia mostra uma mensagem e a ação principal (por exemplo, "Cadastrar aluno"). Lista vazia por causa de filtros mostra a opção de limpar os filtros. |
| RG-23 | Ações que não podem ser desfeitas ou que afetam outras pessoas pedem confirmação. A confirmação diz a ação e a consequência, nunca "Tem certeza?". |
| RG-24 | Botões usam verbo no infinitivo ("Salvar", "Pedir agendamento"). Mensagens de erro dizem o que aconteceu e o que fazer, sem detalhe técnico. |
| RG-25 | Ninguém recebe notificação da própria ação. |
| RG-26 | Todas as telas funcionam no computador e no celular, e podem ser usadas só com o teclado. |
| RG-29 | Sair de um formulário com alterações não salvas pede confirmação. Se salvar falhar, o que foi digitado continua no formulário. |
| RG-33 | Enquanto carrega, a tela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo. |

## 6. Situações

| Item | Situações | Regras de mudança |
| --- | --- | --- |
| Usuário | Aguardando primeiro acesso, Ativo, Inativo | Nasce "Aguardando primeiro acesso". Fica "Ativo" ao trocar a senha e aceitar os termos. Volta para "Aguardando primeiro acesso" quando a psicopedagoga redefine a senha. |
| Conta de responsável | As mesmas do usuário | Além das regras do usuário, fica "Inativo" automaticamente quando não tem nenhum aluno ativo vinculado com acesso permitido (RG-17). Volta ao estado anterior quando passa a ter. A psicopedagoga também pode retirar o acesso. |
| Aluno, professor, turma, curso, dificuldade | Ativo, Inativo | A psicopedagoga inativa e reativa. |
| Evento | Agendado, Realizado, Cancelado | Nasce "Agendado". Vira "Realizado" automaticamente quando passa o horário de término. Vira "Cancelado" quando o criador ou a psicopedagoga cancela, ou quando a psicopedagoga aceita um pedido de cancelamento. Remarcar mantém "Agendado" e guarda o histórico. |
| Resposta do participante | Sem resposta, Confirmada, Recusada | O criador nasce com "Confirmada". Os outros nascem com "Sem resposta". Todos voltam para "Sem resposta" quando o evento é remarcado. |
| Presença do participante | Não registrada, Presente, Faltou | Nasce "Não registrada". Depois que o evento vira "Realizado", o criador ou a psicopedagoga registra e pode corrigir. |
| Pedido de agendamento | Pendente, Aceito, Recusado, Cancelado, Expirado | Nasce "Pendente". A psicopedagoga aceita ou recusa. O autor pode cancelar enquanto está pendente. Vira "Cancelado" automaticamente quando o aluno é inativado ou quando o autor perde o acesso ao aluno. Vira "Expirado" quando a última data sugerida passa sem resposta ou, nos pedidos de remarcação e cancelamento, quando o evento começa. |
| Planejamento semanal | Rascunho, Confirmado | Nasce "Rascunho". Vira "Confirmado" quando a psicopedagoga confirma, e só pode ser confirmado com pelo menos uma atividade. Planejamento confirmado não volta para "Rascunho". Aluno e responsável só veem planejamentos confirmados. Semana encerrada fica só para leitura. |
| Informação | Não lida, Lida | Vira "Lida" quando a psicopedagoga abre. Ela pode marcar de novo como não lida. A situação vale para todas as psicopedagogas. |
| Notificação | Não lida, Lida | Vira "Lida" quando o usuário abre o item ou marca como lida. |

## 7. Notificações

As notificações aparecem só dentro do sistema, no sino e na tela [T03 Notificações](prd-t03-notificacoes.md). O sistema não envia notificação por e-mail (seção 11). O responsável só recebe notificação se tiver conta ativa. Ninguém recebe notificação da própria ação (RG-25).

| Acontecimento | Quem recebe |
| --- | --- |
| Evento criado | Participantes. Quem é incluído depois, numa edição, também recebe este aviso. |
| Evento alterado ou remarcado | Participantes que continuam no evento |
| Participante retirado do evento | Quem foi retirado, com o nome, a data e a hora do evento |
| Evento cancelado | Participantes, com o motivo |
| Lembrete, 24 horas antes do evento | Participantes que não recusaram |
| Participante recusa presença | Quem criou o evento |
| Pedido de agendamento criado | Psicopedagogas |
| Pedido de agendamento aceito ou recusado | Quem pediu, o aluno e os responsáveis do aluno |
| Pedido de agendamento cancelado pelo autor | Psicopedagogas |
| Pedido de agendamento cancelado automaticamente, porque o aluno foi inativado ou o autor perdeu o acesso ao aluno | Psicopedagogas, com o motivo |
| Pedido de agendamento expirado | Quem pediu |
| Atividade adaptada registrada | Psicopedagogas, o aluno e os responsáveis do aluno |
| Observação do professor registrada | Psicopedagogas |
| Informação enviada | Psicopedagogas |
| Acompanhamento visível para a família registrado ou alterado | Aluno e responsáveis |
| Características ou orientações atualizadas | Professores do aluno |
| Planejamento semanal confirmado ou alterado depois de confirmado | Aluno e responsáveis |
| Aluno com responsável com acesso completa 18 anos em 30 dias | Psicopedagogas |

## 8. Navegação por perfil

O menu mostra só o que o perfil pode usar. O topo da tela tem o sino de notificações e o menu do usuário (Minha conta, Ajuda, Sair).

| Perfil | Itens do menu |
| --- | --- |
| Psicopedagoga | Início, Alunos, Agenda, Pedidos de agendamento, Informações recebidas, Atividades adaptadas, Turmas, Professores, Dificuldades, Cursos, Equipe, Formulários, Busca no acervo |
| Professor | Início, Alunos, Turmas, Agenda, Atividades adaptadas |
| Aluno | Início, Meu perfil, Agenda, Meus pedidos, Enviar informação |
| Responsável | Início, Perfil do aluno, Agenda, Meus pedidos, Enviar informação |

Com mais de um aluno vinculado, o responsável escolhe o aluno no Início e pode trocar no cabeçalho de qualquer tela ([T02 Início](prd-t02-inicio.md)).

Cada item do menu leva a uma tela:

| Item do menu | Tela |
| --- | --- |
| Início | [T02 Início](prd-t02-inicio.md) |
| Alunos | [T06 Lista de alunos](prd-t06-lista-de-alunos.md) |
| Meu perfil e Perfil do aluno | [T08 Perfil do aluno](prd-t08-perfil-do-aluno.md) |
| Agenda | [T13 Agenda](prd-t13-agenda.md) |
| Pedidos de agendamento e Meus pedidos | [T15 Pedidos de agendamento](prd-t15-pedidos-de-agendamento.md) |
| Informações recebidas e Enviar informação | [T18 Informações para a psicopedagoga](prd-t18-informacoes-para-a-psicopedagoga.md) |
| Atividades adaptadas | [T16 Atividades adaptadas](prd-t16-atividades-adaptadas.md) |
| Turmas | [T19 Turmas](prd-t19-turmas.md) |
| Professores | [T21 Professores](prd-t21-professores.md) |
| Dificuldades | [T22 Dificuldades](prd-t22-dificuldades.md) |
| Cursos | [T20 Cursos](prd-t20-cursos.md) |
| Equipe | [T23 Equipe](prd-t23-equipe.md) |
| Formulários | [T24 Formulários](prd-t24-formularios.md) |
| Busca no acervo | [T25 Busca no acervo](prd-t25-busca-no-acervo.md) |
| Sino de notificações | [T03 Notificações](prd-t03-notificacoes.md) |
| Minha conta e Sair | [T04 Minha conta](prd-t04-minha-conta.md) |
| Ajuda | [T05 Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md) |

## 9. Fases de entrega

| Fase | Foco | Telas |
| --- | --- | --- |
| 1 | Base | T01 (sem recuperação por e-mail), T02, T03, T04, T05 (termos), T06, T07, T08, T11, T19, T20, T21, T22, T23, T26 |
| 2 | Agenda | T13, T14, T15 |
| 3 | Acompanhamento | T09, T10, T12, T16, T17 |
| 4 | Comunicação | T18 |
| 5 | Complementos | T05 (ajuda), T24, T25 e recuperação de senha por e-mail em T01 |

Uma tela pode citar outra de uma fase posterior. A parte que depende da outra tela (bloco, aba, filtro, ação ou notificação) só aparece quando ela for entregue. Por exemplo, a aba "Planejamento semanal" do perfil (T08, fase 1) só aparece na fase 3, com T12.

## 10. Matriz de permissões

Legenda:

| Valor | Significado |
| --- | --- |
| Sim | Acesso completo. |
| Lê | Só leitura. |
| Próprio | Só o que é dele ou do aluno vinculado. |
| Turmas | Só alunos das suas turmas. |
| Visíveis | Só os registros marcados como visíveis para a família. |
| Não | Sem acesso. |

| Tela | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| T01 a T05 e T26 | Sim | Sim | Sim | Sim |
| T06 Lista de alunos | Sim | Lê, Turmas | Não | Não |
| T07 Cadastro de aluno | Sim | Não | Não | Não |
| T08 Perfil do aluno | Sim | Lê, Turmas | Lê, Próprio | Lê, Próprio |
| T09 Dados de saúde | Sim | Não | Não | Não |
| T10 Acompanhamentos | Sim | Não | Lê, Próprio, Visíveis | Lê, Próprio, Visíveis |
| T11 Características e orientações | Sim | Lê, Turmas | Não | Não |
| T12 Planejamento semanal | Sim | Não | Lê, Próprio | Lê, Próprio |
| T13 Agenda | Sim | Sim, conforme T13 | Próprio | Próprio |
| T14 Evento | Sim | Cria, Turmas | Responde e pede, Próprio | Responde e pede, Próprio |
| T15 Pedidos de agendamento | Analisa | Não | Próprio | Próprio |
| T16 Atividades adaptadas | Lê | Sim, Turmas | Lê, Próprio | Lê, Próprio |
| T17 Observações dos professores | Lê | Próprio, Turmas | Não | Não |
| T18 Informações para a psicopedagoga | Recebe | Não | Envia, Próprio | Envia, Próprio |
| T19 Turmas | Sim | Lê, as suas | Não | Não |
| T20 a T25 | Sim | Não | Não | Não |

## 11. Fora do escopo

- Cópia de segurança dos dados: é rotina de operação do sistema, sem tela para o usuário.
- Integração com o sistema institucional (login institucional unificado, importação de alunos): fica para depois.
- Encaminhamentos para outros setores do campus.
- Conversa em tempo real entre usuários.
- Aplicativo instalável. O sistema web funciona no navegador do celular (RG-26).
- Notificações por e-mail, SMS ou celular. As notificações ficam só dentro do sistema (seção 7). O único e-mail que o sistema envia é o link de redefinição de senha, a partir da fase 5.
- Edição dos termos de uso pelo sistema. A equipe que opera o sistema publica cada nova versão, e os usuários aceitam no próximo login (RG-06).
- Análise de pedidos de exclusão de dados pessoais. O pedido é feito pelo canal de proteção de dados do IFPB ([T05 Ajuda e termos de uso](prd-t05-ajuda-e-termos-de-uso.md)). Se o pedido for atendido, a equipe que opera o sistema faz a exclusão, como exceção à RG-14.
