# 🔧 Linguagem C

> Dono(a) da pasta: @clehdev · Nível: iniciante

## O que é

C é uma linguagem **compilada**, criada nos anos 1970, que está por trás de sistemas operacionais (Linux, partes do Windows e do macOS), bancos de dados, jogos e dispositivos como micro-ondas e carros. Ela é muito usada no início da faculdade porque mostra **como o computador funciona de verdade**: memória, tipos e o caminho do código até o executável.

## Antes de começar

- [ ] Ler os [fundamentos](../../fundamentos/), principalmente [compilada ou interpretada?](../../fundamentos/03-compilada-vs-interpretada.md)
- [ ] Instalar o compilador: [Windows](instalacao/windows.md) · [Mac](instalacao/mac.md)

## Roteiro

Os conceitos gerais (condicionais, repetições, vetores, funções) estão explicados em [lógica](../../disciplinas/logica/), com exemplos em C. Aqui ficam as partes **específicas do C**: compilação, memória, strings e ponteiros.

| # | Assunto | Material | Desafios |
|---|---|---|---|
| 1 | Do código ao executável | [01 · Compilação passo a passo](material/01-do-codigo-ao-executavel.md) | [01 · Olá, mundo](desafios/01-ola-mundo/) |
| 2 | Entrada, saída e variáveis | [02 · printf e scanf](material/02-entrada-e-saida.md) | [02 · Soma](desafios/02-soma/) |
| 3 | Tipos, memória e conversões | [03 · Tipos e memória](material/03-tipos-e-memoria.md) | [03 · Média e situação](desafios/03-media-e-situacao/) |
| 4 | Condicionais e repetições | [Lógica 04](../../disciplinas/logica/material/04-condicionais.md) e [Lógica 05](../../disciplinas/logica/material/05-repeticoes.md) | [Desafios de lógica](../../disciplinas/logica/) (resolva em C!) |
| 5 | Vetores e strings | [04 · Vetores e strings](material/04-vetores-e-strings.md) | [04 · Contar vogais](desafios/04-contar-vogais/) |
| 6 | Funções | [05 · Funções em C](material/05-funcoes.md) | [Lógica 06 · Fatorial](../../disciplinas/logica/desafios/06-fatorial/) |
| 7 | Ponteiros | [06 · Ponteiros](material/06-ponteiros.md) | ⏳ quer criar um? |

> ⏳ = esperando alguém da galera criar! Faltam também materiais sobre **structs**, **arquivos** e **alocação dinâmica** (`malloc`). Veja como no [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Como compilar e rodar

```bash
gcc ola.c -o ola     # compila: gera o executável "ola" (no Windows, "ola.exe")
./ola                # executa (no PowerShell do Windows: .\ola)
```

Dica: compile sempre com avisos ligados. Eles apontam muitos erros de lógica antes de você precisar caçar:

```bash
gcc -Wall -Wextra ola.c -o ola
```

---

[⬅️ Início](../../README.md)
