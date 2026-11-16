# 06 · Proteja o castelo

> Nível: ⭐⭐⭐ Modelagem de dados · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

A guardiã precisa atualizar a quantidade de suprimentos sem deixar o estoque negativo.

## O que construir

Gerencie registros de itens e atualize uma quantidade com uma operação de entrada ou retirada.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Um inteiro N; N linhas com `nome estoque_inicial`; depois uma linha `nome ADICIONAR quantidade` ou `nome RETIRAR quantidade`.

## Saída

Imprima `Estoque: N` depois de uma operação válida, `Insuficiente` quando a retirada ultrapassar o estoque, ou `Nao encontrado` para item ausente.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
2
Pocao 10
Mapa 3
Pocao RETIRAR 4
```

**Saída:**
```text
Estoque: 6
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Em Python/Java, uma classe Item pode guardar os dados; em C, use struct e funções.

</details>

<details>
<summary>Pista 2</summary>

Valide uma retirada antes de alterar o estoque.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/06-castelo/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Em Java/Python, experimente estender Item com um tipo perecível; em C, organize mais campos em structs.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
