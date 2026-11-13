# 02 · Média de N números

> Nível: ⭐⭐ · Assuntos: Scanner, laços, printf, Locale · Criado por: @clehdev

## Enunciado

Leia uma quantidade `N` e depois `N` números inteiros. Mostre a **média** deles com **duas casas decimais**.

## Entrada

- Primeira linha: `N` (de 1 a 100).
- Depois, `N` números inteiros, um por linha.

## Saída

A média com duas casas decimais, usando **ponto** como separador: `7.50`, e não `7,50`.

## Exemplos

| Entrada | Saída |
|---|---|
| `4`<br>`7`<br>`8`<br>`6`<br>`9` | `7.50` |
| `1`<br>`10` | `10.00` |

## 💡 Dicas

<details>
<summary>Dica 1</summary>

Cuidado com a divisão inteira: `soma / n` entre dois `int` descarta os decimais. Veja "Conversões" em [tipos e variáveis](../../material/02-tipos-e-variaveis.md#conversões).

</details>

<details>
<summary>Dica 2 (a pegadinha brasileira!)</summary>

Se o seu computador estiver em português, o `printf("%.2f")` mostra `7,50` e o teste falha. Leia a seção [vírgula ou ponto?](../../material/02-tipos-e-variaveis.md#a-pegadinha-brasileira-vírgula-ou-ponto) e use `Locale.setDefault(Locale.US);`.

</details>
