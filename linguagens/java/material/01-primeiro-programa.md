# 01 · Primeiro programa em Java

> Pré-requisito: JDK instalado ([Windows](../instalacao/windows.md) · [Mac](../instalacao/mac.md))

## O "Olá, mundo" e por que ele é tão grande

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Ola, mundo!");
    }
}
```

Em Python é uma linha. Em Java são cinco. Por quê? Porque em Java **todo código mora dentro de uma classe**. Vamos entender cada palavra (sem pressa, algumas fazem mais sentido mais para frente):

| Trecho | Significa |
|---|---|
| `public class Main` | Cria uma classe chamada `Main`. Tudo em Java fica dentro de classes |
| `public static void main(String[] args)` | O ponto de partida do programa: a JVM procura exatamente esse método |
| `public` | Pode ser acessado de fora da classe |
| `static` | Pertence à classe, não a um objeto. A JVM chama sem criar objeto nenhum |
| `void` | Não retorna nada |
| `String[] args` | Um array de textos com os argumentos da linha de comando |
| `System.out.println(...)` | Mostra um texto e pula linha (`print` sem `ln` não pula) |

> 💡 Não se preocupe em entender tudo agora. `public`, `static` e classes vão ficar claros no material de [classes e objetos](05-classes-e-objetos.md).

## Rodando

### Jeito rápido (Java 11+): ótimo para estudar

```bash
java Main.java
```

### Jeito "de verdade": compilar e depois executar

```bash
javac Main.java     # gera Main.class (bytecode)
java Main           # executa a classe (sem o .class no final!)
```

> ⚠️ No jeito "de verdade", o nome do arquivo precisa ser **igual ao nome da classe pública**: `public class Main` → `Main.java`. É um dos erros mais comuns: `class Main is public, should be declared in a file named Main.java`.

## Regras de sintaxe

- Toda instrução termina com `;`.
- Blocos ficam entre `{ }`.
- Java diferencia maiúsculas de minúsculas: `System` ≠ `system`.
- Comentários: `// uma linha` e `/* várias linhas */`.

## Convenções de nomes

| O quê | Estilo | Exemplo |
|---|---|---|
| Classes | `PascalCase` | `ContaBancaria` |
| Variáveis e métodos | `camelCase` | `saldoTotal`, `calcularMedia()` |
| Constantes | `MAIUSCULAS_COM_UNDERLINE` | `TAXA_MAXIMA` |

O Java não obriga, mas **todo mundo** segue. Código fora do padrão chama atenção numa entrevista.

## Java × C × Python

| | C | Java | Python |
|---|---|---|---|
| Ponto de partida | `int main(void)` | `public static void main(String[] args)` dentro de uma classe | o próprio arquivo |
| Mostrar | `printf("%d\n", x);` | `System.out.println(x);` | `print(x)` |
| Tipos | estáticos | estáticos | dinâmicos |
| Memória | você gerencia (`malloc`/`free`) | automática (*garbage collector*) | automática |
| Orientação a objetos | não tem | **tudo** é classe | opcional |

## 🧪 Teste rápido

1. Por que existe uma classe até no "Olá, mundo"?
2. Qual a diferença entre `print` e `println`?
3. Qual erro aparece se a classe `public class Main` estiver num arquivo `Teste.java` e você usar `javac`?

---

[⬅️ Java](../README.md) · [Próximo: Tipos e variáveis ➡️](02-tipos-e-variaveis.md)
