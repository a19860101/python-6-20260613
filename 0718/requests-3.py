import requests
import bs4
url = 'https://www.taoyuancollege.com.tw/all-courses?category=employed'
response = requests.get(url)
htmlfile = bs4.BeautifulSoup(response.text,'html.parser')


courses = htmlfile.find_all('div',class_='course-item')

for course in courses:
    title = course.find('h5',class_='card-title').text
    # duration = course.find('small',class_='text-muted').text
    duration = course.select_one('.info-row:nth-of-type(2) small').text
    end = course.find('small',class_='text-success').text

    print(title)
    print(duration)
    print(end.strip())
    print('-'*100)