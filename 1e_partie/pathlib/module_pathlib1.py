from pathlib import Path
import shutil
from pprint import pprint

# print(Path.home())
# print(Path.cwd())

p= Path("C:/Users/herma/Desktop/Learning/Py_Orientee_Objet/2e_partie/")
# print("p name", p.name)
# print("p parent", p.parent)
# print("p stem", p.stem)
# print("p suffix", p.suffix)
# print("p parts", p.parts)
# print("p exists", p.exists())
# print("p is_dir", p.is_dir())
# print("p is_file", p.is_file())
# print("p is_fifo", p.is_fifo())

# pprint(dir(p))

# p =Path.home()
p =p /"dossierTest"
# p.mkdir(exist_ok=True)
p = p/"readme.txt"
# p =p /'1'/'2'/'3'/'4'
# p.mkdir(parents=True)
# p = p/'readme'
# p.touch() #creation fichier
# p.unlink() #suppression fichier
# shutil.rmtree(p)
# p.touch()
# p.write_text("Bonjour tout le monde j'apprends python")
h= p.read_text()

print(h)