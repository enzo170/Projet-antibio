# Function to generate the README file
def generate_readme():
    """Generate a README.md file for the project."""
    readme_content = """
# **Analyse de données biologiques : Evolution des bactéries vivantes**

## **Description**
Ce programme Python traite les données biologiques d'un fichier CSV pour analyser la fréquence des bactéries vivantes dans différents échantillons (fécaux, cécaux, et iléaux). Il génère :
1. Des fichiers CSV filtrés.
2. Des graphiques :
   - Un graphique en courbes pour les données fécales.
   - Des graphiques en violon pour les données cécales et iléales.

---

## **Prérequis**
1. **Python 3.8 ou supérieur**.
2. Les bibliothèques Python suivantes :
   - `pandas`
   - `matplotlib`
   - `seaborn`

### Installation des dépendances :
Pour installer les bibliothèques nécessaires, exécutez la commande suivante :
```bash
pip install pandas matplotlib seaborn
