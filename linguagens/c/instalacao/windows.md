# Instalando o compilador de C no Windows

> ⏱️ 15 minutos · Vamos instalar o **GCC** pelo **MSYS2**, o jeito mais usado e atualizado no Windows.

## Já tenho?

Abra o PowerShell e rode:

```powershell
gcc --version
```

Apareceu a versão? Pule para [Testando](#testando). Apareceu "`gcc` não é reconhecido"? Siga os passos.

## 1. Instalar o MSYS2

**Pelo site:** baixe o instalador em **https://www.msys2.org** e instale na pasta padrão, `C:\msys64`.

**Ou pelo terminal (winget):**

```powershell
winget install --id MSYS2.MSYS2 -e
```

## 2. Instalar o GCC

1. No menu Iniciar, abra o **MSYS2 UCRT64** (o ícone amarelo, **não** o "MSYS2 MSYS").
2. Nessa janela, rode:

```bash
pacman -S --needed mingw-w64-ucrt-x86_64-gcc
```

3. Quando perguntar `Proceed with installation? [Y/n]`, aperte **Enter**.

## 3. Colocar o GCC no PATH

Para usar o `gcc` no PowerShell e no VS Code, a pasta dele precisa estar no [PATH](../../../fundamentos/05-ambiente-de-programacao.md#o-path):

1. Aperte `Win`, digite **variáveis de ambiente** e abra **Editar as variáveis de ambiente do sistema**.
2. Clique em **Variáveis de Ambiente...**
3. Em **Variáveis de usuário**, selecione **Path** → **Editar** → **Novo**.
4. Cole: `C:\msys64\ucrt64\bin`
5. **OK** em todas as janelas.

## Testando

**Feche e abra** o PowerShell e rode:

```powershell
gcc --version
```

Agora crie o arquivo `ola.c`:

```c
#include <stdio.h>

int main(void) {
    printf("Ola, mundo!\n");
    return 0;
}
```

Compile e execute:

```powershell
gcc ola.c -o ola
.\ola
```

## VS Code

Instale a extensão **C/C++** (da Microsoft). Ela dá cores, autocompletar e aponta erros enquanto você digita.

## ✅ Checkpoint

O comando `.\ola` mostra `Ola, mundo!`. 🎉

## Deu errado?

| Problema | Solução |
|---|---|
| `gcc` não é reconhecido | Feche e abra o terminal. Se continuar, confira o passo 3 (o caminho precisa ser exatamente `C:\msys64\ucrt64\bin`) |
| Instalei pelo "MSYS2 MSYS" | Repita o passo 2 na janela **MSYS2 UCRT64** |
| Antivírus bloqueou o `ola.exe` | Acontece com executáveis novos. Libere a pasta do projeto no antivírus |

---

[⬅️ Linguagem C](../README.md)
