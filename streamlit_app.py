# import streamlit as st

# st.write("Hello World")


import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px

st.title("Consumo de Energia ao Longo do Tempo")

# # Upload do arquivo JSON
# uploaded_file = st.file_uploader("Escolha o arquivo JSON", type="json")
# Carregar JSON diretamente do repositório
json_path = "medicao.json"

if json_path is not None:
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
        height=500,
        width=1500
    )

    st.plotly_chart(fig, use_container_width=True)

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
        width=1500
    )

    st.plotly_chart(fig2, use_container_width=True)
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
        width=1500
    )

    st.plotly_chart(fig3, use_container_width=True)