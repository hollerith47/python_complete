from datetime import datetime
from zoneinfo import ZoneInfo

"""
NB: il existe deux types de dates
1. une date #naive (date sans info fuseau horaire)
2. une date #aware (date avec info fuseau horaire)"""

now = datetime.now()
print(now.tzinfo) #cette date est naive

now_in_kinshasa = datetime.now(tz=ZoneInfo("Africa/Kinshasa"))
print(now_in_kinshasa)

now_in_alaska = datetime.now(tz=ZoneInfo("America/Nome"))
print(now_in_alaska)

now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver"))
print(now_in_vancouver)