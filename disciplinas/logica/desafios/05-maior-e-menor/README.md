# 05 · Maior e menor

> Nível: ⭐⭐ · Assuntos: vetores, repetição · Criado por: @clehdev · Linguagens: C, Python ou Java

## Enunciado

Leia uma quantidade `N` e depois `N` números inteiros. Mostre o **maior** e o **menor** deles.

## Entrada

- Primeira linha: `N` (de 1 a 100).
- Depois, `N` números inteiros, um por linha. Podem ser negativos e podem se repetir.

## Saída

Duas linhas:

```
Maior: X
Menor: Y
```

## Exemplo

Entrada:
```
5
8
-2
15
3
0
```

Saída:
```
Maior: 15
Menor: -2
```

## 💡 Dicas

<details>
<summary>Dica 1</summary>

Leia os números para um vetor com um laço. Veja "Ler N valores para um vetor" no material de [vetores](../../material/06-vetores.md#ler-n-valores-para-um-vetor).

</details>

<details>
<summary>Dica 2</summary>

Comece o maior **e** o menor com o **primeiro** número lido, nunca com `0`. Por quê? Pense no caso em que todos são negativos (ou todos positivos!).

</details>

<details>
<summary>Dica 3 (desafio extra)</summary>

Dá para resolver **sem vetor**, comparando cada número assim que ele é lido. Tente as duas versões.

</details>
