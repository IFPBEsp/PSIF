# Apresentação da Fundação do PSIF

## Parte 0 – O produto e o board

### O produto
- **Problema:** o IFPB Campus Esperança não tem sistema para a área psicopedagógica. A psicopedagoga usa a aba "Atendimentos" do SUAP, e relatórios, laudos e planejamentos ficam no papel. Professores não recebem orientações sobre os alunos, e alunos e responsáveis não têm onde acompanhar o atendimento nem pedir reuniões.
- **Solução:** o PSIF, um sistema web único que funciona no computador e no celular e tem uma visão por perfil. O principal diferencial é a **agenda de reuniões e atendimentos**.
- **Perfis:** Psicopedagoga, Professor, Aluno e Responsável.
- **Sucesso:** acabar com os registros em papel, fazer todo pedido de reunião passar pela agenda e fazer os professores consultarem as orientações no sistema.
- **Entrega em 5 fases:** Base, Agenda, Acompanhamento, Comunicação e Complementos, somando 26 telas (T01 a T26).

### O board (PSIF BOARD)
- **Colunas:** Open, Backlog, Todo, In Progress, Code Review, Blocked e Closed.
- **Épicos:**
  - #4 Fundação: concluído, 14 de 14.
  - #22 Validação dos PRDs: 1 de 5, só a fase 1 validada.
  - #42 Fase 1, telas base: 0 de 19.
- **Situação:** 44 itens. São 19 em Closed, 1 em In Progress (#43), 2 épicos em Todo e 22 em Backlog. Pela soma dos pontos, cerca de 39% está concluído.
- **Como o time trabalha:** cada issue tem pontos (2, 3, 5 ou 8), um tipo (feature, chore, docs ou epic) e um PR ligado.

---

## Parte 1 – Base de SDD e documentação
- **#2 Configuração do repositório para SDD:**
  - **OpenSpec** (`openspec/config.yaml`): fluxo spec-driven com regras para proposal, design e specs. Exige Definition of Ready, não-objetivos, decisões com trade-offs e riscos com mitigação.
  - **Roteamento por `AGENTS.md`:** o `AGENTS.md` da raiz aponta para `docs/AGENTS.md`, que diz o que ler em cada tarefa. O agente lê só o que é relevante.
  - **Skills dos agentes** em `.agents/skills`, ligadas a `.claude/skills` por symlink: OpenSpec, Spring Boot, Javadoc, shadcn, TanStack Query, Zod e boas práticas de React.
- **Constituição:** `docs/constitution/mission.md`, com missão, problema, solução, usuários e critérios de sucesso.
- **Convenções** (`docs/conventions/`): `git.md` (Conventional Commits e branches), `naming.md`, `code.md` e `writing.md`.
- **Arquitetura documentada:** `docs/backend/` e `docs/frontend/` (`architecture-and-stack.md`), mais `docs/deployment/docker.md`.
- **#21 e #23 PRDs como fonte da verdade:** o índice tem regras transversais, glossário, situações, notificações, matriz de permissões e as 5 fases. São 26 PRDs de tela, e os da fase 1 já foram validados.

---

## Parte 2 – Contratos e Backend
- **#5 Contratos da fundação:** serviços, portas, URLs, regra do BFF e variáveis de ambiente.
- **#6 Estrutura inicial do backend:** Java 21 e Spring Boot 4.1, organizado por domínio.
- **#7 Persistência e migrations:** PostgreSQL, JPA e Liquibase, com o banco só validado (`ddl-auto=validate`).
- **#8 Tratamento global de erros:** `ProblemDetail` e exceções padronizadas.
- **#9 Documentação OpenAPI:** Swagger ligado em dev e desligado em produção.

---

## Parte 3 – Skill de design system do PSIF (#29)
- **Prioridades do produto:** o sigilo do aluno vem primeiro, e tudo funciona a partir de 320px de largura.
- **Fundamentos** (`foundations/`): filosofia visual, princípios de UX e acessibilidade.
- **Tokens e assets:** `tokens.css`, fonte Figtree, sprite de ícones e o símbolo do PSIF.
- **Componentes e padrões:** entradas e ações, listas e calendário, navegação, pessoas e situações, superfícies e sobreposições, além de padrões de tela e de UX.
- **Regras para IA** (`ai-rules/`): checklist de anti-padrões, integração com Tailwind e engenharia de prompt.
- **Verificadores:** scripts que conferem se o resultado segue a skill.

---

## Parte 4 – Frontend e BFF
- **#10 Estrutura inicial do frontend:** Next.js, React, TypeScript, Tailwind e shadcn/ui.
- **#41 Padronizar o frontend para usar somente pnpm.**
- **#13 Estrutura base do BFF:** `backendFetch` só no servidor, com timeout e mapeamento de erros.
- **#12 Geração do client OpenAPI:** Orval gerando um client tipado ligado ao BFF.
- **#11 Layout base da aplicação:** a skill de design system aplicada na prática. Inclui sidebar, gaveta no mobile, breadcrumbs, temas e estados globais.

---

## Parte 5 – Infra e Deploy
- **#14 Docker de desenvolvimento:** Postgres, MinIO, backend e frontend.
- **#15 Docker de produção:** rede privada e volumes persistentes.
- **#16 Proxy reverso com Caddy:** entrada pública única, com HTTPS e domínios.
- **#17 Healthchecks dos serviços:** Actuator, `/api/health` e ordem de inicialização por saúde.
