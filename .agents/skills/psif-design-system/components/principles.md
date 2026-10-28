## 6. PRINCÍPIOS DE COMPONENTES E REUTILIZAÇÃO

1. **Todo componente do PSIF é um cartão branco, um campo, um botão ou uma
   linha de lista.** Antes de criar outro, monte com esses quatro.
2. **Raio único.** `--radius-md` em tudo que é retângulo; círculo só para
   avatar e marcador.
3. **Sem borda decorativa.** Borda existe em campo (`--ink-600`, 1px) e em
   botão secundário (`--navy-700`, 1px). Cartão não tem borda.
4. **Um primário por tela.** O botão `--navy-700` de largura total é a ação
   da tela; o resto é secundário ou link.
5. **Componente novo entra no catálogo**: se a tela precisou de um, ele
   ganha uma subseção aqui antes de ir para a segunda tela.
6. **Todo componente interativo tem todos os estados** da tabela abaixo.
   Componente com metade deles não está pronto.

| Estado | Botão primário | Campo | Linha, cartão ou item clicável |
|---|---|---|---|
| normal | `--navy-700` | branco; sem borda sobre o céu | branco ou transparente |
| hover (web) | `--navy-800` | não se aplica | fundo `--ink-100` |
| foco | anel de §20.5 | anel de §20.5 | anel de §20.5 |
| pressionado | `--navy-900` | não se aplica | fundo `--ink-100` |
| selecionado | não se aplica | não se aplica | filtro: `--navy-700` e texto branco; navegação: `--sky-100` e `--navy-700` |
| desabilitado | `--o-disabled`, sem hover | `--o-disabled` | `--o-disabled` |
| carregando | "Salvando…", bloqueado | não se aplica | esqueleto (§10.5) |
| erro | alerta (§10.7) | borda `--danger-700` e texto | não se aplica |

7. **Use as classes de `assets/components.css`.** Elas já trazem os tokens,
   os estados da tabela acima e o salto para o web. Estilo inline fica para o
   que é só daquela tela, como a largura de uma coluna, e sempre com
   `var(--token)`. Quem muda um componente aqui muda a classe junto, e o
   `assets/catalogo.html` mostra o resultado.

| Componente | Classes | § |
|---|---|---|
| Estrutura da tela | `psif-shell`, `psif-coluna`, `psif-area`, `psif-conteudo`, `psif-pular`, `psif-so-leitor` (texto só para leitor de tela, como a legenda da tabela) | §5.1, §20.4 |
| Barra superior | `psif-barra-superior`, `psif-titulo-tela`, `psif-saudacao`, `psif-botao-icone`, `psif-espaco-icone` (vão do tamanho de um alvo, do lado sem botão, para o título ficar no centro) | §7.3 |
| Navegação | `psif-lateral`, `psif-lateral--aberta`, `psif-lateral--recolhida`, `psif-item`, `psif-item__rotulo`, `psif-trilha` | §7.1, §7.9–§7.12 |
| Cabeçalho (web) | `psif-cabecalho`, `psif-cabecalho--faixa`, `psif-cabecalho__busca`, `psif-cabecalho__resultados` | §7.13 |
| Tabela (web) | `psif-tabela-cartao`, `psif-tabela`, `psif-tabela__chave`, `psif-tabela__numero`, `psif-tabela__aluno` (`__nome`), `psif-paginacao` | §11.8 |
| Botão e link | `psif-botao` (`--secundario`, `--compacto`, `--tela`, `--texto-perigo`), `psif-link` | §8.1, §5.6, §10.3 |
| Caixa de seleção | `psif-caixa` | §8.7 |
| Campo | `psif-campo-grupo`, `psif-rotulo`, `psif-opcional`, `psif-campo` (`--borda`, `--com-botao`), `psif-campo__entrada` (o `<input>` de campo com ícone: busca, e-mail, senha), `psif-selecao`, `psif-erro-campo` | §8.3–§8.6 |
| Filtro | `psif-filtros`, `psif-filtro` | §7.6 |
| Cartão e lista | `psif-cartao` (`--lista`, `--resumo`), `psif-cartao-titulo`, `psif-lista`, `psif-linha`, `psif-secoes` (menu de seções do perfil) | §9.1, §9.3, §7.5 |
| Aluno | `psif-aluno`, `psif-avatar` (`--grande`, `--pequeno`, `--mini`), `psif-situacao` (`--perfil`, `--pendente`, `--encerrada`) | §9.4, §12 |
| Indicadores | `psif-indicadores`, `psif-indicador` | §9.2 |
| Ações rápidas | `psif-atalhos`, `psif-atalho` | §7.8 |
| Feedback | `psif-alerta` (`--erro`), `psif-toast`, `psif-vazio`, `psif-esqueleto` | §10 |
| Folha modal | `psif-veu`, `psif-folha`, `psif-folha__titulo`, `psif-folha__texto`, `psif-folha__acoes` | §9.6, §10.3 |
| Autenticação | `psif-autenticacao`, `psif-cartao--autenticacao`, `psif-logo-login`, `psif-autenticacao__subtitulo`, `psif-autenticacao__linha`, `psif-autenticacao__assinatura` | §9.8, §13.4 |
| Página pública e splash | `psif-funcionalidade` (`__icone`, `__titulo`, `__texto`), `psif-splash` (`__nome`, `__sub`), `psif-progresso` (`__barra`) | §9.7, §13.5 |
| Notificação | `psif-notificacao` (`--lida`, `--pendente`) | §9.5 |
| Linha do tempo | `psif-linha-tempo`, `psif-evento` (`--avanco`, `--relatorio`) | §11.5 |
| Calendário | `psif-mes-cabecalho`, `psif-semana`, `psif-mes`, `psif-dia`, `psif-ponto` | §11.6 |
| Grades | `psif-grade-cartoes`, `psif-grade-painel`, `psif-metades`, `psif-form`, `psif-pilha` (cartões empilhados com `--sp-6`) | §5.3 |
