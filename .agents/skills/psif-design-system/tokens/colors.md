## 3. DESIGN TOKENS

Todo valor visual sai de `scripts/tokens.json` e chega à tela por
`var(--token)` ou por utilitária ligada a token (§26.6).

### 3.1 Cor

| Token | Hex | Papel |
|---|---|---|
| `--navy-700` | `#244A69` | a cor do PSIF: botão primário, título, número, nome em lista, ícone ativo, link |
| `--navy-800` | `#1D3B54` | hover do botão primário |
| `--navy-900` | `#162E41` | pressionado do botão primário |
| `--navy-500` | `#5586A3` | ilustração e marcador, nunca texto |
| `--sky-100` | `#CFE7F5` | fundo de toda tela |
| `--sky-300` | `#A4C7E4` | fundo de atalho e de avatar sem foto |
| `--blue-700` | `#1760B1` | só marca |
| `--blue-300` | `#72BAFC` | só marca: fundo do quadrado do símbolo |
| `--ink-900` | `#000000` | texto principal |
| `--ink-700` | `#616161` | texto secundário |
| `--ink-600` | `#7D7D7D` | borda de campo, ícone inativo |
| `--ink-500` | `#999999` | trilho e separador |
| `--ink-200` | `#E8E8E8` | divisória, esqueleto |
| `--ink-100` | `#F3F3F3` | hover, fundo afundado |
| `--white` | `#FFFFFF` | cartão, campo, folha |
| `--success-700` | `#0E782E` | situação positiva |
| `--success-100` | `#E3F1E7` | fundo de selo positivo |
| `--warning-700` | `#8A5300` | atenção: pendente, alerta, sigiloso |
| `--warning-100` | `#FDF3D6` | fundo de aviso |
| `--danger-700` | `#B42318` | erro, ação destrutiva |
| `--danger-100` | `#FDECEA` | fundo de erro |

### 3.2 Contraste

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
--ink-700 / --ink-100: 5.58:1 ✓ AA
```

Linhas sobre o céu (§3.5), medidas como interface (piso 3:1):

```
--line-on-sky / --sky-100      1.77:1  ✗ sozinha: só onde o texto identifica o controle
--line-on-sky / #fff           1.86:1  ✗ sozinha: idem
--divider-on-sky / --sky-100   1.20:1  decorativa
```

`--line-on-sky` só agrupa: no filtro e na área de envio, o rótulo escrito
identifica o controle (WCAG 1.4.11). Campo vazio só se reconhece pelo
contorno, por isso leva borda `--ink-600` (§8.3).

Pares que reprovam como texto (a banlist de `tokens.json`):

```
--ink-600 / #fff          4.12:1  ✗ texto · ✓ interface (borda, ícone)
--ink-600 / --sky-100     3.22:1  ✗ texto · ✓ interface
--success-700 / --sky-100 4.38:1  ✗ texto: situação só sobre cartão
--navy-500 / --sky-100    3.08:1  ✗ texto · ✓ interface, por pouco
--ink-500 / #fff          2.85:1  ✗ texto · ✗ interface
```

Par fora destas tabelas: `scripts/check_contrast.py <texto> <fundo>`.

### 3.3 Dominância

- **~60% neutro**: céu no fundo, branco nos cartões.
- **~30% estrutural**: `--navy-700` em título, número, nome, ícone e no botão
  primário.
- **Sem cor de acento**: `--blue-*` só na marca (§1.4).

`scripts/check_dominance.py` mede a proporção no CSS de tokens do projeto.
