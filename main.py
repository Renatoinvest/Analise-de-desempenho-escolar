
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Desempenho Escolar", layout="wide")
st.title("📊 Análise de Desempenho Escolar")

# Carregar os dados
@st.cache_data
def load_data():
    return pd.read_csv('data/df_final.csv')

df = load_data()

# Exibir dataframe
st.subheader("Visualização dos Dados")
st.dataframe(df)

# Filtros
materias = df.columns[1:-1]  # Ignora coluna de nome e média final
materia_selecionada = st.selectbox("Selecione a matéria para análise:", materias)

# Análise por nota
st.subheader(f"Distribuição das Notas em {materia_selecionada}")
fig, ax = plt.subplots()
df[materia_selecionada].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_xlabel("Notas")
ax.set_ylabel("Quantidade de Alunos")
st.pyplot(fig)

# Ranking de alunos
st.subheader("Ranking por Média Final")
top_n = st.slider("Número de alunos no ranking:", 5, 50, 10)
df_rank = df.sort_values(by="Média Final", ascending=False).head(top_n)
st.table(df_rank[['Alunos', 'Média Final']].reset_index(drop=True))
