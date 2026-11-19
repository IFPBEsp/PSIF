## 5. LAYOUT

O PSIF é web responsivo. A largura decide o layout (§5.2–§5.11); a forma de
entrada, toque ou mouse, decide hover, menu e tamanho de alvo (§5.12). A tela
estreita é a prioridade, e tudo funciona a partir de 320px.

### 5.1 Estrutura da tela

1. **Barra de ações** (§7.3): voltar à esquerda; busca, ⋯ ou ☰ à direita.
   Acima dela, a área segura do aparelho, nunca menos de `--sp-4`
   (`padding-top: max(var(--sp-4), env(safe-area-inset-top))`). O `env()`
   só vale com `viewportFit: "cover"` no `viewport` do layout raiz.
2. **Título** (§4.3) e **conteúdo**: cartões sobre `--surface-base`.
3. **Barra de ação**: só em tela de tarefa, com o botão primário (§5.6).

A navegação é a barra lateral: gaveta em tela estreita (§7.9), fixa ao lado
do conteúdo em tela larga (§7.10).

### 5.2 Larguras

| Tela | Faixa | Layout |
|---|---|---|
| Estreita | abaixo de `--bp-md` | coluna única, gaveta, barra de ação na base |
| Larga | intermediária, de `--bp-md` até `--bp-lg` | barra lateral recolhida a ícones; painel e perfil em coluna única |
| Larga | a partir de `--bp-lg` | barra lateral aberta, grades de §5.3 |

- Margem lateral: `--page-pad` na estreita, `--sp-8` nas outras.
- Monitor grande: o conteúdo vai até `--w-content`, centralizado no espaço
  ao lado da barra lateral. Abaixo disso, ocupa toda a largura.
- Outros limites: texto corrido até 70ch (§4.3), diálogo até `--w-form`
  (§9.6) e cartão de login até `--w-auth` (§9.8).

### 5.3 Grades

| Peça | Estreita | Intermediária | A partir de `--bp-lg` |
|---|---|---|---|
| Indicadores (§9.2) | 2×2 | linha de 4 | linha de 4 |
| Painel do Início (§14.2) | coluna única | coluna única | 3 colunas: principal 2, apoio 1 |
| Formulário (§15.1) | uma coluna | 2 colunas | 3 colunas |
| Alunos e documentos | cartões e linhas (§11.1, §11.2) | tabela só com as colunas principais | tabela completa (§11.8) |
| Perfil do aluno (§13.2) | uma coluna | uma coluna | tabela e coluna lateral |
| Cartões de funcionalidade (§9.7) | um por linha | 2 por linha | 3 por linha |

Campo de texto longo ocupa a linha inteira em qualquer grade. Tabela que não
cabe rola dentro do cartão, nunca a página.

### 5.4 Breakpoints

`--bp-md` e `--bp-lg`, crescendo por `min-width`. Nenhuma outra largura de
quebra. `var()` não funciona em `@media`: escreva o valor e cite o token num
comentário (`@media (min-width: 768px) /* --bp-md */`), ou use `md:` e `lg:`
do Tailwind.

### 5.5 Gaveta

Na tela estreita, a navegação fica na gaveta que o ☰ abre (§7.9), por cima
do conteúdo. A base da tela fica livre para a barra de ação.

### 5.6 Barra de ação

Tela de tarefa (Novo atendimento, Relatórios, Agenda, Documentos) tem um
botão primário, e só um. Ele vem depois dos campos no DOM, para a ordem de
foco ser título, campos, botão (§20.4). Na tela estreita fica numa faixa
`--surface-base` presa à base, com linha `--divider-on-sky` em cima; a partir
de `--bp-md`, a grade o põe na linha do título, à direita, compacto (§8.1):

```tsx
<div className="pb-36 md:grid md:grid-cols-[minmax(0,1fr)_auto] md:items-start
                md:gap-x-4 md:pb-0">
  <div>
    <h1 className="text-display font-semibold text-primary">Novo atendimento</h1>
    <p className="text-body text-ink-700">José Antonio · 3º ano</p>
  </div>
  <form id="form-atendimento" className="md:col-span-2">
    {/* campos */}
  </form>
  <div className="fixed inset-x-0 bottom-0 z-(--z-sticky) border-t border-(--divider-on-sky)
                  bg-background px-6 pt-3 pb-[max(var(--sp-6),env(safe-area-inset-bottom))]
                  md:static md:col-start-2 md:row-start-1 md:border-0 md:bg-transparent md:p-0">
    <Button type="submit" form="form-atendimento"
      className="w-full md:w-auto md:min-h-(--target-min) md:text-small">
      Salvar atendimento
    </Button>
  </div>
</div>
```

O `pb-36` impede que o último campo fique sob a faixa, e a área segura de
baixo (§5.1) tira o botão de cima da barra de gestos do aparelho. A grade
reserva o espaço do botão: título longo quebra linha em vez de passar por
baixo dele. Tela com regra de envio (Documentos: "PDF, até 20 MB") põe a regra
num `<p>` sob o botão, visível em toda largura, ligada por `aria-describedby`;
sem regra, nem o `<p>` nem o `aria-describedby`. Um botão só: duplicar (um
para cada largura) deixa um deles fora da ordem de foco.

### 5.7 Alinhamento

Tudo à esquerda, a `--card-pad` da borda do cartão. Exceções: título (§4.3);
chevron e horário relativo, à direita.

### 5.8 Ritmo vertical

`--sp-6` entre cartões e entre campos; `--sp-2` entre rótulo e campo e entre
título e descrição; `--sp-4` entre linhas de lista.

### 5.9 Espaço em branco

Céu vazio abaixo do conteúdo é aceitável. Não preencha com cartão decorativo.

### 5.10 Áreas sem conteúdo

Lista vazia vira estado vazio, com motivo e ação (§10.6).

### 5.11 O que muda por largura

| Elemento | Estreita | A partir de `--bp-md` |
|---|---|---|
| Navegação | gaveta pelo ☰ (§7.9) | barra lateral; recolhida até `--bp-lg` (§7.10, §7.12) |
| Breadcrumbs | não aparecem | no topo do conteúdo (§7.11) |
| Ação primária | faixa na base, largura total | ao lado do título, largura automática (§5.6) |
| Folha | `Drawer` que sobe da base | `Dialog` centralizado (§9.6) |
| Listagem | cartões e linhas | tabela (§11.8) |
| Agenda | calendário sobre a agenda do dia | lado a lado (§11.6) |

### 5.12 Toque e mouse

A largura não diz como a pessoa aponta: há tablet com mouse e notebook com
tela de toque. O que depende da entrada usa `@media (hover: hover) and
(pointer: fine)`, a variante `mouse:` de §26.8:

- **Hover**: só com mouse; no toque, o pressionado faz o papel (§17.2).
- **Menu suspenso e dica** (`DropdownMenu`, `Tooltip`): só com mouse. No
  toque, a mesma lista abre em folha, que é `Drawer` na tela estreita e
  `Dialog` na larga (§9.6).
- **Alvo**: o mínimo de §20.6 vale no toque. Com mouse, ação densa (ícone em
  linha de tabela, item de menu) pode usar `--target-fine`, nunca abaixo de
  24px (WCAG 2.5.8). A outra exceção é o dia do calendário na tela estreita
  (§11.6).
