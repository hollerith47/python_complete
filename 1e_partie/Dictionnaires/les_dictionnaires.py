# films = {
#     1:{"titre": "Le Seigneur des Anneaux",
#          "prix": "12£"},
#     2:{"titre": "Harry Potter",
#         "prix": "9£"},
#     3:{"titre": "Blade Runner",
#        "prix": "7.5£"}}
# #vrai code
# films ={"Le Seigneur des Anneaux": 12,
#         "Harry Potter": 9,
#         "Blade Runner": 7.5}
# prix = 0
# for i in films:
#     prix +=films[i]
    
# print(prix,"£", sep="")

# modifier la valeur d'une cle
d= {
    "prenom": "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"}
d["prenom"]= "Julie" #une modification
d["age"] =30 #ajout de la nouvelle cle
# del d["profession"] #suppression d'une cle

# boucler sur un dictionnaire
print(d.keys())
print(d.values())
print()
print(d)
print()

for cle in d:
    print(cle,":", d[cle])
    # print(d[cle])

# la methode items()
print("la methode items()")
print(d.items())
# la boucle avec items()
print()
print("la boucle avec items()")
for cle, valeur in d.items():
    print(cle, valeur)