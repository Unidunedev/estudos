# 04 · Lance a nave

> Nível: ⭐ Iniciante · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

A astronauta precisa saber se o tanque tem combustível suficiente para decolar.

## O que construir

Compare o combustível necessário para uma viagem com a quantidade disponível no tanque.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Três números reais: distância em km, consumo em litros por km e litros disponíveis.

## Saída

Imprima apenas `Autorizada` se o tanque for suficiente, ou `Reabastecer` caso contrário.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
100 0.1 10
```

**Saída:**
```text
Autorizada
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

O programa precisa calcular uma necessidade e compará-la com o estoque.

</details>

<details>
<summary>Pista 2</summary>

Teste o caso em que o tanque tem exatamente a quantidade necessária.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/04-nave/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Calcule também quantos litros restarão no tanque após a viagem.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
