from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
march_8 = datetime(2020, 3, 8, 13, 0, 0, tzinfo=montreal_tz)
print(march_7)
print(march_8)
print()
# changement d'heure d'ete
print(march_7.tzname())
print(march_8.tzname())

print("conversion de fuseau horaire")
# la meilleur facon c de convertir en UTC puis continuer
# ici on utlise le module timedelta
march_7_utc = march_7.astimezone(ZoneInfo("UTC"))
march_8 = march_7_utc + timedelta(days=1)
march_8 = march_8.astimezone(montreal_tz)
print(march_8)

# apres heure d'ete essayons de savoir combien d time passer entre
# le 7 et le 10 mars a montreal

march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
march_10 = datetime(2020, 3, 10, 13, 0, 0, tzinfo=montreal_tz)
utc = ZoneInfo('UTC')
march_7_utc = march_7.astimezone(utc)
march_10_utc = march_10.astimezone(utc)

print(march_10 - march_7)
print(march_10_utc - march_7_utc)
