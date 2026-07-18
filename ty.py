import requests

url = 'https://opendata.tycg.gov.tw/api/v1/dataset.api_access?rid=08274d61-edbe-419d-8fcc-7a643831283d&format=json'

response = requests.get(url)

print(response.json())
for u in response.json():
    # print(u)
    print(u['sna'])
    print(u['ar'])
    print(u['tot'])
    print(u['sbi'])
    print(u['bemp'])
    print(u['sbi_detail'])
    print(u['mday'])
    print('-' * 60)