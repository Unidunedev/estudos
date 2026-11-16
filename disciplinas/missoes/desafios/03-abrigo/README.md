# 03 · Ajude o abrigo

> Nível: ⭐⭐⭐ Modelagem de dados · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

As fichas dos bichinhos estão misturadas e o abrigo precisa encontrar cada animal rapidamente.

## O que construir

Cadastre animais com nome, espécie e idade; depois busque um deles pelo nome.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Um inteiro N (0 a 30); depois N linhas com `nome especie idade` (palavras sem espaços); por fim, o nome a procurar.

## Saída

Se encontrar, imprima `Encontrado: nome especie idade`; caso contrário, `Nao encontrado`.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
3
Luna gato 2
Bidu cachorro 5
Mimi gato 1
Mimi
```

**Saída:**
```text
Encontrado: Mimi gato 1
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Pense em um tipo de registro com campos relacionados: struct em C ou classe em Java/Python.

</details>

<details>
<summary>Pista 2</summary>

Guarde vários registros e percorra a coleção até encontrar o nome.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/03-abrigo/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Permita marcar um animal como adotado. Em Java ou Python, tente uma subclasse como desafio opcional.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
