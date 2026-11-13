# 04 · Contar vogais

> Nível: ⭐⭐ · Assuntos: strings, repetição, char · Criado por: @clehdev

## Enunciado

Leia uma palavra e mostre quantas **vogais** ela tem (`a`, `e`, `i`, `o`, `u`), contando maiúsculas e minúsculas.

## Entrada

Uma única palavra, sem espaços e sem acentos, com no máximo 100 letras.

## Saída

A quantidade de vogais.

## Exemplos

| Entrada | Saída |
|---|---|
| `programacao` | `5` |
| `UNIDUNEDEV` | `5` |
| `xyz` | `0` |

## 💡 Dicas

<details>
<summary>Dica 1</summary>

Leia com `scanf("%100s", palavra);` num vetor `char palavra[101];`. Por que 101?

</details>

<details>
<summary>Dica 2</summary>

Percorra a string até encontrar o `'\0'`. Veja "Percorrendo uma string" no material de [vetores e strings](../../material/04-vetores-e-strings.md#percorrendo-uma-string).

</details>

<details>
<summary>Dica 3</summary>

Para não testar maiúsculas e minúsculas separadamente, use `tolower(letra)` do `<ctype.h>`: ele transforma `'A'` em `'a'`.

</details>
