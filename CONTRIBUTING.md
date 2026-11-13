# Como contribuir com conteúdo

Resolver desafios é ótimo. Criar conteúdo para os colegas é o próximo nível! ⚔️

## ✏️ Melhorar algo que já existe

Achou um erro, uma explicação confusa ou quer adicionar um exemplo? Faça um PR direto. Mudança pequena dá para fazer pelo navegador: abra o arquivo no GitHub e clique no lápis ✏️.

## 📚 Escrever material

1. Crie um arquivo em `<linguagens ou disciplinas>/<pasta>/material/`, numerado na ordem do roteiro: `03-ponteiros.md`.
2. Escreva como se explicasse para um colega: frases curtas, exemplos pequenos e um "teste rápido" no final.
3. Adicione o link no roteiro do `README.md` da pasta.

## 🧩 Criar um desafio

1. Abra uma issue usando o modelo **"Proposta de desafio"**, para combinar a ideia antes.
2. Copie a pasta [`_modelos/desafio/`](_modelos/desafio/) para `<linguagens ou disciplinas>/<pasta>/desafios/NN-nome-do-desafio/`.
3. Escreva o enunciado e crie **pelo menos 3 testes** (`entrada1.txt` + `saida1.txt`, `entrada2.txt` + `saida2.txt`...), incluindo um caso "difícil" (zero, negativo, número grande...).
4. Teste com a sua própria solução, mas **não envie a solução no mesmo PR**: mande depois, num PR separado, como todo mundo.

### Regras dos testes

- A saída do programa é comparada **linha por linha** com o `saidaN.txt`. Espaços no fim da linha e linhas vazias no final são ignorados.
- Diga no enunciado **exatamente** o formato da saída (casas decimais, maiúsculas, texto).
- Nada de mensagens como `Digite um número:` na saída: elas quebram a comparação. Deixe isso claro no enunciado.

## 📁 Criar uma pasta nova (linguagem ou disciplina)

- **Linguagem** (Python, JavaScript, Java...) → `linguagens/<nome>/`. Os desafios aceitam só essa linguagem.
- **Disciplina** (banco de dados, estrutura de dados...) → `disciplinas/<nome>/`. Os desafios aceitam qualquer linguagem suportada.

Uma pasta nova só nasce quando tiver **um(a) dono(a)**: alguém que se compromete a revisar os PRs dela. Assim nenhuma pasta fica abandonada.

1. Abra uma issue dizendo qual pasta, quem é o dono e um roteiro inicial.
2. Siga o formato do [`_modelos/modulo.md`](_modelos/modulo.md).
3. O dono entra no arquivo `.github/CODEOWNERS` e passa a ser chamado automaticamente para revisar os PRs da pasta.
4. Se a linguagem for nova, ela precisa ser adicionada ao `scripts/testar.py` (listas `SUPORTADAS` e `LINGUAGENS_POR_PASTA`, e o jeito de executar em `preparar`) para a correção automática.

## Estilo

- Português simples. Toda palavra técnica é explicada na primeira vez.
- Comandos em blocos de código, indicando Windows ou Mac quando forem diferentes.
- Nomes de arquivos e pastas em minúsculas, com hífen: `02-variaveis-e-tipos`.
