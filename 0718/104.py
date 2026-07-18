import requests
from bs4 import BeautifulSoup

url = 'https://www.104.com.tw/jobs/search/api/jobs?area=6001005000&jobsource=index_s&keyword=python&mode=s&order=15&page=3&pagesize=20'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'referer': 'https://www.104.com.tw/jobs/search/?area=6001005000&jobsource=index_s&keyword=python&mode=s&page=3&order=15'
}

response = requests.get(url,headers = header,verify=False)
json_data = response.json()
print(json_data)
for job in json_data['data']:
    print(job['custName'])
    print(job['jobName'])
    print(job['description'])
    if job['salaryLow'] == 0:
        print('面議')
    else:
        print(job['salaryLow'])

    print('=' * 50)