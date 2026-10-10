# Proposal

## Why

As frentes de backend, frontend e deployment iniciam em paralelo na fundação do projeto. Sem um acordo prévio sobre nomes de serviços, portas, URLs internas e variáveis de ambiente, cada frente define nomes isolados e a integração quebra quando os serviços se encontram no Docker Compose. Definir e centralizar esses contratos antes da implementação garante alinhamento imediato e destrava as frentes técnicas dependentes (issues #6, #10 e #14).

## What Changes

- Cria o documento único de contratos técnicos da fundação em `docs/foundation/contracts.md`.
- Adiciona a entrada do documento de contratos no índice geral em `docs/AGENTS.md`.
- Corrige o exemplo de `API_INTERNAL_URL` em `docs/frontend/architecture-and-stack.md` para refletir a comunicação interna no Docker Compose (`http://backend:8080`).
- Define o template de variáveis de ambiente em `.env.example` na raiz, cobrindo aplicação, frontend, backend, PostgreSQL e MinIO sem segredos.
- Garante o `.env` ignorado no `.gitignore`.
- Formaliza as convenções de serviços, portas em dev e produção, healthchecks e caminho do OpenAPI (`/v3/api-docs`).

### Fora de escopo

- Código de backend, frontend ou infraestrutura executável (Dockerfiles, Compose ou Caddyfile).
- Comandos exatos de healthcheck no Docker Compose (escopo da issue #14).
- Variáveis e regras de autenticação, autorização e tokens (escopo do épico de autenticação).
- Variáveis de integração do MinIO no backend (escopo do épico de storage).
- Criação de domínios ou regras de negócio.

## Capabilities

### New Capabilities

Nenhuma. Esta mudança é restrita a documentação técnica de contratos e definição de variáveis de ambiente da fundação, sem introduzir comportamentos funcionais de sistema. O arquivo `.openspec.yaml` declara `skip_specs: true`.

### Modified Capabilities

Nenhuma. Não há especificações de capacidades funcionais existentes sendo modificadas.

## Impact

- Documentação: novo arquivo `docs/foundation/contracts.md`, atualização do índice `docs/AGENTS.md` e ajuste pontual em `docs/frontend/architecture-and-stack.md`.
- Repositório: criação de `.env.example` na raiz e conferência de `.gitignore`.
- Trilhas dependentes: desbloqueia a implementação das issues #6 (base backend), #10 (base frontend) e #14 (Docker dev).
