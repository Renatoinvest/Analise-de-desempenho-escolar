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
colunas_numericas = df.select_dtypes(include='number').columns.tolist()
materias = st.multiselect("Escolha a(s) matéria(s):", colunas_numericas)
filtro_nota = st.slider("Filtrar por notas", 0.0, 10.0, (7.0, 10.0))

if materias:
    filtro = df[materias].apply(lambda row: row.between(filtro_nota[0], filtro_nota[1])).all(axis=1)
    df_filtrado = df[filtro]
else:
    df_filtrado = df.copy()

st.dataframe(df_filtrado, use_container_width=True)

# Gráfico de média por matéria
st.subheader("📊 Média por Matéria")
media_materias = df[colunas_numericas].mean().sort_values()
fig = px.bar(
    x=media_materias.index,
    y=media_materias.values,
    labels={"x": "Matéria", "y": "Média"},
    title="Média das Notas por Matéria"
)
st.plotly_chart(fig, use_container_width=True)

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
col1.metric("Alunos com nota 10", (df[colunas_numericas] == 10).sum().sum())
col2.metric("Média Geral", round(df[colunas_numericas].mean().mean(), 2))
col3.metric("Abaixo da Média (<6)", (df[colunas_numericas].mean(axis=1) < 6).sum())
