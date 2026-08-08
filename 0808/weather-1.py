import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q=taipei,TW&appid=&units=metric&lang=zh_TW'
response = requests.get(url)

print(response.json())