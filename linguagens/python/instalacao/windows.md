# Instalando o Python no Windows

> ⏱️ 10 minutos

## Já tenho?

```powershell
python --version
```

Apareceu `Python 3.x.x`? Já está instalado. Se abrir a **Microsoft Store**, é só um atalho do Windows: feche e siga os passos.

## Caminho A: pelo site (recomendado)

1. Acesse **https://www.python.org/downloads** e baixe a versão mais recente.
2. Abra o instalador e, **antes de clicar em Install**, marque:
   - ✅ **Add python.exe to PATH** (a mais importante!)
3. Clique em **Install Now**.
4. No final, se aparecer **Disable path length limit**, clique nela também.

## Caminho B: pelo terminal (winget)

```powershell
winget install --id Python.Python.3.13 -e
```

> Troque `3.13` pela versão mais recente, se houver.

## Testando

**Feche e abra** o PowerShell e rode:

```powershell
python --version
pip --version
```

Crie o arquivo `ola.py`:

```python
print("Ola, mundo!")
```

E execute:

```powershell
python ola.py
```

## VS Code

Instale a extensão **Python** (da Microsoft). No canto inferior direito do VS Code, confira se ele escolheu o Python instalado.

## Deu errado?

| Problema | Solução |
|---|---|
| `python` não é reconhecido | Reinstale marcando **Add python.exe to PATH**, ou use `py` no lugar de `python` |
| `python` abre a Microsoft Store | Configurações → Aplicativos → **Aliases de execução de aplicativo** → desative os dois do Python |

---

[⬅️ Python](../README.md)
