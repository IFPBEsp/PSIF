## 22. COMO A IA DEVE INTERPRETAR ESTA SKILL

- **Prioridades**: sigilo, acessibilidade, consistência, nessa ordem
  (`SKILL.md`).
- **Erro mais comum**: marinho em área grande, como cabeçalho ou cartão
  marinho (§2.2).
- **Reutilizar antes de criar**: o que existe em §7–§13 se usa; o que dá para
  montar com cartão, linha de lista, campo e botão se monta. Componente novo
  ganha uma linha na tabela de §6.
- **Lacuna**: estado não descrito (vazio, erro, carregando) sai de §10 com os
  tokens existentes. Valor novo não se inventa; decisão de produto em aberto
  fica em §27.

## 23. PROMPTS PARA GERAR TELAS

Todo prompt de geração fixa a estrutura (§13), a ação primária, os dados e o
nível de sigilo, e os estados que a tela precisa:

```
Gere a tela <nome> do PSIF usando a skill psif-design-system.
Estrutura: <§13.x>. Ação primária: "<verbo + objeto>".
Quem vê: <psicopedagoga | professor | aluno | responsável>.
Dados: <campos>, com sigilo <nenhum | perfil | documento sensível>.
Estados: cheio, vazio ("<frase>"), erro, carregando.
Larguras: estreita, intermediária e larga; toque e mouse.
Temas: claro e escuro.
```

A saída passa pelo "Antes de entregar" do `SKILL.md` e pelo checklist de §24.
