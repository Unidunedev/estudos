# 04 · Métodos (as funções do Java)

> Pré-requisito: [funções (lógica)](../../../disciplinas/logica/material/07-funcoes.md)

Em Java, toda função fica dentro de uma classe, e por isso se chama **método**.

## Métodos estáticos

Enquanto não chegamos em objetos, usaremos métodos `static` (que pertencem à classe):

```java
public class Main {
    static double media(double a, double b) {
        return (a + b) / 2;
    }

    static boolean ehPar(int n) {
        return n % 2 == 0;
    }

    public static void main(String[] args) {
        System.out.println(media(7, 8));   // 7.5
        System.out.println(ehPar(4));      // true
    }
}
```

| Parte | No exemplo |
|---|---|
| Modificador | `static` |
| Tipo de retorno | `double`, `boolean` ou `void` (nada) |
| Nome | `media` (em `camelCase`) |
| Parâmetros | `double a, double b` (cada um com seu tipo) |

> 💡 Diferente do C, a ordem não importa: o método pode estar escrito depois do `main`.

## Sobrecarga: mesmo nome, parâmetros diferentes

```java
static int somar(int a, int b) { return a + b; }
static int somar(int a, int b, int c) { return a + b + c; }
static double somar(double a, double b) { return a + b; }

somar(1, 2);        // usa o primeiro
somar(1, 2, 3);     // usa o segundo
somar(1.5, 2.5);    // usa o terceiro
```

O Java escolhe o método certo pela **quantidade e pelo tipo** dos argumentos. Isso se chama **sobrecarga** (*overloading*). O `println` faz isso: existe uma versão para `int`, outra para `String`, outra para `double`...

## Passagem de parâmetros

Igual ao C: o método recebe uma **cópia** dos valores primitivos.

```java
static void zerar(int x) { x = 0; }

int n = 5;
zerar(n);
System.out.println(n);   // 5: não mudou
```

Mas, com **objetos e arrays**, o método recebe uma cópia da **referência** (o "endereço"), então consegue alterar o conteúdo:

```java
static void zerarPrimeiro(int[] v) { v[0] = 0; }

int[] numeros = {5, 6};
zerarPrimeiro(numeros);
System.out.println(numeros[0]);   // 0: mudou!
```

## Recursão

```java
static long fatorial(int n) {
    if (n == 0) return 1;
    return n * fatorial(n - 1);
}
```

> 💡 Usamos `long` porque o fatorial cresce rápido: `13!` já não cabe num `int`.

## 🧪 Teste rápido

1. O que é sobrecarga?
2. Por que `zerar(n)` não muda o `n`, mas `zerarPrimeiro(numeros)` muda o array?

---

[⬅️ Arrays e strings](03-arrays-e-strings.md) · [Próximo: Classes e objetos ➡️](05-classes-e-objetos.md)
