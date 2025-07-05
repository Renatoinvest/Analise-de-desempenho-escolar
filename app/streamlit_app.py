import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Desempenho Escolar", layout="wide")
st.title("📊 Análise de Desempenho Escolar – Interativo")

# Carregar dados com cache
@st.cache_data
def load_data():
    df = pd.read_csv("data/df_final.csv")
    return df

df = load_data()


# Filtros interativos
st.subheader("📌 Filtros")
materias = st.multiselect("Escolha a(s) matéria(s):", df.columns[1:-1])
filtro_nota = st.slider("Filtrar por notas", 0.0, 10.0, (7.0, 10.0))
df_filtrado = df[(df[materias] >= filtro_nota[0]) & (df[materias] <= filtro_nota[1])]

if materias:
    filtro = df[materias].apply(lambda row: row.between(notas[0], notas[1])).all(axis=1)
    df_filtrado = df[filtro]
else:
    df_filtrado = df.copy()

st.dataframe(df_filtrado, use_container_width=True)

# Gráfico de média por matéria
st.subheader("📊 Média por Matéria")
media_materias = df.iloc[:, 1:-1].mean().sort_values()
fig = px.bar(
    x=media_materias.index,
    y=media_materias.values,
    labels={"x": "Matéria", "y": "Média"},
    title="Média das Notas por Matéria"
)
st.plotly_chart(fig, use_container_width=True)

media_materias = df.iloc[:, 1:-1].mean().sort_values()
fig = px.bar(x=media_materias.index, y=media_materias.values, labels={"x": "Matéria", "y": "Média"})
st.plotly_chart(fig)

# Upload de novo CSV
st.subheader("📅 Carregar Novo CSV")
uploaded_file = st.file_uploader("Faça upload de um novo arquivo CSV", type=["csv"])
if uploaded_file:
    try:
        new_df = pd.read_csv(uploaded_file, sep=";", encoding="utf-8")
        st.write(new_df.head())
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")

# Exportar CSV filtrado
st.subheader("📄 Exportar Dados Filtrados")
st.download_button(
    "Baixar CSV Filtrado",
    df_filtrado.to_csv(index=False).encode("utf-8"),
    "dados_filtrados.csv",
    "text/csv"
)

# Métricas rápidas
st.subheader("📌 Indicadores Rápidos")
col1, col2, col3 = st.columns(3)
col1.metric("Alunos com nota 10", df[df == 10].count().sum())
col2.metric("Média Geral", round(df.iloc[:, 1:-1].mean().mean(), 2))
col3.metric("Alunos Abaixo da Média", df[df.iloc[:, 1:-1].mean(axis=1) < 6].shape[0])
