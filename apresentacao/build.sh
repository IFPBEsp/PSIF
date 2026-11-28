#!/usr/bin/env bash
# Junta a casca, os tokens do PSIF, o sprite de ícones e os slides em fundacao.html.
# Tudo vem desta pasta (assets/ e _*.html); não depende do repositório.
set -euo pipefail
cd "$(dirname "$0")"
SKILL=assets
python3 - "$SKILL" <<'PY'
import sys, pathlib
skill = pathlib.Path(sys.argv[1])
shell = pathlib.Path('_shell.html').read_text()
tokens = (skill / 'tokens.css').read_text()
sprite = (skill / 'icones.svg').read_text()
if sprite.startswith('<?xml'):
    sprite = sprite.split('?>', 1)[1]
sprite = sprite.replace('<svg ', '<svg style="display:none" aria-hidden="true" ', 1)
order = ['_abertura.html'] + [f'_parte-{n}.html' for n in range(6)] + ['_fechamento.html']
slides = '\n'.join(pathlib.Path(f).read_text() for f in order)
out = shell.replace('/*__TOKENS__*/', tokens).replace('<!--__SPRITE__-->', sprite).replace('<!--__SLIDES__-->', slides)
pathlib.Path('fundacao.html').write_text(out)
print('fundacao.html gerado com', out.count('<section class="slide'), 'slides')
PY
