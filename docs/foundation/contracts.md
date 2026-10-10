# Contratos da fundação

Fonte única dos contratos técnicos compartilhados entre backend, frontend e deployment.

---

## 1. Serviços

Os nomes dos serviços na rede interna do Docker:

| Serviço | Papel | Tecnologia |
| --- | --- | --- |
| `caddy` | Reverse proxy e terminação TLS/HTTPS | Caddy |
| `frontend` | Aplicação web e BFF | Next.js (App Router) |
| `backend` | API REST e regras de negócio | Spring Boot |
| `postgres` | Banco de dados relacional | PostgreSQL |
| `minio` | Armazenamento de arquivos e objetos | MinIO |

O contrato fixa o nome dos serviços para resolução de DNS interno no Docker. Nomes específicos de container (`container_name`) não são fixados por este contrato.

## 2. Portas

### Desenvolvimento

Portas publicadas no host para depuração e ferramentas locais:

| Serviço | Porta interna | Porta no host | Finalidade |
| --- | --- | --- | --- |
| `frontend` | 3000 | 3000 | Acesso local à aplicação web |
| `backend` | 8080 | 8080 | Depuração da API e geração de client OpenAPI |
| `postgres` | 5432 | 5432 | Acesso via clientes SQL externos |
| `minio` | 9000 | 9000 | API S3 para testes locais |
| `minio` | 9001 | 9001 | Console web administrativa |

### Produção

Em produção, os serviços internos não são expostos diretamente. Apenas o `caddy` publica portas para a internet:

| Serviço | Porta externa | Protocolo |
| --- | --- | --- |
| `caddy` | 80 | HTTP (redirecionamento para HTTPS) |
| `caddy` | 443 | HTTPS |

## 3. URLs e comunicação

### Comunicação interna (rede Docker)

Containers comunicam-se pelos nomes dos serviços, sem depender de `localhost`:

- Frontend (BFF) para Backend: `http://backend:8080`
- Backend para PostgreSQL: host `postgres` na porta `5432`
- Backend para MinIO: host `minio` na porta `9000`
- Caddy para Frontend: host `frontend` na porta `3000`
- Caddy para Backend: host `backend` na porta `8080`

### URLs públicas

- Desenvolvimento: `http://localhost:3000`
- Produção (domínios de referência):
  - Frontend: `https://app.example.com`
  - Backend: `https://api.example.com`

## 4. Variáveis de ambiente

As variáveis essenciais da fundação ficam registradas no arquivo `.env.example` na raiz do projeto. O `.env` real nunca é versionado e permanece no `.gitignore`.

Estrutura inicial:

```env
APP_ENV=dev

NEXT_PUBLIC_APP_URL=http://localhost:3000
API_INTERNAL_URL=http://backend:8080

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

MINIO_ROOT_USER=
MINIO_ROOT_PASSWORD=
```

Regras de variáveis:
- Nomes em `UPPER_SNAKE_CASE` com prefixo do grupo.
- O prefixo `NEXT_PUBLIC_` é exclusivo para variáveis expostas ao navegador.
- O backend consome as variáveis `POSTGRES_*` diretamente no datasource.
- Variáveis de autenticação ficam para o épico de autenticação.

## 5. Healthchecks

Cada serviço responde por sua própria verificação de saúde. A infraestrutura usa esses critérios para orquestrar a inicialização dependente:

| Serviço | Endpoint / Critério | Significado de saudável |
| --- | --- | --- |
| `backend` | `/actuator/health` (porta 8080) | Aplicação iniciada, migrations concluídas e pronta para receber requisições |
| `frontend` | `/api/health` (porta 3000) | Servidor Next.js respondendo requisições HTTP |
| `postgres` | Conexão TCP ativa | Servidor PostgreSQL aceitando conexões de clientes |
| `minio` | `/minio/health/live` (porta 9000) | Servidor MinIO ativo |
| `caddy` | Sem healthcheck próprio | Monitoramento a definir pelo time |

Ordem de inicialização:
```text
postgres saudável -> backend conecta e executa migrations -> backend saudável -> aplicação disponível
```

A sintaxe exata dos comandos de healthcheck no Docker Compose é definida na issue #14.

## 6. OpenAPI

- Endpoint: `/v3/api-docs`
- Descrição: caminho padrão do springdoc-openapi onde o backend publica o schema OpenAPI em JSON.
- Consumo: utilizado pelo frontend via script `npm run api:generate` com Orval para gerar schemas, tipos TypeScript e clients de requisição.
