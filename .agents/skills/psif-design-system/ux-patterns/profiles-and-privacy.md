## 16. UX OPERACIONAL: PERFIS E MODOS DE USO

### 16.1 Entre atendimentos (interrupção)

A psicopedagoga abre o PSIF entre um aluno e outro, por poucos minutos. O
Início responde "quem é o próximo" sem toque; registrar um atendimento cabe
em uma tela; rascunho não se perde ao recarregar, voltar ou cair a rede (§15.3).

### 16.2 Perfis

O PSIF tem uma visão por perfil (`docs/constitution/mission.md`, no projeto).
A skill não desenha uma tela por perfil: ela dá os padrões para que cada tela
nasça certa para quem a vê.

| Perfil | Vê | Registra |
|---|---|---|
| Psicopedagoga | todos os alunos atendidos, a agenda inteira, usuários | acompanhamento, atendimentos, relatórios, documentos, agenda, cadastro de usuários |
| Professor | alunos atendidos das próprias turmas, com características e orientações | atividades adaptadas e observações |
| Aluno | os próprios dados e a própria agenda | pedidos de reunião e informações para a psicopedagoga |
| Responsável | o atendimento e as reuniões do aluno vinculado | nada além do que o backend liberar |

Padrões que valem para todos:

- **A permissão vem do backend.** O que cada perfil vê sai de `GET /auth/me`
  (`role` e `permissions`). A tela segue a permissão; não decide sozinha.
  Esconder um botão não protege nada: a proteção real é do servidor.
- **O que o perfil não pode, não aparece.** Item de menu, atalho e botão sem
  permissão somem, em vez de aparecer desabilitados. Campo que o perfil não
  pode editar aparece como texto, não como campo.
- **O Início responde a pergunta do perfil sem toque**: a psicopedagoga, quem
  é o próximo; o professor, que aluno dele tem orientação nova; o aluno e o
  responsável, qual a próxima reunião. Mesma estrutura de Início (§14), com os
  cartões que o perfil pode ver.
- **A saudação usa o primeiro nome** ("Olá, Ana!"), nunca o papel.
- **Sem acesso** é tela própria com o que houve e quem libera (§10.8), nunca
  uma tela em branco.
- **Um vocabulário só** (§19.2). Atendimento, aluno e reunião têm o mesmo nome
  em todos os perfis.

### 16.3 Sigilo (dados sensíveis do aluno)

O PSIF guarda dado de saúde de adolescente (laudo médico, relatório
psicológico): dado sensível na LGPD.

- Notificação diz **que** algo aconteceu, não **o que**: "Novo documento no
  prontuário de Valquíria", nunca o nome do laudo ou o diagnóstico.
- Lista mostra nome, turma e situação; nada clínico.
- Documento sensível abre só depois de um toque no item, nunca em
  pré-visualização.
- Toast segue a mesma regra: "Documento enviado.", nunca o nome do laudo.
- Sair fica sempre a dois toques (☰ e Sair).
- Laudo, relatório psicológico e diagnóstico são da psicopedagoga. Outro
  perfil só os vê se o backend liberar aquele documento para ele.
- Documento sigiloso (laudo, relatório psicológico, diagnóstico) leva o selo
  "Sigiloso" (`psif-cadeado` e texto, `--warning-100` / `--warning-700`) na
  lista e na tabela. O resumo da seção Documentos mostra a contagem ("2
  sigilosos"), nunca os nomes.
- O selo só informa; quem pode abrir continua sendo decidido pelo backend.

### 16.4 Professor

- **Meus alunos** lista só os alunos atendidos das turmas em que ele dá aula.
  Os filtros (§11.4) refinam dentro desse recorte, nunca o ampliam.
- **Perfil do aluno** mostra características e orientações em leitura. O que
  o professor registra (atividade adaptada, observação) entra como formulário
  curto (§15) e aparece com autor e data (§12.3).
- **Relatórios** que a psicopedagoga disponibilizou aparecem para ele em
  leitura ("Relatório elaborado e disponibilizado aos professores
  autorizados").
- O professor edita só o que ele mesmo registrou.

### 16.5 Aluno

- O aluno é adolescente. Texto direto, com "você", sem termo técnico
  ("Sua próxima reunião é quinta, 10:00.").
- **Pedir reunião** é formulário curto na agenda (§15): data sugerida, motivo
  em texto livre, enviar. Depois do envio, o pedido aparece na agenda com a
  situação que o backend devolver, em selo com texto (§12.2). A tela não
  inventa situação nem assume que o pedido foi aceito.
- **Enviar informação à psicopedagoga** é texto com anexo opcional (§8). O
  aluno vê o que enviou e quando.
- O aluno não vê observação de professor nem da psicopedagoga, a menos que o
  backend libere.

### 16.6 Responsável

- Acompanha o aluno vinculado: atendimentos, reuniões e o que o backend
  liberar. Em leitura, salvo permissão explícita.
- Responsável com mais de um aluno escolhe o aluno no topo da tela, e o nome
  dele fica visível em todas as telas, para não confundir os dois.
- A tela pode estar no celular da família: vale tudo de §16.3.
