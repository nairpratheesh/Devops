import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=Service("C:\\Users\\prath\\.cache\\selenium\\chromedriver\\win64\\126.0.6478.62\\chromedriver.exe"))
driver.get("http://127.0.0.1:5001/users/get_user_data/200")
time.sleep(5)
element = driver.find_element(By.ID, value='user')
print(driver.current_url)
print(element.text)
