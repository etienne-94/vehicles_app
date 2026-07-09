import pandas as pd
import plotly.express as px
import streamlit as st

# Ler os dados CSV
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho
st.header('Análise de Anúncios de Venda de Veículos')

# Histograma
build_histogram = st.checkbox('Mostrar histograma da quilometragem')

if build_histogram:
    st.write('Distribuição da quilometragem dos veículos')

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribuição da quilometragem dos veículos'
    )

    st.plotly_chart(fig, width='stretch')

# Gráfico de dispersão
build_scatter = st.checkbox(
    'Mostrar gráfico de dispersão (quilometragem vs preço)'
)

if build_scatter:
    st.write('Relação entre quilometragem e preço')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relação entre quilometragem e preço'
    )

    st.plotly_chart(fig, width='stretch')
