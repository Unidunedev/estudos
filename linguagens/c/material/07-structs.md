# 07 · Structs: agrupando dados

> Pré-requisito: [ponteiros](06-ponteiros.md)

O C não tem classes. Mas tem a **struct**: um jeito de juntar várias informações sobre a mesma coisa num tipo só. É o "avô" das classes do Java e do Python.

## O problema

```c
char nome1[50];
int idade1;
double nota1;

char nome2[50];
int idade2;
double nota2;
// ... e assim por diante, para cada aluno 😩
```

## Criando uma struct

```c
#include <stdio.h>
#include <string.h>

struct Aluno {
    char nome[50];
    int idade;
    double nota;
};

int main(void) {
    struct Aluno a;
    strcpy(a.nome, "Ana");
    a.idade = 20;
    a.nota = 9.5;

    printf("%s, %d anos, nota %.1f\n", a.nome, a.idade, a.nota);
    return 0;
}
```

- O **ponto** (`.`) acessa cada campo: `a.nome`, `a.idade`.
- Para textos, use `strcpy` (lembra? não dá para usar `=` com strings).

## typedef: um nome mais curto

Escrever `struct Aluno` toda hora cansa. O `typedef` cria um apelido:

```c
typedef struct {
    char nome[50];
    int idade;
    double nota;
} Aluno;

Aluno a = {"Ana", 20, 9.5};    // agora é só "Aluno"
```

## Vetor de structs

```c
Aluno turma[3] = {
    {"Ana", 20, 9.5},
    {"Bia", 19, 7.0},
    {"Caio", 21, 8.0}
};

double soma = 0;
for (int i = 0; i < 3; i++) {
    soma += turma[i].nota;
}
printf("Media da turma: %.2f\n", soma / 3);
```

## Structs e funções: o "jeito C" de orientação a objetos

```c
typedef struct {
    char titular[50];
    int saldo;
} Conta;

void depositar(Conta *c, int valor) {
    c->saldo += valor;
}

int sacar(Conta *c, int valor) {
    if (valor > c->saldo) return 0;
    c->saldo -= valor;
    return 1;
}

int main(void) {
    Conta conta = {"Ana", 100};
    depositar(&conta, 50);
    sacar(&conta, 30);
    printf("%s: %d\n", conta.titular, conta.saldo);   // Ana: 120
    return 0;
}
```

### A seta `->`

Quando você tem um **ponteiro** para uma struct, usa `->` em vez de `.`:

```c
c->saldo      // é o mesmo que (*c).saldo
```

Por que passar um ponteiro (`Conta *c`)? Porque o C passa **cópias** para as funções (lembra do material de [funções](05-funcoes.md)?). Com o ponteiro, a função mexe na conta **original**.

## Struct × classe

| | Struct (C) | Classe (Java/Python) |
|---|---|---|
| Guarda dados | ✅ | ✅ |
| Tem métodos dentro | ❌ (funções ficam separadas) | ✅ |
| Esconde dados (`private`) | ❌ | ✅ (Java) / por combinado (Python) |
| Herança | ❌ | ✅ |

Compare o exemplo acima com a classe `ContaBancaria` do [Python](../../python/material/05-classes-e-objetos.md) e do [Java](../../java/material/05-classes-e-objetos.md). A ideia é a mesma: dados + operações sobre esses dados. As linguagens orientadas a objetos só juntaram tudo num lugar e acrescentaram proteção e herança. É exatamente o que o **C++** fez com o C.

## 🧪 Teste rápido

1. Qual a diferença entre `a.nome` e `p->nome`?
2. Por que a função `depositar` recebe `Conta *c` e não `Conta c`?
3. Crie uma struct `Produto` com nome, preço e quantidade, e uma função que calcule o valor total em estoque.

---

[⬅️ Ponteiros](06-ponteiros.md) · [Linguagem C](../README.md)
