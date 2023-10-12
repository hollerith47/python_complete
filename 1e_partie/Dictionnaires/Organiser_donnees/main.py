# """
# Dans cet exercice vous devez :
# - Ouvrir le fichier prenoms.txt et lire son contenu.
# - Récupérer chaque prénom séparément dans une liste.
# - Nettoyer les prénoms pour enlever les virgules, points ou espace.
# - Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
# """
from  pathlib import Path

chemin =Path.cwd() / 'prenoms.txt'
chemin_final = Path.cwd() / 'liste_final.txt'

# print(chemin)

with open(chemin, "r", encoding="utf-8") as f:
    lignes = f.read().splitlines()
# print(lignes)

prenoms =[]
for ligne in lignes:
    prenoms.extend(ligne.split())
    # print(prenoms)
    # for prenom in prenoms:
    #     fichier_final = [prenom.strip(",. ")]
    #     print(*fichier_final) 
fichier_final = [prenom.strip(",. ") for prenom in prenoms]
with open(chemin_final, "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(fichier_final)))
