# 02 · Variáveis e tipos de dados

> ⏱️ 15 minutos

## Variável é uma caixinha com etiqueta

Imagine caixinhas numa prateleira. Cada uma tem uma **etiqueta** (o nome) e guarda **uma coisa** (o valor). Você pode olhar o que tem dentro, ou trocar o conteúdo por outro.

```
idade ← 17       a caixinha "idade" guarda 17
idade ← 18       agora guarda 18 (o 17 foi jogado fora)
```

| Pseudocódigo | C | Python |
|---|---|---|
| `idade ← 17` | `int idade = 17;` | `idade = 17` |

> ⚠️ Na programação, o `=` **não** é o "igual" da matemática. `x = x + 1` não é uma equação impossível: significa "pegue o valor de `x`, some 1 e guarde de volta em `x`".

## Tipos de dados

Cada caixinha guarda um **tipo** de coisa:

| Tipo | O que guarda | Exemplos | Em C | Em Python |
|---|---|---|---|---|
| **Inteiro** | Números sem vírgula | `17`, `-3`, `0` | `int` | `int` |
| **Real** | Números com vírgula | `7.5`, `3.14`, `-0.5` | `double` (ou `float`) | `float` |
| **Caractere** | Uma letra ou símbolo | `'A'`, `'?'` | `char` | (texto de 1 letra) |
| **Texto** | Uma sequência de caracteres | `"Ana"`, `"Oi!"` | vetor de `char` | `str` |
| **Lógico** | Verdadeiro ou falso | `verdadeiro`, `falso` | `int` (1 ou 0) ou `bool` | `bool` (`True`/`False`) |

> ⚠️ Em programação, o separador decimal é o **ponto**: `7.5`, nunca `7,5`.

## Por que o tipo importa?

```python
print(7 / 2)     # 3.5   (Python: divisão normal)
print(7 // 2)    # 3     (Python: divisão inteira)
```

```c
printf("%d\n", 7 / 2);      // 3    (C: dois inteiros dão resultado inteiro!)
printf("%f\n", 7.0 / 2);    // 3.500000
```

Em C, dividir dois `int` **descarta a parte decimal**. Esse é um dos erros mais comuns de quem está começando: calcular a média com `int` e ver o `7.5` virar `7`.

## Bons nomes de variáveis

| ✅ Bom | ❌ Ruim | Por quê |
|---|---|---|
| `idade` | `x` | Diz o que guarda |
| `nota_final` / `notaFinal` | `nf` | Sem abreviações misteriosas |
| `total_alunos` | `total alunos` | Espaço não é permitido |
| `media2` | `2media` | Não pode começar com número |
| `preco` | `preço` | Evite acentos: muitas linguagens não aceitam |

Também não pode usar **palavras reservadas** da linguagem como nome (`if`, `for`, `int`, `while`...).

## Entrada e saída

| Pseudocódigo | C | Python |
|---|---|---|
| `leia idade` | `scanf("%d", &idade);` | `idade = int(input())` |
| `escreva idade` | `printf("%d\n", idade);` | `print(idade)` |

> 💡 No Python, o `input()` sempre lê **texto**. Por isso o `int(...)` em volta: ele converte `"17"` (texto) em `17` (número). Sem isso, `"17" + 1` dá erro!

## Trocando valores: o problema dos dois copos

Como trocar o conteúdo de `a` e `b`? Se fizer assim:

```
a ← b
b ← a
```

...você perde o valor original de `a`! É como trocar o suco de dois copos: você precisa de um **terceiro copo**.

```
aux ← a
a ← b
b ← aux
```

Faça o teste de mesa com `a = 1` e `b = 2` nas duas versões e veja a diferença.

## 🧪 Teste rápido

1. Qual tipo você usaria para guardar: a altura de uma pessoa? O número de irmãos? Se ela é maior de idade?
2. Em C, quanto vale `int x = 9 / 2;`?
3. O que acontece com `idade = input()` seguido de `idade + 1` no Python?

---

[⬅️ O que é um algoritmo](01-o-que-e-um-algoritmo.md) · [Próximo: Operadores ➡️](03-operadores.md)
