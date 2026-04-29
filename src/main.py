from cargar_data import cargar_datos, separar_variables
from modelo import dividir_datos, entrenar_modelo
from evaluacion import evaluar, obtener_importancia_caracteristicas
from visualizacion import (visualizar_arbol, interpretar_arbol_raiz, mostrar_decisiones_principales)

def main():
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " CLASIFICACIÓN DE VINOS CON ÁRBOL DE DECISIÓN ".center(58) + "║")
    print("╚" + "="*58 + "╝")
    
    # 1. Cargar datos
    print("\n[1/6] Cargando datos...")
    df, datos = cargar_datos()
    
    # 2. Separar variables
    print("\n[2/6] Separando variables...")
    X, y = separar_variables(df)
    
    # 3. Dividir datos
    print("\n[3/6] Dividiendo datos...")
    X_train, X_test, y_train, y_test = dividir_datos(X, y)
    
    # 4. Entrenar modelo
    print("\n[4/6] Entrenando modelo...")
    modelo = entrenar_modelo(X_train, y_train, max_depth=5)
    
    # 5. Evaluar modelo
    print("\n[5/6] Evaluando modelo...")
    y_predict, accuracy = evaluar(modelo, X_test, y_test)
    
    # 6. Visualizar resultados
    print("\n[6/6] Visualizando resultados...")
    
    # Importancia de características
    obtener_importancia_caracteristicas(modelo, X.columns)
    
    # Interpretar nodo raíz
    interpretar_arbol_raiz(modelo, X.columns)
    
    # Mostrar decisiones principales
    mostrar_decisiones_principales(modelo, X.columns)
    
    # Visualizar árbol
    visualizar_arbol(
        modelo,
        X.columns,
        datos.target_names
    )
    
    print("\n" + "="*60)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print("="*60)
    
    return modelo, accuracy

if __name__ == "__main__":
    main()