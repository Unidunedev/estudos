# 03 · Operadores

> ⏱️ 15 minutos

Operadores são os símbolos que fazem contas e comparações.

## Aritméticos: as contas

| Operador | Significa | Exemplo | Resultado |
|---|---|---|---|
| `+` | Soma | `5 + 3` | `8` |
| `-` | Subtração | `5 - 3` | `2` |
| `*` | Multiplicação | `5 * 3` | `15` |
| `/` | Divisão | `7 / 2` | `3.5` (Python) ou `3` (C, com inteiros) |
| `%` | **Resto** da divisão | `7 % 2` | `1` |

### O operador `%` (resto) é seu melhor amigo

Ele parece estranho, mas resolve um monte de problemas:

| Pergunta | Como responder com `%` |
|---|---|
| O número é par? | `n % 2 == 0` |
| É múltiplo de 5? | `n % 5 == 0` |
| Qual o último dígito? | `n % 10` (ex.: `347 % 10` é `7`) |
| Que horas serão daqui a 30 horas, se agora são 20h? | `(20 + 30) % 24` = `2` |

### Ordem das contas (precedência)

Igual na matemática: `*`, `/` e `%` vêm antes de `+` e `-`.

```
2 + 3 * 4      = 14   (não 20!)
(2 + 3) * 4    = 20
```

Erro clássico na média:

```
nota1 + nota2 / 2      ❌ divide só a nota2
(nota1 + nota2) / 2    ✅
```

> 💡 Na dúvida, **use parênteses**. Não custa nada e deixa o código mais claro.

## Relacionais: as comparações

O resultado de uma comparação é sempre **verdadeiro** ou **falso**.

| Operador | Significa | Exemplo (`x = 5`) | Resultado |
|---|---|---|---|
| `==` | Igual a | `x == 5` | verdadeiro |
| `!=` | Diferente de | `x != 5` | falso |
| `>` | Maior que | `x > 5` | falso |
| `>=` | Maior **ou igual** | `x >= 5` | verdadeiro |
| `<` | Menor que | `x < 10` | verdadeiro |
| `<=` | Menor ou igual | `x <= 4` | falso |

> ⚠️ **`=` guarda, `==` compara.** Em C, escrever `if (x = 5)` não dá erro: ele **guarda** 5 em `x` e o teste fica sempre verdadeiro. Um bug silencioso! Compilar com `-Wall` ajuda a pegar isso.

## Lógicos: juntando condições

| Pseudocódigo | C | Python | É verdadeiro quando... |
|---|---|---|---|
| `E` | `&&` | `and` | **as duas** condições são verdadeiras |
| `OU` | `\|\|` | `or` | **pelo menos uma** é verdadeira |
| `NÃO` | `!` | `not` | inverte: verdadeiro vira falso e vice-versa |

### Tabela-verdade

| A | B | A E B | A OU B | NÃO A |
|---|---|---|---|---|
| V | V | **V** | **V** | F |
| V | F | F | **V** | F |
| F | V | F | **V** | **V** |
| F | F | F | F | **V** |

Exemplos do dia a dia:

- Entrar no cinema: `idade >= 18 OU acompanhado_pelos_pais`
- Passar de ano: `media >= 7 E frequencia >= 75`
- Número entre 1 e 10: `n >= 1 E n <= 10`

> ⚠️ Em C e Python **não** se escreve `1 <= n <= 10` como na matemática... quer dizer, no Python até funciona, mas em C dá um resultado errado sem avisar. Use sempre `n >= 1 && n <= 10`.

## Atalhos que você vai ver muito

| Atalho | Equivale a |
|---|---|
| `x += 5` | `x = x + 5` |
| `x -= 1` | `x = x - 1` |
| `x *= 2` | `x = x * 2` |
| `x++` (só em C) | `x = x + 1` |

## 🧪 Teste rápido

1. Quanto vale `17 % 5`? E `20 % 4`?
2. Escreva a condição: "a nota está entre 0 e 10".
3. `(V E F) OU NÃO F` é verdadeiro ou falso?

---

[⬅️ Variáveis e tipos](02-variaveis-e-tipos.md) · [Próximo: Condicionais ➡️](04-condicionais.md)
