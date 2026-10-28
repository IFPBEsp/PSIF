## 3. DESIGN TOKENS

Todo valor visual do PSIF sai de `scripts/tokens.json` e chega à tela por
`var(--token)`, colado de `assets/tokens.css`. Nenhum hex, raio, sombra ou
espaçamento é digitado na folha de estilo da tela.

Cada valor tem uma origem declarada:

- **medido**: lido dos vetores dos PDFs do protótipo (Figma, quadro de
  390×844). É o PSIF como foi desenhado.
- **amostrado**: lido dos pixels de uma imagem embutida no PDF (logo, ícone
  do app). Valor aproximado: a imagem é JPEG.
- **derivado**: o protótipo não desenha o caso (estado de erro, alerta,
  hover) ou desenha de um jeito que reprova acessibilidade. O valor foi
  calculado para cobrir o caso e está **em aberto em §28** até o design
  ratificar.

### 3.1 Cor: Paleta canônica (produção)

| Token | Hex | Origem | Papel |
|---|---|---|---|
| `--navy-700` | `#244A69` | medido | **a cor do PSIF**: botão primário, título de tela, número de indicador, nome em lista, ícone do item ativo da navegação, link |
| `--navy-800` | `#1D3B54` | derivado | hover do botão primário |
| `--navy-900` | `#162E41` | derivado | pressionado do botão primário |
| `--navy-500` | `#5586A3` | medido | ilustração (Recuperar senha) e marcador gráfico, nunca texto |
| `--sky-100` | `#CFE7F5` | medido | fundo de toda tela (exceto splash) |
| `--sky-300` | `#A4C7E4` | medido | fundo do atalho de Ações Rápidas |
| `--blue-700` | `#1760B1` | amostrado | traço do logo coração-cérebro (login): só marca |
| `--blue-300` | `#72BAFC` | amostrado | fundo do ícone do app (splash): só marca |
| `--ink-900` | `#000000` | medido | texto principal: saudação, rótulo de campo, título de cartão de notificação |
| `--ink-700` | `#616161` | derivado | **texto secundário** (substitui o `#7D7D7D` do protótipo, que reprova AA) |
| `--ink-600` | `#7D7D7D` | medido | borda de campo, ícone inativo: banido como texto |
| `--ink-500` | `#999999` | medido | trilho da barra de progresso do splash: banido como texto |
| `--ink-200` | `#E8E8E8` | medido | divisória entre linhas de lista |
| `--ink-100` | `#F3F3F3` | medido | fundo afundado (área de ícone em cartão de funcionalidade) |
| `--white` | `#FFFFFF` | medido | cartão, campo, barra superior da página pública |
| `--success-700` | `#0E782E` | medido | situação "Em acompanhamento" no perfil do aluno |
| `--success-100` | `#E3F1E7` | derivado | fundo de selo de situação positiva |
| `--warning-700` | `#8A5300` | derivado | texto e marcador de atenção (acompanhamento pendente, alerta) |
| `--warning-100` | `#FDF3D6` | derivado | fundo de aviso |
| `--danger-700` | `#B42318` | derivado | erro de validação, ação destrutiva |
| `--danger-100` | `#FDECEA` | derivado | fundo de mensagem de erro |

Cores encontradas no protótipo que **não** são token, e para onde vão:

- `#144960` (texto e borda do botão "Saiba Mais" da página pública): segunda
  versão do marinho, quase igual. Use `--navy-700`.
- `#1A1A1A` (um texto da página pública): use `--ink-900`.
- Bolinhas 🟢 🟡 🔵 da linha do tempo: são **emoji**, não cor. Viram marcador
  com token (§11.5).
- Sombra preta a 25% (padrão do Figma): vira sombra tingida de marinho (§3.4).

### 3.2 Contraste: verificação com os tokens reais

<!-- ⚠️  Esta tabela é CONFERIDA por `scripts/tests/test_contrast_table.py`:
     cada linha marcada ✓ AA / ✓ AAA é recalculada contra o mesmo motor que o
     resto da skill usa. Ao trocar a paleta, recalcule com
         python3 scripts/check_contrast.py <texto> <fundo>
     e reescreva as linhas. Não edite só o hex e deixe a razão velha. -->

Pares aprovados (texto normal, piso 4.5:1):

```
--ink-900 / #fff: 21.00:1 ✓ AAA
--ink-900 / --sky-100: 16.40:1 ✓ AAA
--navy-700 / #fff: 9.30:1 ✓ AAA
--navy-700 / --sky-100: 7.26:1 ✓ AAA
--navy-700 / --sky-300: 5.25:1 ✓ AA
--navy-700 / --ink-100: 8.38:1 ✓ AAA
#fff / --navy-700: 9.30:1 ✓ AAA
#fff / --navy-800: 11.63:1 ✓ AAA
#fff / --navy-900: 13.99:1 ✓ AAA
--ink-700 / #fff: 6.19:1 ✓ AA
--ink-700 / --sky-100: 4.84:1 ✓ AA
--success-700 / #fff: 5.61:1 ✓ AA
--success-700 / --success-100: 4.81:1 ✓ AA
--warning-700 / #fff: 6.33:1 ✓ AA
--warning-700 / --warning-100: 5.72:1 ✓ AA
--danger-700 / #fff: 6.57:1 ✓ AA
--danger-700 / --danger-100: 5.75:1 ✓ AA
#fff / --danger-700: 6.57:1 ✓ AA
```

Pares que **reprovam** e por isso não existem em tela:

```
--ink-600 / #fff          4.12:1  ✗ texto (passa 3:1 de UI: borda e ícone)
--ink-600 / --sky-100     3.22:1  ✗ texto (passa 3:1 de UI)
--success-700 / --sky-100 4.38:1  ✗ texto: situação só sobre cartão branco
--navy-500 / --sky-100    3.08:1  ✗ texto (passa 3:1 de UI, por pouco)
--ink-500 / #fff          2.85:1  ✗ texto e ✗ UI
```

O primeiro é o mais importante: o protótipo escreve **todo** texto secundário
(rótulo de indicador, descrição, placeholder, metadado de documento) em
`#7D7D7D`. Na implementação, texto secundário é `--ink-700`.

### 3.3 Regra de Dominância do Azul (60-30-10)

Regra de ouro: **fundo céu, cartão branco, ação em marinho.**

- **~60% neutro**: `--sky-100` no fundo, `--white` nos cartões. É o que a tela
  é.
- **~30% estrutural**: `--navy-700` em título, número, nome, ícone, borda de
  ação e no botão primário. É o que a tela *diz*: marca o que se clica e o que
  se lê primeiro.
- **acento**: `--blue-*` só na marca (logo, ícone do app). Não existe cor de
  acento em UI: o PSIF é monocromático em azul de propósito.

Teste de cinco segundos: o único bloco largo de marinho na tela é o botão
primário do rodapé? Se um cartão, uma faixa ou um cabeçalho inteiro ficou
marinho, a dominância inverteu.

Exceção única: o **splash** (§13.5) é marinho de ponta a ponta. É momento de
marca, não tela de trabalho: `check_dominance.py` reprova o splash, e isso é
esperado.
