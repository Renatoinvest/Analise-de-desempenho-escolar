# Código principal do app Streamlit

import streamlit as st
import pandas as pd

df = pd.read_csv('data/df_final.csv')
st.title('📊 Análise de Desempenho Escolar')
st.write(df.head())