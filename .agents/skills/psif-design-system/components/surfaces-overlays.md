## 9. SUPERFÍCIES E SOBREPOSIÇÕES

### 9.1 Cartão

Fundo `--surface-raised`, `--radius-md`, `--card-pad`, sem borda e sem
sombra, largura total menos `--page-pad` de cada lado. Título do cartão
(quando há) em `--fs-body` peso 600 `--navy-700`: "Próximos atendimentos",
"Ações rápidas".

### 9.2 Cartão de indicadores

Os indicadores do Início: **um** cartão com grade 2×2 (uma linha de 4 no
web, §5.3), células separadas por linha `--ink-200`. Cada célula: número em `--fs-display` peso 600
`--navy-700` e rótulo em `--fs-body` `--ink-700` embaixo.

| Número | Rótulo |
|---|---|
| atendimentos de hoje | "Atendimentos hoje" |
| alunos ativos | "Alunos ativos" |
| relatórios pendentes | "Relatórios pendentes" |
| alertas | "Alertas importantes" |

Número com dois dígitos e zero à esquerda (08, 05, 02) é o desenho do
protótipo; o leitor de tela lê "8" (§20.8). Cada célula é tocável e leva à
lista filtrada correspondente.

### 9.3 Cartão de lista

Cartão branco com linhas separadas por `--ink-200`. Linha: dado-chave à
esquerda em `--navy-700`, texto de apoio, chevron (›) `--ink-600` à direita.

- Próximos atendimentos: horário (`--fs-body` peso 600) + nome do aluno.
- Atendimentos do dia (Agenda): horário em `--fs-h1`, nome em `--fs-body`
  peso 600, tipo em `--fs-caption` `--ink-700`.

### 9.4 Cartão de aluno

Cartão branco: avatar `--avatar-md` à esquerda (§12.1); à direita, nome em
`--fs-h2` peso 600 `--navy-700`, curso e ano em `--fs-body` `--ink-700`,
situação em `--fs-body` (§12.2). O cartão inteiro abre o perfil.

### 9.5 Cartão de notificação

Cartão branco: título em `--fs-body` peso 600 (`--navy-700` para não lida,
`--ink-900` para lida), corpo em `--fs-small` `--ink-700` `--lh-normal`, tempo
relativo ("Há 15 min") em `--fs-caption` `--ink-900` no canto superior
direito. Notificação de pendência ("Acompanhamento pendente") ganha marcador
`--warning-700` e a palavra "Pendente" no título.

Não lida não se distingue só pela cor (§20.2): ganha também um ponto
`--navy-700` de `--sp-2` antes do título e "não lida" no nome acessível.

### 9.6 Folha modal

Só como **folha** que sobe da base: seletor de data, lista de seleção,
confirmação de descarte. Fundo `--surface-overlay`, cantos superiores
`--radius-lg`, `--sh-md`, véu `--overlay` atrás, `--z-modal`. Fecha com
gesto, botão "Fechar" e Esc.

Exceção: os resultados da busca global do web abrem como cartão logo abaixo
do campo (§7.13).

### 9.7 Cartão de funcionalidade (página pública)

Cartão branco com círculo `--navy-700` de 48px contendo ícone branco, título
em `--fs-body` peso 600 `--ink-900` e descrição em `--fs-small` `--ink-700`.
Só na página pública.

### 9.8 Cartão de autenticação

Cartão branco central, `--radius-lg`, `--sh-sm`, com logo, subtítulo, campos e
botão primário. Login e Recuperar senha.

### 9.9 Sobreposição fora do contêiner (regra de implementação)

Folha modal e lista de seleção são renderizadas na raiz do documento, não
dentro do cartão que as abriu, senão o `overflow` do cartão as corta.
