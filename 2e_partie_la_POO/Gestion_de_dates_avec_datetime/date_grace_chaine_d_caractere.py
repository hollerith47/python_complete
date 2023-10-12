from datetime import date, datetime

format_iso = date.fromisoformat("2021-10-24")
print(format_iso)

# conversion une date en chaine de caractere dans un format precis
# cfr le site www.strftime.org

# 1 conversion texte date en date chiffre
la_date = datetime.strptime("24 Oct 2021", "%d %b %Y")
print(la_date)

# 2 conversion chiffre en texte
now = datetime.now()
print(now)
now_lettre = now.strftime("%d %B %Y")
print("Date converti en lettre :", now_lettre)