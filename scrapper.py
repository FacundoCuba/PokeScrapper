import json
import csv
import requests
from datetime import datetime

url = "https://es.pvpoke-re.com/data/gamemaster.min.json"
dt = [datetime.now()]

querystring = {"v":"1.28.4.3"}
payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://es.pvpoke-re.com/moves/charged/",
    "Cookie": "migrate=true; _ga_M4QJPH4YVV=GS1.1.1655423722.6.0.1655423722.0; _ga=GA1.1.1537632607.1654815363; __gads=ID=6527b786e4b310ba-2210021d547c0018:T=1654815704:RT=1654815704:S=ALNI_Ma2GFU6doi7cC50jFFUl_HfjL1q-A; __gpi=UID=0000056738bd9359:T=1654815704:RT=1655161694:S=ALNI_MYJu8liISrfgv9aDf5fGJcP65lyXg",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
jsondata = json.loads(response.text)

with open ("moves.csv", "w") as f:
    f = open('moves.csv', 'w')
    moves = jsondata["moves"]
    keys = ["moveId", "name", "abbreviation", "type", "power", "energy", "energyGain", "buffs", "buffTarget", "buffApplyChance", "archetype"]
    writer = csv.writer(f)
    writer.writerow(keys)
    writer = csv.DictWriter(f, fieldnames=keys, restval='', extrasaction='ignore')
    for i in moves:
        writer.writerow(i)
    writer = csv.writer(f)
    writer.writerow(dt)
f.close()

with open ("pokemon.csv", "w") as f:
    f = open('pokemon.csv', 'w')
    pokemon = jsondata["pokemon"]
    keys = ["dex","speciesName","speciesId","baseStats","types","fastMoves","chargedMoves","released","tags"]
    writer = csv.writer(f)
    writer.writerow(keys)
    writer = csv.DictWriter(f, fieldnames=keys, restval='', extrasaction='ignore')
    for i in pokemon:
        writer.writerow(i)
    writer = csv.writer(f)
    writer.writerow(dt)
f.close()
