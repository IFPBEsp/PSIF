## 4. TIPOGRAFIA

### 4.1 Família

**Figtree**, com pilha `var(--font-figtree, 'Figtree'), system-ui,
-apple-system, 'Segoe UI', Roboto, sans-serif` (`--font-sans`). Uma família
só, para tudo. No Next.js, `--font-figtree` vem do `next/font` (§27.2); fora
dele, vale o `'Figtree'` do fallback, carregado pelo Google Fonts.

Identificada pelo desenho dos glifos: o PDF exportado do Figma converte o
texto em glifos Type 3 e não guarda o nome da fonte. Confirme no arquivo
Figma antes de travar a licença (§28).

Pesos usados: 400 (corpo), 500 (valor de campo, nome em lista), 600 (título
de tela, título de cartão, número de indicador, botão).

### 4.2 Escala Tipográfica

Medida nos PDFs (tamanho efetivo de cada texto), consolidada:

| Token | Valor | Peso | Uso |
|---|---|---|---|
| `--fs-splash` | 36px | 400 | "PSIF" no splash |
| `--fs-display` | 32px | 600 | título de tela (§4.3), número de indicador (08, 120), título da página pública |
| `--fs-splash-sub` | 26px | 400 | subtítulo do splash |
| `--fs-h1` | 20px | 600 | saudação do Início, marca na barra lateral |
| `--fs-h2` | 18px | 600 | nome do aluno em cartão, rótulo de botão primário de rodapé |
| `--fs-h3` | 16px | 500 | rótulo e valor de campo (§8.3), título de seção sobre o céu (fora do cartão) |
| `--fs-body` | 15px | 400 | **corpo**: linha de lista, texto de cartão; título de cartão em peso 600 (§9.1) |
| `--fs-small` | 14px | 400 | descrição, placeholder, filtro |
| `--fs-caption` | 12px | 400 | metadado, horário relativo, rótulo de atalho |

Consolidações feitas (o protótipo usa 13 tamanhos):

- 22px e 25px de título de tela → `--fs-h1` (20px). Título de tela é um só.
- 13px → `--fs-small` (14px).
- **Abaixo de 12px não existe.** O protótipo tem 10px na barra inferior (que saiu), 9px
  no rodapé do login e 11px no cartão de funcionalidade, todos sobem para
  `--fs-caption`.

### 4.3 Regras de hierarquia e legibilidade

- Um título de tela por tela, `--navy-700`, peso 600, à esquerda. Celular: a
  barra superior só tem ações (voltar à esquerda; busca ou ⋯ à direita); o
  título vem logo abaixo, em `--fs-display`, seguido de uma linha de contexto
  em `--fs-body` `--ink-700` ("José Antonio · 4 arquivos"). Exceção: folha
  modal e tela de autenticação mantêm o título centralizado. Web:
  `--fs-display` à esquerda (§7.3). O protótipo varia (preto 18px em "Meus
  alunos", preto 25px alinhado à esquerda em "Recuperar senha"): a variação é
  drift, não intenção.
- Texto principal em `--ink-900`; dado que o usuário procura (nome, horário,
  número) em `--navy-700`; texto secundário em `--ink-700`.
- Parágrafo com mais de uma linha usa `--lh-normal`. Título e número usam
  `--lh-tight`.
- Nada em caixa alta corrida. Nada em itálico para ênfase de dado.
- Título de grupo dentro da tela: `--fs-caption` peso 600 `--navy-700`, em
  caixa normal ("Este mês", "Prontuário"), nunca em caixa alta.
- Texto corrido (descrição, observação, corpo de notificação) com no máximo
  65–75 caracteres por linha: `max-width: 70ch`. Dado em lista e tabela pode
  ser mais denso.

### 4.4 Tokens de escala (opcional em CSS)

Altura de linha: `--lh-tight` 1.2 (título, número: é o que o Figma usa) ·
`--lh-snug` 1.35 (linha de lista com duas linhas) · `--lh-normal` 1.5
(parágrafo, descrição de notificação, campo de texto longo). O protótipo usa
1.2 em tudo; em parágrafo isso aperta a leitura e foi corrigido (§28).
