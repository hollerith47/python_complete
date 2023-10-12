import requests
import time

while True:
    r = requests.get("https://api.kanye.rest/")
    if r.status_code == 200:
        print(r.json().get("quote"))
    time.sleep(60)
    