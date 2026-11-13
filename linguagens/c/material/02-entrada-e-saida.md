# 02 · Entrada e saída: printf e scanf

## Variáveis e tipos básicos

| Tipo | Guarda | Exemplo |
|---|---|---|
| `int` | Números inteiros | `int idade = 20;` |
| `float` | Números com vírgula (precisão menor) | `float altura = 1.75;` |
| `double` | Números com vírgula (precisão maior) | `double media = 7.5;` |
| `char` | Um único caractere | `char letra = 'A';` |

> ⚠️ Em C, o separador decimal é o **ponto**: `1.75`, nunca `1,75`.

## printf: mostrar na tela

O `printf` usa **especificadores** (`%d`, `%f`...) para encaixar valores no texto:

```c
int idade = 20;
double media = 7.456;

printf("Idade: %d\n", idade);      // Idade: 20
printf("Media: %.2f\n", media);    // Media: 7.46  (duas casas decimais)
printf("Media: %.1f\n", media);    // Media: 7.5
```

| Especificador | Para | No printf | No scanf |
|---|---|---|---|
| `%d` | `int` | ✅ | ✅ |
| `%f` | `float` | ✅ | ✅ |
| `%lf` | `double` | use `%f` | ✅ (obrigatório para double) |
| `%c` | `char` | ✅ | ✅ |
| `%s` | texto | ✅ | ✅ |

## scanf: ler do teclado

```c
int a, b;
scanf("%d", &a);
scanf("%d", &b);
printf("%d\n", a + b);
```

### Por que o `&`?

O `scanf` precisa saber **onde** guardar o valor lido. O `&a` significa "o **endereço** na memória da variável `a`". Esquecer o `&` é um dos erros mais comuns, e costuma travar o programa com `Segmentation fault`. Você vai entender isso a fundo quando estudar **ponteiros**.

Para `double`, lembre do `%lf`:

```c
double nota;
scanf("%lf", &nota);
```

## Nos desafios: só a resposta!

A correção automática compara **apenas o que o programa imprime**. Então:

```c
// ❌ Quebra a correção
printf("Digite um numero: ");
scanf("%d", &a);

// ✅ Certo
scanf("%d", &a);
```

## 🧪 Teste rápido

1. Qual especificador usar no `scanf` para ler um `double`?
2. O que o `printf("%.1f", 3.14159)` mostra?

---

[⬅️ Do código ao executável](01-do-codigo-ao-executavel.md) · [Próximo: Tipos e memória ➡️](03-tipos-e-memoria.md)
