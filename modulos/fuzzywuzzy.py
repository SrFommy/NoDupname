from fuzzywuzzy import fuzz  # Importar fuzz desde la biblioteca fuzzywuzzy
import pandas as pd # type: ignore
from modulos.normalizacion import normalizar_Text

def comparar_cadenas(cadena1, cadena2):
    """
    Compara dos cadenas usando FuzzyWuzzy y devuelve el ratio de similitud.
    """
    return fuzz.ratio(cadena1, cadena2)

def comparar_en_clusters(df, col_a="NOMBRE_A", col_b="NOMBRE_B", umbral=80):
    """
    Compara registros en un DataFrame usando FuzzyWuzzy.
    - df: DataFrame con las columnas `col_a` y `col_b` para comparar.
    - col_a: Columna en el DataFrame para comparar (por defecto 'NOMBRE_A').
    - col_b: Columna en el DataFrame para comparar (por defecto 'NOMBRE_B').
    - umbral: Umbral de similitud para considerar una coincidencia (por defecto 80).
    Retorna un DataFrame con las coincidencias y su similitud.
    """
    # lineas de normalizacion
    '''df[col_a] = df[col_a].fillna("").astype(str).str.lower()
    df[col_b] = df[col_b].fillna("").astype(str).str.lower()'''
    normalizar_Text(df,col_a,col_b)
    
    # Lista para almacenar los resultados
    resultados = []
    
    # Comparar cada valor de col_a con cada valor de col_b
    for index, row in df.iterrows():
        similitud = comparar_cadenas(row[col_a], row[col_b])
        if similitud >= umbral:  # Filtrar por umbral
            resultados.append({
                "InputID": row["InputID"],  # Conservar el InputID
                f"{col_a}": row[col_a],
                f"{col_b}": row[col_b],
                "Similitud": similitud,
                "TargetID": row["TargetID"],
                "Distance": row["Distance"]
            })
    
    # Convertir resultados a DataFrame
    return pd.DataFrame(resultados)