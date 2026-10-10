# AGENTS: docs

Documentação de referência do projeto. Leia só o arquivo que cobre a tarefa em mãos.

## O que vive nessa pasta

- `backend/architecture.md`: arquitetura do backend (Java, Spring Boot e PostgreSQL em monólito modular com Clean Architecture leve): organização por domínio, autenticação, banco, contratos, erros, API REST, integrações, storage, jobs e ordem de implementação.

- `frontend/architecture.md`: arquitetura do frontend (Next.js com App Router como BFF, React, TypeScript, Tailwind e shadcn/ui): estrutura por feature, autenticação e autorização, Server/Client Components, Server Actions, estado, formulários, API client gerado por OpenAPI, listagens e segurança.

- `conventions/git.md`: padrão de commits (Conventional Commits) e de nomes de branches.

- `deployment/docker.md`: execução e publicação com Docker, Docker Compose e Caddy nos ambientes `dev` e `production`: rede, persistência, HTTPS, healthchecks e operação.
