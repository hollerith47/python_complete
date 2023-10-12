# reponses etudiant1
from pathlib import Path

chemin_prenom = Path.cwd() / "prenoms.txt"

lines = chemin_prenom.read_text().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_clean = [prenom.strip(",. ") for prenom in prenoms]

# print(prenoms_clean)
chemin_prenom.write_text("")
with chemin_prenom.open("a") as f:
    f.write("\n".join(sorted(prenoms_clean)))

# reponses etudiant 2
from pathlib import Path
chemin = Path (r"C:\Users\Utilisateur\Downloads\prénom.txt")
with open(chemin,"r") as f:
    contenu = f.read()
    contenu_sans_saut = contenu.splitlines()
    contenu_texte = " ".join(contenu_sans_saut)
    contenu_liste = contenu_texte.split()
    contenu_liste.sort()
for i in contenu_liste:
    liste_ordre = i.strip(" ,.\n")
    #liste_finale = liste_ordre.split("\n")
    nouveau_fichier = Path (r"C:\Users\Utilisateur\Downloads\prénom2.txt")
    nouveau_fichier.touch()
    nouveau_fichier.write_text(liste_ordre)

# reponses etudiant 3
from pathlib import Path

# OUVRIR FICHIER
FILE = Path.cwd() / "prenoms.txt"
with open(FILE, "r") as f:
    content = f.read()

# RECUPERER PRENOMS SEPAREMENT DANS UNE LISTE
myList = content.split()

# NETTOYER LES PRENOMS AVEC STRIP
clean_list = []
for name in myList:
    clean_list.append(name.strip(", '."))

# ECRIRE LA LISTE PAR ORDRE ALPHABETIQUE DAN UN NOUVEAU FICHIER TEXTE
clean_list.sort()
with open("prenoms_final.txt", "a") as f:
    for name in clean_list:
        f.write(name + "\n")