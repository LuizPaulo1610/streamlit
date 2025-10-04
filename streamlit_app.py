# import streamlit as st

# st.write("Hello World")


import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px

st.set_page_config(
    layout="wide",  # ativa layout amplo
    page_title="Energia elétrica"
)


st.title("Consumo de Energia ao Longo do Tempo")


# # Upload do arquivo JSON
# uploaded_file = st.file_uploader("Escolha o arquivo JSON", type="json")
# Carregar JSON diretamente do repositório
json_path = "medicao.json"


with open(json_path, 'r', encoding='utf-8') as file:
    medicao = json.load(file)

df_med = pd.DataFrame(medicao)

# Gráfico interativo
fig = px.line(
    df_med,
    x='dataReferenciaConsumo',
    y='consumo',
    title="Consumo de Energia ao Longo do Tempo",
    labels={'dataReferenciaConsumo': 'Data/Hora', 'consumo': 'Consumo (kWh)'},
    markers=True,

)

fig.update_layout(width=3000, height=800)
# st.plotly_chart(fig)
# -------------------------------------------------------------------------------------------------------------
# Segundo gráfico: exemplo de consumo cumulativo
df_med['consumo_cumulativo'] = df_med['consumo'].cumsum()
fig2 = px.line(
    df_med,
    x='dataReferenciaConsumo',
    y='consumo_cumulativo',
    title="Consumo Cumulativo de Energia",
    labels={'dataReferenciaConsumo': 'Data/Hora', 'consumo_cumulativo': 'Consumo Cumulativo (kWh)'},
    markers=True,
    height=500,
    width=2500
)

fig2.update_layout(width=3000, height=800)
# st.plotly_chart(fig2)
# ----------------------------------------------------------------------------------------------------------
df_filtered = df_med[['dataReferenciaConsumo', 'consumo']] 

arr = df_filtered['consumo'].to_numpy()

# soma de janelas de tamanho 3 - média móvel de 15min
somas = np.convolve(arr, np.ones(3, dtype=int), 'valid')

max_val = somas.max()
idx_max = somas.argmax()

demandas = list()
for idx, consumo in enumerate(somas):
    demandas.append(
        {
            "dataReferenciaConsumo": df_filtered.loc[idx+2,'dataReferenciaConsumo'],
            "consumo": consumo
        }
    )

df_demanda = pd.DataFrame(demandas)
df_demanda['demanda'] = round(4*df_demanda['consumo'], 3)

# Terceiro gráfico: Demandas
fig3 = px.line(
    df_demanda,
    x='dataReferenciaConsumo',
    y='demanda',
    title="Demanda Medida ao Longo do Tempo",
    labels={'dataReferenciaConsumo': 'Data/Hora', 'demanda': 'Demanda (kW)'},
    markers=True,
    height=500,
    width=2500
)
fig3.update_layout(width=3000, height=800)
# st.plotly_chart(fig3)
# ----------------------------------------------------------------------------------------------------------
# Criando histograma de consumo
fig4 = px.histogram(
    df_med,
    x="consumo",
    title="Distribuição do Consumo",
)
fig4.update_layout(width=3000, height=800)
# ====================================================================================
"""
Usando tabs: Definimos a plotagem por tabs posteriormente.

Para nossa versão basta mudar a plotagem
"""

# Criar abas
tab1, tab2 = st.tabs(["📈 Gráficos de Linha", "📊 Histogramas"])

with tab1:
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)

with tab2:
    st.plotly_chart(fig4)