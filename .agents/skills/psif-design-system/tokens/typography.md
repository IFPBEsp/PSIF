## 4. TIPOGRAFIA

### 4.1 Família

**Figtree** (licença OFL), pela pilha `--font-sans`. No Next.js,
`--font-figtree` vem do `next/font` (§26.2). Pesos: 400 (corpo), 500 (valor de
campo, nome em lista), 600 (título, número, botão).

### 4.2 Escala

| Token | Valor | Peso | Uso |
|---|---|---|---|
| `--fs-display` | 32px | 600 | título de tela, número de indicador, título da página pública |
| `--fs-h1` | 20px | 600 | saudação do Início, marca na barra lateral |
| `--fs-h2` | 18px | 600 | nome do aluno em cartão, rótulo do botão primário |
| `--fs-h3` | 16px | 500 | rótulo e valor de campo, título de seção sobre o céu |
| `--fs-body` | 15px | 400 | linha de lista, texto de cartão; título de cartão em 600 |
| `--fs-small` | 14px | 400 | descrição, placeholder, filtro |
| `--fs-caption` | 12px | 400 | metadado, horário relativo, rótulo de atalho, título de grupo |

Nada abaixo de `--fs-caption`. Campo fica em `--fs-h3`: abaixo de 16px o
Safari dá zoom ao focar.

### 4.3 Hierarquia

- Um título de tela por tela: `--fs-display`, peso 600, `--navy-700`, à
  esquerda, logo abaixo da barra de ações (§7.3), seguido de uma linha de
  contexto em `--fs-body` `--ink-700` ("José Antonio · 4 arquivos"). Folha,
  diálogo e tela de autenticação centralizam o título.
- Texto principal em `--ink-900`; dado que o usuário procura (nome, horário,
  número) em `--navy-700`; secundário em `--ink-700`.
- Título de grupo dentro da tela: `--fs-caption` 600 `--navy-700`, em caixa
  normal ("Este mês", "Prontuário").
- Nada em caixa alta corrida, nada em itálico para ênfase.
- Texto corrido até 70ch por linha; dado em lista e tabela pode ser mais
  denso.

### 4.4 Altura de linha

`--lh-tight` em título e número, `--lh-snug` em linha de lista com duas
linhas, `--lh-normal` em parágrafo e campo de texto longo. Qual tamanho leva
qual altura: `typography.line_height_by_size` no `tokens.json`.
