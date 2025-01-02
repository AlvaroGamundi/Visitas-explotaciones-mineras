from codigo_ejecucion import *
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_folium import st_folium

#CONFIGURACION DE LA PÁGINA
st.set_page_config(
     page_title = 'VISITAS DE SEGUIMENTO AMBIENTAL A EXPLOTACIÓNS MINEIRAS',
     #page_icon = 'risk_score.jpg',
     layout = 'wide')

#Imput
with st.sidebar:
    seleccion_provincia = st.multiselect('Selecciona las provincia:', ['Coruña','Lugo','Ourense','Pontevedra'])


    df=pd.read_csv('C:/Users/alvar/Desktop/Explotaciones_mineras/Analise_explotacions.csv',
               encoding='latin1',skiprows=1,index_col=0,parse_dates=['Fecha visita'],dayfirst=True)
    df=limpieza_datos(df)
    df = df[df['provincia'].isin(seleccion_provincia)]

#MAIN
st.title('VISITAS DE SEGUIMENTO AMBIENTAL A EXPLOTACIÓNS MINEIRAS')


# Ejecutar código cuando se haga clic en el botón "VISUALIZAR VISITAS"
if st.sidebar.button('VISUALIZAR VISITAS'):
    st.write('Designed and Powered by Álvaro Gamundi')
    # Crear el mapa 
    mapa = Mapa(df)
    st_folium(mapa, width=700)

else:
    st.write('SELECCIONA AS PROVINCIAS A VISUALIZAR E PREME O BOTÓN "VISUALIZAR VISITAS"')
    st.write('Designed and Powered by Álvaro Gamundi')
