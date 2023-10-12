from pathlib import Path

# dirs ={}

# p = Path.home()/"Documents" /"Tri"
# for f in p.iterdir():
#     print(f)

# je cree mon dossier dictionnaires
p =Path("C:/Users/herma/Desktop/Learning/Py_Orientee_Objet/2e_partie")
p = p/"Dictionnaires"
p = p/"les_dictionnaires.py"

p= p.touch()
print(p)

# print(p)