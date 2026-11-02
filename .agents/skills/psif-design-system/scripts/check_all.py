#!/usr/bin/env python3
"""
Roda todas as verificações da skill: hook de pre-commit e CI.

Uso:
    python check_all.py           # tudo
    python check_all.py --quick   # só os --check, sem a suíte de testes

Sem pytest, a suíte roda num coletor embutido (test_* com tmp_path).
Saída: 0 tudo passou; 1 alguma verificação falhou.
"""

import argparse
import importlib.util
import inspect
import os
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
TESTS = HERE / "tests"

# Só roda o script que existe. check_dominance e check_checklist medem tela e ficam no CI do projeto.
CANDIDATAS = [
    ("assets derivados em sincronia com a fonte de dados",
     ["gen_tokens_css.py", "--check"]),
    ("DESIGN.md em sincronia com tokens.json e o corpo",
     ["gen_design_md.py", "--check"]),
    ("dist/ em sincronia com a pasta da skill (.md, código e .skill)",
     ["build_dist.py", "--check"]),
    ("versão travada ao conteúdo que ela descreve", ["version_lock.py", "--check"]),
    ("toda referência §N/§N.M resolve", ["check_refs.py"]),
]

VERIFICACOES = [(rotulo, cmd) for rotulo, cmd in CANDIDATAS
                if (HERE / cmd[0]).exists()]


def roda_script(args):
    resultado = subprocess.run(
        [sys.executable, str(HERE / args[0]), *args[1:]],
        capture_output=True, text=True,
    )
    return resultado.returncode == 0, (resultado.stdout + resultado.stderr).strip()


def roda_testes_com_pytest():
    resultado = subprocess.run(
        [sys.executable, "-m", "pytest", str(TESTS), "-q"],
        capture_output=True, text=True,
    )
    return resultado.returncode == 0, resultado.stdout.strip().splitlines()[-1:]


def roda_testes_embutido():
    passou = falhou = 0
    erros = []
    for arquivo in sorted(TESTS.glob("test_*.py")):
        spec = importlib.util.spec_from_file_location(arquivo.stem, arquivo)
        modulo = importlib.util.module_from_spec(spec)
        sys.path.insert(0, str(TESTS.parent))
        spec.loader.exec_module(modulo)
        for nome, fn in sorted(vars(modulo).items()):
            if not (nome.startswith("test_") and callable(fn)):
                continue
            kwargs = {}
            if "tmp_path" in inspect.signature(fn).parameters:
                kwargs["tmp_path"] = Path(tempfile.mkdtemp())
            try:
                fn(**kwargs)
                passou += 1
            except Exception:
                falhou += 1
                erros.append(f"{arquivo.stem}::{nome}\n{traceback.format_exc()}")
    return falhou == 0, [f"{passou} passaram, {falhou} falharam"] + erros


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("--quick", action="store_true",
                        help="pula a suíte de testes; só os --check")
    args = parser.parse_args()

    falhas = 0
    for rotulo, comando in VERIFICACOES:
        ok, saida = roda_script(comando)
        # "—" no início: o script não se aplica aqui; mostra o motivo em vez do ✓.
        if ok and saida.startswith("—"):
            print(saida.splitlines()[0])
        else:
            print(f"{'✓' if ok else '✗'} {rotulo}")
        if not ok:
            falhas += 1
            print("    " + saida.replace("\n", "\n    "))

    if not args.quick:
        tem_pytest = importlib.util.find_spec("pytest") is not None
        ok, linhas = (roda_testes_com_pytest() if tem_pytest
                      else roda_testes_embutido())
        motor = "pytest" if tem_pytest else "coletor embutido (pytest ausente)"
        print(f"{'✓' if ok else '✗'} suíte de regressão — {motor}")
        for linha in linhas:
            print("    " + linha.replace("\n", "\n    "))
        if not ok:
            falhas += 1

    if falhas:
        print(f"\n{falhas} verificação(ões) falharam.", file=sys.stderr)
        return 1
    print("\nTudo em ordem.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
