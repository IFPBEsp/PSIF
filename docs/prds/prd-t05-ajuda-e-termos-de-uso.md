# PRD da tela de Ajuda e termos de uso

| Campo | Valor |
| --- | --- |
| Identificador | T05 |
| Situação | Rascunho |
| Perfis | Psicopedagoga, Professor, Aluno, Responsável |
| Telas relacionadas | [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md), [T04 Minha conta](prd-t04-minha-conta.md), [T26 Estados do sistema](prd-t26-estados-do-sistema.md) |
| Fase de entrega | 1 (termos de uso) e 5 (ajuda) |

As regras RG-xx, as situações, as notificações e a matriz de permissões citadas neste PRD estão no [índice](prd-indice.md).

## 1. Objetivo

Permitir que o usuário aprenda a usar o sistema e saiba como os dados pessoais são tratados, para usar o sistema com segurança e pedir a correção ou a exclusão dos dados quando precisar.

## 2. Escopo

### O que entra no escopo

- Termos de uso: texto, versão e data de vigência.
- Leitura dos termos sem login.
- Ajuda: tópicos de uso filtrados pelo perfil do usuário.
- Ajuda: perguntas frequentes.
- Ajuda: busca nos tópicos.
- Informação sobre como pedir correção e exclusão de dados pessoais.

### O que não entra no escopo

- Aceitar os termos: o aceite no primeiro acesso e o aceite de nova versão acontecem em [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md).
- Editar o texto dos termos pelo sistema: a equipe que opera o sistema publica cada nova versão (seção 11 do índice).
- Analisar pedidos de exclusão de dados pessoais: o pedido é analisado fora do sistema (seção 11 do índice).
- Corrigir dados pessoais: a psicopedagoga altera o cadastro correspondente.

## 3. Usuários e contexto

| Perfil | O que faz nesta tela |
| --- | --- |
| Psicopedagoga | Lê os termos de uso e os tópicos de ajuda do perfil Psicopedagoga, vê as perguntas frequentes e busca nos tópicos. |
| Professor | Lê os termos de uso e os tópicos de ajuda do perfil Professor, vê as perguntas frequentes e busca nos tópicos. |
| Aluno | Lê os termos de uso e os tópicos de ajuda do perfil Aluno, vê as perguntas frequentes e busca nos tópicos. |
| Responsável | Lê os termos de uso e os tópicos de ajuda do perfil Responsável, vê as perguntas frequentes e busca nos tópicos. |

**Contexto:** o usuário tem uma dúvida de uso, quer saber como os dados dele são tratados ou quer ler os termos antes de aceitar. Quem ainda não entrou no sistema também pode ler os termos.

**Origem da jornada:** menu do usuário no topo → Ajuda. Quem está no primeiro acesso ou diante da nova versão dos termos chega pela opção de ler os termos em [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md).

## 4. Informações da tela

| Informação | Descrição funcional |
| --- | --- |
| Termos de uso | Texto completo dos termos. Explica quais dados são coletados, para quê, quem tem acesso e como pedir correção ou exclusão. |
| Versão dos termos | Número da versão dos termos que está em vigor. |
| Data de vigência | Data em que a versão passou a valer, no formato dd/mm/aaaa (RG-18). |
| Canal de proteção de dados | Indicado no texto dos termos. É o canal de proteção de dados pessoais do IFPB, usado para pedir a exclusão de dados. |
| Tópicos de ajuda | Explicações de uso do sistema, só os do perfil do usuário. Fase 5. |
| Perguntas frequentes | Perguntas e respostas de uso do sistema. Fase 5. |
| Busca nos tópicos | Campo de busca que filtra os tópicos de ajuda. Fase 5. |
| Marca do sistema e link "Entrar" | Aparecem quando o usuário abre a tela sem estar logado ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |

## 5. Campos, filtros e ordenação

### 5.1 Campos do formulário

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Busca nos tópicos (fase 5) | Não | Texto livre. Ignora maiúsculas, minúsculas e acentos e começa a partir de 2 caracteres (RG-20). |

### 5.2 Filtros

Não se aplica. A Ajuda mostra só os tópicos do perfil do usuário (RN-08).

### 5.3 Ordenação e paginação

Não se aplica.

## 6. Comportamento esperado

### 6.1 Fluxo principal

1. O usuário escolhe "Ajuda" no menu do usuário.
2. O sistema mostra os termos de uso. Na fase 5, mostra também os tópicos de ajuda do perfil dele e as perguntas frequentes.
3. O usuário lê um tópico, uma pergunta frequente ou os termos.
4. Na fase 5, se quiser achar um assunto, digita na busca e o sistema filtra os tópicos.

### 6.2 Fluxos alternativos

- Usuário sem login: lê só os termos de uso, em uma página com a marca do sistema e o link "Entrar".
- Busca com menos de 2 caracteres: o sistema não busca e orienta o usuário (RG-20).
- Busca sem resultado: o sistema mostra a mensagem de busca vazia.
- Usuário que quer corrigir dados: procura a psicopedagoga, que altera o cadastro (RN-04).
- Usuário que quer excluir dados: usa o canal de proteção de dados pessoais do IFPB indicado nos termos. O pedido é analisado fora do sistema (RN-05).
- Falha de conexão ou erro do sistema: aparece "Sem conexão" ou "Erro inesperado" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)).

### 6.3 Ações do usuário

| Ação | Quem pode | Comportamento esperado |
| --- | --- | --- |
| Ler os termos de uso | Todos os perfis, com ou sem login | Mostra o texto, a versão e a data de vigência. |
| Ler um tópico de ajuda (fase 5) | Todos os perfis, com login | Mostra o tópico do perfil do usuário. |
| Ler as perguntas frequentes (fase 5) | Todos os perfis, com login | Mostra as perguntas e as respostas. |
| Buscar nos tópicos (fase 5) | Todos os perfis, com login | Filtra os tópicos de ajuda pelo texto digitado (RG-20). |
| Entrar | Quem abre a tela sem login | Leva para [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md). |

### 6.4 Estados da tela

| Estado | Comportamento esperado |
| --- | --- |
| Carregando | Segue RG-33. |
| Vazio, sem nenhum registro | Não se aplica: os termos de uso sempre existem. Ajuda sem nenhum tópico para o perfil: ver "Ajuda sem conteúdo" em 7.2. |
| Vazio, por causa dos filtros | A busca sem resultado mostra a mensagem "Nenhum tópico encontrado. Tente outras palavras. (proposta)" e a opção de limpar a busca. |
| Sem permissão | Todos os perfis usam esta tela e os termos podem ser lidos sem login (matriz de permissões, seção 10 do índice). "Acesso negado" e "Não encontrado" (RG-13) não se aplicam. Quem foi inativado com o sistema aberto vê "Acesso desativado" (RG-05, [T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |
| Erro | "Sem conexão" e "Erro inesperado" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |

### 6.5 Entrega por fase

| Fase | O que aparece |
| --- | --- |
| 1 | Termos de uso: texto, versão e data de vigência. O item "Ajuda" do menu do usuário abre a tela só com os termos. |
| 5 | Ajuda: tópicos de uso filtrados pelo perfil, perguntas frequentes e busca nos tópicos, junto com os termos de uso. |

## 7. Regras de negócio

### 7.1 Regras definidas

| Id | Regra |
| --- | --- |
| RN-01 | A tela segue RG-20 na busca de tópicos e RG-26 em todas as partes. |
| RN-02 | Os termos de uso podem ser lidos sem login. Sem login, a página aparece com a marca do sistema e o link "Entrar" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)). |
| RN-03 | Os termos explicam quais dados são coletados, para quê, quem tem acesso e como pedir correção ou exclusão. A tela mostra o texto, a versão e a data de vigência. |
| RN-04 | A correção de dados se pede à psicopedagoga, que altera o cadastro. |
| RN-05 | A exclusão de dados se pede pelo canal de proteção de dados pessoais do IFPB, que os termos indicam. O pedido é analisado fora do sistema. Se for atendido, a equipe que opera o sistema faz a exclusão, como exceção à RG-14 (seção 11 do índice). |
| RN-06 | O aceite dos termos fica registrado com data, hora e versão (RG-06). O aceite acontece em [T01 Acesso ao sistema](prd-t01-acesso-ao-sistema.md), no primeiro acesso e quando há nova versão. |
| RN-07 | O sistema não edita o texto dos termos. Cada nova versão é publicada pela equipe que opera o sistema, e os usuários aceitam no próximo login (RG-06). |
| RN-08 | A Ajuda mostra só os tópicos do perfil do usuário. |
| RN-09 | Sem login, a tela mostra só os termos de uso. Tópicos de ajuda, perguntas frequentes e busca dependem do perfil do usuário e exigem login. |
| RN-10 | A parte de ajuda só aparece na fase 5. Na fase 1, a tela tem só os termos de uso (seção 9 do índice). |

### 7.2 Regras propostas para validação

| Regra | Definição sugerida |
| --- | --- |
| Mensagens propostas | Os textos marcados com (proposta) na seção 9 dependem de validação. |
| Conteúdo dos tópicos e das perguntas frequentes | Cada perfil tem tópicos próprios: Psicopedagoga (cadastros, agenda, pedidos e informações), Professor (alunos das turmas, características e orientações, atividades adaptadas e observações), Aluno e Responsável (perfil, planejamento, agenda, pedidos e envio de informação). A equipe que opera o sistema publica o conteúdo. |
| Ajuda sem conteúdo | Se o perfil não tiver nenhum tópico publicado, a tela mostra "Ainda não há tópicos de ajuda para o seu perfil." |
| Versões anteriores dos termos | O usuário vê só a versão em vigor. |
| Registro do próprio aceite | O usuário logado vê no fim dos termos a data, a hora e a versão do próprio aceite. |
| Alcance da busca | A busca procura no título e no texto dos tópicos e das perguntas frequentes. |

## 8. Notificações

Não se aplica.

## 9. Mensagens

| Situação | Tipo | Mensagem |
| --- | --- | --- |
| Busca sem resultado | Aviso | Nenhum tópico encontrado. Tente outras palavras. (proposta) |
| Busca com menos de 2 caracteres | Aviso | Digite pelo menos 2 caracteres para buscar. (proposta) |
| Ajuda sem tópicos para o perfil | Aviso | Ainda não há tópicos de ajuda para o seu perfil. (proposta) |
| Sem conexão | Erro | Sem conexão com a internet. O que você digitou não foi perdido. |
| Erro inesperado | Erro | Algo deu errado. Tente de novo em alguns minutos. |

## 10. Permissões

| Ação | Psicopedagoga | Professor | Aluno | Responsável |
| --- | --- | --- | --- | --- |
| Ler os termos de uso | Sim, com ou sem login | Sim, com ou sem login | Sim, com ou sem login | Sim, com ou sem login |
| Ler os tópicos de ajuda e as perguntas frequentes (fase 5) | Sim, os do perfil | Sim, os do perfil | Sim, os do perfil | Sim, os do perfil |
| Buscar nos tópicos (fase 5) | Sim | Sim | Sim | Sim |
| Editar o texto dos termos nesta tela | Não | Não | Não | Não |

## 11. Critérios de aceite

- [ ] Dado qualquer perfil, quando escolhe "Ajuda" no menu do usuário, então a tela abre sem "Acesso negado".
- [ ] Dada a fase 1, quando o usuário abre a tela, então ela mostra os termos de uso com texto, versão e data de vigência (dd/mm/aaaa).
- [ ] Dado um usuário sem login, quando ele abre os termos de uso, então o sistema mostra o texto, a marca do sistema e o link "Entrar".
- [ ] Dado o primeiro acesso ou a nova versão dos termos, quando o usuário escolhe ler os termos, então o texto abre sem exigir login.
- [ ] Dados os termos de uso, quando o usuário os lê, então eles explicam quais dados são coletados, para quê, quem tem acesso e como pedir correção ou exclusão.
- [ ] Dados os termos de uso, quando o usuário procura como corrigir dados, então o texto diz que a correção se pede à psicopedagoga, que altera o cadastro.
- [ ] Dados os termos de uso, quando o usuário procura como excluir dados, então o texto indica o canal de proteção de dados pessoais do IFPB.
- [ ] Dada uma nova versão dos termos publicada pela equipe que opera o sistema, quando o usuário entra, então ele precisa aceitá-la e o aceite fica registrado com data, hora e versão (RG-06).
- [ ] Dada a fase 5, quando o usuário logado abre a Ajuda, então a tela mostra só os tópicos do perfil dele e as perguntas frequentes.
- [ ] Dada a Ajuda aberta por um professor, quando ele a lê, então ele não vê tópicos exclusivos dos outros perfis.
- [ ] Dada a busca nos tópicos, quando o usuário digita 2 caracteres ou mais, então o sistema filtra os tópicos ignorando maiúsculas, minúsculas e acentos (RG-20).
- [ ] Dada a busca nos tópicos, quando o usuário digita "ajuda" ou "AJUDA" ou "ajúda", então o resultado é o mesmo.
- [ ] Dada a busca sem resultado, quando o usuário busca um texto que não existe nos tópicos, então o sistema mostra a mensagem de busca vazia.
- [ ] Dada a fase 1, quando o usuário abre a tela, então ela não mostra tópicos de ajuda, perguntas frequentes nem busca.
- [ ] Dado qualquer perfil, quando tenta editar o texto dos termos na tela, então não existe opção de edição.
- [ ] Dado que a conexão caiu, quando o usuário abre a tela, então aparece "Sem conexão" ([T26 Estados do sistema](prd-t26-estados-do-sistema.md)).
- [ ] Dado qualquer perfil, quando usa a tela no computador, no celular ou só com o teclado, então todas as partes funcionam (RG-26).
- [ ] Dado que a tela ainda está carregando, quando o usuário a abre, então ela mostra os títulos e a forma das listas e tabelas, sem os dados, e um aviso de carregamento na área do conteúdo (RG-33).
