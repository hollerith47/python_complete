from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

twenty_days = timedelta(days=20)
now = datetime.now()
now_in_15_days_moins_5_hours = now + timedelta(days=15, hours=-5)

print(now)
print(now_in_15_days_moins_5_hours)

# pour ajouter des mois on utilise relativedelta

now_in_9_mois = now + relativedelta(months=9)
print("dans 9 mois", now_in_9_mois)
