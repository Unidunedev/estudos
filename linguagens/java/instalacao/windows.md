# Instalando o Java (JDK) no Windows

> ⏱️ 10 minutos · Vamos instalar o **JDK 21** (versão LTS) da distribuição gratuita **Eclipse Temurin**.

## Já tenho?

```powershell
java --version
javac --version
```

Os dois mostraram a versão (17 ou mais)? Pule para [Testando](#testando). Se só o `java` funcionou, você tem apenas o JRE: instale o JDK.

## Caminho A: pelo site

1. Acesse **https://adoptium.net** e baixe o **Temurin 21 (LTS)** para Windows (arquivo `.msi`).
2. No instalador, na tela de recursos, ative:
   - ✅ **Add to PATH**
   - ✅ **Set JAVA_HOME variable**
3. Conclua a instalação.

## Caminho B: pelo terminal (winget)

```powershell
winget install --id EclipseAdoptium.Temurin.21.JDK -e
```

## Testando

**Feche e abra** o PowerShell e rode:

```powershell
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

E execute direto, sem compilar antes (Java 11+):

```powershell
java Main.java
```

## VS Code

Instale o **Extension Pack for Java** (da Microsoft). Ele adiciona autocompletar, botão de executar e depuração.

> 💡 Muitas empresas usam o **IntelliJ IDEA Community** (gratuito). Vale experimentar quando os projetos ficarem maiores.

---

[⬅️ Java](../README.md)
