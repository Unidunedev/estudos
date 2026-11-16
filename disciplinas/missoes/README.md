# ☕ Missões da Comunidade — Desafio 2

Aqui ficam os desafios do **segundo desafio da Unidunedev**. As histórias aparecem com animações no [site de missões](https://onboarding.unidunedev.workers.dev/missoes).

Cada missão pode ser resolvida **em C, Python ou Java**, respeitando seu nível. O foco é começar com programas pequenos e, nas missões maiores, praticar registros, funções, classes e objetos. Em C usamos structs e funções, sem classes ou herança.

## Como participar

1. Escolha uma missão no [cardápio](https://onboarding.unidunedev.workers.dev/missoes) e leia o enunciado oficial nesta pasta.
2. Faça um **fork** do repositório `Unidunedev/estudos` para sua conta.
3. Clone **seu fork** no computador e crie uma branch com um nome como `solucao/desafio-02-meu-user`.
4. Crie **um único arquivo** na pasta `solucoes/` daquela missão: `seu-username.c`, `seu-username.py` ou `seu-username.java`. O nome deve ser o seu username real do GitHub em minúsculas.
5. Teste com `python scripts/testar.py CAMINHO/DO/SEU/ARQUIVO`. No Windows, pode ser `py`.
6. Faça commit, push para seu fork e abra PR no repositório original. A liderança revisará o código.

**Importante:** O código pode ter funções, structs, classes e métodos dentro de um arquivo só. No Java, use uma classe `Main` **sem `public`** para que o arquivo tenha o username como nome. O comando `java arquivo.java` é usado pela correção. Para saídas decimais com ponto, configure a formatação com `Locale.US`; a execução padrão do robô Java usa localidade pt-BR.

Os testes verificam o **contrato mínimo** de entrada e saída em cada README. Você pode deixar seu projeto mais elaborado, mas não mostre mensagens como `Digite um número:` em stdout, porque a correção compara o texto exatamente. Funcionalidades extras e qualidade da modelagem podem ser revisadas por pessoas.

## Temporada de estreia

No site da comunidade, o Desafio 2 apresenta **cinco histórias por vez**, numa experiência de escolha inspirada no onboarding. As primeiras são: **Salve o gatinho, Salve a cafeteria, Apague o incêndio, Lance a nave e Proteja o castelo**.

As outras missões permanecem aqui como material preparado para futuras temporadas. A novidade do gatinho fica numa branch separada até a revisão e o anúncio oficial.

## O cardápio

- **01 · [Apague o incêndio](desafios/01-incendio/)** — Os bombeiros precisam prever o consumo de água antes de iniciar o resgate.
- **02 · [Salve a cafeteria](desafios/02-cafeteria/)** — O gatinho barista precisa fechar a conta de pedidos que chegaram juntos.
- **03 · [Ajude o abrigo](desafios/03-abrigo/)** — As fichas dos bichinhos estão misturadas e o abrigo precisa encontrar cada animal rapidamente.
- **04 · [Lance a nave](desafios/04-nave/)** — A astronauta precisa saber se o tanque tem combustível suficiente para decolar.
- **05 · [Organize o laboratório](desafios/05-laboratorio/)** — Os experimentos perderam as etiquetas e a cientista precisa localizar cada registro.
- **06 · [Proteja o castelo](desafios/06-castelo/)** — A guardiã precisa atualizar a quantidade de suprimentos sem deixar o estoque negativo.
- **07 · [Acenda o farol](desafios/07-farol/)** — O operador da ilha precisa descobrir por quantas horas a bateria vai sustentar a luz.
- **08 · [A biblioteca encantada](desafios/08-biblioteca/)** — A coruja bibliotecária precisa registrar empréstimos e devoluções.
- **09 · [Conserte o robô](desafios/09-robo/)** — O robô entregador precisa saber quantas tarefas ainda faltam.
- **10 · [Cuide do jardim da Lua](desafios/10-jardim/)** — As flores lunares precisam receber a quantidade certa de água.
- **11 · [A feira das estrelas](desafios/11-feira/)** — Um comerciante espacial precisa conferir descontos e trocos.
- **12 · [Encontre o pinguim](desafios/12-pinguim/)** — Pipo precisa de três respostas corretas para encontrar o caminho de casa.
- **13 · [Salve o gatinho](desafios/13-gatinho/)** — Ajude a equipe de resgate a verificar se uma escada alcança o galho onde Mingau está.

## Conquistas futuras

Estamos planejando um álbum de selos associado aos PRs **realmente aprovados e integrados**, não a um botão clicado no site. Por enquanto, enviar uma solução ainda não cria selos automaticamente. O PR e o arquivo publicado em `solucoes/` são o registro verificável de participação.

**Os exercícios do Desafio 2 serão liberados conforme o anúncio da comunidade. A missão 13 permanece nesta branch até a revisão.**
