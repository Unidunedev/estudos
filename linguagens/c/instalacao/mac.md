# Instalando o compilador de C no Mac

> ⏱️ 10 minutos

No Mac, o compilador vem nas **Command Line Tools** da Apple. Se você já seguiu a instalação do Git no [comece-por-aqui](https://github.com/Unidunedev/comece-por-aqui/blob/main/01-instalacao/mac.md), provavelmente já tem!

## Já tenho?

Abra o Terminal e rode:

```bash
gcc --version
```

Apareceu um texto com `Apple clang`? Já está instalado. Pule para [Testando](#testando).

## Instalando

```bash
xcode-select --install
```

Clique em **Instalar**, aceite a licença e espere terminar.

> 💡 **Curiosidade:** no Mac, o comando `gcc` na verdade chama o **Clang**, outro compilador de C. Para o que vamos fazer, eles funcionam igual: mesmos comandos, mesmo resultado.

## Testando

Crie o arquivo `ola.c`:

```c
#include <stdio.h>

int main(void) {
    printf("Ola, mundo!\n");
    return 0;
}
```

Compile e execute:

```bash
gcc ola.c -o ola
./ola
```

## VS Code

Instale a extensão **C/C++** (da Microsoft). Ela dá cores, autocompletar e aponta erros enquanto você digita.

## ✅ Checkpoint

O comando `./ola` mostra `Ola, mundo!`. 🎉

---

[⬅️ Linguagem C](../README.md)
