# 09 · Conserte o robô

> Nível: ⭐⭐⭐ Modelagem de dados · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

O robô entregador precisa saber quantas tarefas ainda faltam.

## O que construir

Guarde uma lista de entregas, conclua uma delas e conte quantas permanecem pendentes.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Um inteiro N; N linhas `destino estado` (0 pendente, 1 concluída); por fim o destino da entrega a concluir.

## Saída

Duas linhas: `Pendentes: N` e `Concluidas: N`, nesta ordem.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
3
Centro 0
Norte 0
Sul 1
Norte
```

**Saída:**
```text
Pendentes: 1
Concluidas: 2
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Use uma coleção de registros e uma função para mudar o estado da entrega desejada.

</details>

<details>
<summary>Pista 2</summary>

Se a entrega já estava concluída, não a conte duas vezes.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/09-robo/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Organize Entrega em uma classe (Java/Python) ou struct (C) e mostre também percentual concluído.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
