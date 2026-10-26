## 24. ANTI-PADRÕES (o que nunca fazer)

### 24.1 Cor e identidade

- Área grande em `--navy-700` fora do splash (cabeçalho, cartão, faixa).
- `--blue-*` fora da marca.
- Segunda versão do marinho (`#144960`) ou do preto (`#1A1A1A`).
- Sombra preta.
- Texto secundário em `--ink-600`.

### 24.2 Tokens, tipografia e espaçamento

- Valor literal no lugar de `var(--token)`.
- Texto abaixo de 12px.
- Título de tela fora do padrão (§4.3): preto, à esquerda, outro tamanho.
- Raio diferente de `--radius-md` em retângulo.
- Campo com fonte abaixo de 16px (o iPhone dá zoom ao focar, §8.3).
- Texto corrido sem limite de linha no web: mais de 75 caracteres (§4.3).

### 24.3 Componentes e layout

- Dois botões primários na mesma tela.
- Barra inferior de navegação: a navegação é a barra lateral, que vira gaveta
  no celular (§7.1).
- Linha que abre detalhe sem chevron; chevron em linha que não abre nada.
- Atalho de Ações Rápidas sem ícone.
- Avatar vazio ou com foto de banco de imagem.
- Cartão dentro de cartão.
- Faixa colorida na borda de cartão, alerta ou item de lista: estado vai em
  ícone e texto (§20.2).
- Folha modal para o que cabe na própria tela (§9.6).
- Componente interativo sem os estados de §6.

### 24.4 Formulários e tabelas

- Placeholder como único rótulo.
- Erro comunicado só por borda vermelha, sem texto.
- Aluno ou tipo de atendimento digitado em vez de escolhido.
- Botão com rótulo de outra tela ("Salvar o atendimento" em Relatórios).

### 24.5 Movimento e microinterações

- Animar `width`, `height`, `top` ou `margin`.
- Animação sem `prefers-reduced-motion`.
- Splash que segura o usuário depois do app pronto.

### 24.6 UX operacional e acessibilidade

- Alvo de toque abaixo de 44px.
- Laudo, diagnóstico ou observação em notificação ou lista.
- Emoji como marcador de estado.
- Termo em inglês ou erro de ortografia na tela (§19.5).

## 25. CHECKLISTS DE ENTREGA

`check_checklist.py` roda a parte automática e imprime os itens manuais
abaixo; os itens manuais são decisão humana, não pendência para depois.

### 25.1 Identidade e cor

- [ ] Fundo céu, cartão branco, ação em marinho (§3.3).
- [ ] Nenhuma cor fora de `var(--token)`; `lint_output.py` sem `[ERRO]`.

### 25.2 UI e consistência

- [ ] Componentes do catálogo; um primário por tela.
- [ ] Título de tela no padrão (§7.3).

### 25.3 Acessibilidade (WCAG 2.2 AA: bloqueante)

- [ ] Contraste conferido em §3.2 ou com `check_contrast.py`.
- [ ] Tela conferida no tema claro e no escuro (§27); nenhum `dark:` no código da tela.
- [ ] Todo campo com rótulo; todo ícone sozinho com nome acessível.
- [ ] Alvos de 44px; foco visível; ordem de foco (§20.4).

### 25.4 Responsividade e layout

- [ ] 320px a 1200px sem rolagem horizontal; zoom 200%.

### 25.5 Conteúdo e linguagem

- [ ] Vocabulário de §19.2, formatos de §19.3, ortografia de §19.5.
- [ ] Nada sensível fora do perfil (§16.3).
- [ ] Cada perfil vê só o que a permissão deixa; o que ele não pode, não aparece (§16.2).

### 25.6 UX e heurísticas

- [ ] Estados vazio, erro e carregando desenhados (§10).
- [ ] Voltar não perde conteúdo digitado (§15.3).

### 25.7 Performance e microinterações

- [ ] Lista longa paginada ou virtualizada; imagem sob demanda (§26).

### 25.8 Revisão de design (fechamento)

- [ ] A tela, ao lado das telas do protótipo, parece o PSIF.

### 25.9 Relatório de revisão

Revisão de tela sai com severidade em cada achado, para que o que bloqueia
não se perca entre ajustes:

- **P0**: impede a tarefa ou expõe dado sensível (§16.3).
- **P1**: reprova WCAG 2.2 AA ou foge da identidade (cor, fonte ou raio
  fora do token). Corrige antes de entregar.
- **P2**: incômodo com contorno: estado faltando, texto ambíguo.
- **P3**: polimento.

Cada achado diz onde está, o impacto para quem usa e a correção. Feche com
uma nota de 0 a 4 em acessibilidade, desempenho, uso de token, responsivo e
consistência com o catálogo, e com o que está bom e deve ser mantido.
