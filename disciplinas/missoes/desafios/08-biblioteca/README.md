# 08 · A biblioteca encantada

> Nível: ⭐⭐ Desenvolvendo · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

A coruja bibliotecária precisa registrar empréstimos e devoluções.

## O que construir

Registre livros e altere a disponibilidade de um deles conforme uma operação recebida.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Um inteiro N; N linhas com `titulo autor disponivel` (1 significa disponível, 0 emprestado); por fim `titulo EMPRESTAR` ou `titulo DEVOLVER`.

## Saída

Imprima `Emprestado` após empréstimo válido, `Devolvido` após devolução válida, `Indisponivel` se tentar emprestar um livro já emprestado, ou `Nao encontrado` se não existir.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
2
Aventura Ana 1
Magia Bia 0
Aventura EMPRESTAR
```

**Saída:**
```text
Emprestado
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Cada livro precisa de um título, autor e estado de empréstimo.

</details>

<details>
<summary>Pista 2</summary>

Em C, use struct; em Java/Python, experimente uma classe Livro com um método para cada operação.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/08-biblioteca/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Monte um menu para atualizar vários livros e, se quiser, salve o catálogo em arquivo.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
