import re
import pandas as pd
import unicodedata
from collections import Counter

def palabras_mas_comunes(df, columna, n):
    """
    Función que extrae las n palabras más comunes de una columna de texto en un DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame de entrada.
    columna (str): Nombre de la columna a analizar.
    n (int): Número de palabras más comunes a extraer.

    Retorna:
    list: Lista con las n palabras más frecuentes.
    """
    # Unir todo el texto de la columna en una sola cadena
    texto_total = ' '.join(df[columna].dropna()).lower()
    
    # Eliminar signos de puntuación y números
    palabras = re.findall(r'\b[a-záéíóúüñ]+\b', texto_total)
    
    # Contar frecuencia de palabras
    conteo = Counter(palabras)
    
    # Obtener las n palabras más comunes
    palabras_comunes = [palabra for palabra, _ in conteo.most_common(n)]
    
    return palabras_comunes

def quitar_tildes(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')


#normalizar Texto
def normalizar_Text(df,ColumA,ColumB):

    #eliminar_palabras = list(set(palabras_mas_comunes(df, ColumA, n=3) + palabras_mas_comunes(df, ColumB, n=3)))
    eliminar_palabras =['mini', 'super', 'bar', 'panaderia', 'm/s','ms','kiosco','jardin','abarroteria','restaurante','fonda','minisuper', 'hotel']

    df[ColumA] = df[ColumA].fillna("").astype(str).str.lower()
    df[ColumB] = df[ColumB].fillna("").astype(str).str.lower()
    df[ColumA] = df[ColumA].apply(quitar_tildes)
    df[ColumB] = df[ColumB].apply(quitar_tildes)

    patron = r'\b('+'|'.join(map(re.escape,eliminar_palabras))+r')\b'

    df[ColumA] = df[ColumA].str.replace(patron,'',regex=True).str.strip()
    df[ColumB] = df[ColumB].str.replace(patron,'',regex=True).str.strip()

    return df

'''
data = {'nombreA':['mini super helmán', 'mini panaderia Jonnathan', 'm/s camila', 'ms Diego'],
        'nombreB':['super Anyelo', 'bar Julián', 'mini Paola', 'bar RONY']}
data = pd.DataFrame(data)

print(normalizar_Text(data,ColumA='nombreA',ColumB='nombreB'))'''
