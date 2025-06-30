import requests
import json
import datetime
 

ISS = requests.get(f'http://api.open-notify.org/iss-now.json')
people = requests.get(f'http://api.open-notify.org/astros.json')

data_ISS = ISS.json()
data_people = people.json()

lat = data_ISS["iss_position"]["latitude"]
lon = data_ISS["iss_position"]["longitude"]
number = data_people["number"]
spacecraft_name = data_people["people"][0]["craft"]

timestamp = datetime.datetime.fromtimestamp(data_ISS["timestamp"]) \
    .strftime("%d.%m.%Y %H:%M:%S")

print(f"\n⌚ Сейчас: {timestamp}")
print(f"\nМКС в данный момент находится над {lat}"
      f" широты и над {lon} долготы.")
print(f"\n🚀 Всего людей в космосе в данный момент: {number}\n")
print("="*40)
print(f"{'№':<3} | {'Имя':<20} | {'Корабль':<15}")
print("-"*40)

for i, person in enumerate(data_people["people"], 1):
    print(f"{i:<3} | {person['name']:<20} | {person['craft']:<15}")
print("="*40)