# 02 · Tipos, variáveis e entrada de dados

> Pré-requisito: [variáveis e tipos (lógica)](../../../disciplinas/logica/material/02-variaveis-e-tipos.md)

## Tipos primitivos

| Tipo | Guarda | Exemplo |
|---|---|---|
| `int` | Inteiros (até ~2,1 bilhões) | `int idade = 20;` |
| `long` | Inteiros enormes | `long populacao = 8_000_000_000L;` |
| `double` | Números reais | `double nota = 7.5;` |
| `boolean` | `true` ou `false` | `boolean aprovado = true;` |
| `char` | Um caractere (aspas simples) | `char letra = 'A';` |

> 💡 O `_` em `8_000_000_000` é só para facilitar a leitura. O `L` no final indica que é um `long`.

## String: texto (e não é primitivo!)

```java
String nome = "Ana";
```

`String` começa com maiúscula porque é uma **classe**, não um tipo primitivo. Isso faz diferença na hora de comparar (veja em [arrays e strings](03-arrays-e-strings.md)).

## var: deixe o Java deduzir o tipo (Java 10+)

```java
var idade = 20;          // o Java entende que é int
var nome = "Ana";        // String
```

O tipo continua fixo: `var` só poupa digitação. Use quando o tipo for óbvio.

## Conversões

```java
int a = 7, b = 2;
System.out.println(a / b);             // 3: inteiro dividido por inteiro!
System.out.println((double) a / b);    // 3.5: cast para double antes

int n = Integer.parseInt("42");        // texto → int
double d = Double.parseDouble("7.5");  // texto → double
String s = String.valueOf(42);         // número → texto
```

## Lendo do teclado: Scanner

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nome = sc.nextLine();       // lê a linha inteira
        int idade = sc.nextInt();          // lê um inteiro
        System.out.println(nome + " tem " + idade + " anos");
    }
}
```

| Método | Lê |
|---|---|
| `nextInt()` | Um inteiro |
| `nextDouble()` | Um real |
| `next()` | Uma palavra (até o espaço) |
| `nextLine()` | A linha inteira |
| `hasNextInt()` | Verifica se ainda há um inteiro para ler |

> ⚠️ **A pegadinha do nextLine:** depois de um `nextInt()`, o Enter fica "sobrando". O próximo `nextLine()` lê essa linha vazia. Solução: chamar um `sc.nextLine();` extra para descartar, ou ler tudo com `nextLine()` e converter com `Integer.parseInt`.

## Mostrando números formatados

```java
double media = 7.456;
System.out.println(media);                          // 7.456
System.out.printf("%.2f%n", media);                 // 7.46 (como no C!)
String texto = String.format("Media: %.1f", media); // monta um texto
```

O `%n` é a quebra de linha (funciona em qualquer sistema).

## A pegadinha brasileira: vírgula ou ponto?

O Java usa as configurações regionais do computador (o **Locale**). Num computador em português:

```java
System.out.printf("%.2f%n", 7.5);     // 7,50  😱 (com vírgula!)
```

E o `Scanner` passa a esperar `7,5` na entrada, recusando `7.5` com um `InputMismatchException`.

Isso quebra testes automáticos e integrações com outros sistemas. A solução é fixar o padrão americano (ponto):

```java
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);            // primeira linha do main
        Scanner sc = new Scanner(System.in);
        double nota = sc.nextDouble();           // aceita 7.5
        System.out.printf("%.2f%n", nota);       // mostra 7.50
    }
}
```

> 💡 Poucos cursos falam disso, e muita gente perde horas achando que o código está errado. Nos desafios com números reais, use sempre o `Locale.setDefault(Locale.US);`.

## Constantes

```java
final double PI = 3.14159;   // final: não pode mudar depois
```

## 🧪 Teste rápido

1. Por que `String` começa com maiúscula e `int` não?
2. O que `System.out.println(9 / 2);` mostra?
3. Por que o `printf("%.2f")` pode mostrar vírgula no seu computador?

## 🎯 Pratique

- [02 · Média de N números](../desafios/02-media-de-n/)

---

[⬅️ Primeiro programa](01-primeiro-programa.md) · [Próximo: Arrays e strings ➡️](03-arrays-e-strings.md)
