# 13 · Salve o gatinho 🐾

> Nível: ⭐ Primeiros passos · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

Mingau foi atrás de uma borboleta e acabou preso num galho alto. A equipe de resgate está a caminho, mas precisa saber se a escada disponível alcança o galho. Seu programa vai ajudar a equipe a calcular **quantos metros faltam**, se a escada for curta.

**Lembrete:** esta é uma história de programação. Em situações reais, não tente escalar árvores nem fazer resgates por conta própria; chame uma pessoa responsável ou a equipe adequada.

## O que construir

Crie um programa de terminal que receba **a altura do galho** e **o alcance da escada**, ambos em metros. Compare os valores e mostre se a escada é suficiente ou quanto falta para a equipe trazer o equipamento certo.

Você pode resolver em C, Python ou Java. Não precisa de classes, banco de dados nem interface gráfica para esta primeira versão.

## Entrada

Uma linha contendo dois números reais **não negativos**:

```text
altura alcance
```

Os valores usam ponto como separador decimal.

## Saída

- Se o alcance for maior ou igual à altura, imprima exatamente `Alcanca`.
- Caso contrário, imprima exatamente `Faltam: N.NN`, substituindo `N.NN` pela diferença em metros, com duas casas decimais.

Não imprima prompts extras em stdout, porque a correção compara as saídas.

## Exemplo

**Entrada:**

```text
5 3
```

**Saída:**

```text
Faltam: 2.00
```

## 💡 Pistas (abra quando precisar)

<details>
<summary>Pista 1 · Quais valores entram?</summary>

Você precisa saber a altura que deve ser alcançada e a altura que a escada pode alcançar.

</details>

<details>
<summary>Pista 2 · Como saber se é suficiente?</summary>

Pense numa condição que compare esses valores. Experimente o caso em que a escada tem exatamente o mesmo alcance do galho.

</details>

<details>
<summary>Pista 3 · Como mostrar a diferença?</summary>

Quando a escada é menor que o necessário, a distância que falta pode ser calculada com uma subtração. Sua linguagem precisa formatar o número com duas casas.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entrada e saída. Use o mesmo padrão dos outros desafios:

```bash
python scripts/testar.py disciplinas/missoes/desafios/13-gatinho/solucoes/seu-username.py
```

Substitua o username e a extensão conforme a linguagem. Em C use `.c`, em Python `.py` e em Java `.java`. No Java, use uma classe `Main` sem `public` e formatação `Locale.US` para valores decimais.

## ✨ Depois, se quiser

Organize a comparação em uma função. Teste também valores iguais e a altura zero.

**A entrega só estará aberta quando a comunidade anunciar o Desafio 2.**

[Voltar ao cardápio das missões](../../README.md)
