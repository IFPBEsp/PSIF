"""Fixtures derivadas do tokens.json da skill — não literais de uma paleta."""

import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOKENS = json.loads(
    open(os.path.join(RAIZ, "scripts", "tokens.json"), encoding="utf-8").read())
CORES = TOKENS["color"]
FAMILIAS = TOKENS.get("dominance_families", {})


def _prefixo(papel):
    prefixos = [p for p in FAMILIAS.get(papel, []) if p.endswith("-")]
    assert prefixos, (
        f"tokens.json: `dominance_families` sem prefixo utilizável para o papel "
        f"{papel!r}. Os testes da suíte de design derivam suas fixtures daí.")
    return prefixos[0]


def token(papel, degrau):
    """Nome real de um token daquele papel e degrau. Ex.: ('estrutural', 700)."""
    nome = f"{_prefixo(papel)}{degrau}"
    assert nome in CORES, (
        f"tokens.json não tem `{nome}`, esperado pelos testes para o papel "
        f"{papel!r}. Se a sua escala não tem esse degrau, ajuste a chamada — "
        f"não afrouxe o teste.")
    return nome


def hexa(nome):
    valor = CORES[nome]
    assert valor.startswith("#"), f"{nome} não é um hex literal: {valor}"
    return valor


# Os degraus usados pela suíte. Escolhidos por papel, não por gosto: um escuro
# para fundo, um médio para superfície, um para anel de foco, um de apoio.
ESTRUTURAL_900 = token("estrutural", 900)
ESTRUTURAL_800 = token("estrutural", 800)
ESTRUTURAL_700 = token("estrutural", 700)
ESTRUTURAL_500 = token("estrutural", 500)
APOIO_700 = token("apoio", 700)

HEX_ESTRUTURAL_700 = hexa(ESTRUTURAL_700)
HEX_ESTRUTURAL_900 = hexa(ESTRUTURAL_900)
HEX_APOIO_700 = hexa(APOIO_700)

ALIASES = TOKENS.get("alias_families", {})


# Placeholders para blocos de CSS/HTML de fixture. Bloco literal com
# `.replace()` em vez de f-string: CSS é feito de chaves, e f-string sobre CSS
# vira um campo minado de `{{` — o teste passa a falhar por escaping, não por
# regressão, que é o pior jeito de um teste falhar.
PLACEHOLDERS = {
    "TOKEN_ESTRUTURAL": ESTRUTURAL_700,
    "TOKEN_ESTRUTURAL_900": ESTRUTURAL_900,
    "TOKEN_ESTRUTURAL_800": ESTRUTURAL_800,
    "TOKEN_ESTRUTURAL_500": ESTRUTURAL_500,
    "TOKEN_APOIO": APOIO_700,
    "HEX_ESTRUTURAL": HEX_ESTRUTURAL_700,
}


def concreto(texto):
    """Troca os placeholders pelos tokens reais desta skill."""
    for chave in sorted(PLACEHOLDERS, key=len, reverse=True):
        texto = texto.replace(chave, PLACEHOLDERS[chave])
    return texto
