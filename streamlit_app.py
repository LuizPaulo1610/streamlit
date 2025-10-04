# import streamlit as st

# st.write("Hello World")


import streamlit as st
import pandas as pd
import json
import plotly.express as px

st.title("Consumo de Energia ao Longo do Tempo")

# Upload do arquivo JSON
uploaded_file = st.file_uploader("Escolha o arquivo JSON", type="json")
if uploaded_file is not None:
    medicao = json.load(uploaded_file)
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