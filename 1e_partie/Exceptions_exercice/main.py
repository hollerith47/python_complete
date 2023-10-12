fichier = input("Entrer le chemin du fichier à ouvrir: ")

try :
    content = open(fichier, 'r', encoding="utf-8").read()
    # content =content.read()
    
except FileNotFoundError:
    print("Fichier introuvable")

except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier")

else:
    print(content)