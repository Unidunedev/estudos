# 07 · Coleções: ArrayList e HashMap

Arrays têm tamanho fixo. No dia a dia, o Java usa **coleções**, que crescem sozinhas.

## ArrayList: a lista que cresce

```java
import java.util.ArrayList;
import java.util.List;

List<String> nomes = new ArrayList<>();
nomes.add("Ana");
nomes.add("Bia");
nomes.add("Caio");
nomes.remove("Bia");
System.out.println(nomes.get(0));     // Ana
System.out.println(nomes.size());     // 2
System.out.println(nomes);            // [Ana, Caio]
System.out.println(nomes.contains("Ana"));   // true

for (String nome : nomes) {
    System.out.println(nome);
}
```

### O `<String>`: genéricos

O que vai entre `< >` diz **o tipo dos itens**. Uma `List<String>` só aceita textos: o compilador recusa números. Isso se chama **genéricos**.

> ⚠️ Coleções não aceitam tipos primitivos. Use as **classes empacotadoras**: `List<Integer>` (não `int`), `List<Double>` (não `double`). O Java converte automaticamente entre `int` e `Integer`.

| Primitivo | Empacotador |
|---|---|
| `int` | `Integer` |
| `double` | `Double` |
| `boolean` | `Boolean` |
| `char` | `Character` |

### Por que `List<String> nomes = new ArrayList<>()`?

A variável é do tipo da **interface** (`List`) e o objeto é de uma **implementação** (`ArrayList`). Se um dia precisar trocar por outra lista, você muda uma palavra só. É o "programar para uma interface" do [material anterior](06-heranca-e-polimorfismo.md).

## HashMap: chave e valor

Como um dicionário: procure pela chave, encontre o valor.

```java
import java.util.HashMap;
import java.util.Map;

Map<String, Integer> idades = new HashMap<>();
idades.put("Ana", 20);
idades.put("Caio", 22);
System.out.println(idades.get("Ana"));               // 20
System.out.println(idades.getOrDefault("Bia", 0));   // 0
System.out.println(idades.containsKey("Caio"));      // true

for (Map.Entry<String, Integer> e : idades.entrySet()) {
    System.out.println(e.getKey() + ": " + e.getValue());
}
```

Contando ocorrências:

```java
Map<String, Integer> contagem = new HashMap<>();
for (String p : "oi tchau oi".split(" ")) {
    contagem.put(p, contagem.getOrDefault(p, 0) + 1);
}
```

> 💡 O `HashMap` **não** guarda ordem. Precisa em ordem alfabética? Use `TreeMap`. Na ordem de inserção? `LinkedHashMap`.

## Qual usar?

| Preciso de... | Use |
|---|---|
| Lista que cresce, com repetidos | `ArrayList` |
| Procurar por chave | `HashMap` |
| Itens sem repetição | `HashSet` |
| Chaves em ordem | `TreeMap` |

## Ordenando objetos

```java
List<ContaBancaria> contas = new ArrayList<>();
// ... adiciona contas ...
contas.sort((a, b) -> Double.compare(b.getSaldo(), a.getSaldo()));   // maior saldo primeiro
```

O `(a, b) -> ...` é uma **lambda**: uma função curta, sem nome. Ela diz como comparar duas contas.

## Próximos passos

Com o básico e a orientação a objetos, o caminho natural no mercado é:

| Quero... | Estude |
|---|---|
| Back-end e APIs | **Spring Boot** (o mais pedido em vagas Java no Brasil) |
| Organizar projetos | **Maven** ou **Gradle** |
| Testar código | **JUnit** |
| Apps Android | **Kotlin** (a mesma base, sintaxe mais moderna) |

Os roteiros completos estão no repositório de **trilhas**.

---

[⬅️ Herança e polimorfismo](06-heranca-e-polimorfismo.md) · [Java ☕](../README.md)
