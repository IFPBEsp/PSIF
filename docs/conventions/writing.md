# Convenções de escrita

## Idioma

- Português do Brasil em docs, specs, issues, PRs, interface e Javadoc.
- Na prosa, inglês só onde a ferramenta exige ou o termo não tem tradução consagrada (endpoint, webhook).

## Documentação

- Escreva o que fazer e por quê. Corte o que não muda a decisão de quem lê.
- Cada regra fica em um lugar só; nos outros, aponte para ela.
- Frases curtas, voz ativa, sem introdução nem fecho genéricos.
- Sem travessão e sem emoji.
- Caminhos, comandos e nomes de código vão em `código`. Bloco de código declara a linguagem.

## Interface

- Texto curto. Botão com verbo no infinitivo ("Salvar", "Criar pedido").
- Erro diz o que aconteceu e o que fazer, sem detalhe técnico.
- Confirmação diz a ação e a consequência, não "Tem certeza?".
- O mesmo conceito tem o mesmo nome em todas as telas.

## Comentários

- Sem comentário no código. Nome claro, método pequeno e constante nomeada substituem a explicação (Clean Code).
- No backend, só Javadoc. Use em classe e método público quando o contrato não fica óbvio pelo nome e pela assinatura.
- Javadoc descreve o contrato (o que faz, parâmetros, retorno, exceções), não a implementação.
- Javadoc desatualizado sai no mesmo commit que mudou o código.
