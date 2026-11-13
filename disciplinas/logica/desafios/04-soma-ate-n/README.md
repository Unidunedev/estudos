# 04 · Soma de 1 até N

> Nível: ⭐ · Assuntos: repetição, acumulador · Criado por: @clehdev · Linguagens: C ou Python

## Enunciado

Leia um número inteiro `N` e mostre a soma de todos os números de 1 até `N`.

Por exemplo, para `N = 5`: `1 + 2 + 3 + 4 + 5 = 15`.

## Entrada

Um número inteiro `N`, com `0 <= N <= 10000`.

## Saída

A soma. Se `N` for `0`, a soma é `0`.

## Exemplos

| Entrada | Saída |
|---|---|
| `5` | `15` |
| `100` | `5050` |

## 💡 Dicas

<details>
<summary>Dica 1</summary>

É o padrão **acumulador** do material de [repetições](../../material/05-repeticoes.md#acumulador-quanto-deu-no-total): uma variável começa em 0 e vai somando a cada volta.

</details>

<details>
<summary>Dica 2 (curiosidade)</summary>

Conta a história que o matemático Gauss, ainda criança, resolveu esse problema para `N = 100` em segundos, sem somar um por um: `N * (N + 1) / 2`. Tente as duas formas! Qual delas é mais rápida para `N` gigante?

</details>
