import requests
import bs4

url = 'https://www.tenlong.com.tw/zh_tw/recent'

response = requests.get(url)
htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')

# print(htmlfile)

books = htmlfile.find_all('li', class_='single-book')
for book in books:
    title = book.select_one('.title a').text
    img_url = book.find('img')['src']
    print(img_url)