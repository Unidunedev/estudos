# 4. Sintaxe e semântica

> ⏱️ 15 minutos

## A diferença em uma frase

- **Sintaxe** é a **forma**: as regras de escrita (onde vai ponto e vírgula, chave, parêntese).
- **Semântica** é o **significado**: o que aquilo faz quando roda.

No português é igual:

| Frase | Sintaxe | Semântica |
|---|---|---|
| "O gato bebeu o leite." | ✅ Correta | ✅ Faz sentido |
| "gato O leite bebeu o" | ❌ Errada | Nem dá para entender |
| "O leite bebeu o gato." | ✅ Correta | ❌ Não faz sentido |

## O mesmo programa em 4 linguagens

O programa: ler a idade e dizer se a pessoa é maior de idade.

**C**
```c
#include <stdio.h>

int main(void) {
    int idade;
    scanf("%d", &idade);
    if (idade >= 18) {
        printf("Maior de idade\n");
    } else {
        printf("Menor de idade\n");
    }
    return 0;
}
```

**Python**
```python
idade = int(input())
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

**JavaScript (Node.js)**
```javascript
const idade = Number(require("fs").readFileSync(0, "utf8"));
if (idade >= 18) {
  console.log("Maior de idade");
} else {
  console.log("Menor de idade");
}
```

**Dart**
```dart
import 'dart:io';

void main() {
  final idade = int.parse(stdin.readLineSync()!);
  if (idade >= 18) {
    print('Maior de idade');
  } else {
    print('Menor de idade');
  }
}
```

Repare:

- A **semântica** é a mesma nas quatro: ler um número, comparar com 18, mostrar uma mensagem.
- A **sintaxe** muda bastante:

| | C | Python | JavaScript | Dart |
|---|---|---|---|---|
| Fim de instrução | `;` obrigatório | quebra de linha | `;` opcional | `;` obrigatório |
| Blocos | `{ }` | **indentação** (espaços) | `{ }` | `{ }` |
| Declarar variável | com tipo: `int idade` | só o nome | `const` / `let` | `final` / `var` / tipo |
| Mostrar na tela | `printf` | `print` | `console.log` | `print` |
| Onde começa | função `main` | primeira linha | primeira linha | função `main` |

> 💡 É por isso que **aprender a pensar** (lógica) vale mais do que decorar sintaxe. A sintaxe você consulta; o raciocínio é seu.

## Os 3 tipos de erro

### 1. Erro de sintaxe
Você escreveu algo fora das regras. O compilador ou interpretador **nem roda** o programa e aponta a linha.

```c
printf("Oi")      // faltou o ;
```
```
error: expected ';' before '}' token
```

### 2. Erro de execução (*runtime*)
A sintaxe está certa, mas algo dá errado **enquanto roda**.

```python
numero = int("abc")
```
```
ValueError: invalid literal for int() with base 10: 'abc'
```

Em C, exemplos clássicos são dividir por zero ou acessar uma posição de memória que não existe, o famoso `Segmentation fault`.

### 3. Erro de lógica (semântica)
O mais traiçoeiro: **o programa roda sem reclamar**, mas o resultado está errado.

```c
if (idade > 18)   // deveria ser >=
```

Com 18 anos, o programa diz "Menor de idade". Nenhuma mensagem de erro, só uma resposta errada. É para pegar esse tipo de erro que existem os **testes** dos nossos desafios.

| Erro | Quando aparece | Quem avisa |
|---|---|---|
| Sintaxe | Antes de rodar | Compilador / interpretador |
| Execução | Enquanto roda | O programa "quebra" |
| Lógica | Ninguém avisa | Só os testes (ou o usuário reclamando 😅) |

## Lendo mensagens de erro

Mensagens de erro assustam no começo, mas são suas aliadas. Leia procurando três coisas:

1. **O arquivo e a linha:** `ola.c:7:5` = arquivo `ola.c`, linha 7, coluna 5.
2. **O tipo do erro:** `error`, `warning`, `TypeError`...
3. **A descrição:** geralmente em inglês. Traduzir essa parte já resolve metade dos problemas.

> ⚠️ Às vezes o erro está **uma linha antes** da indicada. Um `;` esquecido na linha 6 costuma ser apontado na linha 7.

## ✅ Checkpoint

1. Qual a diferença entre sintaxe e semântica?
2. Qual dos 3 tipos de erro é o mais difícil de encontrar? Por quê?

## 🧠 Desafio sem IA

Pegue o programa em C acima e provoque, de propósito, um erro de cada tipo. Para o de lógica, faça o programa responder errado para uma idade específica e descubra qual é.

---

[⬅️ Compilada ou interpretada?](03-compilada-vs-interpretada.md) · [Próximo: Seu ambiente de programação ➡️](05-ambiente-de-programacao.md)
