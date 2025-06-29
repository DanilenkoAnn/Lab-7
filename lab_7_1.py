import requests
import json


city_name = 'Kyoto'
key = '620c7d7ac11663ab4536ac0219607ca9'
lang = 'ru'

city = requests.get(f'http://api.openweathermap.org/geo/1.0/'
                    f'zip?zip=600-8216,JP&appid={key}')
data = city.json()
lat = data['lat']
lon = data['lon']

weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?'
                       f'lat={lat}&lon={lon}&appid={key}&lang={lang}')
data = weather.json()

description = data['weather'][0]['description']
temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

print(f'В Киото {description}, температура: {temperature}, '
      f'влажность: {humidity}, давление: {pressure}')

 