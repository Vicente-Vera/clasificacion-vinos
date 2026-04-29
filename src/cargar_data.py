import pandas as pd
from sklearn.datasets import load_wine

def cargar_datos():

    #*cargar datos
    datos=load_wine()

    #*pasar a dataframe
    df=pd.DataFrame(datos.data, columns=datos.feature_names)

    #*agregar columna de target
    df["target"] = datos.target

    #*analisis 
    print("="*50)
    print("Analisis exploratorio")
    print("="*50)

    print("Primeros registros")
    print(df.head())
    print("="*50)

    print("Nombres de variables")
    print(datos.feature_names)
    print("="*50)

    print("Clases")
    print(f"Tipos de vinos: {datos.target_names}")
    print("="*50)

    print("Cantidad de datos")
    print(f"Total de muestras: {len(df)}")
    print(f"Total de caracteristicas: {len(datos.feature_names)}")
    print("="*50)

    print("Estadisticas")
    print(df.describe())
    print("="*50)

    return df, datos

def separar_variables(df):
    #*eliminar respuestas
    X = df.drop('target', axis=1)
    #*dejar solo respuestas
    y = df['target']
    
    print("\n" + "="*50)
    print("Variables separadas")
    print("="*50)
    print(f"Variables independientes (X): {X.shape}")
    print(f"Variable objetivo (y): {y.shape}")
    
    return X, y



