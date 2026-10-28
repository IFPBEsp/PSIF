## 28. VALORES DERIVADOS E DECISÕES EM ABERTO

### 28.1 Por que este arquivo existe

A skill foi extraída de um protótipo, não de um sistema em produção. Onde o
protótipo não desenha um caso, ou desenha de um jeito que reprova
acessibilidade, a skill decidiu um valor, e esse valor fica aqui, em aberto,
até o design confirmar. Valor em aberto é usável; só não é "o que o
protótipo diz".

### 28.2 Valores derivados aguardando ratificação

| Valor | Motivo |
|---|---|
| `--ink-700` `#616161` | texto secundário do protótipo (`#7D7D7D`) reprova AA no branco e no céu |
| `--navy-800`, `--navy-900` | hover e pressionado do botão primário |
| `--success-100`, `--warning-700`, `--warning-100`, `--danger-700`, `--danger-100` | estados de sucesso, alerta e erro que o protótipo não desenha |
| `--sh-sm` tingida | sombra preta do Figma suja o fundo céu |
| `--sh-md`, `--overlay`, `--o-disabled` | folha modal e desabilitado não desenhados |
| `--control-min` 48px em botão e campo | protótipo: 37–39px, abaixo do alvo de 44px |
| valor de campo em 16px (`--fs-h3`) | protótipo: 15px; abaixo de 16px o Safari do iPhone dá zoom ao focar |
| topo do shell `max(--sp-4, área segura)` (§5.1) | protótipo não desenha a barra de status |
| filtro com 44px de altura | protótipo: 23px |
| texto mínimo 12px | protótipo: 9–11px em três lugares |
| `--lh-normal` 1.5 em parágrafo | protótipo: 1.2 em tudo |
| `--w-content`, `--w-form`, `--w-sidebar`, `--bp-md`, `--bp-lg`, margem `--sp-8` no web | protótipo só tem o quadro de celular |
| barra lateral do web (§7.10) e grade de 3 colunas (§5.3) | idem; escolhido em 2026-10; no celular, a mesma barra vira gaveta (§7.9), como pede o frontend do projeto |
| durações e easing de §3.9 | protótipo estático |
| tempo relativo da notificação em `--ink-700` (§9.5) | protótipo: preto; é metadado e segue §4.3 |
| conteúdo sem limite de largura no web (§5.2) | protótipo navegável; ratificar ou voltar a `--w-content` |
| formulário em 3 colunas no web (§15.1) | protótipo navegável |
| grade do painel 2/3 + 1/3 só a partir de `--bp-lg` (§5.3, §14.2) | entre 768 e 1199px a coluna de apoio ficava com uns 160px |
| "Meus alunos" no Início web (§14.1, §14.2) | protótipo navegável; ratificar inclusão |
| Notificações recentes na coluna direita (§14.2) | protótipo navegável |
| barra lateral recolhível, controle no cabeçalho (§7.12) | protótipo navegável |
| cabeçalho em faixa branca com busca global (§7.13) | protótipo navegável; exceção a §9.6 |
| atalhos com coluna mínima de 64px que quebram linha (§7.8) | a proposta pedia 48px; com 48px o rótulo "Notificações" volta a se sobrepor |

### 28.3 Como ratificar um valor

1. O design confirma (ou troca) o valor no arquivo Figma.
2. Troque em `scripts/tokens.json`, regenere `assets/tokens.css` e
   recalcule o par em §3.2 com `check_contrast.py`.
3. Mude "derivado" para "medido" em §3.1, apague a linha daqui e suba a
   versão da skill com entrada no CHANGELOG.

### 28.4 Decisões de design em aberto

- **Fonte**: Figtree foi identificada pelo desenho; o PDF não guarda o nome.
  Confirmar no Figma e a licença de uso (Figtree é OFL).
- **Logo de login**: o símbolo do sistema é o cérebro com cruz (decidido em
  2026-10, §1.1). Falta decidir se ele também substitui o coração-cérebro do
  cartão de login. E o SVG do símbolo foi traçado da imagem do protótipo: se
  o design tiver o vetor original, ele substitui `simbolo-psif.svg` e
  `simbolo-psif-glifo.svg`.
- **Marcadores da linha do tempo**: o protótipo usa emoji (🟢 🟡 🔵). O
  significado de cada cor não está escrito; a skill propõe tipo de evento
  (§11.5).
- **Paleta escura "noturno"** (derivado, §26): substitui os `--dark-*`
  originais. O fundo fica mais profundo e o cartão mais azul, para separar as
  camadas céu e cartão no escuro. Testada no protótipo navegável contra as
  variações escuro, marinho, grafite e suave; todos os pares de texto passam
  AA (§26.5). Véu e sombras do escuro usam a tinta `rgba(3,9,15)` em vez de
  preto puro. Pendente: ratificação do design e teste em tela OLED com brilho
  baixo.
- **Avatar sem foto**: o protótipo deixa o espaço vazio (José Antonio); a
  skill propõe iniciais (§12.1).
- **Limite de envio de arquivo** (§8.5): tipos aceitos e tamanho máximo não
  estão definidos. Os protótipos usam "PDF, até 20 MB" como provisório.
- **"Termo"**: atalho de Ações rápidas e item do menu (§7.2, §7.8). Nem o
  protótipo nem o escopo de origem dizem o que é (termo de uso? de
  consentimento?). Até definir, ele fica fora do menu e dos atalhos; o ícone
  `psif-termo` continua no sprite para quando voltar.
