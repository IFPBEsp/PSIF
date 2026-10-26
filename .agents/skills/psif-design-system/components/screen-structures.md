## 13. ESTRUTURAS DE TELA

Inventário do protótipo: 14 quadros de celular + página pública. Cada tela
nova do PSIF é uma destas estruturas.

### 13.1 Tela de lista

Meus alunos, Documentos, Notificações. Barra superior (§7.3) → busca (§7.7)
→ filtros (§7.6), se houver → cartões ou cartão de lista → botão "+
Adicionar …" no rodapé, se a lista aceita item novo. No web, busca e filtros
dividem a mesma linha, e os cartões vão para a grade de §5.3.

### 13.2 Tela de detalhe (perfil do aluno)

Barra superior com o nome do aluno como título → avatar `--avatar-lg` centralizado
→ cartão de dados (Curso · Turma · Matrícula em três colunas com rótulo
`--fs-body` `--ink-700` e valor `--fs-body` peso 500 `--navy-700`; Situação
embaixo, §12.2) → menu de seções (§7.5).

No web, duas colunas (§5.3): à esquerda (1), avatar, cartão de dados e menu
de seções; à direita (2), o que se abre o perfil para ver: o próximo
atendimento e a Evolução recente (§11.5), com "Ver evolução completa".

### 13.3 Formulário

Novo atendimento, Relatórios. Barra superior → campos sobre o fundo céu,
rótulo acima de cada campo (§8.3) → botão primário fixo no rodapé com o
verbo da tela. Detalhe em §15.

### 13.4 Autenticação

Login, Recuperar senha. Fundo céu, cartão de autenticação central (§9.8).
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
