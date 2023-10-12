import json

fichier = "settings.json"

# pour lire le fichier json
with open(fichier, "r") as f:
    settings = json.load(f)
#     affichage
# print(settings.get('fontSize'))

# modification
settings["fontSize"] = 15
with open(fichier, 'w') as f:
    json.dump(settings, f, indent=4)
print(settings.get('fontSize'))



