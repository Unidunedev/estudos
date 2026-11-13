# 03 · Tabuada

> Nível: ⭐ · Assuntos: repetição (for) · Criado por: @clehdev · Linguagens: C, Python ou Java

## Enunciado

Leia um número inteiro `N` e mostre a tabuada dele, de 1 a 10.

## Entrada

Um número inteiro `N`.

## Saída

Dez linhas, no formato `N x i = resultado`, com um espaço antes e depois do `x` e do `=`.

## Exemplo

Entrada:
```
7
```

Saída:
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

## 💡 Dicas

<details>
<summary>Dica 1</summary>

Use uma repetição com um contador de 1 até 10. Veja o material de [repetições](../../material/05-repeticoes.md).

</details>

<details>
<summary>Dica 2 (Python)</summary>

Para montar a linha: `print(f"{n} x {i} = {n * i}")`

</details>
