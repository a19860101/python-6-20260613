import requests
import bs4

url = 'https://www.tenlong.com.tw/zh_tw/recent'

response = requests.get(url)
htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')

# print(htmlfile)

imgs = htmlfile.find_all('img')
for img in imgs:
    # print(img)
    try:
        print(img['alt'])
        print(img['src'])
        print('-' * 100)
    except:
        continue