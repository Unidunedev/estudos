# 03 · Média e situação

> Nível: ⭐⭐ · Assuntos: double, operadores, if/else · Criado por: @clehdev

## Enunciado

Leia as três notas de um aluno, calcule a **média aritmética** e diga a situação dele:

| Média | Situação |
|---|---|
| 7.0 ou mais | `Aprovado` |
| De 5.0 até menos de 7.0 | `Recuperacao` |
| Menos de 5.0 | `Reprovado` |

## Entrada

Três notas (números com casas decimais, de 0 a 10), uma por linha.

## Saída

Duas linhas:

1. `Media: ` seguido da média **com uma casa decimal**
2. A situação, escrita exatamente como na tabela (sem acento)

## Exemplos

| Entrada | Saída |
|---|---|
| `7`<br>`8`<br>`7.5` | `Media: 7.5`<br>`Aprovado` |
| `2`<br>`3`<br>`4` | `Media: 3.0`<br>`Reprovado` |

## 💡 Dicas

<details>
<summary>Dica 1</summary>

Use `double` e leia com `scanf("%lf", &nota1);`.

</details>

<details>
<summary>Dica 2</summary>

Para mostrar uma casa decimal: `printf("Media: %.1f\n", media);`

</details>

<details>
<summary>Dica 3</summary>

Comece pelo caso mais alto (`>= 7.0`), depois `else if` para `>= 5.0`, e `else` para o resto. E repare: a média exatamente 7.0 é aprovação!

</details>
