import pandas as pd
import numpy as np
from janitor import clean_names
import folium


def limpieza_datos(df):
    df=df.clean_names().drop(columns=['firmado','isa','anotaciones','unnamed_13','75_00_%','revisado','fecha_informe'])
    df['tipo_revision']=df.tipo_revision.replace(['visita'],'Visita')
    df=df.loc[df['tipo_revision']=='Visita']
    df['mes']=df['fecha_visita'].dt.month
    df['fecha_visita'] = df['fecha_visita'].dt.date
    
    return (df)

def Mapa(df):
    mapa=folium.Map(location= [42.7833,-7.8667],zoom_start=8.2)

    for explotacion in range(0,len(df)):
        folium.Marker(location=[df.iloc[explotacion]['latitud'],df.iloc[explotacion]['longitud']],
                 popup=f"Explotación: {df.index[explotacion]} Fecha Visita: {df.iloc[explotacion]['fecha_visita']}").add_to(mapa) 
    
    return (mapa)