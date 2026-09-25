# Python para Inteligência Artificial Aplicada

Repositório de estudos e revisão de **Python com foco em IA aplicada ao desenvolvimento de software**. Aqui ficam os exercícios e projetos feitos ao longo do curso, organizados por módulo — dos fundamentos da linguagem até a integração com APIs de IA e a análise de dados.

## 🎯 Objetivos

- Explorar a sintaxe básica do Python e a manipulação de variáveis, strings e estruturas condicionais
- Aplicar loops e funções para estruturar lógicas e resolver desafios
- Utilizar o Google Colab para praticar e validar os conceitos apresentados
- Manipular listas e dicionários para criar estruturas de dados eficientes
- Integrar APIs de inteligência artificial e desenvolver chatbots interativos
- Analisar grandes conjuntos de dados com bibliotecas como Pandas e NumPy

## 📂 Estrutura

| Módulo | Conteúdo | Status |
| --- | --- | --- |
| [`1_INTRODUCAO`](1_INTRODUCAO/) | `print`, variáveis, operações aritméticas, f-strings e métodos de string (`upper`, `lower`, `strip`, `replace`) | ✅ |
| [`2_CONECTANDO_AO_GEMINI`](2_CONECTANDO_AO_GEMINI/) | Chamada à API do Google Gemini com `google-genai`, chave via `.env` e tratamento de erros da API | ✅ |
| Estruturas condicionais, loops e funções | — | 🔜 |
| Listas e dicionários | — | 🔜 |
| Chatbots interativos | — | 🔜 |
| Análise de dados com Pandas e NumPy | — | 🔜 |

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/)
- [Google Gen AI SDK](https://github.com/googleapis/python-genai) (`google-genai`)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Google Colab](https://colab.research.google.com/)
- Pandas e NumPy *(em breve)*

## 🚀 Como executar

### Exercícios de introdução

```bash
python 1_INTRODUCAO/2_OPERACOES.py
```

### Conectando ao Gemini

1. Entre na pasta e crie um ambiente virtual:

   ```bash
   cd 2_CONECTANDO_AO_GEMINI
   python -m venv .venv
   ```

2. Ative o ambiente:

   ```bash
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1

   # Linux / macOS
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install google-genai python-dotenv
   ```

4. Crie um arquivo `.env` na pasta com a sua chave (gere uma em [Google AI Studio](https://aistudio.google.com/apikey)):

   ```env
   GOOGLE_API_KEY=sua_chave_aqui
   ```

   > ⚠️ O `.env` está no `.gitignore` — nunca faça commit da sua chave.

5. Execute:

   ```bash
   python app.py
   ```

## 👤 Autor

**Leirisson Souza** — [@leirisson99](https://github.com/leirisson99)
