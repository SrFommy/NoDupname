import pandas as pd # type: ignore

def leer_excel(ruta_archivo, hoja=0):
    """
    Lee un archivo Excel y lo convierte en un DataFrame.

    Parámetros:
        ruta_archivo (str): Ruta del archivo Excel.
        hoja (int o str): Nombre o índice de la hoja a leer (por defecto es 0).

    Retorna:
        pd.DataFrame: DataFrame con los datos del archivo Excel.
    """
    try:
        df = pd.read_excel(ruta_archivo, sheet_name=hoja)
        print(f"Archivo '{ruta_archivo}' leído correctamente.")
        return df
    except Exception as e:
        print(f"Error al leer el archivo '{ruta_archivo}': {e}")
        return None

def exportar_excel(df, ruta_archivo, hoja="Hoja1"):
    """
    Exporta un DataFrame a un archivo Excel.

    Parámetros:
        df (pd.DataFrame): DataFrame a exportar.
        ruta_archivo (str): Ruta donde se guardará el archivo Excel.
        hoja (str): Nombre de la hoja en el archivo Excel (por defecto es "Hoja1").
    """
    try:
        df.to_excel(ruta_archivo, sheet_name=hoja, index=False)
        print(f"DataFrame exportado correctamente a '{ruta_archivo}'.")
    except Exception as e:
        print(f"Error al exportar el DataFrame a '{ruta_archivo}': {e}")