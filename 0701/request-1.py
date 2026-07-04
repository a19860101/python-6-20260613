import requests

url = 'https://www.ptt.cc/bbs/WorldCup/index.html'

response = requests.get(url)

print(response)