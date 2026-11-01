# Deployment com Docker, Docker Compose e Caddy

Diretrizes iniciais para executar e publicar a aplicação com Docker e Docker Compose, cobrindo os ambientes `dev` e `production`.

O documento orienta a implementação futura sem fechar antecipadamente os detalhes de infraestrutura: os Dockerfiles e os arquivos Compose são definidos durante a implementação, respeitando os fundamentos daqui.

---

## 1. Arquitetura

A stack inicial tem Caddy, frontend, backend, PostgreSQL e MinIO:

```text
Internet
   ↓
Caddy
 ├── Frontend
 └── Backend
       ├── PostgreSQL
       └── MinIO
```

O Caddy é o ponto de entrada externo, cuidando de reverse proxy, HTTPS, certificados TLS e roteamento para o frontend e o backend. O frontend é a aplicação web acessada pelos usuários, e o backend é a API com as regras de negócio e o acesso aos serviços internos. O PostgreSQL é o banco relacional e o MinIO guarda os arquivos da aplicação.

Os demais serviços permanecem na rede interna do Docker sempre que possível.

## 2. Ambientes e configuração

São dois ambientes, com a mesma estrutura geral de serviços e configurações próprias:

```text
docker-compose.dev.yml
docker-compose.prod.yml
```

A configuração vem de variáveis de ambiente. O `.env` fica fora do Git e guarda os valores reais; o `.env.example` serve de referência das variáveis necessárias para rodar o projeto. Para desenvolvimento, crie o `.env` local a partir do `.env.example` e preencha `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MINIO_ROOT_USER` e `MINIO_ROOT_PASSWORD`. Os grupos de configuração cobrem aplicação, frontend, backend, PostgreSQL, MinIO, autenticação, domínios e integrações externas.

Secrets e credenciais nunca vão para o repositório.

### Estrutura sugerida

```text
project
 ├── docs
 │   └── deployment
 │       └── docker.md
 │
 ├── frontend
 │   └── Dockerfile
 │
 ├── backend
 │   └── Dockerfile
 │
 ├── docker-compose.dev.yml
 ├── docker-compose.prod.yml
 ├── Caddyfile
 ├── .env
 ├── .env.example
 └── .gitignore
```

## 3. Rede e comunicação

Os quatro serviços de desenvolvimento compartilham a rede bridge dedicada `psif-dev`. Os containers se comunicam pelos nomes dos serviços (`frontend → backend`, `backend → postgres`), compartilhando uma rede Docker interna. Dentro de um container `localhost` é o próprio container, então serviços diferentes não podem depender dele para se encontrar. O frontend usa `API_INTERNAL_URL=http://backend:8080`, e o datasource do backend usa `postgres:5432`.

Em produção, só o Caddy recebe tráfego direto da internet:

```text
Internet → 80 / 443 → Caddy → Rede interna Docker
```

PostgreSQL, MinIO, backend e frontend não precisam de exposição pública quando não houver necessidade, e o objetivo é expor externamente apenas as portas 80 e 443, através do Caddy.

## 4. Persistência

Containers são descartáveis e volumes são persistentes. Dados importantes ficam fora do filesystem efêmero dos containers, em volumes que sobrevivem à recriação: PostgreSQL, MinIO e Caddy. No desenvolvimento, `postgres-data` persiste os dados em `/var/lib/postgresql/data` e `minio-data` persiste os objetos em `/data`. `docker compose down` remove containers e rede, mas preserva esses volumes; não use `down -v` se quiser manter dados locais.

O PostgreSQL usa armazenamento persistente e é acessado pelo backend através da rede Docker, sem exposição pública em produção a menos que haja necessidade específica. A evolução do schema é controlada pela aplicação, através da solução de migrations adotada pelo projeto.

O MinIO guarda documentos, anexos, imagens e arquivos gerados, também em armazenamento persistente e acessível pela rede interna. A console administrativa não deve ser exposta publicamente sem necessidade.

## 5. Caddy e HTTPS

O Caddy roteia cada domínio para o serviço correspondente:

```text
app.example.com → Caddy → Frontend
api.example.com → Caddy → Backend
```

Em produção ele também recebe HTTP e HTTPS, gerencia e renova os certificados, redireciona HTTP para HTTPS e encaminha as requisições aos serviços internos. Os domínios precisam apontar corretamente para o servidor antes da configuração definitiva do ambiente.

## 6. Healthchecks e inicialização

Serviços importantes como PostgreSQL, backend e MinIO têm healthchecks quando aplicável, para que a infraestrutura distinga um serviço apenas iniciado de um serviço realmente disponível:

```text
Dependência disponível → aplicação inicia → aplicação fica saudável → serviço disponível
```

Em uma instalação nova, a ordem é:

```text
PostgreSQL inicia → backend conecta → migrations são executadas → backend conclui a inicialização → aplicação disponível
```

A aplicação não depende de alteração manual no schema para iniciar corretamente.

## 7. Desenvolvimento

Pré-requisitos: Docker Engine com Docker Compose v2 e um `.env` local preenchido a partir do `.env.example`. O ambiente de dev roda com `docker-compose.dev.yml` e as variáveis do `.env`:

```bash
docker compose --env-file .env -f docker-compose.dev.yml up -d --build
```

Aqui portas adicionais podem ser expostas quando isso facilitar testes e depuração.

| Serviço | Acesso no host |
| --- | --- |
| Frontend | `http://localhost:3000` |
| Backend e OpenAPI | `http://localhost:8080` e `http://localhost:8080/v3/api-docs` |
| PostgreSQL | `localhost:5432` |
| MinIO API | `http://localhost:9000` |
| MinIO console | `http://localhost:9001` |

Os diretórios locais `backend` e `frontend` são bind mounts para refletir alterações de código. Volumes anônimos protegem `backend/target`, `frontend/node_modules` e `frontend/.next` dos mounts locais.

```bash
# parar sem remover volumes persistentes
docker compose --env-file .env -f docker-compose.dev.yml down

# reiniciar os serviços
docker compose --env-file .env -f docker-compose.dev.yml restart
```

O Compose de desenvolvimento não declara healthchecks. `depends_on` apenas ordena a inicialização do backend após o PostgreSQL, sem garantir que o banco esteja pronto para conexões. O MinIO é iniciado e persistido, mas ainda não há integração dele no backend.

## 8. Produção

Na VPS, mantenha o `.env` fora do Git com os valores reais de produção. Para subir:

```bash
docker compose --env-file .env -f docker-compose.prod.yml up -d --build
```

Em uma instalação nova, espere o backend concluir a inicialização e as migrations antes de considerar o sistema disponível.

### Primeira subida

```text
1. Preparar a VPS e instalar o Docker.
2. Configurar o DNS.
3. Clonar o repositório.
4. Criar o `.env` e configurar credenciais e secrets.
5. Subir os containers.
6. Verificar PostgreSQL e MinIO.
7. Acompanhar a inicialização do backend e confirmar as migrations.
8. Confirmar os healthchecks.
9. Verificar o Caddy e validar o HTTPS.
10. Acessar a aplicação.
```

### Atualização

```text
Atualizar código → reconstruir imagens → recriar os containers necessários → executar migrations pendentes → verificar a saúde dos serviços
```

O comando é o mesmo da subida (`up -d --build`).

## 9. Operação básica

```bash
# containers e logs
docker compose -f docker-compose.prod.yml ps
docker compose -f docker-compose.prod.yml logs -f
docker compose -f docker-compose.prod.yml logs -f backend

# reiniciar um serviço e parar o ambiente
docker compose -f docker-compose.prod.yml restart backend
docker compose -f docker-compose.prod.yml down
```

Em produção, evite comandos que removam volumes sem análise prévia, como `docker compose down -v`. Os volumes podem conter o banco de dados, arquivos, certificados e outros dados persistentes: remover um container e remover um volume são operações diferentes.

## 10. Segurança

Secrets e `.env` fora do Git, HTTPS em produção, banco não exposto publicamente, MinIO não exposto sem necessidade, apenas o Caddy como entrada externa, containers sem privilégios desnecessários e credenciais diferentes entre os ambientes.

## 11. Diferença entre dev e produção

| Item            | Dev                      | Produção                   |
| --------------- | ------------------------ | -------------------------- |
| Compose         | `docker-compose.dev.yml` | `docker-compose.prod.yml`  |
| Configuração    | `.env` local             | `.env` da VPS              |
| Domínio         | local                    | domínio real               |
| HTTPS           | opcional                 | obrigatório                |
| Portas internas | podem ser expostas       | preferencialmente privadas |
| Dados           | desenvolvimento          | reais                      |
| Debug           | permitido                | controlado                 |
| Secrets         | locais                   | fortes e exclusivos        |
| Healthchecks    | não declarados           | previstos quando aplicável |
| MinIO no backend | não integrado           | conforme implementação     |

## 12. Resumo

A infraestrutura inicial coloca o Caddy na frente do frontend e do backend, que por sua vez acessam PostgreSQL e MinIO pela rede interna. Os ambientes são representados por `docker-compose.dev.yml` e `docker-compose.prod.yml`, a configuração vem do `.env` e sua estrutura fica documentada no `.env.example`.

As regras que a infraestrutura precisa respeitar: configuração por variáveis de ambiente, secrets fora do repositório, containers descartáveis, dados persistentes em volumes, comunicação interna pela rede Docker, Caddy como entrada externa, HTTPS em produção, PostgreSQL e MinIO protegidos da internet, healthchecks nos serviços importantes, migrations executadas pela aplicação e dev e produção com estruturas semelhantes.

Em uma frase: o container pode ser recriado, a configuração vem do ambiente, os dados importantes ficam persistidos, os serviços internos permanecem protegidos, o Caddy controla a entrada pública e o Docker Compose controla a execução.
