# 05 · Classes e objetos

> ⏱️ 30 minutos · O coração do Java: **Programação Orientada a Objetos (POO)**.

## Classe × objeto: a planta e a casa

- **Classe** é a **planta** de uma casa: o desenho de como ela é.
- **Objeto** é a **casa construída**. Com uma planta, você constrói várias casas, e cada uma pode ter cor diferente.

| Conceito | No banco | No código |
|---|---|---|
| Classe | "O que é uma conta" | `class ContaBancaria` |
| Objeto | A conta da Ana | `new ContaBancaria("Ana")` |
| Atributo | O saldo | `private double saldo;` |
| Método | Depositar | `public void depositar(double valor)` |
| Construtor | Abrir a conta | `public ContaBancaria(String titular)` |

## A primeira classe

`ContaBancaria.java`:

```java
public class ContaBancaria {
    private String titular;      // atributos
    private double saldo;

    public ContaBancaria(String titular) {   // construtor
        this.titular = titular;
        this.saldo = 0;
    }

    public void depositar(double valor) {    // métodos
        if (valor > 0) {
            saldo += valor;
        }
    }

    public boolean sacar(double valor) {
        if (valor > saldo) {
            return false;
        }
        saldo -= valor;
        return true;
    }

    public double getSaldo() {
        return saldo;
    }

    public String getTitular() {
        return titular;
    }
}
```

`Main.java`:

```java
public class Main {
    public static void main(String[] args) {
        ContaBancaria contaAna = new ContaBancaria("Ana");
        ContaBancaria contaCaio = new ContaBancaria("Caio");

        contaAna.depositar(100);
        contaAna.sacar(30);

        System.out.println(contaAna.getSaldo());    // 70.0
        System.out.println(contaCaio.getSaldo());   // 0.0: cada objeto tem o seu saldo
    }
}
```

## Entendendo as peças

### `new`: construindo o objeto
`new ContaBancaria("Ana")` reserva memória para um objeto novo e chama o **construtor**.

### Construtor
Método especial com o **mesmo nome da classe** e **sem tipo de retorno**. Roda uma vez, na criação, para dar os valores iniciais.

### `this`: "eu mesmo"
`this.titular = titular;` significa "o atributo `titular` **deste objeto** recebe o parâmetro `titular`". O `this` desfaz a confusão entre os dois nomes iguais.

### Modificadores de acesso

| Modificador | Quem pode acessar |
|---|---|
| `private` | Só a própria classe |
| (nenhum) | Classes do mesmo pacote |
| `protected` | Mesmo pacote + classes filhas |
| `public` | Qualquer um |

### Encapsulamento: atributos `private`, acesso por métodos

Os atributos são `private` para ninguém fazer `conta.saldo = 1000000` de fora. A única forma de mudar o saldo é por `depositar` e `sacar`, que **validam** as regras. Para ler, existem os **getters** (`getSaldo()`).

> 💡 Diferente do Python (onde o `_` é só um combinado), no Java o `private` é **obrigatório**: tentar acessar dá erro de compilação.

## Mostrando o objeto: `toString`

```java
@Override
public String toString() {
    return titular + ": R$ " + String.format(java.util.Locale.US, "%.2f", saldo);
}
```

```java
System.out.println(contaAna);   // Ana: R$ 70.00
```

Sem o `toString`, aparece algo como `ContaBancaria@1b6d3586`. O `@Override` indica que você está **substituindo** um método que já existe (todo objeto Java herda um `toString` padrão).

## Estático × de instância

| | `static` | Sem `static` (de instância) |
|---|---|---|
| Pertence a | A **classe** | Cada **objeto** |
| Exemplo | `Math.sqrt(9)` | `conta.depositar(50)` |
| Precisa de `new`? | Não | Sim |

```java
public class ContaBancaria {
    private static int totalDeContas = 0;   // um só, compartilhado por todas

    public ContaBancaria(String titular) {
        this.titular = titular;
        totalDeContas++;
    }
}
```

## record: classes de dados em uma linha (Java 16+)

Para classes que só guardam dados, sem regras:

```java
record Aluno(String nome, double nota) {}

Aluno a = new Aluno("Ana", 9.5);
System.out.println(a.nome());   // Ana
System.out.println(a);          // Aluno[nome=Ana, nota=9.5]
```

O Java gera sozinho construtor, getters, `toString` e `equals`.

## 🧪 Teste rápido

1. Qual a diferença entre classe e objeto?
2. Por que os atributos devem ser `private`?
3. Crie a classe `Aluno` com `nome`, um array de notas e o método `media()`.

## 🎯 Pratique

- [03 · Conta bancária](../desafios/03-conta-bancaria/)

---

[⬅️ Métodos](04-metodos.md) · [Próximo: Herança e polimorfismo ➡️](06-heranca-e-polimorfismo.md)
