# 07 · Funções

> ⏱️ 25 minutos

## O problema

Imagine que seu programa calcula a média em 5 lugares diferentes. Você copia o mesmo código 5 vezes... e depois descobre um erro nele. Agora precisa corrigir em 5 lugares (e vai esquecer um).

**Função** é um pedaço de código com nome, que faz **uma tarefa** e pode ser usado quantas vezes quiser.

## Uma máquina de suco

Pense numa função como uma máquina:

```mermaid
flowchart LR
    A[🍊 laranjas<br/>parâmetros] --> B[⚙️ máquina<br/>função]
    B --> C[🥤 suco<br/>retorno]
```

- **Parâmetros:** o que você coloca na máquina (a entrada).
- **Corpo:** o que a máquina faz por dentro.
- **Retorno:** o que sai dela (o resultado).

Você não precisa saber como a máquina funciona por dentro para usá-la. Você já usou várias funções assim: `printf`, `print`, `len`, `input`...

## Criando uma função

**Pseudocódigo**
```
função media(a, b)
    retorne (a + b) / 2
fim-função

escreva media(7, 8)     → 7.5
```

**C**
```c
double media(double a, double b) {
    return (a + b) / 2;
}

int main(void) {
    printf("%.1f\n", media(7, 8));   // 7.5
    printf("%.1f\n", media(5, 6));   // 5.5
    return 0;
}
```

Em C, a função diz o **tipo do retorno** (`double`) e o **tipo de cada parâmetro**. E ela precisa aparecer **antes** de ser usada (acima do `main`).

**Python**
```python
def media(a, b):
    return (a + b) / 2

print(media(7, 8))   # 7.5
```

## Parâmetros e argumentos

```python
def saudacao(nome):        # "nome" é o PARÂMETRO (a vaga)
    print(f"Oi, {nome}!")

saudacao("Ana")            # "Ana" é o ARGUMENTO (quem ocupa a vaga)
saudacao("Caio")
```

## return × print

Essa diferença confunde muita gente:

| | `print` / `printf` | `return` |
|---|---|---|
| O que faz | **Mostra** na tela | **Devolve** o valor para quem chamou |
| Dá para usar o resultado depois? | ❌ | ✅ |

```python
def dobro(x):
    return x * 2

resultado = dobro(5) + 1    # 11: dá para fazer conta com o retorno
```

Se `dobro` usasse `print` em vez de `return`, ele mostraria `10` na tela, mas `resultado` daria erro, porque a função não devolveu nada.

> 💡 **Regra de ouro:** a função **calcula e retorna**; quem chamou decide se mostra, guarda ou usa em outra conta.

## Funções que não retornam nada

Algumas funções só **fazem** algo, como mostrar uma linha:

```c
void linha(void) {
    printf("--------------\n");
}
```

```python
def linha():
    print("-" * 14)
```

Em C, o `void` significa "nada": não retorna nada, e/ou não recebe nada.

## Escopo: cada função tem suas caixinhas

Variáveis criadas **dentro** de uma função só existem lá dentro:

```python
def calcula():
    total = 10

calcula()
print(total)    # ❌ NameError: total não existe aqui fora
```

Isso é bom! Cada função cuida das suas próprias variáveis, sem bagunçar as das outras. Para tirar um valor de dentro, use `return`.

## Por que usar funções?

| Motivo | Na prática |
|---|---|
| **Não repetir código** | Escreve uma vez, usa em vários lugares |
| **Organizar** | Cada função com uma tarefa: `ler_notas`, `calcular_media`, `mostrar_resultado` |
| **Corrigir em um lugar só** | Achou um erro? Arruma na função, e todos os usos ficam certos |
| **Testar por partes** | Dá para conferir cada função separadamente |

> 💡 Um bom nome de função é um **verbo**: `calcular_media`, `eh_par`, `mostrar_menu`. Se você não consegue dar um nome curto, talvez ela esteja fazendo coisas demais.

## Função que retorna verdadeiro ou falso

```python
def eh_par(n):
    return n % 2 == 0

if eh_par(4):
    print("PAR")
```

```c
int eh_par(int n) {
    return n % 2 == 0;     // em C, verdadeiro é 1 e falso é 0
}
```

## Uma função pode chamar outra (e até ela mesma)

Quando uma função chama **a si mesma**, isso se chama **recursão**. Exemplo clássico, o fatorial (`5! = 5 × 4 × 3 × 2 × 1`):

```python
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
```

Recursão é um assunto mais avançado, mas é bom saber que existe. O mesmo cálculo também dá para fazer com um laço.

## 🧪 Teste rápido

1. Qual a diferença entre parâmetro e argumento?
2. Escreva uma função `maior(a, b)` que **retorne** o maior dos dois.
3. Por que `print(total)` dá erro no exemplo de escopo?

## 🎯 Pratique

- [06 · Fatorial](../desafios/06-fatorial/)

---

[⬅️ Vetores](06-vetores.md) · [Lógica 🧠](../README.md)
