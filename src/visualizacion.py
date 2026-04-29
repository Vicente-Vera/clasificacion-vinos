from sklearn import tree
import matplotlib.pyplot as plt
from pathlib import Path

def visualizar_arbol(modelo, feature_names, class_names, titulo="Árbol de Decisión - Clasificación de Vinos"):

    print("\n" + "="*60)
    print("Visualizacion del tree")
    print("="*60)
    
    plt.figure(figsize=(20, 10))
    
    tree.plot_tree(
        modelo,
        feature_names=feature_names,
        class_names=class_names,
        filled=True,
        rounded=True,
        fontsize=10,
        proportion=True
    )
    
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.tight_layout()

    # Guardar la figura en la carpeta 'grafico' en el directorio raíz del proyecto
    out_dir = Path(__file__).resolve().parent.parent / 'grafico'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / 'arbol_decision.png'
    print(f"Guardando gráfico en: {out_path}")
    plt.savefig(str(out_path), dpi=300, bbox_inches='tight')
    plt.show()

def interpretar_arbol_raiz(modelo, feature_names):

    print("\n" + "="*50)
    print("INTERPRETACIÓN DEL NODO RAÍZ")
    print("="*50)
    
    #* Obtener información del nodo raíz (índice 0)
    feature_idx = modelo.tree_.feature[0]
    threshold = modelo.tree_.threshold[0]
    feature_name = feature_names[feature_idx]
    
    print(f"\nVariable raíz: {feature_name}")
    print(f"Umbral de decisión: {threshold:.4f}")
    print(f"\nRegla del nodo raíz:")
    print(f"  Si {feature_name} <= {threshold:.4f} → Rama izquierda")
    print(f"  Si {feature_name} > {threshold:.4f} → Rama derecha")
    
    return feature_name, threshold

def mostrar_decisiones_principales(modelo, feature_names):

    print("\n" + "="*50)
    print("DECISIONES PRINCIPALES DEL ÁRBOL")
    print("="*50)
    
    tree_rules = tree.export_text(
        modelo,
        feature_names=feature_names
    )
    
    print("\nReglas del árbol:")
    print(tree_rules)