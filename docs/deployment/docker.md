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

Em produção, os demais serviços ficam apenas na rede interna e o Caddy é o único com portas publicadas. O `Caddyfile` fica na raiz do repositório e é montado no container como somente leitura, então o roteamento muda sem reconstruir imagem (basta reiniciar o serviço `caddy`).

## 2. Ambientes e configuração

São dois ambientes, com a mesma estrutura geral de serviços e configurações próprias:

```text
docker-compose.dev.yml
docker-compose.prod.yml
```

A configuração vem de variáveis de ambiente. O `.env` fica fora do Git e guarda os valores reais; o `.env.example` serve de referência das variáveis necessárias para rodar o projeto. Os grupos de configuração cobrem aplicação, frontend, backend, PostgreSQL, MinIO, autenticação, domínios e integrações externas.

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

Os containers se comunicam pelos nomes dos serviços (`backend → postgres`, `backend → minio`, `caddy → frontend`, `caddy → backend`), compartilhando uma rede Docker interna. Dentro de um container `localhost` é o próprio container, então serviços diferentes não podem depender dele para se encontrar.

Em produção, só o Caddy recebe tráfego direto da internet:

```text
Internet → 80 / 443 → Caddy → Rede interna Docker
```

As portas publicadas são apenas estas, e cada uma tem um papel:

```text
80/tcp   redirect para HTTPS e validação do certificado
443/tcp  HTTPS
443/udp  HTTP/3
```

O Caddy encontra `frontend` e `backend` pelo nome do serviço na rede `psif-prod`. PostgreSQL, MinIO, backend e frontend não publicam portas em produção e ficam acessíveis apenas pela rede interna.

## 4. Persistência

Containers são descartáveis e volumes são persistentes. Dados importantes ficam fora do filesystem efêmero dos containers, em volumes que sobrevivem à recriação: PostgreSQL, MinIO e Caddy.

O PostgreSQL usa armazenamento persistente e é acessado pelo backend através da rede Docker, sem exposição pública em produção a menos que haja necessidade específica. A evolução do schema é controlada pela aplicação, através da solução de migrations adotada pelo projeto.

O MinIO guarda documentos, anexos, imagens e arquivos gerados, também em armazenamento persistente e acessível pela rede interna. A console administrativa não deve ser exposta publicamente sem necessidade.

## 5. Caddy e HTTPS

O Caddy roteia cada domínio para o serviço correspondente, e o roteamento fica no `Caddyfile` da raiz do repositório:

```caddyfile
{$APP_DOMAIN} {
	reverse_proxy frontend:3000
}

{$API_DOMAIN} {
	reverse_proxy backend:8080
}
```

`APP_DOMAIN` e `API_DOMAIN` vêm do `.env` e são obrigatórios: sem eles o compose falha em vez de subir com rota quebrada. Os domínios precisam apontar para o servidor antes da primeira subida, senão a emissão do certificado falha.

Em produção o Caddy recebe HTTP e HTTPS, emite e renova os certificados e redireciona HTTP para HTTPS (308). Declarar o endereço com `http://` no `Caddyfile` desativa o redirect automático para aquele domínio, então os blocos usam apenas o domínio.

Certificados e os dados da conta usada na emissão ficam no volume `caddy-data` (`/data`), e a configuração salva automaticamente pelo Caddy fica no volume `caddy-config` (`/config`). Recriar o container reaproveita o certificado, sem nova emissão. Perder o `caddy-data` força uma nova emissão, e emissões repetidas podem atingir o limite de requisições do Let's Encrypt. A renovação também é automática, sem tarefa agendada no servidor.

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

Dev e produção usam os mesmos healthchecks, com as verificações de `docs/foundation/contracts.md`, seção 5:

| Serviço | Comando no container |
| --- | --- |
| `postgres` | `pg_isready` com o usuário e o banco do `.env` |
| `minio` | `curl` em `/minio/health/live` |
| `backend` | `wget` em `/actuator/health`, esperando `"status":"UP"` |
| `frontend` | `wget` em `/api/health`, esperando `"status":"UP"` |

O `backend` sobe com `depends_on` em `condition: service_healthy` sobre o `postgres`, e o `frontend` de produção espera o `backend` saudável. Não há espera própria no container do `backend`: a ordem fica com o Compose. Como o Liquibase roda antes de a aplicação ficar pronta, o `/actuator/health` só responde depois das migrations, e o `backend` só fica saudável depois delas. `docker compose ps` mostra o estado de saúde de cada serviço.

## 7. Desenvolvimento

O ambiente de dev roda com `docker-compose.dev.yml` e as variáveis do `.env`:

```bash
docker compose --env-file .env -f docker-compose.dev.yml up -d --build
```

Aqui portas adicionais podem ser expostas quando isso facilitar testes e depuração.

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
4. Criar o `.env` com credenciais e secrets, `APP_ENV=production`, `APP_DOMAIN` e `API_DOMAIN` (a subida falha sem esses três) e `NEXT_PUBLIC_APP_URL=https://<APP_DOMAIN>`. Esta última tem valor padrão de dev e não barra a subida: se não for trocada, os links e redirects do Next apontam para `localhost`.
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

Como isso aparece na configuração:

- Só o Caddy publica portas, com as três portas descritas em Rede e comunicação.
- O `Caddyfile` é versionado e montado no container como somente leitura.
- O volume `caddy-data` guarda as chaves privadas dos certificados e a chave da conta de emissão: fica fora do repositório e não deve ser copiado nem exposto.
- Todos os serviços, incluindo o Caddy, rodam com `no-new-privileges`.

## 11. Diferença entre dev e produção

| Item              | Dev                      | Produção                   |
| ----------------- | ------------------------ | -------------------------- |
| Compose           | `docker-compose.dev.yml` | `docker-compose.prod.yml`  |
| Configuração      | `.env` local             | `.env` da VPS              |
| Domínio           | local                    | domínio real               |
| HTTPS             | opcional                 | obrigatório                |
| Portas publicadas | podem ser expostas       | só 80 e 443 (Caddy)        |
| Dados             | desenvolvimento          | reais                      |
| Debug             | permitido                | controlado                 |
| Secrets           | locais                   | fortes e exclusivos        |

## 12. Resumo

A infraestrutura inicial coloca o Caddy na frente do frontend e do backend, que por sua vez acessam PostgreSQL e MinIO pela rede interna. Os ambientes são representados por `docker-compose.dev.yml` e `docker-compose.prod.yml`, a configuração vem do `.env` e sua estrutura fica documentada no `.env.example`.

As regras que a infraestrutura precisa respeitar: configuração por variáveis de ambiente, secrets fora do repositório, containers descartáveis, dados persistentes em volumes, comunicação interna pela rede Docker, Caddy como entrada externa, HTTPS em produção, PostgreSQL e MinIO protegidos da internet, healthchecks nos serviços importantes, migrations executadas pela aplicação e dev e produção com estruturas semelhantes.

Em uma frase: o container pode ser recriado, a configuração vem do ambiente, os dados importantes ficam persistidos, os serviços internos permanecem protegidos, o Caddy controla a entrada pública e o Docker Compose controla a execução.
