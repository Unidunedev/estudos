# 01 · Primeiros passos em Python

> Pré-requisito: Python instalado ([Windows](../instalacao/windows.md) · [Mac](../instalacao/mac.md))

## Dois jeitos de rodar Python

### 1. Modo interativo (REPL)

Digite `python` (ou `python3`) no terminal. Aparece o `>>>`, e cada linha roda na hora:

```python
>>> 2 + 3
5
>>> nome = "Ana"
>>> nome.upper()
'ANA'
```

Ótimo para testar ideias rápidas. Para sair: `exit()`.

### 2. Arquivo .py

Para programas de verdade, escreva num arquivo e rode com `python arquivo.py`.

## O programa mínimo

```python
print("Ola, mundo!")
```

Só isso. Sem `main`, sem `#include`, sem `;`. O Python executa o arquivo **de cima para baixo**.

## Comentários

```python
# Isto é um comentário: o Python ignora.

"""
Texto entre três aspas pode ocupar várias linhas.
É muito usado para documentar funções.
"""
```

## Indentação é obrigatória

Em vez de `{ }`, o Python usa **espaços no início da linha** para saber o que está dentro de um `if`, `for` ou função:

```python
idade = 20
if idade >= 18:
    print("Maior de idade")    # dentro do if (4 espaços)
    print("Pode votar")        # também dentro
print("Fim")                   # fora do if
```

> ⚠️ Use sempre **4 espaços**. Misturar Tab e espaços dá `IndentationError`.

## Entrada e saída

```python
nome = input()                 # lê uma linha como TEXTO
idade = int(input())           # converte para inteiro
altura = float(input())        # converte para número real

print("Oi,", nome)             # Oi, Ana  (o print separa com espaço)
print(f"{nome} tem {idade} anos")   # f-string: o jeito moderno
print(f"Altura: {altura:.2f}")      # duas casas decimais
```

### f-strings: o jeito favorito de montar textos

Coloque um `f` antes das aspas e as variáveis entre `{ }`:

| f-string | Resultado (`x = 3.14159`, `n = 7`) |
|---|---|
| `f"{n}"` | `7` |
| `f"{x:.2f}"` | `3.14` |
| `f"{n:03d}"` | `007` |
| `f"{n * 2}"` | `14` (aceita contas!) |

### Lendo vários números na mesma linha

```python
a, b = map(int, input().split())    # entrada: "3 5"
```

O `split()` quebra o texto nos espaços, e o `map(int, ...)` converte cada pedaço para inteiro.

## Python × C lado a lado

| | C | Python |
|---|---|---|
| Declarar variável | `int idade = 20;` | `idade = 20` |
| Fim de instrução | `;` | quebra de linha |
| Blocos | `{ }` | indentação |
| Mostrar | `printf("%d\n", x);` | `print(x)` |
| Ler inteiro | `scanf("%d", &x);` | `x = int(input())` |
| Verdadeiro/falso | `1` / `0` | `True` / `False` |
| E / OU / NÃO | `&&` `\|\|` `!` | `and` `or` `not` |
| Divisão inteira | `7 / 2` (entre ints) | `7 // 2` |
| Potência | `pow(2, 10)` | `2 ** 10` |

## 🧪 Teste rápido

1. Abra o REPL e calcule `2 ** 100`. O Python aguenta números desse tamanho?
2. Leia nome e idade e mostre: `Ana tera 30 anos em 2036` (calcule com base na idade).

---

[⬅️ Python](../README.md) · [Próximo: Tipos e estruturas de dados ➡️](02-tipos-e-estruturas.md)
