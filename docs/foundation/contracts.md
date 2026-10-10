# Contratos da fundação

Contratos técnicos compartilhados entre backend, frontend e deployment para a fundação do projeto.

---

## 1. Serviços

Os serviços da stack inicial e seus papéis estão definidos em `docs/deployment/docker.md` (seção 1 - Arquitetura).

O contrato fixa os nomes dos serviços para resolução de DNS interno no Docker, sem fixar `container_name`.

## 2. Portas

As regras de portas em produção (80 e 443 expostas apenas pelo Caddy) estão em `docs/deployment/docker.md` (seção 3 - Rede e comunicação).

Em `docs/deployment/docker.md` (seção 7 - Desenvolvimento) é permitido expor portas adicionais em desenvolvimento sem listar quais. Este contrato fixa a lista publicada no host:

- `frontend`: `3000`
- `backend`: `8080`
- `postgres`: `5432`
- `minio`: `9000` (API) e `9001` (console)

## 3. URLs e comunicação

A comunicação interna pelos nomes dos serviços está em `docs/deployment/docker.md` (seção 3 - Rede e comunicação). Os domínios de referência para produção estão em `docs/deployment/docker.md` (seção 5 - Caddy e HTTPS).

- Frontend (BFF) para backend: `API_INTERNAL_URL=http://backend:8080` (ver `docs/frontend/architecture-and-stack.md`, seção 21 - Segurança).
- URL pública em desenvolvimento: `NEXT_PUBLIC_APP_URL=http://localhost:3000`.

## 4. Variáveis de ambiente

A lista e estrutura das variáveis da fundação estão no arquivo `.env.example` na raiz do projeto.

As regras de nomenclatura e o uso de `NEXT_PUBLIC_` seguem `docs/conventions/naming.md` (seção Ambiente).

O backend lê as variáveis `POSTGRES_*` diretamente no datasource. Variáveis de autenticação ficam para o épico de autenticação.

## 5. Healthchecks

A ordem de inicialização entre serviços está em `docs/deployment/docker.md` (seção 6 - Healthchecks e inicialização). Os comandos exatos no Compose ficam para a issue #14.

Endpoints e significado de saudável:

- `backend`: `/actuator/health` (porta 8080). Saudável quando migrations foram concluídas e a aplicação aceita requisições.
- `frontend`: `/api/health` (porta 3000). Saudável quando o servidor web responde requisições HTTP.
- `postgres`: porta 5432. Saudável quando aceita conexões TCP ativas.
- `minio`: `/minio/health/live` (porta 9000). Saudável quando o serviço responde ativo.
- `caddy`: sem healthcheck próprio inicial (a definir pelo time).

## 6. OpenAPI

A integração do Orval com OpenAPI está em `docs/frontend/architecture-and-stack.md` (seção 12 - API client).

O backend publica a especificação em `/v3/api-docs` (padrão springdoc-openapi, issue #9), de onde o frontend a consome.
