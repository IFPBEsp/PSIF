# Convenções de nomeação

## Idioma

Código em inglês, incluindo o vocabulário de negócio: `Product`, `OrderItem`, `cancel`. Texto visível ao usuário fica em português. Um termo por conceito em todas as camadas.

## Backend (Java)

| Elemento | Padrão | Exemplo |
| --- | --- | --- |
| Pacote | minúsculo | `products.domain` |
| Módulo de negócio | plural | `products`, `orders` |
| Classe, record, enum | PascalCase | `Order`, `OrderStatus` |
| Método e variável | camelCase | `cancel`, `createdAt` |
| Constante e valor de enum | UPPER_SNAKE_CASE | `MAX_ITEMS`, `CANCELED` |

```text
ProductController   CreateProductRequest   ProductResponse
ProductService      ProductRepository      ProductNotFoundException
```

- Sem sufixo `Impl`: a implementação diz o que a diferencia (`EmailGateway`, `SmtpEmailProvider`).
- Método de domínio é verbo de negócio: `order.cancel()`, não `setStatus(...)`.
- Query do Spring Data segue o padrão do framework: `findByStatus`.

## Banco de dados

- Tabela no plural, coluna no singular, ambas em snake_case: `orders.created_at`.
- PK `id`, FK `<entidade>_id`: `product_id`.
- Constraints: `pk_`, `fk_`, `uk_`, `idx_`, `ck_` + tabela e colunas.
- Migration segue o formato de nome da ferramenta, com descrição em snake_case começando por verbo: `create_orders_table`.

## API REST

- Recurso no plural, em kebab-case: `/products`, `/order-items`.
- Ação fora do CRUD vira sub-rota: `POST /orders/{id}/cancel`.
- JSON e parâmetros em camelCase.

## Frontend (TypeScript)

```text
product-form.tsx              → ProductForm
create-product.schema.ts      → createProductSchema
create-product.action.ts      → createProductAction
products.keys.ts              → productKeys
use-products-filters.ts       → useProductsFilters
product.types.ts
```

- Arquivo e pasta em kebab-case, exceto os do Next.js (`page.tsx`, `layout.tsx`).
- Tipo em PascalCase, sem prefixo `I`. Props como `<Componente>Props`.
- Tipos gerados pelo Orval mantêm o nome do contrato.

## Ambiente

- UPPER_SNAKE_CASE com prefixo do grupo: `API_INTERNAL_URL`, `AUTH_ACCESS_COOKIE_NAME`.
- `NEXT_PUBLIC_` só para o que o navegador pode ver. Toda variável nova entra no `.env.example`.
