# Tasks

## 1. Documentação de contratos

- [x] 1.1 Criar a pasta `docs/foundation` e o documento `docs/foundation/contracts.md`, e verificar que o documento traz serviços, portas dev/prod, URLs internas e públicas, estrutura do `.env.example`, healthchecks e caminho do OpenAPI.
- [x] 1.2 Adicionar a entrada de `docs/foundation/contracts.md` no índice geral em `docs/AGENTS.md`, e verificar o link no documento.
- [x] 1.3 Atualizar o exemplo de `API_INTERNAL_URL` em `docs/frontend/architecture-and-stack.md` para `http://backend:8080`, e verificar o trecho alterado.

## 2. Configuração de ambiente e repositório

- [x] 2.1 Criar o arquivo `.env.example` na raiz com as variáveis da fundação (`APP_ENV`, `NEXT_PUBLIC_APP_URL`, `API_INTERNAL_URL`, `POSTGRES_*`, `MINIO_ROOT_*`) sem valores secretos, e verificar que os nomes das variáveis seguem `docs/conventions/naming.md` e que só o que o navegador vê usa `NEXT_PUBLIC_`.
- [x] 2.2 Conferir o `.gitignore` para assegurar que `.env` esteja ignorado e que `.env.example` permaneça rastreável pelo Git, verificando via `git check-ignore`.

## 3. Validação

- [x] 3.1 Validar que os critérios de aceite da issue #5 estão atendidos e que nenhum arquivo de código ou segredo foi inserido, inspecionando o diff com `git status` e `git diff`.
- [x] 3.2 Executar `openspec validate` para confirmar a conformidade dos artefatos da change.
