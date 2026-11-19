## 13. ESTRUTURAS DE TELA

Cada tela nova do PSIF é uma destas estruturas.

### 13.1 Tela de lista

Meus alunos, Documentos, Notificações. Barra de ações (§7.3) → busca (§7.7)
→ filtros (§7.6), se houver → cartões ou cartão de lista → botão "+
Adicionar …", se a lista aceita item novo. A partir de `--bp-md`, busca e
filtros dividem a mesma linha, e alunos e documentos viram tabela (§11.8).

### 13.2 Tela de detalhe (perfil do aluno)

**Tela estreita**: barra de ações só com voltar ("Voltar para Alunos") e ⋯
("Mais ações do aluno") → cabeçalho: avatar `--avatar-md` à esquerda; à
direita, nome em `--fs-display` 600 `--navy-700`, "Curso · Turma ·
Matrícula" em `--fs-small` `--ink-700` e o selo de situação (§12.2) → cartão
Próximo atendimento (§9.10) → título de grupo "Prontuário" e a grade de
seções (§7.5). Contato e responsáveis ficam em "Dados do aluno".

**A partir de `--bp-md`**: cabeçalho do aluno com abas (§9.9, §7.5); a aba
aberta ocupa o conteúdo. Em Documentos, na tela larga: tabela (§11.8) à
esquerda e, numa coluna `--w-aside` à direita, área de envio (§8.5) e aviso de
sigilo (§9.11). Na faixa intermediária, a coluna lateral desce para baixo da
tabela.

### 13.3 Formulário

Novo atendimento, Relatórios. Barra de ações → campos sobre o fundo céu,
rótulo acima de cada campo (§8.3) → botão primário com o verbo da tela
(§5.6). Detalhe em §15.

### 13.4 Autenticação

Login, Recuperar senha. Fundo céu, cartão de autenticação central (§9.8).

- **Login**: símbolo e "PSIF", nome por extenso, e-mail e senha com ícone e
  borda (§8.3), "Mostrar senha" (§20.7), "Lembrar-me" (§8.7) e "Esqueceu a
  senha?", "Entrar" e, no rodapé do cartão, "Não tem acesso? Fale com a
  psicopedagoga do campus."
- **Recuperar senha**: voltar, título, texto de orientação, campo de e-mail,
  "Enviar instruções" e "Voltar para o login".

### 13.5 Início (painel)

Ver §14.

### 13.6 Página pública

Cabeçalho branco (símbolo e "PSIF" à esquerda; "Entrar" compacto à direita e
☰ na tela estreita) → selo "Plataforma institucional" → título `--fs-display`
→ descrição `--fs-body` `--ink-700` → "Entrar no sistema" (primário) e "Saiba
mais" (secundário) → "Funcionalidades principais" com cartões de
funcionalidade (§9.7, grade em §5.3). Conteúdo até `--w-content` (§5.2).
