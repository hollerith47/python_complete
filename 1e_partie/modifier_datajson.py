import json

chemin = "C:/Users/herma/Desktop/Learning/Py_Orientee_Objet/2e_partie/data.json"

# ecriture
with open(chemin, 'w') as f:
    donnees = json.dump(list(range(6)), f, indent=4)

# lecture
with open(chemin, "r") as f:
    donnees =json.load(f)
    print(donnees)
    
# ajouter un element dans json
donnees.append(6)
with open(chemin, "w") as f:
    json.dump(donnees, f, indent=4)
