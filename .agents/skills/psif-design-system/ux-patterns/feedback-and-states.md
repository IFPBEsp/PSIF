## 10. FEEDBACK E ESTADOS

### 10.1 Alertas fixos

Cartão no topo do conteúdo, fundo `--warning-100` (atenção) ou `--danger-100`
(erro), texto `--fs-small` na cor `-700` da família, ícone à esquerda e ação
em link à direita ("Ver alunos"). "Alertas importantes" do Início leva à
lista deles.

### 10.2 Toast

Sonner, com as cores da ponte (§26.3): cartão `--surface-overlay`, texto
`--ink-900`, ícone na cor do tipo (`psif-sucesso` em `--success-700`, erro em
`--danger-700`, aviso em `--warning-700`). `--z-toast`, acima da barra de
ação. O Sonner já anuncia ao leitor de tela.

- **Sucesso**: "Atendimento salvo." Some em 4 segundos.
- **Erro de negócio ou de integração**: o que houve e o que fazer ("Não foi
  possível salvar o atendimento. Tente de novo."). Fica até ser fechado.
- **Aviso**: algo que a pessoa precisa saber agora e não bloqueia.

Não é toast: erro de campo (§10.7) e informação que fica (§10.1). Texto do
toast segue o sigilo de §16.3.

### 10.3 Confirmação de descarte e de exclusão

Em folha ou diálogo (§9.6):

- Voltar de formulário com conteúdo: "Descartar este atendimento?";
  "Continuar editando" (primário, foco inicial) e "Descartar" (texto
  `--danger-700`). Esc e o véu cancelam.
- Excluir: "Excluir este documento?", o que sai ("Laudo médico.pdf sai do
  prontuário de José Antonio.") e "Não dá para desfazer."; "Manter documento"
  (primário, foco inicial) e "Excluir" (texto `--danger-700`, hover
  `--danger-100`). `role="alertdialog"`.

### 10.4 Progresso

O progresso de uma ação é o rótulo do botão ("Enviando…"). Envio de arquivo
longo usa `Progress`: trilho `--ink-200`, preenchimento `--navy-700`.

### 10.5 Carregando

Esqueleto no formato do componente, em `--ink-200`, blocos com `--radius-md`
e, na linha de lista, um quadro de `--tile-icon`. Nunca spinner solto nem
tela em branco: muita gente abre o PSIF na rede da escola.

### 10.6 Estado vazio

Dentro do cartão que estaria cheio: o que não há, o porquê ou o próximo passo,
e a ação.

- "Nenhum atendimento hoje." e "+ Novo agendamento"
- "Nenhum documento anexado." e "+ Adicionar documento"
- "Nenhum aluno encontrado para "Mar"." e "Limpar busca"

### 10.7 Erro

- **Campo**: abaixo do campo, `--fs-small` `--danger-700`, dizendo o que
  fazer ("Informe a data do atendimento"). Erro de campo do backend entra no
  mesmo lugar, por `form.setError`.
- **Envio** (negócio ou integração): toast de erro, ou alerta quando a
  mensagem precisa ficar. O que foi digitado fica.
- **Sem acesso (403) e não encontrado (404)**: tela própria com o que houve e
  quem libera.
- **Inesperado**: tela de erro com "Tentar de novo", nunca o texto da
  exceção.

### 10.8 Dado real

- **Nome longo** ("Maria Eduarda dos Santos Albuquerque") quebra em até duas
  linhas em lista e aparece inteiro no perfil. Filho de flex ou grid com texto
  leva `min-width: 0`.
- **Número grande** com ponto de milhar: "1.234 alunos" (§19.3).
- **Lista longa** pagina ou carrega sob demanda (§11.8).
- **Sem acesso**: "Você não tem acesso a este aluno. Fale com a
  psicopedagoga."
- **Sem rede**: o que foi digitado fica (§15.3) e a ação oferece "Tentar de
  novo".
- Contêiner de texto sem altura fixa (§20.13).
