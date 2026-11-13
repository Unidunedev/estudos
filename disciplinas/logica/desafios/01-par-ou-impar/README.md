# 01 · Par ou ímpar

> Nível: ⭐ · Assuntos: operador `%`, condicionais · Criado por: @clehdev · Linguagens: C, Python ou Java

## Enunciado

Leia um número inteiro e diga se ele é par ou ímpar.

## Entrada

Um número inteiro (pode ser zero ou negativo).

## Saída

`PAR` ou `IMPAR`, em maiúsculas e sem acento.

## Exemplos

| Entrada | Saída |
|---|---|
| `4` | `PAR` |
| `7` | `IMPAR` |

## 💡 Dicas

<details>
<summary>Dica 1</summary>

Um número é par quando o **resto da divisão por 2** é zero. O operador de resto é o `%`.

</details>

<details>
<summary>Dica 2 (pegadinha dos negativos!)</summary>

Em C, `-3 % 2` dá `-1`, não `1`. Em Python dá `1`. Se você testar `resto == 1` para ímpar, o C erra com negativos. Qual teste funciona nas duas linguagens?

</details>
