"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime
import re


def clean_data():

    # pd.set_option('display.max_rows', None)
    credito = pd.read_csv("./solicitudes_credito.csv", sep=";")
    df = pd.DataFrame(credito)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(lambda x : datetime.strptime(x, '%Y/%m/%d') if (len(re.findall('^\d+/', x)[0])-1) == 4 else datetime.strptime(x, '%d/%m/%Y'))
    df = df.dropna()
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["barrio"] = df["barrio"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.lower()

    df["línea_credito"]=df["línea_credito"].str.replace("\-"," ",regex = True).astype(str)
    df["línea_credito"]=df["línea_credito"].str.replace("\_"," ",regex = True).astype(str)

    df["barrio"]=df["barrio"].str.replace("\-"," ",regex = True).astype(str)
    df["barrio"]=df["barrio"].str.replace("\_"," ",regex = True).astype(str)

    df["monto_del_credito"]=df["monto_del_credito"].str.replace("\$","",regex = True).astype(str)
    df["monto_del_credito"]=df["monto_del_credito"].str.replace("\,","",regex = True).astype(str)
    df["monto_del_credito"]=df["monto_del_credito"].str.replace("\.00","",regex = True).astype(str)
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'])

    df["idea_negocio"]=df["idea_negocio"].str.replace("\-"," ",regex = True).astype(str)
    df["idea_negocio"]=df["idea_negocio"].str.replace("\_"," ",regex = True).astype(str)
    df = df.drop_duplicates()

    return df