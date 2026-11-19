#!/usr/bin/env python3
"""
Lê skill.config.json: nome, título, pastas de conteúdo e arquivos exportados.

Uso:
    from skill_config import config
    cfg = config()
    cfg.nome, cfg.pastas_de_conteudo, cfg.tem_camada("design")
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(HERE, ".."))
CAMINHO = os.path.join(RAIZ, "skill.config.json")

CAMPOS_OBRIGATORIOS = ("name", "title", "layers", "content_dirs")


class Config:
    def __init__(self, dados, caminho):
        self._d = dados
        self.caminho = caminho

    @property
    def nome(self):
        return self._d["name"]

    @property
    def titulo(self):
        return self._d["title"]

    @property
    def camadas(self):
        return list(self._d["layers"])

    def tem_camada(self, nome):
        return nome in self._d["layers"]

    @property
    def pastas_de_conteudo(self):
        return list(self._d["content_dirs"])

    @property
    def arquivos_exportados(self):
        """Avulsos que a exportação leva além das pastas de conteúdo."""
        return list(self._d.get("export", {}).get("files", ["SKILL.md"]))


    @property
    def design(self):
        return self._d.get("design", {})

    def exige(self, chave, onde):
        """Lê um campo de `design` que o script chamador não sabe inventar."""
        if chave not in self.design:
            sys.exit(f"[ERRO] skill.config.json sem design.{chave} (exigido por {onde})")
        return self.design[chave]


def config(caminho=CAMINHO):
    if not os.path.exists(caminho):
        sys.exit(f"[ERRO] skill.config.json não encontrado em {caminho}")
    with open(caminho, encoding="utf-8") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError as e:
            sys.exit(f"[ERRO] skill.config.json inválido: {e}")

    faltando = [c for c in CAMPOS_OBRIGATORIOS if c not in dados]
    if faltando:
        sys.exit(f"[ERRO] skill.config.json sem {', '.join(faltando)} (campos obrigatórios)")
    return Config(dados, caminho)
