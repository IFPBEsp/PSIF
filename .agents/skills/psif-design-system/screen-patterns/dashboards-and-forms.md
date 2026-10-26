## 14. PAINEL (INÍCIO)

O Início é o único painel do PSIF.

### 14.1 Hierarquia de leitura (de cima para baixo)

1. Saudação (§7.3).
2. Indicadores (§9.2): o estado do dia.
3. Próximos atendimentos (§9.3): o que vem agora.
4. Ações rápidas (§7.8): atalhos.

### 14.2 Indicadores do painel

Quatro, sempre os mesmos: atendimentos hoje, alunos ativos, relatórios
pendentes, alertas importantes. Indicador novo entra no lugar de um destes,
não como quinta célula.

### 14.3 Cartões do painel

No celular, três cartões, nesta ordem, com `--sp-6` entre eles; no web, a
composição de §14.7, que acrescenta Meus alunos e Notificações recentes. Nenhum cartão decorativo ou de boas-vindas além da
saudação.

### 14.4 Filtros do painel

Não há. O Início é sempre "hoje, meus alunos".

### 14.5 Resumo

Número com rótulo em frase completa. Se houver alerta, o indicador "Alertas
importantes" leva à lista (§10.1).

### 14.6 Detalhamento

Cada indicador e cada linha de "Próximos atendimentos" é tocável e leva à
lista ou ao perfil correspondente.

### 14.7 Início no web

A barra lateral libera largura; ela vai para o que a psicopedagoga abriria em
seguida, não para enfeite, e nenhuma coluna fica vazia:

1. Alerta de pendência (§10.1), quando há: "Acompanhamento pendente", com
   "Ver aluno".
2. Indicadores em linha de 4 (§9.2).
3. Grade do painel (§5.3), em 3 colunas a partir de `--bp-lg`:
   - **Esquerda (2):** Próximos atendimentos, com horário em `--fs-h1` e tipo
     em `--fs-caption` (a mesma linha da Agenda, §9.3); embaixo, **Meus
     alunos**: cartão de lista com avatar `--target-min`
     (`.psif-avatar--pequeno`), nome, turma e a situação como terceira linha
     (§12.2), e "Ver todos".
   - **Direita (1):** Ações rápidas e, embaixo, Notificações recentes: as três
     últimas, em linhas com o título, a frase e o tempo de §9.5, e "Ver
     todas".

Entre `--bp-md` e `--bp-lg`, os mesmos cartões em coluna única, na ordem
acima.

Sigilo (§16.3): Meus alunos e Notificações recentes mostram só nome, turma,
situação e o fato, nunca dado clínico.

Calendário não entra: numa coluna de 1/3 o dia fica menor que o alvo de
toque (§11.6).

## 15. FORMULÁRIOS AVANÇADOS

### 15.1 Formulários longos

O PSIF não tem formulário longo: Novo atendimento tem quatro campos (Aluno,
Data, Tipo de atendimento, Descrição); Relatórios tem três blocos (Relatório
semanal, Síntese de desenvolvimento do mês, Status do ciclo). Rótulo acima.

- **Celular:** coluna única.
- **Web:** grade de 3 colunas para campo curto (Aluno · Data · Tipo); campo
  de texto longo (`textarea`) e o que não é campo ocupam a linha inteira. Sem
  largura máxima (§5.2).

### 15.2 Formulário em etapas

Não há. Se um formulário passar de uma tela, divida em seções no mesmo
formulário antes de pensar em etapas.

### 15.3 Rascunho automático

Atendimento e relatório salvam rascunho local enquanto se digita. Voltar com
conteúdo pergunta antes de descartar (§10.3). Abrir de novo recupera o
rascunho com aviso "Rascunho recuperado".

### 15.4 Validação

Ao sair do campo e ao salvar, nunca a cada tecla. Obrigatórios: Aluno, Data,
Tipo. Data no futuro é aceita só na Agenda.

Obrigatório não ganha marca; **opcional** ganha "(opcional)" no rótulo,
"Descrição (opcional)" (§8.3). No PSIF quase todo campo é obrigatório:
marcar a exceção é menos ruído que um asterisco em cada rótulo, e não depende
de legenda. Campo nativo obrigatório leva `aria-required="true"`; na seleção
em folha (§8.4), a obrigatoriedade aparece na validação ("Selecione o
aluno.").

### 15.5 Feedback de envio

Botão vira "Salvando…" e bloqueia. Sucesso ao criar leva aos detalhes do que
foi criado; ao editar, fica na tela. Os dois com toast (§10.2). Falha mantém
tudo preenchido e mostra o erro onde §10.7 manda.

### 15.6 Campos, seleção, busca e envio

Ver §8.3–§8.7.
