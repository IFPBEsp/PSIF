## 13. ESTRUTURAS DE TELA

Inventário do protótipo: 14 quadros de celular + página pública. Cada tela
nova do PSIF é uma destas estruturas.

### 13.1 Tela de lista

Meus alunos, Documentos, Notificações. Barra superior (§7.3) → busca (§7.7)
→ filtros (§7.6), se houver → cartões ou cartão de lista → botão "+
Adicionar …" no rodapé, se a lista aceita item novo. No web, busca e filtros
dividem a mesma linha, e alunos e documentos viram tabela (§11.8).

### 13.2 Tela de detalhe (perfil do aluno)

**Celular**: barra superior só com ações (voltar, "Voltar para Alunos", e ⋯,
"Mais ações do aluno") → cabeçalho: avatar `--avatar-md` à esquerda; à
direita, nome em `--fs-display` 600 `--navy-700`, "Curso · Turma · Matrícula"
em `--fs-small` `--ink-700` e o selo de situação (§12.2) → cartão Próximo
atendimento (§9.11) → título de grupo "Prontuário" e a grade de seções
(§7.5). Os dados completos (contato, responsáveis) ficam em "Dados do aluno".

**Web**: cabeçalho do aluno com abas (§9.10, §7.5); a aba aberta ocupa o
conteúdo. Em Documentos: tabela (§11.8) à esquerda e, em coluna de 320px à
direita, área de envio (§8.5) e aviso de sigilo (§9.12). Abaixo de
`--bp-lg` a coluna lateral desce para baixo da tabela.

### 13.3 Formulário

Novo atendimento, Relatórios. Barra superior → campos sobre o fundo céu,
rótulo acima de cada campo (§8.3) → botão primário fixo no rodapé com o
verbo da tela. Detalhe em §15.

### 13.4 Autenticação

Login, Recuperar senha. Fundo céu, cartão de autenticação central (§9.8).
Login: logo, nome por extenso, e-mail e senha com ícone e borda (§8.3),
"Mostrar senha" (§20.7), "Lembrar-me" (§8.7) e "Esqueceu a senha?", "Entrar",
"Não tem acesso? Fale com a psicopedagoga do campus." e a assinatura (§1.2).
Recuperar senha: voltar, título, texto de orientação, campo de e-mail, botão
"Enviar instruções", link "Voltar para o login" e a ilustração de envelope e
cadeado no rodapé.

### 13.5 Splash

Tela inteira `--surface-brand`. Centro: ícone do app (`--ic-brand`), "PSIF"
em `--fs-splash` branco, "Plataforma de Suporte Psicopedagógico" em
`--fs-splash-sub` branco. Rodapé: barra de progresso branca sobre trilho
`--ink-500`. Única tela marinha do sistema.

### 13.6 Início (painel)

Ver §14.

### 13.7 Página pública

Cabeçalho branco (ícone do app em quadrado `--navy-700` à esquerda; "Entrar"
compacto e ☰ à direita) → selo "Plataforma institucional" → título
`--fs-display` → descrição `--fs-body` `--ink-700` → "Entrar no sistema"
(primário) e "Saiba mais" (secundário) → "Funcionalidades principais" com
cartões de funcionalidade (§9.7).
