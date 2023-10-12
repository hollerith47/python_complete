from pathlib import Path

p = Path.home().iterdir()
Doc_m = Path.home()/"Documents"
print("Chemin complet vers mes documents",Doc_m)
Dow_l = Path.home()/ "Downloads"
print("Chemin complet vers downloads",Dow_l)
# affichons slmn le nom des fichiers contenu dans le dossier
# print("fichier du dossier downloads")
# for f in Dow_l.glob("*.pdf"):
#     print(f.name)
    
# for _ in Doc_m.glob("*.pdf"):
#     print(_.name)

# print()
# print("Affichager des contenus du dossier et des sous-dossiers")
# print("fichier du dossier downloads")
# for f in Dow_l.rglob("*.pdf"):
#     print(f.name)
print()    
# print("fichier du dossier documents")
# for _ in Doc_m.rglob("*.pdf"):
#     print(_.name)

print("affichage des dossiers dans mes documents")
for f in Doc_m.iterdir():
    # print(f.name) #afficher seulement le nom
    print(f) #affichage du chemin complet

print()    
print("J'affiche le chemin complet des fichiers et dossiers dans download")
for f in Dow_l.iterdir():
    print(f)