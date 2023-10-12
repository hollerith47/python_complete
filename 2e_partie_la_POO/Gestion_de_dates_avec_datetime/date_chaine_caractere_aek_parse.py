import dateparser
from dateutil import parser



# 1 conversion text only from english
my_birthd = parser.parse("17 november 2022")
print(my_birthd)

# 2 conversion avec dateparser
""" ici on utilise un module externe #dateparser
 a installer avec pip pour recuperer les chaines de
 caractere date en n'importe qu'elle langue"""

now = dateparser.parse("aujourd'hui")
print("aujourd'hui", now)

previous_mois = dateparser.parse("il ya un mois")
print("il y a un mois ",previous_mois)

previous_year = dateparser.parse("one year ago at midnight")
