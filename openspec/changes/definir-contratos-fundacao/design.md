# Design

## Context

O projeto esta estruturando a base tecnica inicial em paralelo, dividida nas trilhas de backend, frontend e deployment. Conforme descrito em `proposal.md`, as equipes precisam de alinhamento previo sobre nomes de servicos, portas, comunicacao interna e variaveis de ambiente antes de escrever codigo ou arquivos Compose.

Este design orienta a criacao do documento de contratos em `docs/foundation/contracts.md` como fonte unica da verdade, a atualizacao dos indices em `docs/AGENTS.md`, a correcao em `docs/frontend/architecture-and-stack.md` e a criacao do template `.env.example`.

## Goals / Non-Goals

**Goals:**
- Definir a localizacao e a estrutura de `docs/foundation/contracts.md` como referencia centralizada.
- Atualizar o roteamento de documentacao em `docs/AGENTS.md`.
- Alinhar a documentacao de frontend corrigindo o valor de `API_INTERNAL_URL` no exemplo do documento.
- Definir as variaveis obrigatorias do arquivo `.env.example` na raiz do repositorio.
- Formalizar as regras de portas para dev e producao, URLs de rede interna, semantica de healthchecks e caminho do OpenAPI.

**Non-Goals:**
- Escrever codigo em Java, TypeScript ou arquivos executaveis do Docker e Compose.
- Implementar as diretivas completas de healthcheck em arquivos YAML do Docker Compose (escopo da issue #14).
- Definir credenciais, variaveis ou regras de autenticacao e tokens (escopo do epico de autenticacao).
- Estabelecer variaveis de storage do backend para integracao com o MinIO (escopo do epico de storage).

## Decisions

### 1. Documento central em `docs/foundation/contracts.md` e catalogacao em `docs/AGENTS.md`
- **Racional:** Segue o padrao do projeto onde a documentacao tecnica fica agrupada em subpastas tematicas em kebab-case em ingles (`constitution/`, `backend/`, `frontend/`, `deployment/`, `conventions/`). A trilha do epico #4 classifica esta etapa como `foundation/project`.
- **Alternativa rejeitada:** Colocar `contracts.md` solto na raiz de `docs/` ou dentro de `docs/conventions/`. A raiz viola a consistencia dos indices e `conventions/` trata de padroes de escrita e codigo, nao contratos entre servicos.

### 2. `API_INTERNAL_URL=http://backend:8080` no Compose e correcao no documento de frontend
- **Racional:** Entre containers na rede interna do Docker, a comunicacao ocorre via HTTP direto pelo nome do servico e sua respectiva porta interna. Na linha 508 de `docs/frontend/architecture-and-stack.md`, o exemplo cita `https://api.example.com`, o que gera ambiguidade entre chamada externa e chamada interna via rede Docker.
- **Alternativa rejeitada:** Manter a referencia de domínio externo no exemplo, induzindo o BFF a tentar sair pela internet para acessar a propria API na mesma infraestrutura Compose.

### 3. Publicacao de portas no host em dev e exposicao restrita em producao
- **Racional:** Em desenvolvimento, desenvolvedores necessitam inspecionar o PostgreSQL (porta 5432) com clientes SQL externos, acessar a console do MinIO (porta 9001), testar a API do MinIO (porta 9000), depurar a API do backend (porta 8080) e acessar o frontend (porta 3000). A porta 8080 tambem e necessaria para o Orval gerar clients no host. Em producao, a superficie de ataque permanece reduzida, expondo somente as portas 80 e 443 gerenciadas pelo Caddy.
- **Alternativa rejeitada:** Expor apenas o Caddy em desenvolvimento. Isso exigiria configuracoes complexas de proxy reverso local para conexoes de banco de dados e console administrativa.

### 4. Fixacao de nomes de servicos no contrato, sem amarrar `container_name`
- **Racional:** A resolucao de DNS na rede interna do Compose opera sobre os nomes dos servicos (`caddy`, `frontend`, `backend`, `postgres`, `minio`). O atributo `container_name` e um detalhe de conveniencia operacional e nao deve ser imposto como contrato de integracao.
- **Alternativa rejeitada:** Obrigar nomes especificos de containers no contrato, engessando o arquivo Compose sem necessidade arquitetural.

### 5. Backend lendo `POSTGRES_*` diretamente no `.env.example`
- **Racional:** Centraliza as definicoes de banco em tres variaveis unicas (`POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`). O backend Spring Boot mapeia essas variaveis na configuracao do datasource sem duplicacao de campos no `.env.example`.
- **Alternativa rejeitada:** Incluir variaveis do padrao Spring Boot (`SPRING_DATASOURCE_*`) no `.env.example`, gerando redundancia com as variaveis consumidas pela imagem do Postgres.

### 6. Contrato de healthchecks por endpoint e significado semantico
- **Racional:** O documento de contratos estabelece a responsabilidade de saude de cada servico: backend responde 200 em `/actuator/health`, frontend responde 200 em `/api/health`, Postgres aceita conexoes TCP ativas, e MinIO responde ao endpoint de liveness. Caddy nao tera healthcheck proprio inicialmente. A traducao para comandos do Compose (`test: [...]`) fica para a issue #14.
- **Alternativa rejeitada:** Especificar blocos YAML completos de healthcheck no documento de contratos, antecipando decisoes operacionais de Docker Compose.

### 7. Caminho do OpenAPI definido em `/v3/api-docs`
- **Racional:** E o caminho padrao gerado pelo springdoc-openapi (issue #9), compativel com a configuracao do Orval no frontend (`npm run api:generate`).
- **Alternativa rejeitada:** Customizar o endpoint para `/api-docs` ou similar no Spring Boot, exigindo ajustes desnecessarios de configuracao.

## Risks / Trade-offs

- [Divergencia entre contratos documentados e configuracao do Compose] -> Mitigacao: Estabelecer `docs/foundation/contracts.md` como fonte unica e vincular os criterios de aceite das issues #6, #10 e #14 diretamente a ele.
- [Vazamento acidental de credenciais via `.env`] -> Mitigacao: Fornecer `.env.example` apenas com valores vazios ou de dev e validar explicitamente que `.env` consta no `.gitignore`.
- [Falha na geracao de client do Orval por backend indisponivel no host] -> Mitigacao: O contrato define explicitamente a exposicao da porta 8080 no host em dev e a rota `/v3/api-docs`.

## Open Questions

- `MINIO_ENDPOINT`: Qual sera o nome exato da variavel consumida pelo backend para se conectar ao MinIO? Fica para decisao no epico de storage durante a integracao do S3 client.
- `Healthcheck do Caddy`: O Caddy v2 nao dispoe de healthcheck nativo sem modulo extra ou rota de ping dedicada. A necessidade de monitorar o container do Caddy sera avaliada na issue #16.




