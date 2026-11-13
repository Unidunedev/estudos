# 06 · Fatorial

> Nível: ⭐⭐ · Assuntos: funções, repetição · Criado por: @clehdev · Linguagens: C, Python ou Java

## Enunciado

O **fatorial** de um número `N` (escrito `N!`) é a multiplicação de todos os inteiros de 1 até `N`:

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Por definição, `0! = 1`.

Escreva uma **função** `fatorial(n)` que **retorne** o fatorial de `n`. Depois, leia um número e mostre o resultado usando a sua função.

## Entrada

Um número inteiro `N`, com `0 <= N <= 12`.

## Saída

O valor de `N!`.

## Exemplos

| Entrada | Saída |
|---|---|
| `5` | `120` |
| `0` | `1` |

## 💡 Dicas

<details>
<summary>Dica 1</summary>

Lembre a diferença entre `return` e `print` no material de [funções](../../material/07-funcoes.md#return--print): a função **retorna**, e quem chamou **mostra**.

</details>

<details>
<summary>Dica 2</summary>

É um acumulador, mas de **multiplicação**: ele precisa começar em `1`, não em `0`. Por quê?

</details>

<details>
<summary>Dica 3 (por que só até 12?)</summary>

O fatorial cresce muito rápido. `13!` já passa de 6 bilhões, mais do que cabe num `int` em C. Teste o que acontece com `13` e pesquise sobre o tipo `long long`. No Python não tem esse problema: os inteiros crescem à vontade.

</details>
