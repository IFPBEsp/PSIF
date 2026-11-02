## 8. AÇÕES E ENTRADA DE DADOS

### 8.1 Botões

| Tipo | Visual | Uso |
|---|---|---|
| **Primário** | fundo `--navy-700`, texto `--white` `--fs-h2` 600, `--radius-lg`, `--sh-sm`, largura total, altura `--control-min` | a ação da tela: "Salvar atendimento", "Entrar" |
| **Secundário** | fundo `--white`, borda 1px `--navy-700`, texto `--navy-700` | ação alternativa ao lado do primário |
| **Compacto** | primário com `--fs-small`, largura automática, altura `--target-min` | "Entrar" no cabeçalho da página pública; o botão de tela já fica compacto a partir de `--bp-md` (§5.6) |
| **Link** | texto `--navy-700`, sublinhado | navegação dentro de texto: "Esqueceu a senha?" |

Estados em §6. Carregando troca o rótulo ("Salvando…") e bloqueia novo
clique. Botão de adicionar começa com "+": "+ Novo agendamento".

Barra de ação da tela estreita: §5.6.

### 8.2 Menu de opções

Linha com mais de uma ação abre a lista: `DropdownMenu` com mouse; no
toque, folha (§9.6). Alvo dos itens em §5.12.

### 8.3 Campos

Rótulo acima do campo, `--fs-h3` `--ink-900`. Campo: fundo `--white`, borda
1px `--ink-600` sobre qualquer fundo, `--radius-lg`, `--input-pad`, altura
`--control-min`, valor em `--fs-h3` 500 `--navy-700`, placeholder em
`--fs-small` `--ink-700`. A borda é o que mostra o campo vazio (§3.2).

- Opcional e obrigatório: §15.4; "(opcional)" em `--ink-700` 400.
- Ícone à esquerda (envelope, cadeado): `--ink-600`, `--ic-md`.
- Texto longo ("Descrição"): mesma caixa, quatro linhas de altura mínima,
  `--lh-normal`.
- Erro: borda `--danger-700` e mensagem em texto embaixo (§10.7).
- Foco: no contêiner do campo, por `:focus-within` (§20.5).

### 8.4 Seleção

"Aluno" e "Tipo de atendimento" abrem a lista como o menu de §8.2. Busca no topo da lista quando ela passa de sete itens (Aluno sempre).
Chevron (⌄) `--ic-md` à direita. Aluno vem sempre da lista, nunca digitado.
Tipo de atendimento: Individual, Em grupo, Com a família, Reunião com
professor.

Marcação: `<label>` visível e gatilho com `aria-labelledby` no rótulo e no
valor ("Aluno, Anitta Peniwyse"). O gatilho anuncia o que abre:
`aria-haspopup="listbox"` no menu com mouse (`Select`, ou `Command` num
`Popover` quando há busca) e `aria-haspopup="dialog"` na folha do toque. Sem valor,
"Selecione" no estilo de placeholder. Escolher fecha a lista e devolve o foco
ao botão.

### 8.5 Envio de arquivo

"+ Adicionar documento" abre o seletor do sistema; depois do envio, a linha
entra na lista com nome, tamanho e data (§11.2). Tipos aceitos e tamanho
máximo aparecem antes do envio, nunca só no erro; os valores vêm do backend
(§27).

Na tela larga, a coluna lateral de Documentos (§13.2) tem também uma área de
envio: cartão `--white` `--radius-2xl` com borda tracejada de 2px
`--line-on-sky`, quadro de ícone `--tile-icon-lg` em `--sky-100`, "Arraste um
arquivo para cá" (`--fs-h3` 600), "ou escolha no computador" (texto com
estilo de link, sem `<a>`) e a regra de envio em `--fs-caption`. A área
inteira é um `<button>` que abre o seletor e aceita arrastar; hover
`--ink-100`. Na tela estreita, só o botão da barra de ação.

### 8.6 Data e máscaras

Data em `dd/mm/aaaa`, com botão de calendário à direita que abre o mês
(§11.6), alvo `--target-min`. Hora em `hh:mm`, 24 horas. Matrícula só com
dígitos.

### 8.7 Caixa de seleção

Quadrado `--sp-4`, `--radius-xs`, borda `--ink-600`; marcado, fundo
`--navy-700` com ✓ `--white`. O rótulo fica à direita e a linha inteira é o
alvo, com `--target-min`. "Lembrar-me" no login vem desmarcado (§27).
