## 24. CHECKLIST DE ENTREGA

Um item por linha, com o § da regra. Item sem marca: `check_checklist.py`
e `lint_output.py` conferem. Item `· manual`: decisão humana; o
`check_checklist.py` imprime a lista a cada execução.

### 24.1 Cor e identidade

- [ ] Fundo céu, cartão branco, ação em marinho; nenhuma área grande em marinho (§2.2) · manual
- [ ] `--blue-*` só no símbolo da marca (§1.4) · manual
- [ ] Toda cor, raio, sombra e espaçamento por `var(--token)` ou utilitária da ponte (§26.6)
- [ ] Nenhum token da banlist como cor de texto; texto secundário em `--ink-700` (§3.2)
- [ ] Sombra tingida, nunca preta (§3.4)
- [ ] z-index só pelas camadas nominais (§3.10)

### 24.2 Tipografia e raio

- [ ] Família só por `--font-sans` (§4.1)
- [ ] Título de tela em `--fs-display` 600 `--navy-700`, à esquerda, abaixo da barra de ações (§4.3) · manual
- [ ] Nenhum texto abaixo de `--fs-caption` (§4.2) · manual
- [ ] Texto corrido até 70ch (§4.3) · manual
- [ ] Raio na escala (§3.6)
- [ ] Raio pelo papel da peça, filho menor ou igual ao pai (§3.6) · manual

### 24.3 Componentes e layout

- [ ] Componentes da tabela de §6; componente novo ganha linha nela (§6) · manual
- [ ] Um botão primário por tela (§5.6) · manual
- [ ] Navegação na barra lateral e na gaveta, sem barra inferior (§7.1) · manual
- [ ] Chevron em toda linha que abre detalhe, e só nela (§9.3) · manual
- [ ] Sem cartão dentro de cartão (§9.1) · manual
- [ ] Sem faixa colorida na borda de cartão, alerta ou linha (§20.2) · manual
- [ ] Folha ou diálogo só para o que não cabe na tela (§9.6) · manual
- [ ] Todo componente interativo com os estados de §6 (§6) · manual
- [ ] Avatar com foto real ou iniciais (§12.1) · manual
- [ ] Selo com texto (§12.2)
- [ ] Filtro anuncia o estado ou diz que abre seleção (§7.6)

### 24.4 Formulários, listas e tabelas

- [ ] Todo campo com `<label>` visível; placeholder não é rótulo (§20.7)
- [ ] Erro de campo em texto, não só na borda (§10.7)
- [ ] Aluno e tipo de atendimento escolhidos de lista (§8.4) · manual
- [ ] Rótulo do botão com o verbo e o objeto da tela (§19.1) · manual
- [ ] Dado tabular em `<table>` (§20.8)
- [ ] Tabela com estado na URL e lista longa paginada (§11.8) · manual
- [ ] Estados vazio, erro e carregando desenhados (§10) · manual
- [ ] Voltar não perde o que foi digitado (§15.3) · manual

### 24.5 Movimento

- [ ] Só `opacity`, `transform` e cor animados (§17.4)
- [ ] Animação respeita `prefers-reduced-motion` (§17.5)

### 24.6 Acessibilidade

- [ ] Contraste conferido em §3.2 ou com `check_contrast.py` (§20.1) · manual
- [ ] Foco visível, nunca `outline: none` sem substituto (§20.5)
- [ ] Botão só de ícone com nome acessível (§20.7)
- [ ] Ordem de foco (§20.4) · manual
- [ ] Alvo mínimo por token (§20.6)
- [ ] Cor nunca é o único canal (§20.2) · manual
- [ ] Sem altura fixa em contêiner de texto (§20.13)
- [ ] Sem `dark:` nem `--dark-*` no código da tela (§25.2)
- [ ] Tela conferida no tema claro e no escuro (§25) · manual

### 24.7 Conteúdo, sigilo e perfis

- [ ] Nada clínico em lista, notificação, toast ou pré-visualização (§16.3) · manual
- [ ] O que o perfil não pode, não aparece (§16.2) · manual
- [ ] Sem termo em inglês na tela (§19.2)
- [ ] Vocabulário do domínio (§19.2) · manual
- [ ] Data, hora e número no formato brasileiro (§19.3) · manual
- [ ] Ortografia (§19.5) · manual
- [ ] Sem travessão nem exclamação fora da saudação (§19.4) · manual
- [ ] Emoji nunca é ícone nem marcador (§18) · manual

### 24.8 Larguras e entrada

- [ ] De 320px a monitor grande sem rolagem horizontal, e zoom de 200% (§20.13) · manual
- [ ] Conferida na tela estreita, na faixa intermediária e a partir de `--bp-lg` (§5.2) · manual
- [ ] Hover, menu suspenso e alvo menor só com mouse (§5.12) · manual
- [ ] `max-w` por token ou 70ch, nunca pela escala do Tailwind nem em px (§5.2)
- [ ] Conteúdo até `--w-content`, centralizado em monitor grande (§5.2) · manual

### 24.9 Relatório de revisão

Revisão de tela sai com severidade em cada achado:

- **P0**: impede a tarefa ou expõe dado sensível (§16.3).
- **P1**: reprova WCAG 2.2 AA ou foge da identidade. Corrige antes de
  entregar.
- **P2**: incômodo com contorno: estado faltando, texto ambíguo.
- **P3**: polimento.

Cada achado diz onde está, o impacto para quem usa e a correção. Feche com
uma nota de 0 a 4 em acessibilidade, desempenho, uso de token, responsivo e
consistência com §6, e com o que está bom e deve ser mantido.
