from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://www.nike.com/tw/w/sale-3yaep'
driver.get(url)
driver.maximize_window()
time.sleep(5)

titles = driver.find_elements(By.CLASS_NAME, 'product-card__title')
# print(titles)
for title in titles:
    print(title)

time.sleep(2)

driver.quit()