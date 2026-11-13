# Instalando o Python no Mac

> ⏱️ 10 minutos

## Já tenho?

```bash
python3 --version
```

O macOS pode já trazer um Python 3 junto com as Command Line Tools, mas costuma ser uma versão antiga. Recomendamos instalar a mais recente.

## Caminho A: pelo site

Baixe o instalador para macOS em **https://www.python.org/downloads** e siga as telas.

## Caminho B: Homebrew

```bash
brew install python
```

## Testando

```bash
python3 --version
pip3 --version
```

Crie o arquivo `ola.py`:

```python
print("Ola, mundo!")
```

E execute:

```bash
python3 ola.py
```

> 💡 No Mac, use `python3` e `pip3`. Nos nossos tutoriais, onde estiver `python`, troque por `python3`.

## VS Code

Instale a extensão **Python** (da Microsoft).

---

[⬅️ Python](../README.md)
