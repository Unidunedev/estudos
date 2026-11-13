# 03 · Tipos e memória em C

> Pré-requisito: [variáveis e tipos (lógica)](../../../disciplinas/logica/material/02-variaveis-e-tipos.md)

Em C, você enxerga a memória de perto. Entender isso agora evita muitos bugs misteriosos depois.

## Cada tipo ocupa um tamanho

A memória é uma fila enorme de **bytes** (cada byte = 8 bits, 8 zeros ou uns). Cada tipo ocupa uma quantidade de bytes:

| Tipo | Tamanho comum | Guarda |
|---|---|---|
| `char` | 1 byte | Um caractere (ou números de -128 a 127) |
| `int` | 4 bytes | Inteiros de cerca de -2,1 bilhões a 2,1 bilhões |
| `long long` | 8 bytes | Inteiros enormes (até ~9 quintilhões) |
| `float` | 4 bytes | Reais, com ~7 dígitos de precisão |
| `double` | 8 bytes | Reais, com ~15 dígitos de precisão |

Descubra os tamanhos na sua máquina com o `sizeof`:

```c
printf("int: %zu bytes\n", sizeof(int));
printf("double: %zu bytes\n", sizeof(double));
```

## Estouro (overflow): quando o número não cabe

Um `int` tem limite. Passou dele, o valor "dá a volta" e vira um número errado, **sem nenhum aviso**:

```c
int grande = 2147483647;   // o maior int
grande = grande + 1;
printf("%d\n", grande);    // -2147483648 (!)
```

É como o hodômetro de um carro antigo que volta para 000000. Se o resultado pode ser grande (fatorial, por exemplo), use `long long` com `%lld`.

## Números reais não são exatos

```c
double x = 0.1 + 0.2;
printf("%.17f\n", x);      // 0.30000000000000004
```

O computador guarda reais em binário, e alguns números (como 0,1) não têm representação exata, como 1/3 não tem em decimal (0,333...). Consequência prática:

```c
if (x == 0.3)              // ❌ falso!
```

Para comparar reais, aceite uma pequena margem de erro, ou arredonde ao mostrar (`%.2f`).

## Variável sem valor guarda lixo

```c
int soma;                  // ❌ quanto vale? ninguém sabe!
for (int i = 1; i <= 3; i++) soma += i;
```

Em C, uma variável criada sem valor inicial pega o que estava "largado" naquele pedaço da memória. O resultado muda a cada execução. **Sempre inicialize:** `int soma = 0;`.

> 💡 Compile com `-Wall -Wextra`: o compilador avisa muitos desses casos.

## Conversão de tipos (cast)

Lembra que `7 / 2` dá `3` entre inteiros? Para forçar a divisão real:

```c
int total = 7, quantidade = 2;
double media = (double) total / quantidade;   // 3.5
```

O `(double)` converte o valor antes da conta. Isso se chama **cast**.

## 🧪 Teste rápido

1. Por que `int x = 3000000000;` dá problema?
2. Qual o perigo de comparar dois `double` com `==`?
3. O que acontece com uma variável `int` declarada sem valor inicial?

---

[⬅️ printf e scanf](02-entrada-e-saida.md) · [Próximo: Vetores e strings ➡️](04-vetores-e-strings.md)
