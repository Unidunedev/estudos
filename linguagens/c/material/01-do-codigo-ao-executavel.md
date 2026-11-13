# 01 · Do código ao executável

> Pré-requisito: [compilada ou interpretada?](../../../fundamentos/03-compilada-vs-interpretada.md)

Quando você roda `gcc ola.c -o ola`, parece uma etapa só. Mas, por baixo, o GCC faz **quatro**:

```mermaid
flowchart LR
    A[ola.c<br/>código-fonte] -- 1. pré-processador --> B[ola.i<br/>código expandido]
    B -- 2. compilação --> C[ola.s<br/>assembly]
    C -- 3. montagem --> D[ola.o<br/>código objeto]
    D -- 4. ligação --> E[ola<br/>executável]
```

## 1. Pré-processamento

Trata as linhas que começam com `#`. O `#include <stdio.h>` é substituído pelo **conteúdo inteiro** do arquivo `stdio.h`, que diz ao compilador que funções como `printf` existem.

```bash
gcc -E ola.c -o ola.i
```

Abra o `ola.i`: o seu programa de 6 linhas virou centenas! É tudo o que veio do `stdio.h`.

## 2. Compilação

Traduz o C para **assembly**, uma linguagem de baixo nível que ainda dá para ler (mais ou menos 😅). É aqui que aparecem os **erros de sintaxe**.

```bash
gcc -S ola.c -o ola.s
```

## 3. Montagem

Transforma o assembly em **código de máquina** (binário). O resultado, o **código objeto**, ainda não roda sozinho.

```bash
gcc -c ola.c -o ola.o
```

## 4. Ligação (*linking*)

Junta o seu código objeto com o código das bibliotecas que você usou (o `printf` não foi você que escreveu!) e gera o **executável** final.

```bash
gcc ola.o -o ola
```

Se você usar uma função que não existe, o erro aparece aqui: `undefined reference to ...`.

## Anatomia do "Olá, mundo"

```c
#include <stdio.h>          // traz as funções de entrada e saída (printf, scanf)

int main(void) {            // todo programa em C começa pela função main
    printf("Ola, mundo!\n"); // mostra o texto; \n é a quebra de linha
    return 0;               // 0 avisa ao sistema: "terminei sem erros"
}
```

## 🧪 Teste rápido

1. Em qual etapa o `#include` é resolvido?
2. Se você escrever `prinf` em vez de `printf`, em qual etapa o erro aparece? Teste e veja!

---

[⬅️ Linguagem C](../README.md) · [Próximo: printf e scanf ➡️](02-entrada-e-saida.md)
