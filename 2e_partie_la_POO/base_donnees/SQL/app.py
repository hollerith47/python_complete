import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
# Creation du tableau
c.execute("""
CREATE TABLE IF NOT  EXISTS employees(
	prenom text,
	nom text
)
""")
# ajouter des donnees dans le tableau en passant par un dictionnaire
d ={"prenom": "Ingrid", "nom": "Makiese" }
c.execute("INSERT INTO employees VALUES (:prenom, :nom)", d)
# recuperer les donnees
# c.execute("SELECT * FROM employees WHERE prenom='Herman'")
# donnees = c.fetchall() #pour recuperer toutes les donnees
# print(donnees)
# c.execute("SELECT * FROM employees")
# premier = c.fetchone()
# print(premier)
# deuxieme = c.fetchone()
# print(deuxieme)

conn.commit()
conn.close()
