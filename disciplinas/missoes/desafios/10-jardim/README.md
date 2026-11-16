# 10 · Cuide do jardim da Lua

> Nível: ⭐⭐ Desenvolvendo · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

As flores lunares precisam receber a quantidade certa de água.

## O que construir

Registre as plantas e calcule o consumo total de água por dia.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Um inteiro N (0 a 30); depois N linhas `nome litros_por_dia`.

## Saída

Uma linha `Total: N.NN`, com duas casas decimais.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
3
Rosa 1.5
Lirio 2
Cacto 0.25
```

**Saída:**
```text
Total: 3.75
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

A cada planta, some apenas a quantidade de água indicada.

</details>

<details>
<summary>Pista 2</summary>

Você pode usar um vetor em C, uma lista em Python ou uma coleção em Java.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/10-jardim/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Permita remover plantas e atualize a soma.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
