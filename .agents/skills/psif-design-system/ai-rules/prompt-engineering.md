## 22. COMO A IA DEVE INTERPRETAR ESTA SKILL

### 22.1 Hierarquia de prioridades

A ordem é a da regra de ouro do `SKILL.md`: sigilo, acessibilidade,
consistência, protótipo. Por isso a skill **corrige** o protótipo onde ele reprova (texto cinza,
alvo de toque, rótulo só em placeholder), e registra cada correção em §28.

### 22.2 Dominância de cor: a regra que mais se erra

O erro típico ao gerar tela do PSIF: cabeçalho marinho, cartão marinho,
selo marinho. O marinho é ação e dado; área é céu e branco (§3.3).

### 22.3 Reutilizar vs. criar componente (árvore de decisão)

1. Existe em §7–§13? Use.
2. Dá para montar com cartão + linha de lista + campo + botão? Monte.
3. Só então crie, e acrescente uma linha à tabela de §6.

### 22.4 Quando simplificar vs. adensar

Celular, uma mão, entre atendimentos: simplifique. Uma coluna, um primário,
listas curtas com busca.

### 22.5 Preencher lacunas com coerência

Estado que o protótipo não desenha (vazio, erro, carregando) sai de §10 com
os tokens existentes. Valor novo não se inventa: vai para §28 como derivado.

## 23. PROMPTS PARA GERAR TELAS CONSISTENTES

### 23.1 Regras invioláveis

As do `SKILL.md` valem para todo prompt. Na geração, as que mais escapam:
token banido como texto (banlist do cheat sheet) e cor de tema escrita na
tela (`dark:`, hex escuro), quando o tema sai dos tokens (§26).

### 23.2 O que todo prompt de geração deve fixar

Qual estrutura de tela (§13.1–§13.7), qual é a ação primária, que dados
aparecem e com que nível de sigilo, e quais estados (vazio, erro,
carregando) a tela precisa.

### 23.3 Modelo de prompt (preencher)

```
Gere a tela <nome> do PSIF usando a skill psif-design-system.
Estrutura: <§13.x>. Ação primária: "<verbo + objeto>".
Quem vê: <psicopedagoga | professor | aluno | responsável>.
Dados: <campos>, com sigilo <nenhum | perfil | documento sensível>.
Estados: cheio, vazio ("<frase>"), erro, carregando.
Use os componentes de §6 e as utilitárias de §27.6; confira nos temas claro e escuro.
```

### 23.4 Como validar a saída de uma IA

Rode `check_checklist.py` (e `lint_output.py` como complemento) no que foi gerado; corrija todo
`[ERRO]`; passe pelos itens manuais de §25.
