# 03 · Arrays e strings

> Pré-requisito: [vetores (lógica)](../../../disciplinas/logica/material/06-vetores.md)

## Arrays

```java
int[] notas = new int[5];               // 5 posições, todas começam em 0
int[] primos = {2, 3, 5, 7, 11};        // já com valores
System.out.println(primos[0]);          // 2
System.out.println(primos.length);      // 5 (tamanho, sem parênteses!)
```

Diferente do C, o Java **confere** os limites: acessar `primos[5]` gera um erro claro, o `ArrayIndexOutOfBoundsException`, em vez de ler lixo da memória.

### Percorrendo

```java
for (int i = 0; i < primos.length; i++) {
    System.out.println(primos[i]);
}

// for-each: quando não precisa do índice
for (int p : primos) {
    System.out.println(p);
}
```

### Utilitários da classe Arrays

```java
import java.util.Arrays;

int[] v = {5, 2, 9, 1};
Arrays.sort(v);                              // ordena: [1, 2, 5, 9]
System.out.println(Arrays.toString(v));      // "[1, 2, 5, 9]"
```

> ⚠️ `System.out.println(v)` mostra algo como `[I@1b6d3586` (o endereço do array). Use `Arrays.toString(v)`.

## Strings

```java
String nome = "Unidunedev";
nome.length()            // 10 (aqui COM parênteses: é um método)
nome.charAt(0)           // 'U'
nome.toUpperCase()       // "UNIDUNEDEV"
nome.substring(0, 3)     // "Uni"
nome.contains("dev")     // true
nome.split("d")          // array: ["Uni", "une", "ev"]
"  oi  ".trim()          // "oi"
```

> ⚠️ `length` em arrays (sem parênteses) e `length()` em String (com parênteses). Todo mundo confunde no começo.

## ⚠️ Nunca compare String com `==`

```java
String a = "cafe";
String b = new Scanner(System.in).nextLine();   // usuário digita "cafe"

a == b            // false  😱
a.equals(b)       // true   ✅
a.equalsIgnoreCase("CAFE")   // true: ignora maiúsculas
```

**Por quê?** Para objetos (e `String` é um objeto), o `==` compara **se são o mesmo objeto na memória**, e não se têm o mesmo conteúdo. Às vezes dá `true` por coincidência (o Java reaproveita textos iguais escritos no código), o que torna esse bug ainda mais traiçoeiro.

> 💡 Regra: `==` para primitivos (`int`, `double`, `char`...). `.equals()` para objetos (`String` e qualquer classe).

## Strings são imutáveis

```java
String s = "oi";
s.toUpperCase();          // cria um texto NOVO, mas você não guardou
System.out.println(s);    // "oi"
s = s.toUpperCase();      // agora sim
```

### Montando textos grandes: StringBuilder

Juntar textos com `+` dentro de um laço cria um objeto novo a cada volta. Para muitos pedaços, use o `StringBuilder`:

```java
StringBuilder sb = new StringBuilder();
for (int i = 1; i <= 3; i++) {
    sb.append(i).append(" ");
}
System.out.println(sb.toString());   // "1 2 3 "
```

## 🧪 Teste rápido

1. Qual o erro ao acessar `v[10]` num array de 5 posições?
2. Por que `a == b` pode dar `false` com dois textos iguais?
3. Como mostrar um array inteiro na tela?

---

[⬅️ Tipos e variáveis](02-tipos-e-variaveis.md) · [Próximo: Métodos ➡️](04-metodos.md)
