
# b = """Bonjour je suis Herman Makiese"""

# a = 5
# c = a
# c = 10
# print(id(a))
# print(id(c))
# a = 3
# b = 6
# a = b
# b = 7

# print(a)
# print(type(True))

# a = "J'ai une classe de "+ "30" + " élèves"
# b = "10" + " + " + "5" + " est égal à " + "15"
# c = 10 + int("5")
# d = "L'addition de 10 + 5 est égal à " + str(10 + 5)

# print(a)
# print(b)
# print(c)
# print(d)

# prenom = input("Entrer votre prénom: ")
# ville_de_naissance =  input("Entrer votre ville de naissance: ")
# age = input("Entrer votre age: ")

# print(prenom)
# print(ville_de_naissance)
# print(age)
# a = ("12345")
# b = ", ".join(a)
# print(b)

# chaine = "Pierre, Julien, Anne, Marie, Lucien"
# chaine = chaine.split(", ")
# chaine.sort()
# chaine_en_ordre = ", ".join(chaine)
# print(chaine_en_ordre)

# i =2
# i **= 4
# print(i)

# protocole = "https://"
# nom_du_site = "docstring"
# extension = "fr"
# page = "glossaire"

# # Modifiez le code à partir d'ici 
# URL = f"{protocole}www.{nom_du_site}.{extension}/{page}/"
# URL_1 = "{}www.{}.{}/{}/".format(protocole,nom_du_site,
#                                      extension, page)
# print(URL)
# print(URL_1)
#  b = get_w
# Veuillez entrer un premier nombre : 5
# Veuillez entrer un deuxième nombre : 10
# Le résultat de l'addition du nombre 5 avec le nombre 10 est égal à 15"
# a = ''
# b =''
# while not(a.isdigit() and b.isdigit()):
#     a = input('Entrez un premieur nombre:')
#     b = input('Entrez un deuxieme nombre:')
    
#     if not(a.isdigit() and b.isdigit()):
#         print('Veuillez entrer deux nombres valides')

# a = int(a)
# b = int(b)
# print(f"le resultat de l'addition de {a} avec {b} est egal a {a+b} ")

# nbre1 =''
# nbre2 =''
# while not(nbre1.isdigit() and nbre2.isdigit()):
#     nbre1 = input('Entrez un premier nombre: ')
#     nbre2 = input('Entrez un deuxième nombre: ')
    
#     if not(nbre1.isdigit() and nbre2.isdigit()):
#         print('Veuillez entrer les nombres valides')

# a = int(nbre1)
# b = int(nbre2)
# print(f"le resultat de l'addition de {a} avec {b} est egal a {a+b} ")

# langage = "Python"
# if langage == "Python":
#     print(f"Vous êtes bien en train d'apprendre le langage {langage}")

# a = True and (False or True)
# print(a)

# liste = [1, 2, [3, "Python", 4], 5, 6]
# h = liste[2][1]
# print(h)

# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])
# liste = ["Java", "Python", "C++"]
# liste.remove("Python")
# liste.append("Python")
# print(liste)
# *******************************************
# liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
# trois_premiers = liste[:3] # INSÉRER CODE ICI
# trois_derniers = liste[3:] # INSÉRER CODE ICI
# milieu = liste[1:-1] # INSÉRER CODE ICI
# premier_dernier = liste[::5]# INSÉRER CODE ICI

# print(trois_premiers)
# print(trois_derniers)
# print(milieu)
# print(premier_dernier)
# ***************************************

# interval = range(10)
# print(interval)
# print(type(interval))
# print(list(interval))
# print(interval.start)
# print(interval.step)
# print(interval.stop)
# ****************************
# liste = [4, 7, 9, 3, 1, 8, 2]
# print(sorted(liste))
# # ****************************
# film = "le seigneur des anneaux"
# film.title()
# print(film)

# ***************************************
mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."


if mdp == "":
    print(mdp_trop_court.upper())
elif len(mdp) < 8:
    print(mdp_trop_court)
elif mdp.isdigit() :
    print("Votre mot de passe ne contient que des nombres")
else:
    print("Inscription terminée")