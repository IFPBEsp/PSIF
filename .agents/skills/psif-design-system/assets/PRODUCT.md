# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Uma visão por perfil. A permissão de cada um vem do backend.

- **Psicopedagoga do campus** (usuária principal). Abre o PSIF entre um
  atendimento e outro, por poucos minutos, às vezes com o aluno ou a família
  na sala. Quer saber quem atende hoje, o que falta e registrar o atendimento
  sem perder o que digitou. Cadastra usuários e gerencia a agenda.
- **Professores.** Veem os alunos atendidos das próprias turmas, com
  características e orientações, e registram atividades adaptadas e
  observações. Não veem laudo nem diagnóstico.
- **Alunos.** Adolescentes. Veem os próprios dados e a agenda, pedem reuniões
  e enviam informações à psicopedagoga.
- **Responsáveis.** Acompanham o atendimento e as reuniões do aluno.

## Product Purpose

Tirar do papel o acompanhamento psicopedagógico de alunos do IFPB: registrar
atendimentos, relatórios, documentos e a evolução de cada aluno, e organizar a
agenda. Sucesso é a psicopedagoga responder "quem é o próximo?" sem tocar em
nada e registrar um atendimento em uma tela.

## Positioning

Feito para o trabalho de uma psicopedagoga de campus do IFPB, que hoje cabe
só em parte na aba "Atendimentos" do SUAP e no resto fica no papel.

## Operating Context

- Web responsivo: celular entre atendimentos e para alunos e responsáveis;
  computador para relatórios e agenda, com a mesma identidade e barra lateral.
- Tema claro, escuro e sistema.
- A tela pode estar virada para o aluno ou para a família.
- Português do Brasil, formatos brasileiros (15/06/2026, 09:00, 1.234).

## Capabilities and Constraints

- Telas: splash, login, recuperar senha, Início, Meus alunos, perfil do
  aluno, novo atendimento, relatórios, agenda, documentos, evolução,
  notificações e página pública.
- Laudo, relatório psicológico, diagnóstico e observação são dado sensível de
  adolescente (LGPD): só no perfil do aluno, depois de um toque deliberado;
  nunca em lista, notificação ou pré-visualização.
- Cada perfil registra só o que a permissão dele deixa: a psicopedagoga, o
  acompanhamento; o professor, atividades adaptadas e observações; o aluno,
  pedidos de reunião e informações. Professor não vê dado médico.
- Sem autocadastro: a psicopedagoga cadastra os usuários; o login diz "Não
  tem acesso? Fale com a psicopedagoga do campus.".
- Em aberto: o que é "Termo".

## Brand Commitments

PSIF (Plataforma de Suporte Psicopedagógico), do IFPB. O símbolo é o cérebro
com cruz branco sobre quadrado azul (`simbolo-psif.svg` desta pasta). A
identidade visual é
a da skill `psif-design-system` (DESIGN.md desta pasta) e não se substitui:
mudança de cor, fonte, raio ou espaçamento passa pela skill, não pela tela.

## Evidence on Hand

Protótipo Figma do PSIF (14 quadros de celular e a página pública, em PDF) e
o TCC *Inclusion of Diversity* (IFPB Campus Esperança, 2022) como escopo de
origem. Não há depoimentos, métricas nem números reais de uso: não invente.

## Product Principles

1. Sigilo do aluno acima de tudo.
2. O Início responde "quem é o próximo?" sem toque.
3. Registrar cabe em uma tela, e rascunho nunca se perde.
4. Consistência vence novidade: reutilizar o padrão existente antes de criar.

## Accessibility & Inclusion

WCAG 2.2 AA inegociável: contraste de 4.5:1 em texto, alvo de toque de 44px,
rótulo visível em todo campo, foco visível, estado nunca só na cor, respeito a
movimento reduzido.
