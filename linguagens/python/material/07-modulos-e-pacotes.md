# 07 · Módulos, pacotes e ambientes virtuais

> O que transforma seus scripts em **projetos** de verdade.

## Módulos: dividir o código em arquivos

Todo arquivo `.py` é um **módulo**. Você pode usar o que está em um arquivo dentro de outro:

```python
# banco.py
class ContaBancaria:
    ...
```

```python
# main.py
from banco import ContaBancaria

conta = ContaBancaria("Ana")
```

## A biblioteca padrão: "pilhas incluídas"

O Python já vem com centenas de módulos prontos. O lema da linguagem é *batteries included*:

| Módulo | Para quê |
|---|---|
| `math` | `sqrt`, `pi`, `floor`... |
| `random` | Números e escolhas aleatórias |
| `datetime` | Datas e horas |
| `json` | Ler e escrever JSON (como o do nosso [mural](https://github.com/Unidunedev/onboarding/tree/main/membros)!) |
| `os` e `pathlib` | Arquivos e pastas |
| `csv` | Planilhas em CSV |

```python
import random
print(random.choice(["pedra", "papel", "tesoura"]))
```

## `if __name__ == "__main__"`

Você vai ver isso em todo projeto Python:

```python
def principal():
    print("Rodando!")

if __name__ == "__main__":
    principal()
```

Significa: "só rode `principal()` se este arquivo foi executado **diretamente**". Se outro arquivo fizer `import` dele, o código não roda sozinho. É o equivalente ao `main` do C e do Java.

## pip: instalando bibliotecas de terceiros

O **PyPI** (https://pypi.org) tem mais de 500 mil bibliotecas. Para instalar uma:

```bash
pip install requests
```

```python
import requests
resposta = requests.get("https://api.github.com/users/octocat")
print(resposta.json()["name"])
```

## Ambientes virtuais (venv): cada projeto na sua caixa

Se você instala tudo "no Python do computador", logo os projetos brigam entre si: um precisa da versão 1 de uma biblioteca, outro precisa da 2.

A solução profissional é criar um **ambiente virtual** por projeto: uma pasta com um Python e bibliotecas só daquele projeto.

```bash
python -m venv .venv
```

Ativar:

| Sistema | Comando |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Mac / Linux | `source .venv/bin/activate` |

O terminal passa a mostrar `(.venv)` no começo. Agora o `pip install` instala só neste projeto.

> 💡 Coloque `.venv/` no `.gitignore`: a pasta é grande e cada pessoa cria a sua.

### requirements.txt: a lista de compras do projeto

```bash
pip freeze > requirements.txt      # salva as bibliotecas instaladas
pip install -r requirements.txt    # outra pessoa instala tudo de uma vez
```

É assim que um colega clona seu projeto e consegue rodar na máquina dele.

> No Windows, se o PowerShell bloquear a ativação ("execução de scripts foi desabilitada"), rode uma vez: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Próximos passos

Com o básico e a orientação a objetos, você está pronto para escolher um caminho:

| Quero... | Estude |
|---|---|
| Fazer APIs e back-end | **FastAPI** (moderno e simples) ou **Django** (completo) |
| Trabalhar com dados | **pandas** e **Jupyter** |
| Automatizar tarefas | `pathlib`, `csv`, **Playwright** |
| Testar código | **pytest** |

Os roteiros completos de cada caminho estão no repositório de **trilhas**.

---

[⬅️ Herança e encapsulamento](06-heranca-e-encapsulamento.md) · [Python 🐍](../README.md)
