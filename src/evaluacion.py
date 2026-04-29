from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

def evaluar(modelo, X_test, y_test):

    #*predicciones
    y_predict= modelo.predict(X_test)

    print("\n" + "="*60)
    print("Evaluacion del modelo")
    print("="*60)

    #*accuracy o precision creo q era xd
    accuracy=accuracy_score(y_test, y_predict)
    print(f"Accuracy (Precisión): {accuracy:.4f}")
    print(f"Accuracy en porcentaje: {accuracy*100:.2f}%")

    #* Reporte de clasificación
    print("\nReporte de clasificacion:")
    print(classification_report(
        y_test, y_predict,
        target_names=['Vino Clase 0', 'Vino Clase 1', 'Vino Clase 2']
    ))
    
    return y_predict, accuracy

def obtener_importancia_caracteristicas(modelo, feature_names):
    importancia = modelo.feature_importances_
    
    print("\n" + "="*50)
    print("Importancia de caracteristicas")
    print("="*50)
    
    #* crear un ranking
    ranking = sorted(
        zip(feature_names, importancia),
        key=lambda x: x[1],
        reverse=True
    )
    
    print("\nCaracterísticas ordenadas por importancia:")
    for i, (feature, imp) in enumerate(ranking, 1):
        print(f"{i}. {feature}: {imp:.4f}")
    
    return importancia
