📊 Análise de Desempenho Escolar

Este projeto utiliza Python, Pandas e Streamlit para analisar dados de desempenho escolar, com o objetivo de identificar padrões entre os alunos, matérias com maiores dificuldades e destaques acadêmicos. A proposta é transformar dados brutos em informações acionáveis para escolas, professores e gestores.

🔍 Objetivos
Limpar e organizar dados escolares.

Identificar alunos com maior desempenho (notas 10).

Detectar matérias com maior taxa de reprovação ou dificuldade.

Criar visualizações para facilitar a interpretação.

Desenvolver um painel interativo com Streamlit.

🗂 Estrutura do Projeto

bash
Copiar
Editar
desempenho-escolar-analysis/
├── README.md                 # Este arquivo

├── requirements.txt          # Dependências do projeto

├── LICENSE                   # Licença do projeto

├── data/                     # Local para os arquivos CSV

├── notebooks/                # Jupyter Notebooks para análise

│   ├── 01-limpeza-dados.ipynb

│   ├── 02-analise-exploratoria.ipynb

│   ├── 03-ranking-alunos.ipynb

│   └── 04-visualizacoes.ipynb

└── app/

    └── streamlit_app.py      # Painel interativo com Streamlit
    
▶️ Como Usar

1. Clone o repositório
bash
Copiar
Editar
git clone https://github.com/Renatoinvest/Analise-de-desempenho-escolar
cd desempenho-escolar-analysis
2. Crie um ambiente virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Execute os notebooks
Abra o Jupyter:

bash
Copiar
Editar
jupyter notebook
Ou use o VS Code para explorar os arquivos .ipynb na pasta notebooks.

5. Rode o painel Streamlit
bash
Copiar
Editar
streamlit run app/streamlit_app.py

📈 Possíveis Insights

Alunos com maior número de notas 10 e em quais matérias.

Matérias com maior concentração de notas baixas.

Comparativo entre turmas ou períodos (se houver mais dados).

Visualizações interativas para tomadas de decisão pedagógica.

📌 Tecnologias Utilizadas
Python

Pandas, NumPy

Matplotlib, Seaborn, Plotly

Jupyter Notebook

Streamlit

📄 Licença
Este projeto está licenciado sob a Licença MIT.
