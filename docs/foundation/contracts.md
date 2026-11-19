# Contratos da fundação

Acordos entre backend, frontend e deployment para integrar as três frentes no Compose sem conflito de nomes, portas, URLs e variáveis.

---

## 1. Serviços e portas

Cada serviço é encontrado na rede Docker pelo nome abaixo (o contrato não fixa `container_name`) e escuta na mesma porta dentro do container e, em dev, no host.

| Serviço | Papel | Porta | Publicada em dev |
| --- | --- | --- | --- |
| `caddy` | Entrada pública: reverse proxy, HTTPS e roteamento para `frontend` e `backend` | `80` e `443` | não, só roda em produção |
| `frontend` | Aplicação Next.js dos usuários, que também atua como BFF | `3000` | sim |
| `backend` | API Spring Boot com as regras de negócio | `8080` | sim |
| `postgres` | Banco relacional | `5432` | sim |
| `minio` | Armazenamento de arquivos | `9000` (API) e `9001` (console) | sim |

Em produção, só o `caddy` publica portas; os demais ficam na rede interna.

## 2. URLs

Entre containers, use o nome do serviço, nunca `localhost` (que, dentro de um container, é o próprio container):

- `frontend` → `backend`: `http://backend:8080`
- `backend` → `postgres`: `postgres:5432`
- `backend` → `minio`: `http://minio:9000`
- `caddy` → `frontend`: `http://frontend:3000`
- `caddy` → `backend`: `http://backend:8080`

URLs públicas:

- Dev: `http://localhost:3000` (aplicação) e `http://localhost:8080` (API).
- Produção: `APP_DOMAIN` → `frontend` e `API_DOMAIN` → `backend`, via `caddy` com HTTPS. Domínios reais ainda não definidos.

## 3. BFF

Em fluxos autenticados, o navegador não chama o `backend`: chama o `frontend` em caminhos relativos sob `/api` (mesma origem), e o Next.js repassa ao `backend` por `API_INTERNAL_URL`. O domínio público da API atende integrações e outros sistemas.

`/api` no `frontend` é reservado aos Route Handlers. O `backend` não usa prefixo `/api`: o BFF traduz `/api/products` para `${API_INTERNAL_URL}/products`.

## 4. Variáveis de ambiente

Nomes em UPPER_SNAKE_CASE com prefixo do grupo. `NEXT_PUBLIC_` só para o que o navegador pode ver, pois o Next.js as embute no bundle do cliente; das abaixo, só `NEXT_PUBLIC_APP_URL` é visível.

| Variável | Uso |
| --- | --- |
| `APP_ENV` | Ambiente (`dev` ou `production`); perfil do Spring no `backend` |
| `NEXT_PUBLIC_APP_URL` | URL pública da aplicação |
| `API_INTERNAL_URL` | URL do `backend` usada pelo BFF |
| `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` | Nome, usuário e senha do banco; lidas pelo `backend` diretamente no datasource |
| `MINIO_ROOT_USER`, `MINIO_ROOT_PASSWORD` | Usuário e senha do administrador do MinIO |
| `APP_DOMAIN`, `API_DOMAIN` | Domínios públicos da aplicação e da API em produção |

- `.env.example` da raiz: todas as variáveis, sem valores secretos; toda variável nova entra nele. O `backend` usa este.
- `.env.example` do `frontend`: só as variáveis que o `frontend` lê.
- `.env`: valores reais, fora do Git.
- Variáveis de autenticação ficam para o épico de autenticação.
- Variáveis de conexão do `backend` com o MinIO ficam para o épico de storage.

## 5. Healthchecks

Um serviço só está disponível quando saudável, não apenas iniciado. Ordem numa instalação nova:

```text
postgres saudável → backend conecta → migrations executadas → backend saudável → aplicação disponível
```

| Serviço | Verificação | Saudável quando |
| --- | --- | --- |
| `backend` | `GET /actuator/health` na `8080` (Spring Boot Actuator, só esse endpoint exposto) | Migrations concluídas e aceita requisições |
| `frontend` | `GET /api/health` na `3000` | Responde HTTP, sem consultar o `backend` |
| `postgres` | Conexão na `5432` | Aceita conexões |
| `minio` | `GET /minio/health/live` na `9000` | Responde |
| `caddy` | Sem healthcheck na fundação | |

## 6. OpenAPI

O `backend` publica a especificação em `/v3/api-docs` (padrão do springdoc-openapi). Em dev, o `frontend` a lê do `backend` em execução para gerar o client da API.
