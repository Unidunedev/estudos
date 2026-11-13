# ☕ Java

> Dono(a) da pasta: @clehdev · Nível: iniciante → orientação a objetos

## O que é

Java é uma linguagem **compilada para bytecode** e executada pela **JVM**, totalmente orientada a objetos. É uma das mais usadas em **back-end corporativo** (bancos, e-commerce, governo) e é a base do **Android**. Leia o **[sobre o Java](sobre.md)**: história, JDK × JRE × JVM, onde se usa, frameworks e o que os cursos raramente contam.

## Antes de começar

- [ ] Ler os [fundamentos](../../fundamentos/)
- [ ] Ter feito (ou estar fazendo) a [lógica de programação](../../disciplinas/logica/)
- [ ] Instalar o JDK: [Windows](instalacao/windows.md) · [Mac](instalacao/mac.md)

## Roteiro

### Parte 1: o básico da linguagem

| # | Assunto | Material | Desafios |
|---|---|---|---|
| 1 | Estrutura de um programa, compilar e rodar | [01 · Primeiro programa](material/01-primeiro-programa.md) | [01 · Olá, Java](desafios/01-ola-java/) |
| 2 | Tipos, Scanner, printf e a pegadinha do Locale | [02 · Tipos e variáveis](material/02-tipos-e-variaveis.md) | [02 · Média de N números](desafios/02-media-de-n/) |
| 3 | Arrays, Strings e o `.equals()` | [03 · Arrays e strings](material/03-arrays-e-strings.md) | Os de [lógica](../../disciplinas/logica/) (em Java!) |
| 4 | Métodos, sobrecarga e recursão | [04 · Métodos](material/04-metodos.md) | [Lógica 06 · Fatorial](../../disciplinas/logica/desafios/06-fatorial/) |

### Parte 2: orientação a objetos

| # | Assunto | Material | Desafios |
|---|---|---|---|
| 5 | Classes, objetos, construtores e encapsulamento | [05 · Classes e objetos](material/05-classes-e-objetos.md) | [03 · Conta bancária](desafios/03-conta-bancaria/) |
| 6 | Herança, polimorfismo, abstratas e interfaces | [06 · Herança e polimorfismo](material/06-heranca-e-polimorfismo.md) | ⏳ quer criar um? |
| 7 | ArrayList, HashMap e genéricos | [07 · Coleções](material/07-colecoes.md) | ⏳ quer criar um? |

> ⏳ Faltam materiais sobre **exceções** (`try/catch`), **enums** e **streams**. Veja como contribuir no [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Como rodar

```bash
java Main.java              # roda direto (Java 11+), ótimo para estudar
```

```bash
javac Main.java && java Main    # compila e executa (o jeito tradicional)
```

## Nos desafios

- O arquivo se chama `seu-username.java`, como nas outras pastas. A classe pode se chamar `Main`: no modo `java arquivo.java` o nome do arquivo não precisa bater com o da classe.
- Se tiver mais de uma classe no arquivo, a classe com o `main` precisa ser a **primeira**.
- A correção automática roda o Java **como um computador brasileiro** (pt-BR), igual ao seu. Com números reais, comece o `main` com `Locale.setDefault(Locale.US);` para usar ponto em vez de vírgula. Veja [vírgula ou ponto?](material/02-tipos-e-variaveis.md#a-pegadinha-brasileira-vírgula-ou-ponto)

---

[⬅️ Início](../../README.md)
