# 03 · Conta bancária

> Nível: ⭐⭐ · Assuntos: classes, objetos, encapsulamento · Criado por: @clehdev

## Enunciado

Crie uma **classe** `ContaBancaria` com:

- os atributos **privados** `titular` e `saldo` (inteiro);
- um construtor que recebe o titular e o saldo inicial;
- os métodos `depositar(valor)` e `sacar(valor)`. O `sacar` retorna `boolean` e **não** deixa o saldo ficar negativo;
- os getters `getTitular()` e `getSaldo()`.

Depois, use a classe para processar uma lista de operações.

> 💡 É o mesmo desafio da [pasta de Python](../../../python/desafios/03-conta-bancaria/). Fez nas duas? Compare as soluções!

## Entrada

- Linha 1: o nome do titular.
- Linha 2: o saldo inicial (inteiro).
- Depois, uma operação por linha, até a palavra `FIM`:
  - `DEPOSITO valor`
  - `SAQUE valor`

## Saída

| Situação | Mensagem |
|---|---|
| Depósito | `Deposito de X realizado` |
| Saque com saldo suficiente | `Saque de X realizado` |
| Saque maior que o saldo | `Saldo insuficiente` |

E, ao final: `Titular: saldo final X`

## Exemplo

Entrada:
```
Ana
100
DEPOSITO 50
SAQUE 30
SAQUE 500
FIM
```

Saída:
```
Deposito de 50 realizado
Saque de 30 realizado
Saldo insuficiente
Ana: saldo final 120
```

## 💡 Dicas

<details>
<summary>Dica 1: duas classes num arquivo só</summary>

Nos desafios, tudo fica no arquivo `seu-username.java`. Coloque a classe com o `main` **primeiro** e a `ContaBancaria` depois, **sem** o `public`:

```java
public class Main {
    public static void main(String[] args) { ... }
}

class ContaBancaria {
    ...
}
```

</details>

<details>
<summary>Dica 2: lendo as operações</summary>

```java
while (true) {
    String linha = sc.nextLine();
    if (linha.equals("FIM")) break;     // .equals, nunca ==
    String[] partes = linha.split(" ");
    String operacao = partes[0];
    int valor = Integer.parseInt(partes[1]);
}
```

Leia o titular e o saldo também com `nextLine()` (e `Integer.parseInt`) para fugir da pegadinha do `nextInt`.

</details>
