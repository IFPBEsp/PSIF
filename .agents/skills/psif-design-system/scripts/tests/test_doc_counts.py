"""Trava as contagens que a documentação afirma contra a realidade medida."""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

CONFIG = json.loads((RAIZ / "skill.config.json").read_text(encoding="utf-8"))
PASTAS_DE_CONTEUDO = CONFIG["content_dirs"]

# Arquivos de prosa que descrevem a skill para quem vai consumi-la. Um só
# conferido deixa o outro livre para repetir o erro do "§1–§25".
PROSA = [rel for rel in ("README.md", "scripts/README.md")
         if (RAIZ / rel).exists()]


def secoes_reais():
    numeros = set()
    for pasta in PASTAS_DE_CONTEUDO:
        for md in (RAIZ / pasta).rglob("*.md"):
            numeros.update(int(n) for n in re.findall(
                r"^## (\d+)\. ", md.read_text(encoding="utf-8"), re.M))
    return numeros


def test_faixa_de_secoes_afirmada_bate_com_os_headings():
    """A faixa "§N ao §M" citada na prosa bate com os headings."""
    numeros = secoes_reais()
    if not numeros:
        return  # skill sem numeração § — legítimo; nada a conferir.

    esperado = f"§{min(numeros)} ao §{max(numeros)}"
    padrao = re.compile(r"§(\d+) ao §(\d+)")
    for rel in PROSA:
        texto = (RAIZ / rel).read_text(encoding="utf-8")
        achados = padrao.findall(texto)
        if not achados:
            continue
        assert all(f"§{a} ao §{b}" == esperado for a, b in achados), (
            f"{rel} afirma a faixa {achados}; os headings dão {esperado}."
        )


def test_numeracao_de_secoes_nao_tem_buraco():
    """§N citado sem §N existir é o que o check_refs.py pega; falta de §N no meio da faixa é outra coisa."""
    numeros = secoes_reais()
    if not numeros:
        return
    faltando = set(range(min(numeros), max(numeros) + 1)) - numeros
    assert not faltando, f"seções ausentes na faixa: {sorted(faltando)}"


def test_prosa_lista_exatamente_os_scripts_exportados():
    """O README promete um conjunto de scripts ao consumidor; a verdade é `export.files` do skill.config.json."""
    exportados = {rel.split("/")[-1]
                  for rel in CONFIG.get("export", {}).get("files", [])
                  if rel.startswith("scripts/") and rel.endswith(".py")
                  and not rel.startswith("scripts/tests/")}

    readme = RAIZ / "README.md"
    if not readme.exists():
        return
    bloco = re.search(r"O que a exportação leva:\n\n```\n(.*?)```",
                      readme.read_text(encoding="utf-8"), re.S)
    if bloco is None:
        # Sem o bloco não há promessa a conferir. É legítimo — mas se
        # exportados existe e o README fala de scripts, vale escrevê-lo.
        return
    listados = set(re.findall(r"scripts/([\w-]+\.py)", bloco.group(1)))

    assert listados == exportados, (
        f"README.md lista {sorted(listados)}; a exportação leva "
        f"{sorted(exportados)}. Faltando no README: "
        f"{sorted(exportados - listados)}; sobrando: "
        f"{sorted(listados - exportados)}."
    )


def test_pastas_de_conteudo_declaradas_existem():
    """Config que aponta para pasta inexistente falha tarde, dentro do export, com uma mensagem sobre outra coisa."""
    faltando = [p for p in PASTAS_DE_CONTEUDO if not (RAIZ / p).is_dir()]
    assert not faltando, (
        f"skill.config.json declara pasta(s) de conteúdo que não existem: "
        f"{faltando}"
    )


def test_arquivos_declarados_no_export_existem():
    faltando = [rel for rel in CONFIG.get("export", {}).get("files", [])
                if not (RAIZ / rel).exists()]
    assert not faltando, (
        f"skill.config.json declara em `export.files` arquivo(s) inexistente(s): "
        f"{faltando}"
    )


def test_subsecoes_sem_buraco():
    por_secao = {}
    for pasta in PASTAS_DE_CONTEUDO:
        for md in (RAIZ / pasta).rglob("*.md"):
            for sec, sub in re.findall(r"^### (\d+)\.(\d+)\s", md.read_text(encoding="utf-8"), re.M):
                por_secao.setdefault(int(sec), set()).add(int(sub))
    buracos = {sec: sorted(set(range(1, max(subs) + 1)) - subs)
               for sec, subs in por_secao.items() if set(range(1, max(subs) + 1)) - subs}
    assert not buracos, f"subseções faltando: {buracos}"
