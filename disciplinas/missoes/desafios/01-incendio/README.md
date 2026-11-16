# 01 · Apague o incêndio

> Nível: ⭐ Iniciante · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

Os bombeiros precisam prever o consumo de água antes de iniciar o resgate.

## O que construir

Faça um programa que calcule quantos litros de água serão utilizados durante uma operação.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Dois números reais: vazão de água em litros por minuto e duração em minutos.

## Saída

Uma linha no formato `Litros: N.NN`, com duas casas decimais.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
5 3
```

**Saída:**
```text
Litros: 15.00
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Identifique quais valores entram no cálculo e qual unidade a resposta deve ter.

</details>

<details>
<summary>Pista 2</summary>

Em C, use scanf e printf; em Python, input e print; em Java, Scanner e impressão com Locale.US.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/01-incendio/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Acrescente o preço por litro e calcule o custo da operação.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
