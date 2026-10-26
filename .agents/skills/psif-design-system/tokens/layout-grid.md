## 5. LAYOUT

O PSIF é desenhado em celular (quadro de 390×844, iPhone 13/14) e cresce a
partir dele.

### 5.1 Estrutura da tela (shell)

De cima para baixo, toda tela autenticada:

1. **Barra superior** (§7.3): voltar à esquerda, título centralizado.
   Telas-raiz têm o menu (☰) à direita (§7.2); o Início troca o título
   pela saudação.
   Acima dela, só a área segura do aparelho, nunca menos de `--sp-4`:
   `padding-top: max(var(--sp-4), env(safe-area-inset-top))` no shell. O
   protótipo não desenha a barra de status; com `--sp-4`, o título cai na
   altura em que ele o mostra.
2. **Conteúdo**: cartões brancos sobre `--surface-base`, rolando.
3. **Rodapé fixo**: só em tela de tarefa, com o botão primário (§5.6).

No web, acima da barra superior, o cabeçalho em faixa branca (§7.13), de
ponta a ponta da área ao lado da barra lateral.

A navegação é a barra lateral: gaveta pelo ☰ no celular (§5.5) e fixa à
esquerda no web, a partir de `--bp-md` (§7.10). O resto do shell não muda: barra superior, conteúdo
e rodapé de tela de tarefa ficam na área à direita dela.

### 5.2 Largura do conteúdo

- `--w-mobile` (390px) é o quadro de referência do protótipo: o tamanho em
  que tudo foi medido.
- No web, o conteúdo ocupa toda a área ao lado da barra lateral
  (`--w-sidebar`, 240px), sem largura máxima. Ele começa junto da barra,
  nunca centralizado numa coluna estreita. (Derivado, §29.2.)
- Texto corrido continua até 70ch (§4.3): a área cresce, a linha de leitura
  não.
- Formulário no web: grade de 3 colunas para campo curto (Aluno · Data ·
  Tipo); campo de texto longo ocupa a linha inteira (§15.1).
- Margem lateral: `--page-pad` (24px) no celular; `--sp-8` (32px) no web.

### 5.3 Grade de conteúdo

No celular, coluna única. A única grade do protótipo é a dos **indicadores**
do Início: 2×2 dentro de um só cartão, separadas por linha `--ink-200`
(§9.2). Atalhos de Ações Rápidas: 4 por linha; quebram linha em vez de
encolher (§7.8).

No web (a partir de `--bp-md`):

- Indicadores do Início em uma linha de 4, no mesmo cartão (§9.2).
- Grade do painel (`.psif-grade-painel`): coluna única entre `--bp-md` e
  `--bp-lg`; a partir de `--bp-lg`, 3 colunas com `--sp-6` de vão, a lista
  principal em 2 e o apoio em 1. Abaixo de `--bp-lg`, a coluna de apoio
  ficaria com uns 160px, e atalho e título de notificação não cabem.
  Composição do Início em §14.7.
- Lista de cartões iguais (alunos, documentos): 2 por linha; 3 a partir de
  `--bp-lg`.
- Formulário em 3 colunas (§15.1).

### 5.4 Breakpoints (tokens)

Mobile-first, crescendo por `min-width`: `--bp-md` 768px · `--bp-lg` 1200px.
Derivados: o protótipo só tem o quadro de celular.

`var()` não funciona dentro de `@media`: escreva o valor e cite o token num
comentário: `@media (min-width: 768px) /* --bp-md */`. Nenhuma outra largura
de quebra.

### 5.5 Gaveta de navegação (celular)

Abaixo de `--bp-md`, a navegação fica numa gaveta que o ☰ abre (§7.9), por
cima do conteúdo, com `--z-modal`. Não ocupa espaço do shell: a base da tela
fica livre para o botão primário da tela de tarefa (§5.6).

### 5.6 Barra de ação

Tela de tarefa (Novo atendimento, Relatórios, Agenda, Documentos) tem **um**
botão primário de largura total fixo no rodapé, a `--page-pad` das bordas.
É a única ação primária da tela. No web, o mesmo botão sobe para a direita da
barra superior, com largura automática (§7.3).

**É um botão só, não dois.** Escreva-o como o último filho de
`.psif-barra-superior`, com a classe `.psif-botao--tela`:

```html
<header class="psif-barra-superior">
  <button class="psif-botao-icone" aria-label="Voltar">…</button>
  <h1 class="psif-titulo-tela">Novo atendimento</h1>
  <button class="psif-botao psif-botao--tela" type="submit" form="…">Salvar atendimento</button>
</header>
```

`.psif-botao--tela` é `position: fixed` no celular: isso tira o botão do
fluxo da barra superior (onde está escrito no HTML deixa de importar) e o
`left`/`right`/`bottom: var(--page-pad)` o estica para a largura toda do
rodapé. No web, a regra muda só para `position: static`: o botão volta a
ser o último item do flex da barra superior, do tamanho do próprio
conteúdo, encostado à direita porque o título ao lado (`flex: 1 1 auto`)
ocupa o resto. Nenhum JavaScript move nada; são duas leituras da mesma regra
de posição.

Duplicar o botão (um fixo no rodapé com `.psif-so-celular`, outro na barra
com uma classe de visibilidade própria) parece a solução mais óbvia, e já
aconteceu mais de uma vez, mas sai pior: dois elementos que podem divergir
de rótulo, dois lugares para o `form=` apontar, e nenhum ganho sobre o
único botão acima.

### 5.7 Alinhamento

Tudo alinha à esquerda dentro do cartão, a `--card-pad` da borda. Exceções:
título de tela (centro, só no celular) e chevron/horário relativo (direita).

### 5.8 Ritmo vertical

`--sp-6` entre cartões e entre campos; `--sp-2` entre rótulo e campo e entre
título e descrição; `--sp-4` entre linhas de lista (com divisória).

### 5.9 Espaço em branco

O protótipo deixa grandes áreas de céu vazio abaixo do conteúdo (Agenda,
Documentos). Isso é aceitável: o céu é o neutro. Não preencha com cartão
decorativo.

### 5.10 Áreas sem conteúdo

Lista vazia não é área vazia: é estado vazio com motivo e ação (§10.6).

### 5.11 Celular e web, lado a lado

O mesmo HTML serve os dois; `components.css` faz a troca a partir de
`--bp-md` (768px). Use a tabela para saber o que muda e abra a seção para o
detalhe.

| Elemento | Celular | Web |
|---|---|---|
| Navegação | gaveta pelo ☰ (§7.2, §7.9) | barra lateral fixa (§7.10) |
| Breadcrumbs | não aparecem (§7.11) | acima do título (§7.11) |
| Listagem | cartões e linhas de lista (§11.1) | tabela (§11.8) |
| Título da tela | centralizado (§7.3) | à esquerda (§7.3) |
| Ação primária | rodapé, largura total (§5.6) | topo, à direita, largura automática (§5.6) |
| Margem lateral | `--page-pad` | `--sp-8` |
| Largura | a tela | toda a área ao lado da barra lateral; texto corrido até 70ch (§5.2) |
| Cabeçalho | não aparece | faixa branca com ☰ recolher, busca, Notificações e Meu perfil (§7.13) |
| Barra lateral | gaveta (§7.9) | fixa, recolhível para só ícones (§7.12) |
| Formulário | uma coluna | 3 colunas; texto longo na linha inteira (§15.1) |
| Indicadores | 2×2 | linha de 4 (§9.2) |
| Cartões | coluna única | coluna única até `--bp-lg`; depois grade de 3: principal 2, apoio 1 (§5.3) |
| Lista de alunos e documentos | um por linha | 2 por linha; 3 a partir de `--bp-lg` |
| Início | três cartões (§14.3) | alerta, indicadores; próximos e Meus alunos à esquerda, atalhos e notificações à direita (§14.7) |
| Perfil do aluno | uma coluna (§13.2) | duas colunas (§13.2) |
| Agenda | calendário sobre a agenda do dia | lado a lado (§11.6) |
| Hover | não há | igual ao pressionado (§17.2) |
