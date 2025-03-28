from modulos.utils import leer_excel
from modulos.utils import exportar_excel
from modulos.fuzzywuzzy import comparar_en_clusters
from modulos.fuzzywuzzy import comparar_en_clusters
import os

def comparar_en_grupo(grupo, col_a="NOMBRE_A", col_b="NOMBRE_B", umbral=80):
    """
    Aplica `comparar_en_clusters` a un grupo de datos.
    """
    return comparar_en_clusters(grupo, col_a=col_a, col_b=col_b, umbral=umbral)

def main():
    file_path = os.path.join("bases") + "/"
    try:
        dfA = leer_excel(file_path + "matriz_navegador_geo.xlsx")
        if dfA is not None:
            # Verificar si la columna 'InputID' existe
            if "InputID" not in dfA.columns:
                raise ValueError("La columna 'InputID' no existe en el DataFrame.")
            
            # Aplicar la comparación en grupos
            resultado = dfA.groupby("InputID").apply(comparar_en_grupo)
            resultado = resultado.reset_index(drop=True)
            
            # Exportar el resultado
            exportar_excel(resultado, file_path + "resultado_navegador_geotrack.xlsx")
        else:
            print("Error: No se pudo leer el archivo Excel.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    main()