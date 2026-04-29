from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def dividir_datos(X, y, test_size=0.2, random_state=42):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state
    )
    
    print("\n" + "="*50)
    print("Division de datos")
    print("="*50)
    print(f"Datos de entrenamiento: {X_train.shape[0]} muestras")
    print(f"Datos de prueba: {X_test.shape[0]} muestras")
    print(f"Porcentaje test: {test_size*100}%")
    
    return X_train, X_test, y_train, y_test

def entrenar_modelo(X_train, y_train, max_depth=3, random_state=42):
    print("\n" + "="*50)
    print("Entrenamiento del modelo")
    print("="*50)
    
    #* Crear modelo
    modelo = DecisionTreeClassifier(
        max_depth=max_depth,
        random_state=random_state
    )
    
    #*Entrenar
    modelo.fit(X_train, y_train)
    
    print(f"Profundidad máxima del árbol: {max_depth}")
    print(f"Número de nodos: {modelo.tree_.node_count}")
    print(f"Profundidad real del árbol: {modelo.get_depth()}")
    
    return modelo