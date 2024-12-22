Instructions pour lancer et utiliser le programme:

# Description
- Ce programme Python analyse la fréquence des bactéries vivantes dans différents échantillons (fécaux, cécaux, iléaux).
- Il génère des fichiers CSV filtrés et des graphiques :
  - Des graphiques en courbes pour les échantillons concernant la population bactérienne dans la matière fécale des souris.
  - Des graphiques en violon pour les données concernant la population bactérienne dans le caecum et l'ileum des souris.

## Prérequis
- Python 3.8 ou supérieur
- Bibliothèques Python :
  - `pandas`
  - `matplotlib`
  - `seaborn`

### Installation des bibliothèques
- Exécutez la commande suivante pour installer les bibliothèques nécessaires :
  ```sh
  pip install pandas matplotlib seaborn




Limitations fonctionnelles de notre programme:

# Graphiques différents
- Notre programme renvoie des graphiques qui ne ressemblent pas exactement aux graphiques attendus. Ces différences sont dûes à de potentielles erreurs:
      - Erreurs au niveau de la lecture des fichiers csv, problèmes de lecture au niveau des lignes ou au niveau des colonnes du fichier pris en compte.
      - Erreurs au niveau du code, imprécisions possibles dans l'appellation des variables par exemple.

## Graphiques non analysés
- Notre programme n'est pas en mesure d'analyser les données des graphiques. Une fois les graphiques obtenus, l'analyse de ces derniers doit être faite par l'utilisateur.
