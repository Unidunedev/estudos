# 🐍 Sobre o Python

> Leitura rápida para entender **o que é**, **onde se usa** e **o que os cursos raramente contam**.

## Em uma frase

Python é uma linguagem **interpretada**, de **tipagem dinâmica e forte**, criada para ser **fácil de ler**. É uma das linguagens mais usadas do mundo, principalmente em dados, inteligência artificial, automação e back-end.

## Um pouco de história

- Criada por **Guido van Rossum**, na Holanda, e lançada em **1991**.
- O nome não vem da cobra, e sim do grupo de comédia britânico **Monty Python**. É por isso que os exemplos da documentação oficial usam "spam" e "eggs" em vez de "foo" e "bar".
- A grande virada foi o **Python 3** (2008), que quebrou a compatibilidade com o Python 2. O Python 2 foi oficialmente aposentado em 2020. Se um tutorial usa `print "oi"` sem parênteses, ele é do Python 2: procure outro.

## Como o Python roda

Você escreve um arquivo `.py` e o **interpretador** executa:

```bash
python programa.py
```

Por baixo, o Python primeiro compila seu código para **bytecode** (aqueles arquivos `.pyc` na pasta `__pycache__`) e depois uma máquina virtual executa esse bytecode. Por isso dizemos que ele é interpretado "com um pé no meio-termo" (veja [compilada ou interpretada?](../../fundamentos/03-compilada-vs-interpretada.md)).

## Onde o Python é mais usado

| Área | Para quê | Ferramentas famosas |
|---|---|---|
| **Dados e análise** | Planilhas gigantes, gráficos, relatórios | pandas, NumPy, Matplotlib, Jupyter |
| **Inteligência artificial** | Treinar e usar modelos de IA | PyTorch, TensorFlow, scikit-learn |
| **Back-end (APIs e sites)** | Servidores que respondem aos apps | **Django**, **FastAPI**, Flask |
| **Automação** | Robôs que fazem tarefas repetitivas | Selenium, Playwright, scripts do dia a dia |
| **DevOps e infraestrutura** | Scripts de deploy e servidores | Ansible, scripts de nuvem |
| **Ciência e educação** | Pesquisa, cálculos, ensino | SciPy, a primeira linguagem de muitas faculdades |

### Trilhas onde ele aparece

| Trilha | Peso do Python |
|---|---|
| Dados / IA | ⭐⭐⭐ É a principal linguagem |
| Back-end | ⭐⭐ Muito usado (Django, FastAPI) |
| DevOps | ⭐⭐ Scripts e automação |
| QA / Testes | ⭐⭐ Automação de testes (pytest, Selenium) |
| Front-end e Mobile | ⭐ Pouco usado |

## O que os cursos raramente contam

1. **"Python é lento" é verdade e mentira ao mesmo tempo.** O Python puro é bem mais lento que C. Mas as bibliotecas pesadas (NumPy, PyTorch) são escritas **em C e C++** por baixo. Você escreve em Python e o trabalho pesado roda em C. É por isso que a IA "roda em Python".
2. **Indentação não é estética, é sintaxe.** Misturar Tab com espaços quebra o programa. Configure o editor para usar **4 espaços** (o padrão do VS Code já é assim).
3. **Existe um guia de estilo oficial: a PEP 8.** Nomes de variáveis e funções em `snake_case` (`nota_final`), classes em `PascalCase` (`ContaBancaria`). Seguir isso faz seu código parecer profissional.
4. **Ambientes virtuais (venv) evitam dor de cabeça.** Cada projeto deve ter suas próprias bibliotecas. Instalar tudo "no Python do computador" vira bagunça. Veja em [módulos e pacotes](material/07-modulos-e-pacotes.md).
5. **`python` ou `python3`? `py`?** No Mac e no Linux, muitas vezes o comando é `python3`. No Windows, existe também o `py`. São o mesmo Python.
6. **O Zen do Python.** Abra o Python no terminal e digite `import this`. É a "filosofia" da linguagem em 19 frases, como "Simples é melhor que complexo".

## Ecossistema

| | |
|---|---|
| **Gerenciador de pacotes** | `pip` (instala bibliotecas do PyPI, com mais de 500 mil pacotes) |
| **Arquivo de dependências** | `requirements.txt` ou `pyproject.toml` |
| **Testes** | `pytest` |
| **Formatador** | `black` / `ruff` |
| **Documentação oficial** | https://docs.python.org/pt-br/3/ (tem tradução em português!) |

---

[⬅️ Python](README.md)
