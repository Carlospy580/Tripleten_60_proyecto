import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Gráfica sobre autos de distintas marcas")

hist_button = st.button('Construir histograma')
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') 
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True) 

build_scatter = st.checkbox('Construir un scatterplot')
if build_scatter: 
    st.write('Construyendo un gráfico de dispersión')  
    fig = px.scatter(car_data, x="odometer", y="price") 
    st.plotly_chart(fig, use_container_width=True) 