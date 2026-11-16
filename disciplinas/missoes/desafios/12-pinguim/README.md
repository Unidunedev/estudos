# 12 · Encontre o pinguim

> Nível: ⭐⭐ Desenvolvendo · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

Pipo precisa de três respostas corretas para encontrar o caminho de casa.

## O que construir

Implemente a lógica de pontuação de um quiz com três perguntas e alternativas numeradas.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Três números inteiros representando as escolhas do jogador. As respostas corretas são, nesta ordem, 2, 1 e 3. Você pode inventar as perguntas correspondentes.

## Saída

Uma linha `Acertos: N`, onde N vai de 0 a 3.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
2 1 3
```

**Saída:**
```text
Acertos: 3
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Use um vetor ou lista de respostas corretas e compare com as respostas recebidas.

</details>

<details>
<summary>Pista 2</summary>

No modo de correção automática, imprima apenas a pontuação; uma interface mais interativa pode ser um bônus.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/12-pinguim/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Crie as três perguntas e adicione um modo interativo para jogar novamente.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
