# 03 · Strings (textos)

## Criando textos

```python
nome = "Ana"
frase = 'Aspas simples tambem funcionam'
paragrafo = """Tres aspas
permitem varias linhas"""
```

## Texto é uma sequência

Cada letra tem um índice, como numa lista:

```python
palavra = "python"
palavra[0]      # 'p'
palavra[-1]     # 'n'
palavra[0:3]    # 'pyt'
palavra[::-1]   # 'nohtyp'
len(palavra)    # 6
for letra in palavra:
    print(letra)
```

> ⚠️ Textos são **imutáveis**: `palavra[0] = "P"` dá erro. Para "mudar", você cria um texto novo.

## Métodos mais úteis

| Método | Exemplo | Resultado |
|---|---|---|
| `upper()` / `lower()` | `"Oi".upper()` | `'OI'` |
| `strip()` | `"  oi  ".strip()` | `'oi'` (remove espaços das pontas) |
| `split()` | `"a b c".split()` | `['a', 'b', 'c']` |
| `" ".join(lista)` | `"-".join(["a", "b"])` | `'a-b'` |
| `replace()` | `"cafe".replace("e", "é")` | `'café'` |
| `count()` | `"banana".count("a")` | `3` |
| `startswith()` | `"Unidunedev".startswith("Uni")` | `True` |
| `find()` | `"banana".find("n")` | `2` (−1 se não achar) |
| `isdigit()` | `"123".isdigit()` | `True` |

## Juntando textos

```python
"Ola, " + nome          # concatenação com +
f"Ola, {nome}"          # f-string (preferida)
"ha" * 3                # 'hahaha'
```

> ⚠️ `"Idade: " + 20` dá erro: não dá para somar texto com número. Use `f"Idade: {20}"` ou `"Idade: " + str(20)`.

## Comparando textos

```python
"abc" == "abc"          # True
"Ana" == "ana"          # False: maiúscula é diferente!
"Ana".lower() == "ana"  # True
"banana" < "maca"       # True: compara em ordem alfabética
```

## Caracteres e números

Por baixo, cada letra é um número (o código Unicode):

```python
ord("A")    # 65
chr(66)     # 'B'
```

É assim que funcionam as cifras simples, como a de César (deslocar cada letra).

## 🧪 Teste rápido

1. Como contar quantas palavras tem a frase `"eu gosto de cafe"`?
2. Transforme `"  Unidunedev  "` em `"UNIDUNEDEV"` numa linha só.

## 🎯 Pratique

- [01 · Palíndromo](../desafios/01-palindromo/)

---

[⬅️ Tipos e estruturas](02-tipos-e-estruturas.md) · [Próximo: Funções ➡️](04-funcoes.md)
