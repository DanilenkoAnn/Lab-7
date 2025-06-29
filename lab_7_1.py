import requests
import json


city_name = 'Kyoto'
key = 'b0873bc9e25b956902373a672b123374'
weather = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&lang=ru&units=metric')
data = weather.json()

weather = data['weather'][0]['description']
temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

print(f'В Киото погода: {weather}, температура: {temperature}, влажность: {humidity}, давление: {pressure}')