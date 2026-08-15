import requests
import bs4

url = 'https://www.ncl.edu.tw/XCProduct/Rss?XsmSId=0Q035604894351531469'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'xml')
items = soup.find_all('item')
print(items)
for item in items:
    title = item.find('title').text
    content = item.find('content:encoded').text
    print(title)
    print(content)

