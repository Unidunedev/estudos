# 🔧 Sobre o C

> Leitura rápida para entender **o que é**, **onde se usa** e **o que os cursos raramente contam**.

## Em uma frase

C é uma linguagem **compilada**, de **tipagem estática e fraca**, **procedural** (sem classes), que dá **controle total sobre a memória**. É uma das linguagens mais antigas ainda em uso, e está, literalmente, por baixo de quase tudo.

## Um pouco de história

- Criada por **Dennis Ritchie** nos **Laboratórios Bell**, entre **1969 e 1973**, para escrever o sistema operacional **Unix**.
- Veio de uma linguagem chamada **B** (por isso o nome "C", a letra seguinte).
- O livro *"The C Programming Language"* (1978), de Kernighan e Ritchie, é tão famoso que tem apelido: **"K&R"**. Foi ele que popularizou o programa **"Hello, world"**, que hoje todo mundo usa como primeiro programa, em qualquer linguagem.
- Versões padronizadas: C89, C99, C11, **C17** (a que usamos na correção automática) e C23.

## Onde o C é usado (mais do que você imagina)

| Área | Exemplos |
|---|---|
| **Sistemas operacionais** | O núcleo do **Linux** (e, portanto, do **Android**), partes do Windows e do macOS |
| **Sistemas embarcados** | Micro-ondas, máquinas de lavar, carros, marca-passos, satélites, Arduino |
| **Bancos de dados** | SQLite (o banco mais usado do mundo: está no seu celular), PostgreSQL, Redis |
| **Outras linguagens** | O interpretador oficial do **Python** (CPython) é escrito em C. O PHP e o Ruby também |
| **Redes e servidores** | Nginx, o servidor web que entrega boa parte da internet |
| **Jogos e gráficos** | Motores de jogos e drivers de placa de vídeo (geralmente em C e C++) |

### Trilhas onde ele aparece

| Trilha | Peso do C |
|---|---|
| Sistemas embarcados e IoT | ⭐⭐⭐ A principal |
| Sistemas operacionais e infraestrutura | ⭐⭐⭐ |
| Segurança da informação | ⭐⭐ Entender falhas de memória exige C |
| Back-end, front-end, mobile | Raramente usado direto, mas está por baixo de tudo |

### A família do C

Muitas linguagens copiaram a sintaxe do C: `{ }`, `;`, `if`, `for`, `while`. Por isso, depois de aprender C, você lê **C++, Java, C#, JavaScript, Go e Dart** quase sem estranhar.

| Linguagem | Relação com o C |
|---|---|
| **C++** | "C com classes": adiciona orientação a objetos. Muito usado em jogos |
| **C#** | Da Microsoft, inspirado em C++ e Java |
| **Rust** | Moderna, tão rápida quanto C, mas com proteções contra os erros de memória |

## O que os cursos raramente contam

1. **"Por que aprender C se ninguém usa no mercado?"** Usa, sim (veja acima), mas o principal motivo é outro: C mostra o que as outras linguagens **escondem**. Depois de entender ponteiros e memória, você entende por que o Python e o Java se comportam do jeito que se comportam.
2. **O C não tem classes**, e mesmo assim dá para organizar o código de um jeito parecido com orientação a objetos, usando `struct` + funções. Veja em [structs](material/07-structs.md).
3. **Comportamento indefinido (*undefined behavior*).** Acessar fora de um vetor ou usar variável sem valor não é "erro": o padrão do C diz que **qualquer coisa** pode acontecer. Pode funcionar no seu computador e quebrar no do professor. Compile sempre com `-Wall -Wextra`.
4. **Segurança:** grande parte das falhas de segurança famosas na história vieram de erros de memória em C (como o *buffer overflow*). É por isso que linguagens como Rust estão crescendo.
5. **GCC × Clang × MSVC:** existem vários compiladores. No Windows usamos o GCC (via MSYS2); no Mac, o `gcc` é na verdade o Clang. Para os nossos desafios, tanto faz.
6. **`main` retorna um número por um motivo:** o `return 0` avisa ao sistema operacional se o programa deu certo. Scripts e ferramentas de automação usam esse número para saber se continuam ou param.

## Ecossistema

| | |
|---|---|
| **Compiladores** | GCC, Clang, MSVC |
| **Automação de build** | `make` (Makefile), CMake |
| **Depuração** | `gdb`, e o depurador do VS Code |
| **Achar erros de memória** | Valgrind, e as opções `-fsanitize=address` do GCC/Clang |
| **Referência** | https://en.cppreference.com/w/c |

---

[⬅️ Linguagem C](README.md)
