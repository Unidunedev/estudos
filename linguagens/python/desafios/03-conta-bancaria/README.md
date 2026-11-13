# 03 · Conta bancária

> Nível: ⭐⭐ · Assuntos: classes, objetos, métodos · Criado por: @clehdev

## Enunciado

Crie uma **classe** `ContaBancaria` com:

- os atributos `titular` e `saldo`;
- o método `depositar(valor)`;
- o método `sacar(valor)`, que **não** deixa o saldo ficar negativo.

Depois, use a classe para processar uma lista de operações.

## Entrada

- Linha 1: o nome do titular.
- Linha 2: o saldo inicial (inteiro).
- Depois, uma operação por linha, até a palavra `FIM`:
  - `DEPOSITO valor`
  - `SAQUE valor`

Todos os valores são inteiros positivos.

## Saída

Uma linha para cada operação:

| Situação | Mensagem |
|---|---|
| Depósito | `Deposito de X realizado` |
| Saque com saldo suficiente | `Saque de X realizado` |
| Saque maior que o saldo | `Saldo insuficiente` (o saldo não muda) |

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
<summary>Dica 1</summary>

Comece pela classe, igual ao material de [classes e objetos](../../material/05-classes-e-objetos.md). Faça o `sacar` **retornar** `True` ou `False`, e deixe o `print` para fora da classe.

</details>

<details>
<summary>Dica 2</summary>

Para ler as operações:

```python
while True:
    linha = input()
    if linha == "FIM":
        break
    operacao, valor = linha.split()
    valor = int(valor)
```

</details>

<details>
<summary>Dica 3</summary>

Sacar **exatamente** todo o saldo é permitido. Teste esse caso!

</details>
