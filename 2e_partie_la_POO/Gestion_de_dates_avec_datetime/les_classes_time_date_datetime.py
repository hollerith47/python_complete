from datetime import time, date, datetime
from dateutil import parser
import dateparser

le_temps = time(hour=10, minute=18, second=24)
la_date = date(year=2019, month=12, day=27)
le_temps_et_date = datetime(year=2021, month=11, day=17, hour=20, minute=12, second=55)
now = datetime.now()

print(now)
print((now.hour))
print((now.minute))
print((now.second))
print((now.year))
print('+'*50)

# parser only in english
december_2024 = parser.parse("31 november 2024")
hmak = parser.parse("17 november 2022")
# print('Anniversaire de Minu', Minu)
# print('Anniversaire de Hmak', hmak)
print('+'*50)

# dateparser meme en francais
aujourdhui = dateparser.parse("aujourd'hui")
print(aujourdhui)



