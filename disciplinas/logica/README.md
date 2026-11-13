# 🧠 Lógica de programação

> Dono(a) da pasta: @clehdev · Nível: iniciante

## O que é

Lógica de programação é a habilidade de **quebrar um problema em passos** que um computador consegue seguir. É a parte que **não muda** de uma linguagem para outra: quem tem boa lógica aprende qualquer sintaxe.

Os desafios desta pasta podem ser resolvidos em **C** (`.c`) ou **Python** (`.py`).

## Antes de começar

- [ ] Ler os [fundamentos](../../fundamentos/)
- [ ] Ter uma linguagem instalada:
  - **C:** veja a [instalação do C](../../linguagens/c/README.md#antes-de-começar)
  - **Python:** baixe em **https://www.python.org/downloads** (no Windows, marque **Add python.exe to PATH** na primeira tela do instalador) e confira com `python --version`

## Roteiro

Siga na ordem. Cada material tem exemplos em **pseudocódigo, C e Python**, lado a lado, e termina com um teste rápido.

| # | Assunto | Material | Desafios |
|---|---|---|---|
| 1 | Algoritmos, pseudocódigo e teste de mesa | [01 · O que é um algoritmo](material/01-o-que-e-um-algoritmo.md) | — |
| 2 | Variáveis, tipos, entrada e saída | [02 · Variáveis e tipos](material/02-variaveis-e-tipos.md) | — |
| 3 | Operadores aritméticos, relacionais e lógicos | [03 · Operadores](material/03-operadores.md) | — |
| 4 | Condicionais | [04 · Condicionais](material/04-condicionais.md) | [01 · Par ou ímpar](desafios/01-par-ou-impar/) · [02 · O maior de três](desafios/02-maior-de-tres/) |
| 5 | Repetições | [05 · Repetições](material/05-repeticoes.md) | [03 · Tabuada](desafios/03-tabuada/) · [04 · Soma até N](desafios/04-soma-ate-n/) |
| 6 | Vetores (listas) | [06 · Vetores](material/06-vetores.md) | [05 · Maior e menor](desafios/05-maior-e-menor/) |
| 7 | Funções | [07 · Funções](material/07-funcoes.md) | [06 · Fatorial](desafios/06-fatorial/) |

> 💡 Quer contribuir? Faltam desafios ⭐⭐ e ⭐⭐⭐ em todos os assuntos, e materiais sobre **matrizes** e **recursão**. Veja o [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Como rodar

```bash
# C
gcc minha-solucao.c -o programa
./programa

# Python
python minha-solucao.py
```

> 💡 Para testar com a entrada de um teste sem digitar: `python minha-solucao.py < testes/entrada1.txt`. O `<` manda o conteúdo do arquivo como se fosse o teclado.

---

[⬅️ Início](../../README.md)
