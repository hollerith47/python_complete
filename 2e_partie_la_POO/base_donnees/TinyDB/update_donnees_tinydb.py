from tinydb import TinyDB, Query, where

db = TinyDB("data.json", indent=4)

# 1ere methode avec update
db.update({'roles': ['Junior']}) #comme on n'a rien indiquer la mise a jour se fera partout
# avec specification de l'endroit a modifier
# db.update({'roles': ["Pythonista"]}, where('name')=='Herman')
# db.update({'score': 800}, where('name') == 'Herman')

herman = db.search(where('name')=="Herman")
print(herman)

# 2e methode du type create if not exists avec upsert()
db.upsert({'name': "Pierre", 'score':20, "roles":["Senior"]}, where('name')=="Pierre")
# db.upsert({'name': "Jean Claude", 'score':3, "roles":["Senior"]}, where('name')=="Jean Claude")

# on supprime les elements avec la methode remove()
db.remove(where('score') == 3)

# suppression de tous les elements dans la db
# db.truncate()