## 26. PERFORMANCE

### 26.1 Por que isto é uma restrição de qualidade, não um extra

O PSIF roda no celular da psicopedagoga, muitas vezes na rede da escola.
Tela lenta no meio de um atendimento é tela que não se usa.

### 26.2 Listas longas

Alunos ativos passam de cem (o Início mostra 120). Lista com busca e filtro,
paginada ou virtualizada; nunca renderizar todos os cartões com foto de uma
vez.

### 26.3 Imagens e uploads

- Foto de aluno em miniatura (80px) carregada sob demanda; sem foto, iniciais
  (§12.1).
- Documento (laudo, relatório em PDF) mostra nome, tamanho e data na lista;
  o arquivo só baixa ao abrir.

### 26.4 Entradas de alta frequência

Busca de aluno e de documento com espera de ~300ms após a digitação antes de
filtrar.

### 26.5 Percepção de carregamento

Esqueleto no formato do cartão (§10.5), nunca tela em branco. O splash não
segura o usuário depois que o app está pronto.

### 26.6 Rede instável e modo degradado

Formulário de atendimento e relatório guarda rascunho local (§15.3). Envio
que falhou fica marcado na lista e pode ser repetido.
