
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Desempenho Escolar", layout="wide")

st.title("📊 Análise de Desempenho Escolar – Interativo")

# Carregar dados
@st.cache_data
def load_data():
    df = pd.read_csv("data/df_final.csv")
    return df

df = load_data()

st.subheader("📌 Filtros")
materias = st.multiselect("Selecione as matérias", df.columns[1:-1])
notas = st.slider("Selecione a faixa de notas", 0.0, 10.0, (6.0, 10.0))

if materias:
    df_filtrado = df[(df[materias] >= notas[0]) & (df[materias] <= notas[1])]
else:
    df_filtrado = df.copy()

st.dataframe(df_filtrado)

st.subheader("📊 Média por Matéria")
media_materias = df.iloc[:, 1:-1].mean().sort_values()
fig = px.bar(x=media_materias.index, y=media_materias.values, labels={"x": "Matéria", "y": "Média"})
st.plotly_chart(fig, use_container_width=True)

st.subheader("📥 Carregar Novo CSV")
uploaded_file = st.file_uploader("Faça upload de um novo arquivo CSV", type=["csv"])
if uploaded_file:
    new_df = pd.read_csv(uploaded_file, sep=";", encoding="utf-8")
    st.write(new_df.head())

st.subheader("📤 Exportar Dados Filtrados")
st.download_button("Baixar CSV Filtrado", df_filtrado.to_csv(index=False), "dados_filtrados.csv", "text/csv")

# Métricas rápidas
st.subheader("📌 Indicadores Rápidos")
col1, col2, col3 = st.columns(3)
col1.metric("Notas 10", (df == 10).sum().sum())
col2.metric("Média Geral", round(df.iloc[:, 1:-1].mean().mean(), 2))
col3.metric("Abaixo da Média (<6)", (df.iloc[:, 1:-1].mean(axis=1) < 6).sum())
