# import streamlit as st

# st.write("Hello World")


import streamlit as st
import pandas as pd
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
        markers=True
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
        height=500
    )

    st.plotly_chart(fig2, use_container_width=True)