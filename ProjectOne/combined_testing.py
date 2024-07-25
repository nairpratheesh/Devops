import requests
import pymysql

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

db_check_status = 0
result = 0
schema_name = 'mydb'
user_name = "candidate5"
user_id = 3403


def back_testing(id, name):
    url_str = f'http://127.0.0.1:5000/users/{user_id}'
    requests.post(url_str, json={"user_name": user_name})
    return requests.get(url_str)


res = back_testing(user_id, user_name)

conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
# Getting a cursor from Database
cursor = conn.cursor()

cursor.execute(f"SELECT * FROM mydb.users WHERE id= {user_id}")

record = cursor.fetchall()

for row in record:
    id_from_db = row[0]
    name_from_db = row[1]

cursor.close()
conn.close()


def db_check(id_db, name_db):
    global db_status
    if id_db == user_id and name_db == user_name:
        db_status = 1
    return db_status


driver = webdriver.Chrome(
    service=Service("C:\\Users\\prath\\.cache\\selenium\\chromedriver\\win64\\126.0.6478.62\\chromedriver.exe"))
driver.get(f"http://127.0.0.1:5001/users/get_user_data/{user_id}")
element = driver.find_element(By.ID, value='user')
time.sleep(10)
db_test = db_check(id_from_db, name_from_db)

if res.status_code == 200 and res.json().get("user_name") == user_name and db_test == 1 and element.text == user_name:
    print("User creation test succeeded")
else:
    print("User creation test failed")
