# 02 · Tipos e estruturas de dados

> Pré-requisito: [variáveis e tipos (lógica)](../../../disciplinas/logica/material/02-variaveis-e-tipos.md)

## Tipos básicos

| Tipo | Exemplo | Para quê |
|---|---|---|
| `int` | `42`, `-7` | Inteiros (de **qualquer** tamanho!) |
| `float` | `3.14`, `-0.5` | Números reais |
| `str` | `"Ana"`, `'cafe'` | Texto |
| `bool` | `True`, `False` | Verdadeiro ou falso |
| `None` | `None` | "Nada", ausência de valor |

Descubra o tipo de qualquer coisa com `type()`:

```python
type(42)       # <class 'int'>
type("42")     # <class 'str'>
```

> 💡 Diferente do C, o `int` do Python **não estoura**: `2 ** 1000` funciona.

## As 4 estruturas que você vai usar todo dia

### Lista (`list`): uma fila de itens, que pode mudar

```python
frutas = ["maca", "banana", "uva"]
frutas.append("manga")      # adiciona no fim
frutas[0] = "pera"          # troca o primeiro
frutas.remove("uva")        # remove pelo valor
print(len(frutas))          # 3
print("banana" in frutas)   # True
```

### Tupla (`tuple`): uma lista que não muda

```python
ponto = (10, 20)
x, y = ponto       # "desempacota" em duas variáveis
```

Use quando os dados não devem mudar, como coordenadas ou uma data.

### Dicionário (`dict`): pares de chave e valor

É como uma agenda: você procura pelo **nome** (chave) e encontra o **telefone** (valor).

```python
aluno = {"nome": "Ana", "idade": 20, "curso": "ADS"}
print(aluno["nome"])          # Ana
aluno["idade"] = 21           # altera
aluno["periodo"] = 3          # adiciona chave nova
print(aluno.get("email", "sem email"))   # valor padrão se não existir

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
```

Contando ocorrências, um uso clássico:

```python
contagem = {}
for palavra in ["oi", "tchau", "oi"]:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)   # {'oi': 2, 'tchau': 1}
```

### Conjunto (`set`): itens sem repetição

```python
cores = {"azul", "verde", "azul"}
print(cores)      # {'azul', 'verde'}: o repetido sumiu
```

Ótimo para remover duplicados: `list(set(minha_lista))`.

## Qual usar?

| Situação | Estrutura |
|---|---|
| Uma sequência que cresce ou muda | `list` |
| Dados fixos, que não devem mudar | `tuple` |
| Procurar algo por um nome ou código | `dict` |
| Não aceitar repetidos / testar se algo existe rapidinho | `set` |

## Fatiamento (slicing): o superpoder das listas e textos

```python
nums = [10, 20, 30, 40, 50]
nums[1:3]     # [20, 30]   (do índice 1 até o 3, sem incluir o 3)
nums[:2]      # [10, 20]   (do começo)
nums[-1]      # 50         (índice negativo conta do fim!)
nums[::-1]    # [50, 40, 30, 20, 10]   (invertido)
```

## Compreensão de lista (list comprehension)

Um jeito curto de criar listas a partir de outras:

```python
quadrados = [n * n for n in range(1, 6)]         # [1, 4, 9, 16, 25]
pares = [n for n in range(10) if n % 2 == 0]     # [0, 2, 4, 6, 8]
```

> 💡 Comece escrevendo com `for` normal. Quando se sentir confortável, troque pela forma curta.

## ⚠️ A pegadinha da cópia

```python
a = [1, 2, 3]
b = a           # b NÃO é uma cópia: é outro nome para a MESMA lista
b.append(4)
print(a)        # [1, 2, 3, 4]  😱

c = a.copy()    # agora sim, uma cópia de verdade
```

## 🧪 Teste rápido

1. Crie um dicionário com 3 países e suas capitais e mostre todos com um `for`.
2. Qual o resultado de `"python"[::-1]`?
3. Como remover os números repetidos de `[3, 1, 3, 2, 1]`?

## 🎯 Pratique

- [02 · Frequência de palavras](../desafios/02-frequencia-de-palavras/)

---

[⬅️ Primeiros passos](01-primeiros-passos.md) · [Próximo: Strings ➡️](03-strings.md)
