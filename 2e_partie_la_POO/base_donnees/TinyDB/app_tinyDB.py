from tinydb import TinyDB, Query, where

db = TinyDB('data.json', indent=4)
"""
# ajouter une donnee
db.insert({"name": "Patrick", "score": 0})

# ajouter plusieurs donnees directements
db.insert_multiple([
{"name": "Ingrid", "score": 140},
{"name": "Alliance", "score": 210},
{"name": "Christian", "score": 300},
{"name": "David", "score": 250}
])
"""

# chercher dans la base de donnees
"""chercher les informations dans la base de donnees, pour ce faire
on utilise le module Query et where
"""
User= Query()
# patrick = db.search(User.name =="Patrick")
# herman = db.search(User.name =="David")
avec_where = db.search(where("score") > 100)
print(avec_where)

# pour verifier les elements de la bd on utilise tjr len
print(len(db))
# on peut aussi utiliser count pour trouver le nombre d'occurance dans notre bd
nb_occurence = db.count(where("score") == 100)
print(type(nb_occurence))