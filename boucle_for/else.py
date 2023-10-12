# prenoms =['Pierre', 'Patrick', 'Herman', 'Jean']

# for prenom in prenoms :
#     if prenom =="Herman":
#         print(f"{prenom} a été trouvé !")
#         break
# else:
#     print("Herman est introuvable")

# ********************
# for i in range(1,11):
#     print(f"Utilisateur {i}")
# ********************

# mot ="Python"
# for i in reversed(mot):
#     print(i)

# for i in (range(len(mot))):
#     print(i)

# nombre = 7
# for i in range(11):
#     print(f"{i} x {nombre} = {i * nombre}")
# resultat = "Exercice réussi !"
# i = 9
# while i < 10:
#     print(resultat)
#     i +=1

# continuer = "o"

# while continuer == "o":
#     print("On continue !")
#     reponse= input("Voulez-vous continuer ? o/n ")
#     if reponse !="o":
#         break

# nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
# nombres_pairs = [i for i in nombres if i%2==0]
# # for i in nombres:
# #     if i % 2 == 0:
# #         nombres_pairs.append(i)

# print(nombres_pairs)

# # ---------------------------------------------------- #

# nombres = range(-10, 10)
# nombres_positifs = [i for i in nombres if i >=0]
# # for i in nombres:
# #     if i >= 0:
# #         nombres_positifs.append(i)
# print(nombres_positifs)

# # ---------------------------------------------------- #

# nombres = range(5)
# nombres_doubles = [i*2 for i in nombres]
# # for i in nombres:
# #     nombres_doubles.append(i * 2)
# print(nombres_doubles)

# # ---------------------------------------------------- #

# nombres = range(10)
# nombres_inverses = [i if i%2 ==0  else -i for i in nombres]
# # for i in nombres:
# #     if i % 2 == 0:
# #         nombres_inverses.append(i)
# #     else:
# #         nombres_inverses.append(-i)
# print(nombres_inverses)

# nombres = range(51)
# nombres_pairs = [i for i in nombres if i%2==0]
# print(nombres_pairs)


# print(not True and 10 == 10)
# i = 0
# while i < 10:
#     print(i)
#     i += 1
# a = 5
# str(a)
# print(type(a))

# 
#
liste = [3, 5, 7, 3, 1, 2, 3, 8, 3, 0, 2]
i = 3
while i in liste:
    liste.remove(i)
    # i = i
print(liste)
