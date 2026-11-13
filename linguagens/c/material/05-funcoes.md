# 05 · Funções em C

> Pré-requisito: [funções (lógica)](../../../disciplinas/logica/material/07-funcoes.md)

## Anatomia

```c
double media(double a, double b) {
    return (a + b) / 2;
}
```

| Parte | No exemplo | Significa |
|---|---|---|
| Tipo de retorno | `double` | O tipo do valor que a função devolve (`void` = nada) |
| Nome | `media` | Como você chama a função |
| Parâmetros | `double a, double b` | O que ela recebe, cada um com seu tipo |
| Corpo | `{ ... }` | O que ela faz |
| `return` | `return (a + b) / 2;` | Devolve o resultado e **encerra** a função |

## A ordem importa: protótipos

O C lê o arquivo de cima para baixo. Se o `main` usar uma função escrita **depois** dele, o compilador reclama. Duas soluções:

**1. Escrever a função antes do `main`** (mais simples):
```c
int dobro(int x) { return x * 2; }

int main(void) {
    printf("%d\n", dobro(4));
    return 0;
}
```

**2. Declarar um protótipo no topo** (útil em programas grandes):
```c
int dobro(int x);            // protótipo: "essa função existe"

int main(void) {
    printf("%d\n", dobro(4));
    return 0;
}

int dobro(int x) { return x * 2; }
```

## O main também é uma função

`int main(void)` é a função que o sistema operacional chama quando o programa começa. O `return 0;` no final avisa ao sistema que tudo terminou bem. Um valor diferente de 0 significa "deu erro". É por isso que a nossa correção automática acusa "o programa encerrou com erro" quando o `main` não retorna 0.

## Passagem por valor: a função recebe uma cópia

```c
void zerar(int x) {
    x = 0;
}

int main(void) {
    int n = 5;
    zerar(n);
    printf("%d\n", n);    // 5: o n original não mudou!
    return 0;
}
```

A função recebe uma **cópia** do valor. Mudar a cópia não muda o original. Para uma função alterar uma variável de quem chamou, é preciso passar o **endereço** dela, com ponteiros. É exatamente o que o `scanf` faz com o `&`. Veja no próximo material.

> ⚠️ Vetores são a exceção: uma função **consegue** alterar um vetor recebido, porque o vetor é passado como endereço.

```c
void zerar_tudo(int v[], int tamanho) {
    for (int i = 0; i < tamanho; i++) v[i] = 0;   // altera o vetor original
}
```

## Funções de bibliotecas

Você já usa funções que não escreveu. Cada grupo vem de uma **biblioteca**, incluída com `#include`:

| Biblioteca | Funções |
|---|---|
| `<stdio.h>` | `printf`, `scanf`, `fgets` |
| `<string.h>` | `strlen`, `strcmp`, `strcpy` |
| `<math.h>` | `sqrt` (raiz), `pow` (potência), `fabs` (valor absoluto) |
| `<ctype.h>` | `toupper`, `tolower`, `isdigit` |

> 💡 Ao usar `<math.h>` no Linux, às vezes é preciso compilar com `-lm` no final: `gcc programa.c -o programa -lm`. A nossa correção automática já faz isso.

## 🧪 Teste rápido

1. O que significa `void` no tipo de retorno?
2. Por que a função `zerar` do exemplo não muda o `n`?
3. O que é um protótipo?

---

[⬅️ Vetores e strings](04-vetores-e-strings.md) · [Próximo: Ponteiros ➡️](06-ponteiros.md)
