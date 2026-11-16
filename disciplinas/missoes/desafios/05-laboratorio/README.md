# 05 · Organize o laboratório

> Nível: ⭐⭐ Desenvolvendo · Linguagens: C, Python e Java · Desafio 2 da Unidunedev

## A história

Os experimentos perderam as etiquetas e a cientista precisa localizar cada registro.

## O que construir

Nesta etapa automática, registre experimentos em memória e localize um pelo nome. O salvamento em arquivo será verificado manualmente como evolução.

Este é o **núcleo verificável da missão**: o robô confere a entrada e a saída abaixo. Se você quiser criar um programa maior, com menu, funções ou classes, ótimo! Só mantenha esta saída exata para os testes.

## Entrada

Um inteiro N (0 a 30); N linhas `nome data descricao` (sem espaços; data como AAAA-MM-DD); por fim, o nome que deseja buscar.

## Saída

Imprima `Encontrado: nome data descricao` ou `Nao encontrado`.

**Não imprima perguntas como** `Digite um valor:` em stdout; a saída é comparada exatamente com os testes. Use ponto (`.`) para separar as casas decimais. No Java, a saída numérica com ponto pode exigir `Locale.US`.

## Exemplo

**Entrada:**
```text
2
Pocao 2026-01-01 azul
Soro 2026-01-02 verde
Soro
```

**Saída:**
```text
Encontrado: Soro 2026-01-02 verde
```

## 💡 Pistas (abra só quando precisar)

<details>
<summary>Pista 1</summary>

Separe registro, consulta e exibição em partes menores.

</details>

<details>
<summary>Pista 2</summary>

Na versão completa, salve os registros num arquivo local e carregue-os ao iniciar; não é necessário JSON em C.

</details>

## 🧪 Testes

A pasta `testes/` contém três pares de entradas e saídas. Para executar no seu fork:

```bash
python scripts/testar.py disciplinas/missoes/desafios/05-laboratorio/solucoes/seu-username.py
```

Substitua o username e a extensão pela linguagem escolhida. Em C, use `.c`; em Java, `.java`. Para Java, uma classe `Main` sem `public` funciona num arquivo com o username.

## ✨ Para ir além (opcional)

Permita salvar e carregar registros em arquivo e editar descrições.

As funcionalidades extras devem continuar compatíveis com os testes básicos. Nos projetos com arquivos ou modelagem mais avançada, a revisão humana também avalia a organização do código.

[Voltar ao cardápio das missões](../../README.md)
