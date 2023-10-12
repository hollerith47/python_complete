import json

chemin = "C:/Users/herma/Desktop/Learning/Py_Orientee_Objet/2e_partie/fichier.json"

# ecrire
with open(chemin, 'w') as g:
    json.dump(list(range(10)), g, indent=3)
    
# lire
with open(chemin, 'r') as f:
    liste = json.load(f)
    print(type(liste))