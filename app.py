import pandas as pd
import plotly.express as px
import streamlit as st

# Ler os dados
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho
st.header('Análise de Anúncios de Venda de Veículos')

# Botão para histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando histograma da quilometragem dos veículos')

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribuição da quilometragem dos veículos'
    )

    st.plotly_chart(fig, width='stretch')

# Botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando gráfico de dispersão entre quilometragem e preço')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relação entre quilometragem e preço'
    )

    st.plotly_chart(fig, width='stretch')
