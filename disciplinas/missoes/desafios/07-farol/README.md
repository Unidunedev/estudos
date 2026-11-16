# 07 · Acenda o farol

> Nível: ⭐ Iniciante · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

O operador da ilha precisa descobrir por quantas horas a bateria vai sustentar a luz.

## O que construir

Calcule a autonomia da bateria considerando a energia guardada e o gasto por hora.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Dois números reais: energia disponível e gasto por hora.

## Saída

Imprima `Horas: N.NN` com duas casas se o gasto for maior que zero; caso contrário imprima `Invalido`.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
100 20
```

**Saída:**
```text
Horas: 5.00
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Antes de dividir, pense em qual valor pode provocar divisão por zero.

</details>

<details>
<summary>Pista 2</summary>

O resultado representa horas e deve ter duas casas decimais.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/07-farol/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Pergunte a duração da noite e informe se a autonomia será suficiente.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
