<p align="center">
  <img src="https://onboarding.unidunedev.workers.dev/favicon.svg" width="80" alt="" />
</p>

<h1 align="center">Estudos ☕</h1>

<p align="center">
  Onde a galera da <b>Unidunedev</b> aprende, pratica e ensina: uma pasta por linguagem ou matéria, com conteúdo, desafios e correção automática.
</p>

---

## 🗺️ Por onde começar

> Nunca usou Git? Faça primeiro o [comece-por-aqui](https://github.com/Unidunedev/comece-por-aqui). Para mandar suas soluções, você vai precisar de **fork** e **Pull Request**.

1. **[Fundamentos](fundamentos/)**: o que acontece quando um programa roda, linguagens compiladas e interpretadas, sintaxe e semântica. Leia antes de qualquer linguagem.
2. **[Lógica de programação](disciplinas/logica/)**: a base de tudo. Se está começando, comece por aqui.
3. **Escolha uma linguagem ou disciplina** e siga o roteiro do `README.md` dela.
4. **Resolva os desafios** e mande sua solução por PR.

O repositório tem três tipos de pasta:

```
estudos/
├── fundamentos/      ← leitura: como a programação funciona
├── linguagens/       ← uma pasta por linguagem (C, Python...)
└── disciplinas/      ← matérias que valem para qualquer linguagem (lógica, banco de dados...)
```

| Pasta | O que tem | Linguagens aceitas nos desafios |
|---|---|---|
| [`fundamentos/`](fundamentos/) | Como a programação funciona por baixo dos panos | — |
| [`disciplinas/logica/`](disciplinas/logica/) | Algoritmos, variáveis, condições, repetições, vetores e funções | C, Python ou Java |
| [`linguagens/c/`](linguagens/c/) | Compilação, memória, ponteiros e structs | C |
| [`linguagens/python/`](linguagens/python/) | Do básico às classes, herança e ambientes virtuais | Python |
| [`linguagens/java/`](linguagens/java/) | JVM, tipos, classes, herança, interfaces e coleções | Java |

Cada linguagem tem um **`sobre.md`**: história, como ela roda, onde é usada no mercado, frameworks, trilhas de carreira e o que os cursos raramente contam.

> 💡 **Linguagem ou disciplina?** "Quero aprender C" → `linguagens/`. "Tenho prova de lógica (ou de banco de dados)" → `disciplinas/`. Os desafios de uma linguagem aceitam só ela; os de disciplina aceitam qualquer linguagem suportada.

> 🧭 Quer saber **o que estudar para seguir uma carreira** (front-end, back-end, mobile...)? Isso fica no repositório de **trilhas**, que aponta para as pastas daqui.

## 🧩 Como cada pasta funciona

Todas seguem o mesmo formato. Aprendeu uma, sabe usar todas:

```
linguagens/c/
├── README.md              ← roteiro: o que aprender e em que ordem
├── instalacao/            ← como instalar o que for preciso (Windows e Mac)
├── material/              ← explicações e resumos (escritos pela galera também!)
└── desafios/
    └── 01-ola-mundo/
        ├── README.md      ← enunciado, nível e dicas
        ├── testes/        ← entrada1.txt e saida1.txt (usados na correção automática)
        └── solucoes/
            ├── ana-dev.c  ← um arquivo por pessoa
            └── joaodev.c
```

## 🚀 Enviando sua solução

1. Faça **fork** deste repositório e clone o **seu fork**.
2. Crie uma branch: `git switch -c solucao/c-01-seu-username`
3. Crie o arquivo na pasta `solucoes/` do desafio, com o **seu username do GitHub em minúsculas**:
   ```
   linguagens/c/desafios/01-ola-mundo/solucoes/seu-username.c
   ```
4. Teste na sua máquina (veja abaixo).
5. Commit, push e **Pull Request**.

Um robô roda a sua solução com os testes do desafio. ✅ verde, passou! ❌ vermelho? Clique em **Details** para ver qual teste falhou e o que era esperado.

### Testando antes de enviar

Com o Python instalado, na pasta do repositório:

```bash
python scripts/testar.py linguagens/c/desafios/01-ola-mundo/solucoes/seu-username.c
```

> No Windows, se `python` não funcionar, use `py`.

## 🤝 A dinâmica da galera

### Três papéis

Cada um sobe no seu ritmo:

| Papel | O que faz | Exemplo de contribuição |
|---|---|---|
| 🌱 **Aprendiz** | Resolve desafios | `solucoes/seu-username.c` |
| ⚔️ **Colaborador** | Escreve material ou cria desafios novos | um resumo sobre ponteiros, um desafio ⭐⭐ |
| 🛡️ **Mentor** | Revisa os PRs de uma pasta e ajuda quem travou | comentários e aprovações |

### 📅 Desafio da semana

- **Segunda:** sai o desafio da semana no grupo.
- **Até domingo:** todo mundo manda sua solução por PR.
- **Domingo:** destacamos 2 ou 3 soluções com ideias interessantes. Não é ranking: é para aprender com jeitos diferentes de pensar.

### 💬 Dúvida vira material

Travou? Pergunte na aba **Discussions** deste repositório (ou no grupo). Quando uma explicação ficar boa, transforme ela num arquivo da pasta `material/` com um PR. Quem pergunta e quem responde estão, juntos, criando conteúdo para os próximos.

### 📜 Combinados

1. **Tente sozinho primeiro.** Olhe as soluções dos colegas **depois** de mandar a sua: aí sim, compare e aprenda.
2. **IA para entender, não para resolver.** Pedir para a IA explicar um erro: ✅. Pedir a solução pronta: ❌.
3. **Nada de trabalhos avaliados da faculdade aqui.** Os desafios são para praticar o conteúdo, não para resolver lista que vale nota.
4. **Gentileza nas revisões.** Todo mundo aqui está aprendendo.

## ✨ Quer contribuir com conteúdo?

Veja o [CONTRIBUTING.md](CONTRIBUTING.md): como propor desafios, escrever material e até criar uma pasta nova.

---

<p align="center">Feito com café, código e vontade de aprender 💜</p>
