# Convenções de código

## Formatação

- UTF-8, LF, linha final, sem espaço à direita.
- 4 espaços em Java, 2 no resto. Largura de linha definida na configuração do formatador.
- Formatação em massa vai em commit separado.

## Geral

- Um arquivo, uma responsabilidade. Nada de `utils.ts` ou `Helper` genéricos.
- Retorno antecipado em vez de `if` aninhado.
- Valor com significado vira constante nomeada.
- Código morto ou comentado é removido.

## Backend (Java)

- Injeção pelo construtor com campos `final`.
- `record` para Request, Response e value objects.
- `Optional` só como retorno. Coleção vazia em vez de `null`.
- Exceção específica em vez de `RuntimeException`. Não engula exceção.
- Sem nome totalmente qualificado no código (`java.util.List`): use import. FQN só para resolver conflito entre duas classes com o mesmo nome.
- Evite `@Data` do Lombok em entidade JPA.
- Sem comentário no código, só Javadoc. Regra em `writing.md`, seção Comentários.

## Frontend (TypeScript)

- Strict, sem `any`; use `unknown` e estreite.
- Named export, exceto onde o Next.js exige default.
- Import com alias `@/*`; relativo só na mesma pasta. Ordem: externos, `@/`, relativos.
- Sem `console.log` commitado. `key` de lista vem do dado, não do índice.

## Testes

- Teste acompanha a mudança no mesmo PR.
- Nome descreve o comportamento: `shouldCancelPendingOrder`, `it("cancels pending order")`.
- Java: `<Alvo>Test` (unitário) e `<Alvo>IT` (integração), no mesmo pacote. TypeScript: `<alvo>.test.ts(x)` ao lado do arquivo.
- Teste não depende de ordem, de outro teste nem de serviço externo real.
