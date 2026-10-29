## 8. AÇÕES E ENTRADA DE DADOS

### 8.1 Botões

| Tipo | Visual | Uso |
|---|---|---|
| **Primário** | fundo `--navy-700`, texto branco `--fs-h2` peso 600, `--radius-lg`, `--sh-sm`, largura total, `min-height: var(--control-min)` | a ação da tela: "Salvar atendimento", "Entrar", "Enviar instruções" |
| **Secundário** | fundo branco, borda 1px `--navy-700`, texto `--navy-700` | ação alternativa ao lado do primário: "Saiba mais" |
| **Compacto** | primário com `--fs-small`, largura automática, altura `--target-min` | ação no cabeçalho da página pública: "Entrar". O botão de tela (§5.6) já fica compacto sozinho no web; não some `--compacto` a ele |
| **Link** | texto `--navy-700`, sublinhado | navegação dentro de texto: "Esqueceu a senha?", "Fale com a psicopedagoga do campus", "Voltar para o login" |

Estados: hover `--navy-800`, com transição de cor em `--dur-fast`;
pressionado `--navy-900`; desabilitado
`--o-disabled`; carregando troca o rótulo por "Salvando…" e bloqueia novo
toque. Botão de adicionar começa com "+": "+ Novo agendamento", "+ Adicionar
documento".

**Barra de ação do celular.** O botão de tela (§5.6) fica numa faixa
`--surface-base` presa à base, com linha de 1px `--divider-on-sky` em cima,
`--sp-3` em cima e `--sp-6` nas laterais e embaixo. A regra que vale antes do
envio ("PDF, até 20 MB") fica logo abaixo do botão, em `--fs-caption`
`--ink-700`, ligada ao botão por `aria-describedby`.

### 8.2 Menu de opções

Lista em folha modal (§9.6) quando uma linha tem mais de uma ação. Nunca menu
flutuante pequeno: o alvo de toque não cabe.

### 8.3 Campos

Rótulo **acima** do campo, `--fs-h3`, `--ink-900` (medido no Novo
atendimento). Campo: fundo branco, `--radius-lg`, `--input-pad`,
`min-height: var(--control-min)`, valor em `--fs-h3` (16px) peso 500
`--navy-700`: abaixo de 16px o Safari do iPhone dá zoom ao focar o campo,
placeholder em `--fs-small` `--ink-700`.

- Campo opcional: o rótulo termina em "(opcional)", em `--ink-700` peso 400.
  Obrigatório não ganha marca (§15.4).
- Borda 1px `--ink-600` sempre, sobre o céu e sobre o cartão. Branco sobre o
  céu dá 1.28:1, e um campo vazio só se reconhece pelo contorno (WCAG
  1.4.11); `--ink-600` passa 3:1 nos dois fundos. O Novo atendimento do
  protótipo não tem borda: correção registrada em §28.2.
- Ícone à esquerda (envelope, cadeado) em `--ink-600`, `--ic-md`.
- Campo de texto longo ("Descrição", "Relatório semanal"): mesma caixa,
  altura mínima de quatro linhas, `--lh-normal`.
- Erro: borda `--danger-700` **e** mensagem em texto abaixo (§20.9).

### 8.4 Seleção e busca

Seleção ("Aluno", "Tipo de atendimento") abre lista em folha modal. A lista
ganha busca no topo quando passa de sete itens (Aluno sempre; Tipo de
atendimento, com quatro opções, não precisa): no celular a busca abre o
teclado por cima da lista. Chevron (⌄) `--ic-md` à direita. Aluno é sempre escolhido da lista,
nunca digitado.

Marcação: `<label>` visível + `<button aria-haspopup="dialog">` com
`aria-labelledby` apontando para o rótulo **e** para o valor: o leitor de
tela lê "Aluno, Anitta Peniwyse". Sem valor, o botão mostra "Selecione" no
estilo de placeholder (§8.3). Escolher fecha a folha e devolve o foco ao
botão.

"Tipo de atendimento" no protótipo parece campo de texto (sem ⌄): é
seleção: Individual, Em grupo, Com a família, Reunião com professor.

### 8.5 Envio de arquivo

"+ Adicionar documento" abre o seletor do sistema. Depois do envio, a linha
aparece na lista com nome, tamanho e data (§11.2). Tipos aceitos e tamanho
máximo escritos antes do envio, não no erro. Os valores vêm do backend; o
PSIF ainda não os definiu (§28.4). Em protótipo, escreva "PDF, até 20 MB" e
avise que é provisório.

**Web**: além do botão "+ Adicionar documento" no cabeçalho do cartão de
documentos, a coluna lateral tem uma área de envio: cartão branco
(`--radius-2xl`) com borda tracejada de 2px `--line-on-sky`, quadro de ícone
`--tile-icon-lg` em `--sky-100`, "Arraste um arquivo para cá" (`--fs-h3`
600), "ou escolha no computador" (texto com estilo de link, sem `<a>`: um
link dentro do `<button>` é HTML inválido e confunde o leitor de tela) e a
regra de envio em
`--fs-caption`. A área inteira é um `<button>`: o teclado abre o seletor.
Hover `--ink-100`. **Celular**: sem área de envio; só o botão da barra de
ação.

### 8.6 Data e máscaras

Data em `dd/mm/aaaa`, com ícone de calendário à direita que abre o seletor
de mês (§11.6): botão próprio, `--ink-900`, alvo `--target-min` (§18). Hora em `hh:mm`, 24 horas. Matrícula só com dígitos.

### 8.7 Caixa de seleção

Quadrado de 16px, `--radius-xs`, borda `--ink-600`; marcado: fundo
`--navy-700` com ✓ branco. Rótulo clicável à direita ("Lembrar-me", desmarcado por padrão: a máquina
pode ser compartilhada, §28.4); a área
de toque é a linha toda, com altura `--target-min`. No projeto, `Checkbox`
com `Label` (§6).
