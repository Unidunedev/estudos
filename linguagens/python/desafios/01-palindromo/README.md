# 01 · Palíndromo

> Nível: ⭐ · Assuntos: strings, fatiamento · Criado por: @clehdev

## Enunciado

Um **palíndromo** é uma palavra que se lê igual de trás para frente: `arara`, `radar`, `ovo`.

Leia uma palavra e diga se ela é um palíndromo, **sem diferenciar maiúsculas de minúsculas** (`Ana` é palíndromo).

## Entrada

Uma palavra, sem espaços e sem acentos.

## Saída

`SIM` ou `NAO`.

## Exemplos

| Entrada | Saída |
|---|---|
| `arara` | `SIM` |
| `Ana` | `SIM` |
| `python` | `NAO` |

## 💡 Dicas

<details>
<summary>Dica 1</summary>

Veja o fatiamento com `[::-1]` no material de [strings](../../material/03-strings.md).

</details>

<details>
<summary>Dica 2</summary>

Para ignorar maiúsculas, transforme tudo em minúsculas antes de comparar.

</details>

<details>
<summary>Desafio extra</summary>

Resolva também **sem** o `[::-1]`, comparando a primeira letra com a última, a segunda com a penúltima... É assim que se faz em C!

</details>
