# 04 · Funções em Python

> Pré-requisito: [funções (lógica)](../../../disciplinas/logica/material/07-funcoes.md)

## O básico

```python
def media(a, b):
    """Retorna a média de dois números."""
    return (a + b) / 2

print(media(7, 8))   # 7.5
```

- `def` cria a função.
- O texto entre `"""` logo abaixo é a **docstring**: a documentação da função. Passe o mouse sobre ela no VS Code e veja.

## Parâmetros com valor padrão

```python
def saudacao(nome, saudacao="Ola"):
    return f"{saudacao}, {nome}!"

saudacao("Ana")              # 'Ola, Ana!'
saudacao("Ana", "Bom dia")   # 'Bom dia, Ana!'
```

## Argumentos nomeados

```python
def ficha(nome, idade, curso):
    return f"{nome}, {idade} anos, {curso}"

ficha(curso="ADS", nome="Ana", idade=20)   # a ordem não importa se der o nome
```

## Retornando mais de um valor

```python
def maior_e_menor(numeros):
    return max(numeros), min(numeros)

maior, menor = maior_e_menor([4, 9, 1])
```

Na verdade, o Python retorna uma **tupla** e desempacota nas duas variáveis.

## Dicas de tipo (type hints)

Opcional, mas cada vez mais usado em projetos profissionais:

```python
def dobro(x: int) -> int:
    return x * 2
```

O Python **não** obriga os tipos, mas o VS Code passa a avisar quando você usa errado. Isso ajuda muito em projetos grandes.

## Funções são valores

Em Python, dá para guardar uma função numa variável e passar para outra função:

```python
def gritar(texto):
    return texto.upper() + "!"

acao = gritar
print(acao("oi"))    # OI!

nomes = ["bia", "Ana", "caio"]
print(sorted(nomes, key=str.lower))   # ordena ignorando maiúsculas
```

## Funções anônimas (lambda)

Funções de uma linha, sem nome:

```python
dobro = lambda x: x * 2
alunos = [("Ana", 9), ("Bia", 7)]
alunos.sort(key=lambda aluno: aluno[1])   # ordena pela nota
```

> 💡 Use `lambda` só para coisas bem curtas. Se ficou complicado, crie uma função normal com nome.

## ⚠️ A pegadinha do padrão mutável

```python
def adicionar(item, lista=[]):     # ❌ a MESMA lista é reaproveitada entre as chamadas!
    lista.append(item)
    return lista

adicionar(1)   # [1]
adicionar(2)   # [1, 2]  😱

def adicionar(item, lista=None):   # ✅ o jeito certo
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

## 🧪 Teste rápido

1. Crie `eh_par(n)` que retorne `True` ou `False`.
2. Crie `resumo(notas)` que retorne a média, a maior e a menor nota.

---

[⬅️ Strings](03-strings.md) · [Próximo: Classes e objetos ➡️](05-classes-e-objetos.md)
