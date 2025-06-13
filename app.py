import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
hist_button = st.button('Criar histograma')  # criar um botão

if st.checkbox('Criar um histograma'):  # se o botão for clicado
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
# criar um histograma
    fig = px.histogram(car_data, x='odometer')
# exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar gráfico de dispersão (odômetro x preço)'):
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True,
                    theme='streamlit', key=None)
