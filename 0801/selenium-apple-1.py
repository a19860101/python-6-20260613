from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

url = 'https://www.apple.com/tw/shop/refurbished/mac'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

all_products = []

while True:
    products = driver.find_elements(By.CLASS_NAME, 'rf-refurb-producttile')
    for product in products:
        title = product.find_element(By.CLASS_NAME, 'rf-refurb-producttile-link').text
        price = product.find_element(By.CSS_SELECTOR, 'span.rf-refurb-producttile-currentprice').text
        p = {}
        p['title'] = title
        p['price'] = price
        all_products.append(p)
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div[3]/button')
    if btn.get_attribute('disabled'):
        break
    btn.click()
    time.sleep(2)
print(f'共找到{len(all_products)}筆整修品')
for product in all_products:
    print(f'商品名稱：{product['title']}')
    print(f'價格：{product['price']}')
    print('*' * 100)
# print(len(all_products))

driver.quit()

