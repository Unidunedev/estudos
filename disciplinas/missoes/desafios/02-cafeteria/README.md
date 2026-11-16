# 02 · Salve a cafeteria

> Nível: ⭐ Iniciante · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

O gatinho barista precisa fechar a conta de pedidos que chegaram juntos.

## O que construir

Uma cafeteria vende café por 5 unidades, bolo por 8 e chá por 4. Receba as quantidades e calcule o total do pedido.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Três inteiros não negativos, nesta ordem: quantidade de cafés, bolos e chás.

## Saída

Uma linha no formato `Total: N.NN`, com duas casas decimais.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
1 1 1
```

**Saída:**
```text
Total: 17.00
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Os preços são fixos neste primeiro desafio; as quantidades são os dados de entrada.

</details>

<details>
<summary>Pista 2</summary>

Um menu interativo com novos pedidos pode vir depois, como evolução do seu projeto.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/02-cafeteria/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Monte um menu que permita vários pedidos, usando laços e funções.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
