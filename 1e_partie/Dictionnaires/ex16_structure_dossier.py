from pathlib import Path
import os

chemin = Path.cwd().parent  # comme je suis déjà dans un sous-dossiers
# chemin= chemin.parent
d = {"Films": ["Le seigneur des anneaux", "Harry Potter", "Moon", "Forrest Gump"],
     "Employes": ["Paul", "Pierre", "Marie"], "Exercices": ["les_variables", "les_fichiers", "les_boucles"]}
for key, value in d.items():
    for name in value:
        os.makedirs(chemin / key / name, exist_ok=True)
