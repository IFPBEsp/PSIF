# Status do PSIF

## Resumo

- **Produto:** PSIF / Inclusion of Diversity, um sistema web de apoio ao atendimento psicopedagógico do IFPB Campus Esperança. Tem quatro perfis: Psicopedagoga, Professor, Aluno e Responsável. O principal diferencial é a agenda de reuniões e atendimentos.
- **Fase atual:** a **Fundação técnica está concluída** e os **PRDs da fase 1 estão validados**. A **implementação das telas da fase 1 ainda não começou**: o único item em andamento é a definição de contratos e do modelo de dados (#43).
- **Ainda não existe nenhuma tela de negócio funcionando.** O que roda hoje é a infraestrutura: backend, frontend e BFF, Docker, Caddy, healthchecks, layout base e design system.

| Coluna do board | Itens | Pontos* |
| --- | --- | --- |
| Closed | 19 | 73 |
| In Progress | 1 | 5 |
| Todo | 2 (épicos) | – |
| Backlog | 22 | 109 |
| Open, Code Review, Blocked | 0 | 0 |
| **Total** | **44** | **187** |

\* Pontos tirados do rótulo numérico de cada issue (2, 3, 5 ou 8). Épicos não têm pontos. Pela soma de pontos, **cerca de 39% do que está no board foi concluído**.

---

## 1. O que foi feito no repositório

Linha do tempo do repositório, de 19/09 a 25/11/2026: 142 commits e PRs de #3 a #65.

### Setembro: início e documentação
- O repositório foi criado com templates de issue, documentação inicial, arquitetura de backend e frontend, `docker.md` e a convenção de Conventional Commits.

### Outubro: SDD, contratos, PRDs e primeiras bases
- **Fluxo com SDD (#2):** OpenSpec inicializado, roteamento `AGENTS.md`, skills dos agentes e convenções (`code`, `git`, `naming` e `writing`).
- **Constituição:** `docs/constitution/mission.md` com a missão, o problema, a solução, os usuários e os critérios de sucesso.
- **Contratos da fundação (#5):** serviços e portas, URLs internas e públicas, BFF sob `/api`, variáveis de ambiente, healthchecks e OpenAPI.
- **PRDs (#21):** um índice com as regras transversais (RG-01 a RG-33, glossário, situações, notificações, navegação, fases e matriz de permissões) e 26 PRDs de tela (T01 a T26).
- **Backend base (#6, #7, #8, #9):** Java 21 e Spring Boot 4.1 (WebMVC, Data JPA, Validation, Actuator), PostgreSQL e Liquibase. Tem tratamento global de erros com `ProblemDetail`, OpenAPI com springdoc e testes de integração com Testcontainers.
- **Frontend base (#10):** Next.js 16, React 19, TypeScript, Tailwind 4 e shadcn/ui, organizado por features e com testes em Vitest.

### Novembro: infraestrutura, layout e design system
- **Skill de design system do PSIF (#29):** tokens, tipografia Figtree, ícones e símbolo, regras de interface e verificadores.
- **BFF (#13):** client server-side para o backend, mapeamento de erros e pasta de Route Handlers.
- **Client OpenAPI (#12):** geração com Orval, ligada ao `backendFetch` por um mutator e usada só no servidor.
- **Layout base (#11):** sidebar recolhível, gaveta mobile (Drawer), header, breadcrumbs, tema claro, escuro ou do sistema, página "Meu perfil" com seletor de tema, estados globais (carregando, erro, não encontrado, vazio) e link para pular ao conteúdo.
- **Docker de desenvolvimento (#14) e de produção (#15):** imagens de produção, rede privada e volumes persistentes. Os serviços são `frontend`, `backend`, `postgres` e `minio`.
- **Caddy (#16):** entrada pública com HTTPS em produção.
- **Healthchecks (#17):** Actuator no backend, rota `/api/health` no frontend e ordem de inicialização por saúde nos composes.
- **pnpm (#41):** passou a ser o único gerenciador de pacotes do frontend (Corepack e cache no build).
- **Validação dos PRDs da fase 1 (#23):** ajustes em T01, T05 e T11 depois da revisão.

### O que ainda não existe no código
- Nenhum domínio de negócio no backend: só `shared/config` e `shared/error`. O changelog do Liquibase existe, mas ainda não tem tabelas de negócio.
- No frontend não há features de negócio, só o layout e a página de perfil. O client gerado ainda está vazio, porque só tem o arquivo de índice dos schemas.
- Ainda não há autenticação, autorização, storage no MinIO nem notificações.

---

## 2. Board: o que já foi feito (Closed, 19 itens)

| # | Item | Pts | Responsável | Fechada em |
| --- | --- | --- | --- | --- |
| 2 | Inicia configuração do repo para trabalhar com SDD | 5 | jefter-dev, MeloWillian | 10/10 |
| 4 | **Épico: Fundação do projeto** (14/14 sub-issues) | – | – | 24/11 |
| 5 | Definir contratos da fundação do projeto | 2 | Dario-Arthur | 13/10 |
| 6 | Criar estrutura inicial do backend | 3 | Dario-Arthur | 20/10 |
| 7 | Configurar persistência e migrations | 3 | Dario-Arthur | 31/10 |
| 8 | Implementar tratamento global de erros | 3 | JoseArthurAlmeida | 31/10 |
| 9 | Configurar documentação OpenAPI | 2 | Dario-Arthur | 24/10 |
| 10 | Criar estrutura inicial do frontend | 3 | euAllanDev | 28/10 |
| 11 | Criar layout base da aplicação | 8 | Dario-Arthur | 15/11 |
| 12 | Configurar geração do client OpenAPI | 2 | Brunafern | 14/11 |
| 13 | Criar estrutura base do BFF | 3 | JoseArthurAlmeida | 06/11 |
| 14 | Criar ambiente Docker de desenvolvimento | 5 | euAllanDev | 11/11 |
| 15 | Criar ambiente Docker de produção | 3 | JoseArthurAlmeida | 15/11 |
| 16 | Configurar proxy reverso com Caddy | 2 | JoseArthurAlmeida | 21/11 |
| 17 | Adicionar healthchecks dos serviços | 2 | Brunafern | 23/11 |
| 21 | Criar a primeira versão dos PRDs das telas | 8 | jefter-dev, MeloWillian | 17/10 |
| 23 | Validar os PRDs da fase 1 (Base) | 8 | euAllanDev | 24/11 |
| 29 | Criar skill de design system do PSIF | 8 | Brunafern | 03/11 |
| 41 | Padronizar o frontend para usar somente pnpm | 3 | JoseArthurAlmeida | 24/11 |

---

## 3. Board: em andamento

### In Progress (1)
| # | Item | Pts | Responsável | Épico |
| --- | --- | --- | --- | --- |
| 43 | Definir contratos e modelo de dados da fase 1 | 5 | Dario-Arthur | #42 Fase 1 |

### Todo (2 épicos)
| # | Épico | Progresso |
| --- | --- | --- |
| 22 | Épico: Validação dos PRDs | 1/5 sub-issues (só a fase 1 validada) |
| 42 | Épico: Fase 1, telas base | 0/19 sub-issues |

---

## 4. Board: o que ficou para depois (Backlog, 22 itens)

Nenhum item do backlog tem responsável.

### 4.1 Validação dos PRDs restantes (épico #22), 15 pts
| # | Item | Pts |
| --- | --- | --- |
| 24 | Validar os PRDs da fase 2 (Agenda) | 5 |
| 25 | Validar os PRDs da fase 3 (Acompanhamento) | 5 |
| 26 | Validar o PRD da fase 4 (Comunicação) | 2 |
| 27 | Validar os PRDs da fase 5 (Complementos) | 3 |

### 4.2 Fase 1, telas base (épico #42), 94 pts no backlog

**Bases técnicas da fase 1**
| # | Item | Pts |
| --- | --- | --- |
| 44 | Implementar identidade, sessão e autorização | 8 |
| 45 | Criar padrão de cadastro no backend, com Cursos (T20) | 5 |
| 46 | Criar kit de lista e formulário no frontend, com Cursos (T20) | 8 |
| 47 | Criar casca autenticada e estados do sistema (T26) | 5 |
| 48 | Criar base de arquivos: foto e anexos | 5 |

**Telas**
| # | Item | Pts |
| --- | --- | --- |
| 49 | T22 Dificuldades | 3 |
| 50 | T19 Turmas | 5 |
| 51 | T21 Professores | 5 |
| 52 | T01 Acesso ao sistema e T05 Termos de uso | 5 |
| 53 | T04 Minha conta | 3 |
| 54 | T23 Equipe | 3 |
| 55 | T06 Lista de alunos | 5 |
| 56 | T07 Cadastro de aluno: dados, turma, dificuldades e acesso | 8 |
| 57 | T07 Cadastro de aluno: responsáveis e maioridade | 8 |
| 58 | T03 Notificações | 5 |
| 59 | T08 Perfil do aluno | 5 |
| 60 | T11 Características e orientações | 5 |
| 61 | T02 Início | 3 |

Contando o #43, que está em andamento, o épico da fase 1 soma **99 pontos**, com **0 concluídos**.

---

## 5. Cobertura dos PRDs no board

Todas as fases dos PRDs (`docs/prds/prd-indice.md`, seção 9) estão no board pelo **épico #22 Validação dos PRDs**, que tem uma issue de validação por fase. A implementação, por enquanto, só tem épico na fase 1 (#42).

| Fase | Foco | Telas | Validação (épico #22) | Implementação |
| --- | --- | --- | --- | --- |
| 1 | Base | T01, T02, T03, T04, T05 (termos), T06, T07, T08, T11, T19, T20, T21, T22, T23, T26 | #23, Closed | Épico #42 (19 issues) |
| 2 | Agenda | T13 Agenda, T14 Evento, T15 Pedidos de agendamento | #24, Backlog | – |
| 3 | Acompanhamento | T09 Dados de saúde, T10 Acompanhamentos, T12 Planejamento semanal, T16 Atividades adaptadas, T17 Observações dos professores | #25, Backlog | – |
| 4 | Comunicação | T18 Informações para a psicopedagoga | #26, Backlog | – |
| 5 | Complementos | T05 Ajuda, T24 Formulários, T25 Busca no acervo, recuperação de senha por e-mail (T01) | #27, Backlog | – |

---

## 6. Observações

- O épico **#4 Fundação** está fechado com 14/14 sub-issues. O **#2 (SDD)**, o **#21 (PRDs)** e o **#29 (design system)** não pertencem a nenhum épico.
