import requests
import bs4
from dotenv import load_dotenv
import os

from soupsieve import SelectorSyntaxError

load_dotenv()
# 常數
TOKEN = os.getenv('TOKEN')
GET_UPDATES_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
SEND_MESSAGES_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

update_id = 0

def get_rate():
    try:
        c = 'jpy'
        url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'
        response = requests.get(url)
        htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')
        title = htmlfile.select_one(f'.{c.upper()} .title-item:nth-of-type(2)').text.strip()
        rate = htmlfile.select_one(f'.{c.upper()} .CashSBoardRate').text
        if rate == '':
            print(f'{title}沒有現金匯率')
            return f'{title}沒有現金匯率'
        else:
            # print(f'{title}匯率為{rate}')
            return f'{title}匯率為{rate}'

    except AttributeError:
        print('請輸入正確的貨幣代號！')
        return '請輸入正確的貨幣代號！'
    except SelectorSyntaxError:
        return '不可數字開頭！'
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

            #匯率
            if user_text == '/rate':
                user_text = get_rate()
            # /start
            if user_text == '/start':
                user_text = 'Hello 我是你的激起人!!!'

            send_data = {'chat_id': chat_id, 'text': user_text}
            send_msg = requests.post(SEND_MESSAGES_URL, data=send_data, timeout=30)

    except Exception as e:
        print('error')
        print(e)
        continue
