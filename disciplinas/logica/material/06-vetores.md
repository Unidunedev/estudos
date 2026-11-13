# 06 · Vetores (listas)

> ⏱️ 25 minutos

## O problema

Guardar as notas de 3 alunos é fácil: `nota1`, `nota2`, `nota3`. E de 40 alunos? 40 variáveis? E se a turma mudar de tamanho?

**Vetor** (ou *array*; no Python, **lista**) é uma variável que guarda **vários valores do mesmo tipo**, um do lado do outro, cada um numa posição numerada.

## Um armário com gavetas numeradas

```
notas:   [ 7.5 | 8.0 | 6.5 | 9.0 | 10.0 ]
índice:     0     1     2     3      4
```

- O vetor inteiro tem **um** nome: `notas`.
- Cada gaveta é acessada pelo **índice** (a posição): `notas[2]` é `6.5`.

> ⚠️ **O índice começa em 0**, não em 1! Num vetor de 5 elementos, as posições vão de `0` a `4`. Tentar acessar `notas[5]` é um dos erros mais comuns da programação.

## Criando e usando

**C**: o tamanho é fixo e definido na criação.
```c
double notas[5] = {7.5, 8.0, 6.5, 9.0, 10.0};
printf("%.1f\n", notas[0]);   // 7.5
notas[2] = 7.0;               // troca o 6.5 por 7.0
```

**Python**: a lista cresce e diminui à vontade.
```python
notas = [7.5, 8.0, 6.5, 9.0, 10.0]
print(notas[0])     # 7.5
notas[2] = 7.0
notas.append(8.5)   # adiciona no final
print(len(notas))   # 6 (tamanho da lista)
```

| Ação | C | Python |
|---|---|---|
| Criar | `int v[5];` | `v = []` ou `v = [0] * 5` |
| Ler a posição `i` | `v[i]` | `v[i]` |
| Tamanho | você guarda numa variável | `len(v)` |
| Adicionar no fim | (tamanho fixo) | `v.append(x)` |

## Percorrendo um vetor com um laço

Vetores e laços andam juntos: o contador do laço vira o índice.

```c
for (int i = 0; i < 5; i++) {
    printf("Aluno %d: %.1f\n", i + 1, notas[i]);
}
```

```python
for i in range(len(notas)):
    print(f"Aluno {i + 1}: {notas[i]}")

# ou, quando você não precisa do índice:
for nota in notas:
    print(nota)
```

> ⚠️ Em C, ninguém impede você de acessar `notas[10]` num vetor de 5. O programa lê "lixo" da memória ou quebra (`Segmentation fault`). No Python, aparece `IndexError: list index out of range`.

## Algoritmos clássicos com vetores

### Somar todos os elementos (acumulador)
```python
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
```

### Encontrar o maior
```python
maior = notas[0]          # começa com o PRIMEIRO, não com 0!
for nota in notas:
    if nota > maior:
        maior = nota
```

> 💡 Por que começar com `notas[0]` e não com `0`? Se todos os valores forem negativos, o `0` "ganharia" sem estar no vetor.

### Procurar um valor
```python
encontrou = False
for nota in notas:
    if nota == 10:
        encontrou = True
```

### Ler N valores para um vetor

```c
int n;
scanf("%d", &n);
int v[100];                     // espaço para até 100 números
for (int i = 0; i < n; i++) {
    scanf("%d", &v[i]);
}
```

```python
n = int(input())
v = []
for _ in range(n):
    v.append(int(input()))
```

## Texto é um vetor de caracteres

A palavra `"CAFE"` é, por dentro, um vetor:

```
[ 'C' | 'A' | 'F' | 'E' ]
   0     1     2     3
```

Por isso dá para pegar uma letra: `palavra[0]` é `'C'`. Em C, os textos têm um detalhe a mais (o `'\0'` no final), explicado no [material de C](../../../linguagens/c/material/04-vetores-e-strings.md).

## Matrizes: vetores de vetores

Uma tabela com linhas e colunas, como uma planilha ou um tabuleiro de jogo da velha:

```python
tabuleiro = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", "X"],
]
print(tabuleiro[1][2])   # linha 1, coluna 2 → "O"
```

## 🧪 Teste rápido

1. Num vetor `v = [4, 8, 15, 16, 23, 42]`, quanto vale `v[3]`? E qual é o último índice válido?
2. Por que o "maior" deve começar com o primeiro elemento?
3. Escreva um laço que mostre os elementos de um vetor de trás para frente.

## 🎯 Pratique

- [05 · Maior e menor](../desafios/05-maior-e-menor/)

---

[⬅️ Repetições](05-repeticoes.md) · [Próximo: Funções ➡️](07-funcoes.md)
