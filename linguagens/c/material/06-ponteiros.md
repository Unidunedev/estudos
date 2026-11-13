# 06 · Ponteiros: o famoso bicho-papão (que nem é tão feio)

> Pré-requisito: [tipos e memória](03-tipos-e-memoria.md) e [funções em C](05-funcoes.md)

## Endereços de memória

Lembra da memória como uma fila enorme de caixinhas? Cada caixinha tem um **endereço**, como as casas de uma rua têm número.

```c
int idade = 20;
printf("valor: %d\n", idade);        // 20
printf("endereco: %p\n", &idade);    // algo como 0x7ffd5e8c
```

O `&` significa "**o endereço de**". Você já usa ele no `scanf("%d", &idade)`: está dizendo "guarde o número lido **neste endereço**".

## O que é um ponteiro?

**Ponteiro é uma variável que guarda um endereço.** Em vez de guardar o valor, ela guarda **onde** o valor está.

Analogia: a variável é uma casa; o ponteiro é um papel com o **endereço** da casa anotado.

```c
int idade = 20;
int *p = &idade;     // p é um ponteiro para int, e guarda o endereço de idade
```

```
   idade              p
 ┌───────┐        ┌──────────┐
 │  20   │ ◄───── │ endereço │
 └───────┘        │ de idade │
                  └──────────┘
```

## Os dois símbolos

| Símbolo | Lê-se | Exemplo | Resultado |
|---|---|---|---|
| `&` | "endereço de" | `&idade` | Onde `idade` mora |
| `*` | "o valor apontado por" | `*p` | O valor que está no endereço guardado em `p` |

```c
int idade = 20;
int *p = &idade;

printf("%d\n", *p);   // 20: vai até o endereço e lê o valor
*p = 21;              // vai até o endereço e muda o valor
printf("%d\n", idade);// 21: idade mudou, porque p aponta para ela!
```

> 💡 O `*` tem dois papéis: na **declaração** (`int *p`) ele diz "p é um ponteiro". **Depois** (`*p`), ele significa "o valor apontado".

## Para que serve? Funções que alteram variáveis

No material de funções, a função `zerar` não conseguia mudar o `n`, porque recebia uma cópia. Com ponteiro, ela recebe o **endereço** e mexe no original:

```c
void zerar(int *x) {
    *x = 0;           // muda o valor que está no endereço recebido
}

int main(void) {
    int n = 5;
    zerar(&n);        // manda o endereço de n
    printf("%d\n", n);  // 0
    return 0;
}
```

Exemplo clássico: trocar duas variáveis.

```c
void trocar(int *a, int *b) {
    int aux = *a;
    *a = *b;
    *b = aux;
}
```

Agora você entende o `scanf`: ele precisa mudar a sua variável, então recebe o **endereço** dela.

## Vetores e ponteiros são parentes

O nome de um vetor é, na prática, o endereço do primeiro elemento. Por isso:

```c
char palavra[50];
scanf("%49s", palavra);    // sem &: "palavra" já é um endereço
```

E por isso uma função consegue alterar um vetor que recebe: ela recebe o endereço, não uma cópia.

## Cuidados

| Erro | Exemplo | Consequência |
|---|---|---|
| Ponteiro sem destino | `int *p; *p = 5;` | Escreve num lugar aleatório da memória: `Segmentation fault` |
| Esquecer o `&` no scanf | `scanf("%d", n);` | O scanf usa o **valor** de `n` como endereço: quebra |
| Ponteiro para o nada | `int *p = NULL; *p = 1;` | `Segmentation fault` |

> 💡 Boa prática: se ainda não sabe para onde o ponteiro aponta, inicialize com `NULL` e confira antes de usar: `if (p != NULL)`.

## Por que outras linguagens não têm isso?

Linguagens como Python, Java e JavaScript usam endereços por baixo dos panos, mas **escondem** isso de você e cuidam da memória sozinhas. O C deixa tudo nas suas mãos: dá mais trabalho, mas é por isso que ele é tão rápido e tão usado em sistemas, e por isso que aprender C faz você entender **todas** as outras linguagens melhor.

## 🧪 Teste rápido

1. Qual a diferença entre `&x` e `*p`?
2. Por que o `scanf` precisa do `&`?
3. Escreva uma função `dobrar(int *x)` que dobre o valor da variável recebida.

---

[⬅️ Funções](05-funcoes.md) · [Linguagem C](../README.md)
