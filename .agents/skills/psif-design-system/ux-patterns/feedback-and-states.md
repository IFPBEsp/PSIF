## 10. FEEDBACK E ESTADOS

O protótipo só desenha o estado "cheio". Tudo nesta seção é derivado com os
tokens existentes.

### 10.1 Alertas e avisos fixos

Cartão no topo do conteúdo: fundo `--warning-100` (atenção) ou
`--danger-100` (erro), texto `--fs-small` na cor `-700` da mesma família,
ícone à esquerda, ação em link à direita ("Ver alunos"). "Alertas
importantes" do Início leva a uma lista destes.

### 10.2 Aviso rápido (toast)

O projeto usa Sonner (seção 11 de `docs/frontend/architecture-and-stack.md`).
O toast cobre o feedback pontual de uma ação:

- **Sucesso**: "Atendimento salvo." Some em 4 segundos.
- **Erro de negócio ou de integração**: o que houve e o que fazer, sem detalhe
  técnico ("Não foi possível salvar o atendimento. Tente de novo."). Fica até
  ser fechado ou ter ação ("Tentar de novo").
- **Aviso**: algo que a pessoa precisa saber agora e não bloqueia.

Visual no tema do PSIF: o `Toaster` usa as cores da ponte (§27.3), cartão
`--surface-overlay` com texto `--ink-900`; sucesso com ícone `--success-700`,
erro com ícone e texto `--danger-700`, aviso com ícone `--warning-700`. Estado nunca
só na cor: ícone e texto dizem o tipo. `--z-toast`, acima do botão de rodapé no
celular. O Sonner já anuncia ao leitor de tela; não duplique `role`.

Toast não serve para:

- **Erro de campo.** Fica no campo (§10.7).
- **Informação permanente** ou que a pessoa vai consultar depois. Isso é
  alerta fixo (§10.1).
- **Dado sensível.** O toast pode aparecer com a tela virada para a família:
  "Documento enviado.", nunca o nome do laudo (§16.3).

### 10.3 Confirmação de descarte

Voltar de formulário com conteúdo abre folha (§9.6): "Descartar este
atendimento?" com "Continuar editando" (primário) e "Descartar" (texto
`--danger-700`, `.psif-botao--texto-perigo`). O foco abre em "Continuar
editando"; Esc e o véu cancelam. Montada em `exemplos/novo-atendimento.html`.

### 10.4 Progresso

Barra do splash: trilho `--ink-500`, preenchimento branco. Em tela de
trabalho, progresso é o rótulo do botão ("Enviando…").

### 10.5 Carregando (esqueleto)

Esqueleto no formato do componente (cartão de aluno, linha de lista) em
`--ink-200` sobre o cartão branco. Sem spinner solto no meio da tela, e nunca
tela em branco: o PSIF roda no celular, muitas vezes na rede da escola. O
splash não segura o usuário depois que o app está pronto.

### 10.6 Estado vazio

Dentro do cartão que estaria cheio: uma frase do que não há, uma do porquê
ou do próximo passo, e a ação.

- "Nenhum atendimento hoje." + "+ Novo agendamento"
- "Nenhum documento anexado." + "+ Adicionar documento"
- "Nenhum aluno encontrado para "Mar"." + "Limpar busca"

### 10.7 Erro

O tipo de erro decide onde ele aparece (seção 11 da doc de frontend do
projeto):

- **Validação de campo**: abaixo do campo, `--fs-small` `--danger-700`,
  dizendo o que fazer ("Informe a data do atendimento"). Erro de campo vindo do
  backend entra no mesmo lugar, por `form.setError`.
- **Erro de negócio ou de integração no envio**: toast de erro (§10.2), ou
  alerta (§10.1) quando a mensagem precisa ficar na tela. O que foi digitado
  fica.
- **Sem acesso (403)** e **não encontrado (404)**: tela própria, com o que
  houve e quem libera (§10.8).
- **Erro inesperado**: tela de erro com "Tentar de novo", nunca o texto da
  exceção.

### 10.8 Dados reais e limites

A tela é desenhada com dado de verdade, não só com o caso bonito do
protótipo:

- **Nome longo** ("Maria Eduarda dos Santos Albuquerque") quebra em até duas
  linhas no cartão e na lista, e aparece inteiro no perfil. Filho de flex ou
  grid com texto leva `min-width: 0`.
- **Número grande** com ponto de milhar: "1.234 alunos" (§19.3).
- **Lista longa** pagina ou carrega sob demanda (§11.8); alunos ativos passam
  de cem, e nunca se renderizam todos os cartões com foto de uma vez; lista
  vazia é estado
  vazio (§10.6).
- **Sem acesso** (professor fora da turma, sessão expirada): diz o que houve
  e quem libera: "Você não tem acesso a este aluno. Fale com a
  psicopedagoga.", nunca uma tela em branco.
- **Sem rede**: o que foi digitado fica (rascunho, §15.3) e a ação oferece
  "Tentar de novo".
- Nenhuma largura fixa em contêiner de texto: ele cresce com o texto
  (§20.13).
