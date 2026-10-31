## 19. LINGUAGEM DE INTERFACE

Português do Brasil, frase curta, tom de colega de trabalho.

### 19.1 Rótulos de botão

Verbo + objeto, e o objeto é o da tela:

| Tela | Rótulo |
|---|---|
| Novo atendimento | Salvar atendimento |
| Relatórios | Salvar relatório (o protótipo repete "Salvar o atendimento", que é erro) |
| Agenda | + Novo agendamento |
| Documentos | + Adicionar documento |
| Login | Entrar |
| Recuperar senha | Enviar instruções |

Sem artigo no rótulo ("Salvar atendimento", não "Salvar o atendimento").

### 19.2 Vocabulário do domínio

| Use | Não use |
|---|---|
| atendimento | sessão, consulta, ticket |
| aluno / aluna | paciente, usuário, cliente |
| acompanhamento (em, pendente, encerrado) | status, caso aberto |
| psicopedagoga / psicopedagogo | admin, operador |
| relatório, laudo, prontuário | documento técnico, ficha |
| evolução | histórico de progresso, timeline |
| turma, série, período, matrícula, curso | grupo, nível, ID |
| aluno com necessidade específica | aluno especial, aluno de inclusão, portador de deficiência |
| deficiência · dificuldade: uma não é sinônimo da outra | problema, limitação |

O nome da deficiência ou da dificuldade é dado de saúde: aparece só no perfil
do aluno, nunca em lista, notificação ou indicador (§16.3).

Nenhum termo em inglês na tela: nada de "Loading", "Status", "Dashboard",
"Upload".

### 19.3 Formatos (padrão brasileiro)

- Data: `15/06/2026`. Mês por extenso no calendário: "Junho 2026".
- Hora: `09:00`, 24 horas.
- Tempo relativo em notificação: "Há 15 min", "Há 1 hora", "Há 2 horas",
  "Ontem".
- Tamanho de arquivo: "12 MB".
- Ano escolar: "3º ano", não "3 ano".
- Número: ponto como separador de milhar ("1.234").

### 19.4 Tom e mensagens

- Saudação: "Olá, Ana!", com o primeiro nome e vírgula, não ponto; nunca o
  papel (§16.2). Embaixo, a data de hoje, sem exclamação.
- Erro diz o que fazer, não de quem é a culpa.
- Notificação: título curto do fato + uma frase de contexto, sem dado
  sensível (§16.3).

Texto de interface sem vício de texto gerado:

- **Comece pelo fato.** Corte abertura vazia ("Aqui está", "Vale lembrar
  que", "É importante notar"): "Atendimento salvo.", não "Pronto! Seu
  atendimento foi salvo com sucesso."
- **Sem advérbio de ênfase**: "realmente", "simplesmente", "apenas",
  "facilmente", "rapidamente" não acrescentam nada.
- **Voz ativa, com quem age**: "A psicopedagoga liberou o relatório", não
  "O relatório foi liberado". Na mensagem para quem usa, "você".
- **Diga o que é**, sem a volta do "não é X, é Y".
- **Um ponto de exclamação no app inteiro**: o da saudação.
- **Sem travessão em texto de tela**: use vírgula ou ponto.

### 19.5 Ortografia: erros do protótipo que não passam para o produto

| No protótipo | Correto |
|---|---|
| Relatório pentende | Relatórios pendentes |
| atendimento de hoje | Atendimentos hoje |
| Relatorios / Relatorio Semanal | Relatórios / Relatório semanal |
| Relátorio psicologico.pdf | Relatório psicológico.pdf |
| Laudo medico.pdf | Laudo médico.pdf |
| Declação.pdf | Declaração.pdf |
| informe o seu E-gmail | Informe seu e-mail |
| Serie · Periodo | Série · Período |
| Informatica - 3 ano | Informática · 3º ano |
| Dados dos Alunos (no perfil de uma aluna) | Dados do aluno |
| Cadastre-se acompanhe todos os atendimentos | Cadastre e acompanhe todos os atendimentos |
| Olá. Psicopedagoga! | Olá, Ana! |
| Descreva o Atendimento.... | Descreva o atendimento… |
