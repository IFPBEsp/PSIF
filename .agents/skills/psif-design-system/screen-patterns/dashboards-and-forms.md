## 14. PAINEL (INÍCIO)

O Início é o único painel do PSIF.

### 14.1 Hierarquia e regras

De cima para baixo, com `--sp-6` entre os cartões:

1. Saudação (§7.3).
2. Alerta de pendência (§10.1), quando há: "Acompanhamento pendente", com
   "Ver aluno".
3. Indicadores (§9.2): sempre os quatro. Indicador novo substitui um deles,
   não vira quinta célula.
4. Próximos atendimentos (§9.3).
5. Ações rápidas (§7.8).

Sem filtro: o Início é sempre "hoje, meus alunos". Sem cartão decorativo ou
de boas-vindas além da saudação. Cada indicador e cada linha leva à lista ou
ao perfil.

### 14.2 Início na tela larga

A largura extra vai para o que a psicopedagoga abriria em seguida, e nenhuma
coluna fica vazia. Abaixo dos indicadores, a grade do painel (§5.3):

- **Principal (2 colunas):** Próximos atendimentos, na linha da Agenda
  (§9.3); embaixo, **Meus alunos**: cartão de lista com avatar
  `--target-min`, nome, turma e situação (§12.2), e "Ver todos".
- **Apoio (1 coluna):** Ações rápidas e, embaixo, Notificações recentes: as
  três últimas, no formato de §9.5, e "Ver todas".

Na faixa intermediária, os mesmos cartões em coluna única, nessa ordem.

Meus alunos e Notificações recentes mostram só nome, turma, situação e o
fato (§16.3). O calendário fica na Agenda (§11.6); o Início já mostra os
próximos atendimentos.

## 15. FORMULÁRIOS

### 15.1 Tamanho e grade

Novo atendimento tem quatro campos (Aluno, Data, Tipo de atendimento,
Descrição); Relatórios tem três blocos (Relatório semanal, Síntese de
desenvolvimento do mês, Situação do ciclo). Rótulo acima. Grade por faixa em
§5.3: campo curto divide a linha (Aluno · Data · Tipo); texto longo e o que
não é campo ocupam a linha inteira.

### 15.2 Formulário em etapas

Não há. Formulário que passar de uma tela ganha seções no mesmo formulário.

### 15.3 Rascunho automático

Atendimento e relatório salvam rascunho enquanto se digita, em
`sessionStorage`: o rascunho pode ter dado sensível (§16.3) e o computador
da escola é compartilhado. Sobrevive a recarregar, voltar e cair a rede;
some quando a aba fecha.

- Chave com o id do usuário: `psif:rascunho:<usuario>:<formulario>`.
- Apagado ao salvar, ao descartar e no logout.
- Rascunho que precise durar mais vai para o backend, nunca para
  `localStorage`.
- Abrir de novo recupera com o aviso "Rascunho recuperado".
- Envio que falhou por rede fica marcado na lista e pode ser repetido.

Voltar com conteúdo pergunta antes de descartar (§10.3).

### 15.4 Validação

Ao sair do campo e ao salvar, nunca a cada tecla. Obrigatórios: Aluno, Data,
Tipo. Data no futuro só na Agenda.

Obrigatório não ganha marca; opcional ganha "(opcional)" no rótulo (§8.3).
Campo nativo obrigatório leva `aria-required="true"`; na seleção (§8.4), a
obrigatoriedade aparece na validação ("Selecione o aluno.").

### 15.5 Feedback de envio

Botão vira "Salvando…" e bloqueia. Ao criar, sucesso leva ao detalhe do que
foi criado; ao editar, fica na tela. Os dois com toast (§10.2). Falha mantém
tudo preenchido e mostra o erro como §10.7 manda.

### 15.6 Campos, seleção, busca e envio

Ver §8.3–§8.7.
