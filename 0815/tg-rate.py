import requests
import bs4

# 常數
TOKEN = ''
GET_UPDATES_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
SEND_MESSAGES_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

update_id = 0