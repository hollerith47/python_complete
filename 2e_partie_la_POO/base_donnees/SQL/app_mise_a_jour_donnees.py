import sqlite3

conn = sqlite3.connect("database1.db")
c = conn.cursor()
# Creation du tableau
c.execute("""
CREATE TABLE IF NOT  EXISTS employees(
	prenom text,
	nom text,
	salaire int
)
""")
d ={"salaire": 30000,
	"prenom": "Paul",
	"nom": "Dupont"}
# c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)
# c.execute("""UPDATE employees SET salaire=:salaire
# WHERE prenom=:prenom AND nom=:nom""", d)

# supprimer dans le tableau
c.execute("DELETE FROM employees where prenom=10000")

conn.commit()
conn.close()
