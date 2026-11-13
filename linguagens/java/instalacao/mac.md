# Instalando o Java (JDK) no Mac

> ⏱️ 10 minutos · Vamos instalar o **JDK 21** (versão LTS) da distribuição gratuita **Eclipse Temurin**.

## Já tenho?

```bash
java --version
javac --version
```

> ⚠️ O Mac às vezes mostra uma mensagem pedindo para instalar o Java mesmo sem ele estar instalado. Se aparecer, siga os passos abaixo.

## Caminho A: pelo site

Baixe o **Temurin 21 (LTS)** para macOS (arquivo `.pkg`) em **https://adoptium.net**. Escolha **aarch64** para Mac com chip M1/M2/M3/M4, ou **x64** para Mac com Intel.

## Caminho B: Homebrew

```bash
brew install --cask temurin@21
```

## Testando

```bash
java --version
javac --version
```

Crie o arquivo `Main.java`:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Ola, mundo!");
    }
}
```

E execute:

```bash
java Main.java
```

## VS Code

Instale o **Extension Pack for Java** (da Microsoft).

---

[⬅️ Java](../README.md)
