import requests
import bs4

# 常數
TOKEN = ''
GET_UPDATES_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
SEND_MESSAGES_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

update_id = 0

while True:
    try:
        param = {
            'offset': update_id,
            'timeout': 30
        }
        response = requests.get(GET_UPDATES_URL, params=param, timeout=35)
        data = response.json()
        for update in data['result']:
            update_id = update['update_id'] + 1
            chat_id = update['message']['chat']['id']
            user_text = update['message']['text']
            send_data = {'chat_id': chat_id, 'text': user_text}
            send_msg = requests.post(SEND_MESSAGES_URL, data=send_data, timeout=30)

    except:
        print('error')
        continue
