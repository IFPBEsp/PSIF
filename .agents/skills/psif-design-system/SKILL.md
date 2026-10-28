---
name: psif-design-system
description: >
  Design system do PSIF, a Plataforma de Suporte Psicopedagógico do IFPB. Use
  ao criar, revisar ou ajustar qualquer tela, componente, CSS, HTML, JSX ou
  protótipo do PSIF, no celular ou no web (Início, atendimentos, alunos, perfil
  do aluno, relatórios, agenda, documentos, evolução, notificações, login,
  página pública). Use também quando o pedido não cita o PSIF pelo nome mas
  fala de app de psicopedagogia, de acompanhamento psicopedagógico de alunos
  ou de atendimento a alunos no IFPB, e ao escolher cor, fonte, espaçamento,
  ícone ou texto de interface para esse produto.
metadata:
  version: "0.15.1"
  last-updated: "2026-10"
---

# PSIF Design System

Com esta skill, o resultado tem que parecer o PSIF: o protótipo do Figma,
corrigido onde ele reprova acessibilidade.

Quem paga por um atalho é a psicopedagoga, que abre o app entre um
atendimento e outro, às vezes com o aluno na sala. Paga também o aluno
adolescente, cujo laudo não pode aparecer numa notificação.

## Regra de ouro

**Fundo céu, cartão branco, ação em marinho.** O marinho (`--navy-700`)
marca o que se clica e o que se lê primeiro: título, número, nome, botão.
Fora do splash, ele não pinta área grande.

Teste de cinco segundos: o único bloco largo de marinho na tela é o botão
primário?

Quando duas regras brigarem, vale esta ordem:

1. **Sigilo do aluno** (§16.3). Nada o sacrifica.
2. **Acessibilidade WCAG 2.2 AA** (§20).
3. **Consistência.** Reutilize o padrão existente antes de inventar variação.
4. **Fidelidade ao protótipo.** Onde ele reprova os itens 1 e 2, a skill
   corrige e registra a correção em §28.

## Como usar esta skill

O frontend do PSIF é Next.js com Tailwind CSS v4 e shadcn/ui. Esse é o caminho
padrão, e §27 diz como os tokens entram nele.

1. **Ligue os tokens ao Tailwind e ao shadcn (§27).** `assets/tokens.css`
   entra no `globals.css` depois do Tailwind; a ponte de §27.3 aponta os
   papéis do shadcn (`--primary`, `--card`) para os tokens. Na tela, use as
   utilitárias da tabela de §27.6 ou `var(--token)`: um hex digitado à mão vira
   a segunda versão da paleta, e ela diverge.
2. **Monte a tela com os componentes do shadcn, no visual do catálogo.** Toda
   tela do PSIF é uma estrutura de §13 feita de cartão, linha de lista, campo e
   botão. `assets/components.css` e `assets/catalogo.html` são a referência de
   medida, estado e marcação de cada um (§6); no projeto, eles viram variantes
   do `Button`, do `Card` e do `Input` do shadcn, não uma folha de CSS paralela.
3. **Desenhe os estados que o protótipo não tem**: vazio, erro, carregando
   (§10) e dado real, como nome longo ou falta de acesso (§10.8).
4. **Decida celular e web juntos.** A mesma tela serve os dois e muda a partir
   de 768px (`md:` no Tailwind). O que muda está em §5.11.
5. **Confira os dois temas.** Claro e escuro saem dos mesmos tokens (§26); não
   escreva `dark:` na tela.
6. **Respeite o perfil de quem vê.** Psicopedagoga, professor, aluno e
   responsável veem coisas diferentes (§16).
7. **Verifique antes de entregar** (fim deste arquivo).

Se a skill não cobrir um caso, derive do protótipo, do token existente e do
componente mais parecido, nessa ordem, e registre o valor novo em §28 como
derivado.

## Mapa de referências

Cada arquivo é dono das suas seções (§) e cuida delas sozinho. A numeração
permite citar "ver §N.M" de qualquer lugar da skill.

| Arquivo | § | Abra quando |
|---|---|---|
| `tokens/colors.md` | §3.1–§3.3 | precisa de uma cor e de onde ela veio (medida ou derivada), ou de um par de contraste já verificado |
| `tokens/scales.md` | §3.4–§3.10 | vai escrever sombra, raio, espaçamento, padding de componente, ícone, superfície ou z-index |
| `tokens/typography.md` | §4 | precisa do tamanho e peso de um texto específico (título, número, rótulo, metadado) |
| `tokens/layout-grid.md` | §5 | monta o esqueleto da tela: barra superior, rodapé, margens, grade, celular e web |
| `tokens/brand-identity.md` | §1 | a tela mostra o símbolo, o logo ou o nome PSIF |
| `tokens/motion-icons.md` | §17–§18 | vai animar algo ou escolher um ícone |
| `tokens/dark-mode.md` | §26 | a tela precisa funcionar no tema escuro, ou vai mexer na troca de tema |
| `tokens/palette-backlog.md` | §28 | vai usar ou criar valor que o protótipo não tem, ou quer saber o que está em aberto |
| `foundations/visual-philosophy.md` | §2 | precisa decidir camada (céu, cartão, marinho), se cabe decoração ou como tratar o que o navegador desenha |
| `foundations/accessibility.md` | §20 | campo, ícone sem texto, alvo de toque, foco, leitor de tela, dado sensível em tela |
| `foundations/ux-principles.md` | §21 | vai decidir um fluxo que a skill não cobre |
| `components/principles.md` | §6 | quer a classe pronta de um componente, os estados dele, ou vai criar um novo |
| `components/navigation.md` | §7 | barra lateral (fixa, recolhível, gaveta), cabeçalho com busca global, barra superior, breadcrumbs, voltar, menu, busca, filtros, ações rápidas |
| `components/inputs-actions.md` | §8 | botão, link, campo, seleção, data, envio de arquivo, caixa de seleção |
| `components/surfaces-overlays.md` | §9 | cartão (indicador, lista, aluno, notificação, login) ou folha modal |
| `components/lists-and-calendar.md` | §11 | lista de alunos ou documentos, tabela do web, linha do tempo da evolução, calendário, agenda |
| `components/people-and-status.md` | §12 | avatar, situação do aluno, observações |
| `components/screen-structures.md` | §13 | começa uma tela nova e precisa da estrutura dela |
| `screen-patterns/dashboards-and-forms.md` | §14–§15 | mexe no Início ou num formulário (validação, rascunho, envio) |
| `ux-patterns/feedback-and-states.md` | §10 | precisa de estado vazio, erro, carregando, toast, confirmação ou dado real |
| `ux-patterns/profiles-and-privacy.md` | §16 | a tela é vista por professor, aluno ou responsável, ou mostra dado sensível do aluno |
| `ux-patterns/language.md` | §19 | escreve qualquer texto de interface: rótulo, mensagem, data, notificação |
| `ai-rules/prompt-engineering.md` | §22–§23 | vai gerar tela com IA ou escrever o prompt para isso |
| `ai-rules/anti-patterns-checklist.md` | §24–§25 | revisa uma tela antes de entregar |
| `ai-rules/tailwind-integration.md` | §27 | sempre que escrever código de tela: liga os tokens ao Tailwind v4 e ao shadcn/ui |

Quando um tema aparece em mais de um arquivo, **o arquivo dono do § é a
fonte de verdade** e os outros só apontam para ele. Se você copiar o
conteúdo, a próxima mudança vai atualizar uma cópia e esquecer a outra.

## Cheat sheet: o mínimo que vale para todo resultado

```
Fonte:              'Figtree', system-ui · uma família, pesos 400/500/600
Fundo da tela:      --surface-base (--sky-100 #CFE7F5)
Cartão:             --surface-raised (branco), --radius-md 8px, sem borda, sem sombra
Ação primária:      --navy-700 (#244A69), texto branco, min-height --control-min (48px;
                    web: 44px, compacto)
                    celular: largura total no rodapé · web: no topo, à direita
Título de tela:     --fs-h1 20px, 600, --navy-700 · centralizado no celular, à esquerda no web
Texto:              principal --ink-900 · dado-chave --navy-700 · secundário --ink-700
Corpo:              --fs-body 15px · campo 16px · menor texto possível 12px (--fs-caption)
Espaçamento:        escala de 4px, 4px … 48px · margem --page-pad 24px (web: 32px)
Raio:               2px / 8px / 10px / 999px, e nenhum outro
Contraste mínimo:   4.5:1 texto · 3:1 texto grande e ícone
Alvo de toque:      --target-min (44px) em largura e altura
Nunca como texto:   --ink-600 (o cinza #7D7D7D do protótipo), --ink-500,
                    --navy-500, --sky-300, --blue-300
                    (banlist em scripts/tokens.json)
Tema escuro:        mesmos tokens, classe .dark no <html>; nada de dark: na tela (§26)
Estilo:             utilitária do Tailwind ou var(--token), via ponte do shadcn (§27)
```

## Assets e scripts

- **`assets/tokens.css`**: o `:root` com todos os tokens, o bloco `.dark`
  (§26), o foco visível, as superfícies do navegador (§2.4) e o movimento
  reduzido. Entra no `globals.css` depois do Tailwind (§27).
- **`assets/components.css`**: as classes de cada componente, com todos os
  estados e o salto para o web (§6). **`assets/catalogo.html`** monta cada
  uma. No projeto, são a referência de medida e estado para as variantes do
  shadcn, não CSS para importar ao lado do Tailwind (§27.7).
- **`assets/exemplos/`**: telas completas do protótipo (Login, Início, Meus
  alunos, Perfil do aluno, Agenda e Novo atendimento), celular e web no mesmo
  HTML. `exemplos.js` faz a gaveta, a barra recolhível, o "Mostrar senha" e a
  confirmação de descarte funcionarem.
  Para começar uma tela parecida, parta da estrutura da mais próxima em vez do
  zero.
- **`assets/icones.svg`**: os ícones do PSIF (§18), para usar com
  `<svg><use href="icones.svg#psif-calendario"></use></svg>`.
- **`assets/simbolo-psif.svg`**: o símbolo, para colar inline (§1.1).
  `simbolo-psif-glifo.svg` traz só o glifo, em `currentColor`; os `.png`
  servem onde SVG não entra.
- **`assets/DESIGN.md`** e **`assets/PRODUCT.md`**: o sistema e o produto
  nos formatos que a skill impeccable lê. Num projeto que a usa, copie os dois
  para a raiz e ela passa a desenhar dentro da identidade do PSIF.
- **`scripts/lint_output.py <arquivo>`**: cor fora da paleta, token banido
  como texto, raio e espaçamento fora da escala, sombra preta, fonte errada,
  alvo de toque pequeno (também em style inline), `var()` para token
  inexistente.
- **`scripts/check_checklist.py <arquivo>`**: a parte automática de §25 e a
  lista do que continua manual.
- **`scripts/check_contrast.py <texto> <fundo>`**: contraste de um par que
  não está em §3.2.
- **`scripts/check_dominance.py <css>`** e **`scripts/check_consumer.py
  <css>`**: no CSS de tokens do projeto, medem a dominância de cor e a
  divergência com a skill.


## Regras invioláveis

```
✗ Inventar item novo quando um do catálogo já resolve.
✗ Usar valor "no olho": todo valor sai do dado canônico.
✗ Mostrar laudo, diagnóstico ou observação fora do perfil do aluno.
✗ Deixar campo sem rótulo visível, ou usar emoji como ícone ou marcador.
```

## Antes de entregar

1. Rode `lint_output.py` e `check_checklist.py` no que você gerou e corrija
   todo `[ERRO]`. Cada `[AVISO]` pede uma decisão: corrija, ou escreva por
   que ele passa.
2. Passe pelos itens manuais de §25.
3. Se a tela copiou do protótipo o texto cinza `#7D7D7D`, o botão de 39px, o
   título preto à esquerda ou o rótulo só em placeholder, refaça a tela. Esses
   quatro reprovam acessibilidade ou fogem do padrão.
