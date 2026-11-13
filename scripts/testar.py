"""
Testa as soluções dos desafios contra os arquivos da pasta testes/.

Uso:
  python scripts/testar.py linguagens/c/desafios/01-ola-mundo/solucoes/seu-username.c
  python scripts/testar.py --todas

Para cada desafio, roda a solução com cada testes/entradaN.txt e compara a
saída com testes/saidaN.txt (ignorando espaços no fim das linhas e linhas
vazias no final).

No GitHub Actions, a variável PR_AUTHOR faz o script conferir se o nome do
arquivo é o username de quem abriu o PR.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TEMPO_LIMITE = 5  # segundos por teste

# Extensões aceitas por pasta (vale o caminho mais específico).
# Pasta de linguagem aceita só a própria; disciplinas aceitam qualquer linguagem suportada.
LINGUAGENS_POR_PASTA = {
    "linguagens/c": {".c"},
    "linguagens/python": {".py"},
    "disciplinas": {".c", ".py"},
}
SUPORTADAS = {".c", ".py"}
IGNORAR = {".gitkeep", "README.md"}

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass


def normalizar(texto: str) -> list[str]:
    linhas = [linha.rstrip() for linha in texto.replace("\r\n", "\n").split("\n")]
    while linhas and linhas[-1] == "":
        linhas.pop()
    return linhas


def preparar(arquivo: Path, pasta_tmp: Path) -> tuple[list[str] | None, str]:
    """Devolve o comando para executar a solução (ou None e a mensagem de erro)."""
    relativo = arquivo.resolve().relative_to(RAIZ).as_posix()
    if arquivo.suffix == ".py":
        return [sys.executable, str(arquivo)], ""

    compilador = shutil.which("gcc") or shutil.which("clang")
    if not compilador:
        return None, "não encontrei o gcc. Veja linguagens/c/instalacao/ para instalar."
    executavel = pasta_tmp / ("programa.exe" if os.name == "nt" else "programa")
    resultado = subprocess.run(
        [compilador, "-std=c17", "-Wall", "-Wextra", "-O0", relativo, "-o", str(executavel), "-lm"],
        capture_output=True,
        text=True,
        cwd=RAIZ,  # mensagens de erro com o caminho curto do arquivo
    )
    if resultado.stderr.strip():
        aviso = "erro de compilação" if resultado.returncode else "avisos do compilador"
        print(f"   📋 {aviso}:")
        for linha in resultado.stderr.strip().splitlines():
            print(f"      {linha}")
    if resultado.returncode != 0:
        return None, "não compilou. Corrija os erros acima (veja a linha indicada)."
    return [str(executavel)], ""


def testar(arquivo: Path, autor: str | None) -> bool:
    relativo = arquivo.resolve().relative_to(RAIZ).as_posix()
    print(f"\n🧪 {relativo}")

    partes = Path(relativo).parts
    if "solucoes" not in partes or partes.index("solucoes") != len(partes) - 2:
        print("   ❌ a solução precisa estar dentro da pasta solucoes/ de um desafio.")
        return False

    pasta = max(
        (p for p in LINGUAGENS_POR_PASTA if relativo.startswith(p + "/")),
        key=len,
        default=partes[0],
    )
    permitidas = LINGUAGENS_POR_PASTA.get(pasta, SUPORTADAS)
    if arquivo.suffix not in permitidas:
        print(f"   ❌ a pasta {pasta}/ aceita apenas: {', '.join(sorted(permitidas))}")
        return False

    nome = arquivo.stem
    if not re.fullmatch(r"[a-z0-9]([a-z0-9-]*[a-z0-9])?", nome):
        print("   ❌ o nome do arquivo precisa ser o seu username do GitHub, em minúsculas.")
        return False
    if autor and nome != autor.lower():
        print(f"   ❌ este PR é de @{autor}, então o arquivo deveria se chamar {autor.lower()}{arquivo.suffix}")
        return False

    desafio = arquivo.parent.parent
    entradas = sorted(
        (desafio / "testes").glob("entrada*.txt"),
        key=lambda p: int(re.sub(r"\D", "", p.stem) or 0),
    )
    if not entradas:
        print("   ⚠️ este desafio ainda não tem testes. Nada para conferir.")
        return True

    with tempfile.TemporaryDirectory() as tmp:
        comando, erro = preparar(arquivo, Path(tmp))
        if comando is None:
            print(f"   ❌ {erro}")
            return False

        passou = 0
        for entrada in entradas:
            numero = entrada.stem.replace("entrada", "")
            saida_esperada = entrada.with_name(f"saida{numero}.txt")
            texto_entrada = entrada.read_text(encoding="utf-8")
            try:
                execucao = subprocess.run(
                    comando,
                    input=texto_entrada,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=TEMPO_LIMITE,
                )
            except subprocess.TimeoutExpired:
                print(f"   ❌ teste {numero}: demorou mais de {TEMPO_LIMITE}s. Será um laço infinito?")
                break  # se travou num teste, provavelmente trava em todos

            esperado = normalizar(saida_esperada.read_text(encoding="utf-8"))
            recebido = normalizar(execucao.stdout)
            if execucao.returncode != 0 and execucao.returncode is not None:
                print(f"   ❌ teste {numero}: o programa encerrou com erro (código {execucao.returncode}).")
                if execucao.stderr.strip():
                    print("      " + execucao.stderr.strip().splitlines()[-1])
                continue
            if recebido == esperado:
                passou += 1
                print(f"   ✅ teste {numero}")
            else:
                print(f"   ❌ teste {numero}: saída diferente da esperada")
                print("      entrada:  " + (" | ".join(normalizar(texto_entrada)) or "(nenhuma)"))
                print("      esperado: " + " | ".join(esperado))
                print("      recebido: " + (" | ".join(recebido) or "(nada)"))

        total = len(entradas)
        print(f"   {'🎉' if passou == total else '📊'} {passou}/{total} testes passaram")
        return passou == total


def main() -> int:
    argumentos = sys.argv[1:]
    autor = os.environ.get("PR_AUTHOR") or None

    if not argumentos or argumentos == ["--todas"]:
        arquivos = [
            p for p in RAIZ.glob("**/desafios/*/solucoes/*")
            if p.is_file() and p.name not in IGNORAR
        ]
        autor = None  # rodando tudo: não confere o autor
    else:
        arquivos = [Path(a) for a in argumentos]
        arquivos = [p for p in arquivos if p.name not in IGNORAR]

    if not arquivos:
        print("Nenhuma solução para testar. ☕")
        return 0

    resultados = []
    for arquivo in sorted(arquivos):
        if not arquivo.exists():
            print(f"\n❌ arquivo não encontrado: {arquivo}")
            resultados.append(False)
            continue
        resultados.append(testar(arquivo, autor))

    falhas = resultados.count(False)
    print()
    if falhas:
        print(f"💪 {falhas} solução(ões) ainda não passaram. Ajuste e faça um novo commit no mesmo PR!")
        return 1
    print("☕ Tudo certo!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
