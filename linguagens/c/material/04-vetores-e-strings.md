# 04 · Vetores e strings em C

> Pré-requisito: [vetores (lógica)](../../../disciplinas/logica/material/06-vetores.md)

## Vetores em C

```c
int numeros[5];                       // 5 inteiros (com lixo dentro!)
int primos[5] = {2, 3, 5, 7, 11};     // já com valores
int zeros[100] = {0};                 // todos começam em 0
```

Em C, o vetor tem **tamanho fixo**, definido na criação. E o C **não confere** se você passou do limite:

```c
int v[5];
v[7] = 10;     // ❌ escreve numa memória que não é sua: comportamento imprevisível
```

Pode não dar erro na hora e quebrar o programa em outro lugar, ou terminar com `Segmentation fault`. A responsabilidade é sua: sempre percorra com `i < tamanho`.

### Guardando o tamanho

Diferente do Python (`len`), o C não guarda o tamanho para você. O costume é usar uma constante:

```c
#define MAX 100

int v[MAX];
int n;                          // quantos realmente estão em uso
scanf("%d", &n);
for (int i = 0; i < n; i++) {
    scanf("%d", &v[i]);
}
```

## Strings: vetores de char com um terminador

Em C não existe um tipo "texto". Uma **string** é um vetor de `char` que termina com um caractere especial, o `'\0'` (o "terminador nulo"):

```c
char nome[] = "Ana";
```

```
[ 'A' | 'n' | 'a' | '\0' ]
   0     1     2     3
```

Por isso, uma palavra de 3 letras ocupa **4** posições. Ao criar um vetor para guardar texto, reserve **uma posição a mais** para o `'\0'`.

> 💡 O `'\0'` é como as funções sabem onde o texto acaba. Percorrer uma string é ir de letra em letra até encontrar o `'\0'`.

## Lendo strings

```c
char palavra[50];
scanf("%49s", palavra);        // lê UMA palavra (para no espaço)
```

Repare: **sem `&`** no `palavra`. O nome de um vetor já é um endereço de memória (você vai entender no material de [ponteiros](06-ponteiros.md)). O `49` impede de ler mais letras do que cabem (deixando 1 para o `'\0'`).

Para ler uma **linha inteira**, com espaços:

```c
char frase[100];
fgets(frase, sizeof(frase), stdin);   // inclui o '\n' do Enter no final
```

## Funções úteis de string

Precisam de `#include <string.h>`:

| Função | O que faz |
|---|---|
| `strlen(s)` | Quantidade de letras (sem contar o `'\0'`) |
| `strcpy(destino, origem)` | Copia um texto para outro vetor |
| `strcmp(a, b)` | Compara: `0` se forem iguais |
| `strcat(destino, origem)` | Junta `origem` no final de `destino` |

> ⚠️ Em C, **não** dá para comparar textos com `==`, nem copiar com `=`. Use `strcmp` e `strcpy`.

## Percorrendo uma string

```c
char palavra[] = "banana";
int quantidade_a = 0;
for (int i = 0; palavra[i] != '\0'; i++) {
    if (palavra[i] == 'a') {
        quantidade_a++;
    }
}
printf("%d\n", quantidade_a);   // 3
```

> 💡 `'a'` com aspas **simples** é um caractere. `"a"` com aspas **duplas** é uma string (vetor). Não dá para comparar um `char` com `"a"`.

## 🧪 Teste rápido

1. Quantas posições ocupa a string `"cafe"`?
2. Por que o `scanf("%s", palavra)` não usa `&`?
3. Como verificar se duas strings são iguais em C?

## 🎯 Pratique

- [04 · Contar vogais](../desafios/04-contar-vogais/)

---

[⬅️ Tipos e memória](03-tipos-e-memoria.md) · [Próximo: Funções ➡️](05-funcoes.md)
