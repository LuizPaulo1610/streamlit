# import json
# import pandas as pd


# with open('medicao.json', 'r', encoding='utf-8') as file:
#     medicao = json.load(file)

# df_med = pd.DataFrame(medicao)

# # Consumo de 5 em 5 min
# import plotly.express as px
# import plotly.io as pio

# # Criar gráfico interativo
# fig = px.line(
#     df_med,
#     x='dataReferenciaConsumo',
#     y='consumo',
#     title="Consumo de Energia ao Longo do Tempo",
#     labels={'dataReferenciaConsumo': 'Data/Hora', 'consumo': 'Consumo (kWh)'},
#     markers=True
# )

# # Mostrar no navegador / dashboard
# pio.renderers.default = "browser"  # força abrir no navegador
# fig.show()