# 02 · Frequência de palavras

> Nível: ⭐⭐ · Assuntos: dicionários, split, ordenação · Criado por: @clehdev

## Enunciado

Leia uma frase e mostre **quantas vezes cada palavra aparece**, em ordem alfabética, sem diferenciar maiúsculas de minúsculas.

## Entrada

Uma linha com palavras separadas por espaço (sem pontuação e sem acentos).

## Saída

Uma linha por palavra diferente, em **ordem alfabética** e em **minúsculas**, no formato `palavra: quantidade`.

## Exemplo

Entrada:
```
o cafe e o codigo e o cafe
```

Saída:
```
cafe: 2
codigo: 1
e: 2
o: 3
```

## 💡 Dicas

<details>
<summary>Dica 1</summary>

`input().lower().split()` já te dá a lista de palavras em minúsculas.

</details>

<details>
<summary>Dica 2</summary>

Use um dicionário para contar. Veja o exemplo "Contando ocorrências" no material de [tipos e estruturas](../../material/02-tipos-e-estruturas.md#dicionário-dict-pares-de-chave-e-valor).

</details>

<details>
<summary>Dica 3</summary>

`sorted(dicionario)` devolve as chaves em ordem alfabética.

</details>
