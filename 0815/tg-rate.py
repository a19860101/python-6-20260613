import requests
import bs4

# 常數
TOKEN = ''
GET_UPDATES_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
SEND_MESSAGES_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

update_id = 0

response = requests.get(GET_UPDATES_URL)
msg = response.json()
print(msg)
for update in msg['result']:
    print(update['message']['text'])
    print(update['message']['chat']['id'])
    print(update['update_id'])
