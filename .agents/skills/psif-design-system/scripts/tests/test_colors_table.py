"""A tabela de §3.1 e o grupo color do tokens.json têm os mesmos tokens e hex."""

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
COLORS_MD = RAIZ / "tokens" / "colors.md"
TOKENS = json.loads((RAIZ / "scripts" / "tokens.json").read_text(encoding="utf-8"))
LINHA = re.compile(r"^\| `--([\w-]+)` \| `(#[0-9A-Fa-f]{6})` \|", re.M)


def _tabela():
    texto = COLORS_MD.read_text(encoding="utf-8")
    secao = texto.split("### 3.1", 1)[1].split("\n### ", 1)[0]
    return {nome: hexa.upper() for nome, hexa in LINHA.findall(secao)}


def test_tabela_e_tokens_json_tem_os_mesmos_tokens():
    tabela = set(_tabela())
    json_ = set(TOKENS["color"])
    assert tabela == json_, (f"só na tabela: {sorted(tabela - json_)}; "
                             f"só no tokens.json: {sorted(json_ - tabela)}")


def test_hex_da_tabela_bate_com_o_tokens_json():
    tabela = _tabela()
    erradas = [f"--{n}: {h} na tabela, {TOKENS['color'][n]} no tokens.json"
               for n, h in tabela.items()
               if n in TOKENS["color"] and TOKENS["color"][n].upper() != h]
    assert not erradas, "\n  ".join(erradas)
