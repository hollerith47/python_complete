from pathlib import Path


chemin = "C:/Users/herma/Desktop/Learning/Py_complet/objectif.txt"
dirObjectif = Path.home().iterdir()

print(dirObjectif)


with open(chemin, 'r') as f:
    contenu = repr(f.read()) #repr() empeche le retour a la ligne
    print(contenu)
print(chemin)