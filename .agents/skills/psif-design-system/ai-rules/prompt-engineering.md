## 22. COMO A IA DEVE INTERPRETAR ESTA SKILL

### 22.1 Hierarquia de prioridades (em conflito, o de cima vence)

1. Sigilo do aluno (§16.3).
2. Acessibilidade WCAG 2.2 AA (§20).
3. Consistência com o catálogo (§6–§13).
4. Fidelidade ao protótipo.

Por isso a skill **corrige** o protótipo onde ele reprova (texto cinza,
alvo de toque, rótulo só em placeholder), e registra cada correção em §29.

### 22.2 Dominância de cor: a regra que mais se erra

O erro típico ao gerar tela do PSIF: cabeçalho marinho, cartão marinho,
selo marinho. O marinho é ação e dado; área é céu e branco (§3.3).

### 22.3 Reutilizar vs. criar componente (árvore de decisão)

1. Existe em §7–§13? Use.
2. Dá para montar com cartão + linha de lista + campo + botão? Monte.
3. Só então crie, e acrescente ao catálogo (§6).

### 22.4 Quando simplificar vs. adensar

Celular, uma mão, entre atendimentos: simplifique. Uma coluna, um primário,
listas curtas com busca.

### 22.5 Preencher lacunas com coerência

Estado que o protótipo não desenha (vazio, erro, carregando) sai de §10 com
os tokens existentes. Valor novo não se inventa: vai para §29 como derivado.

## 23. PROMPTS PARA GERAR TELAS CONSISTENTES

### 23.1 Regras invioláveis (a IA nunca faz)

- Hex, px de raio ou sombra fora de `var(--token)`.
- `--ink-600` (`#7D7D7D`) como texto.
- Campo sem rótulo visível (exceto busca, §7.7).
- Emoji como ícone ou marcador.
- Dado clínico em lista, notificação ou pré-visualização.
- Cor de tema escrita na tela (`dark:`, hex escuro): o tema escuro sai dos
  tokens (§27).

### 23.2 O que todo prompt de geração deve fixar

Qual estrutura de tela (§13.1–§13.7), qual é a ação primária, que dados
aparecem e com que nível de sigilo, e quais estados (vazio, erro,
carregando) a tela precisa.

### 23.3 Modelo de prompt (preencher)

```
Gere a tela <nome> do PSIF usando a skill psif-design-system.
Estrutura: <§13.x>. Ação primária: "<verbo + objeto>".
Dados: <campos>, com sigilo <nenhum | perfil | documento sensível>.
Estados: cheio, vazio ("<frase>"), erro, carregando.
Cole assets/tokens.css; nenhum valor fora de var(--token).
```

### 23.4 Como validar a saída de uma IA

Rode `lint_output.py` e `check_checklist.py` no arquivo gerado; corrija todo
`[ERRO]`; passe pelos itens manuais de §25.
