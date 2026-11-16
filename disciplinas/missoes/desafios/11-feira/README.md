# 11 · A feira das estrelas

> Nível: ⭐ Iniciante · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

Um comerciante espacial precisa conferir descontos e trocos.

## O que construir

Calcule o total de dois produtos, aplique um desconto percentual e descubra o troco ou a falta de dinheiro.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Seis números: `preco1 quantidade1 preco2 quantidade2 desconto_percentual valor_pago`.

## Saída

Imprima `Troco: N.NN` se o pagamento for suficiente ou `Falta: N.NN` se não cobrir o total.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
10 2 5 1 10 30
```

**Saída:**
```text
Troco: 7.50
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Primeiro calcule o subtotal e depois aplique o percentual de desconto.

</details>

<details>
<summary>Pista 2</summary>

Compare o valor final com o dinheiro pago e formate o resultado com duas casas.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/11-feira/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Separe o cálculo em funções e valide quantidades negativas.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
