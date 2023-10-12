import os

chemin = "C:/Users/herma/Desktop/Learning/Py_Orientee_Objet"
hjk= len(chemin)
print(hjk)
dossier = os.path.join(chemin, 'dossier')
print(dossier)
if not os.path.exists(dossier):
    os.makedirs(dossier)
else:
    os.removedirs(dossier)