## 5. LAYOUT

O PSIF é desenhado em celular (quadro de 390×844, iPhone 13/14) e cresce a
partir dele.

### 5.1 Estrutura da tela (shell)

De cima para baixo, toda tela autenticada:

1. **Barra superior** (§7.3): só ações, voltar à esquerda e busca, ⋯ ou ☰
   à direita (§7.2). O título vem logo abaixo, à esquerda (§4.3); o Início
   troca o título pela saudação.
   Acima dela, só a área segura do aparelho, nunca menos de `--sp-4`:
   `padding-top: max(var(--sp-4), env(safe-area-inset-top))` no shell. O
   protótipo não desenha a barra de status; com `--sp-4`, o título cai na
   altura em que ele o mostra.
2. **Conteúdo**: cartões brancos sobre `--surface-base`, rolando.
3. **Rodapé fixo**: só em tela de tarefa, com o botão primário (§5.6).

No web, no topo do conteúdo, os breadcrumbs e o botão de Notificações
(§7.13); a busca global e o usuário ficam na barra lateral (§7.10).

A navegação é a barra lateral: gaveta pelo ☰ no celular (§5.5) e fixa à
esquerda no web, a partir de `--bp-md` (§7.10). O resto do shell não muda: barra superior, conteúdo
e rodapé de tela de tarefa ficam na área à direita dela.

### 5.2 Largura do conteúdo

- `--w-mobile` (390px) é o quadro de referência do protótipo: o tamanho em
  que tudo foi medido.
- No web, o conteúdo ocupa toda a área ao lado da barra lateral
  (`--w-sidebar`, 240px), sem largura máxima. Ele começa junto da barra,
  nunca centralizado numa coluna estreita. (Derivado, §28.2.)
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
- Grade do painel: coluna única entre `--bp-md` e
  `--bp-lg`; a partir de `--bp-lg`, 3 colunas com `--sp-6` de vão, a lista
  principal em 2 e o apoio em 1. Abaixo de `--bp-lg`, a coluna de apoio
  ficaria com uns 160px, e atalho e título de notificação não cabem.
  Composição do Início em §14.2.
- Alunos e documentos no web viram tabela (§11.8). Cartões iguais em grade
  (2 por linha, 3 a partir de `--bp-lg`) ficam para os cartões de
  funcionalidade da página pública (§9.7).
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

**Um botão só no DOM, depois dos campos.** Assim a ordem de foco é a mesma
nos dois formatos: título, campos, botão (§20.4). No celular ele fica na
barra de ação presa à base (§8.1); no web a grade o põe na linha do título,
à direita:

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
                  bg-background px-6 pt-3 pb-6
                  md:static md:col-start-2 md:row-start-1 md:border-0 md:bg-transparent md:p-0">
    <Button type="submit" form="form-atendimento"
      className="w-full md:w-auto md:min-h-(--target-min) md:text-small">
      Salvar atendimento
    </Button>
  </div>
</div>
```

O botão vem depois do formulário no DOM e aponta para ele com `form=`. No
celular, a faixa `fixed` fica presa à base, com a linha `--divider-on-sky` em
cima; o `pb-36` impede que o último campo fique embaixo dela. O Novo
atendimento não tem regra de envio. Tela que tem (Documentos: "PDF, até 20
MB") põe a regra num `<p>` sob o botão, visível nos dois formatos, e liga o
botão a ela com `aria-describedby`; sem regra, nem o `<p>` nem o
`aria-describedby` existem. No web, a grade de duas colunas põe a faixa na primeira
linha, ao lado do título, sem linha nem fundo, e reserva o espaço dela: título
longo quebra linha em vez de passar por baixo do botão. A barra de ações do
topo (§7.3) fica acima deste bloco. Nenhum JavaScript move nada.

Duplicar o botão (um no rodapé, só no celular, e outro na barra, só no web)
parece mais simples, mas sai pior: dois elementos que podem divergir de
rótulo, e um deles fora da ordem de foco.

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

Lista vazia vira estado vazio, com motivo e ação (§10.6).

### 5.11 Celular e web, lado a lado

A mesma tela serve os dois; as utilitárias `md:` fazem a troca a partir de
`--bp-md` (768px). Use a tabela para saber o que muda e abra a seção para o
detalhe.

| Elemento | Celular | Web |
|---|---|---|
| Navegação | gaveta pelo ☰ (§7.2, §7.9) | barra lateral fixa (§7.10) |
| Breadcrumbs | não aparecem (§7.11) | acima do título (§7.11) |
| Listagem | cartões e linhas de lista (§11.1) | tabela (§11.8) |
| Título da tela | abaixo da barra de ações, `--fs-display`, à esquerda (§4.3) | `--fs-display`, à esquerda (§4.3) |
| Ação primária | rodapé, largura total (§5.6) | topo, à direita, largura automática (§5.6) |
| Margem lateral | `--page-pad` | `--sp-8` |
| Largura | a tela | toda a área ao lado da barra lateral; texto corrido até 70ch (§5.2) |
| Topo do conteúdo | só a barra de ações (§7.3) | breadcrumbs e Notificações; busca e usuário na barra lateral (§7.13) |
| Barra lateral | gaveta (§7.9) | fixa, recolhível para só ícones (§7.12) |
| Formulário | uma coluna | 3 colunas; texto longo na linha inteira (§15.1) |
| Indicadores | 2×2 | linha de 4 (§9.2) |
| Cartões | coluna única | coluna única até `--bp-lg`; depois grade de 3: principal 2, apoio 1 (§5.3) |
| Lista de alunos e documentos | cartões e linhas, um por linha | tabela (§11.8) |
| Início | saudação, alerta, indicadores, próximos, atalhos (§14.1) | alerta, indicadores; próximos e Meus alunos à esquerda, atalhos e notificações à direita (§14.2) |
| Perfil do aluno | uma coluna (§13.2) | duas colunas (§13.2) |
| Agenda | calendário sobre a agenda do dia | lado a lado (§11.6) |
| Hover | não há | igual ao pressionado (§17.2) |
