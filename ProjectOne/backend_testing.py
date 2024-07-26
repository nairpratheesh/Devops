import pymysql
import requests

db_check_status = 0
result = 0
schema_name = 'mydb'
user_name = "test35"
user_id = 35


def back_testing(id, name):
    print("from back_testing", user_id, user_name)
    url_str = f'http://127.0.0.1:5000/users/{user_id}'
    print("connecting to rest app")
    requests.post(url_str, json={"user_name": user_name})
    print("connected  to rest app",url_str)
    return requests.get(url_str)

res = back_testing(user_id, user_name)
conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
# Getting a cursor from Database
cursor = conn.cursor()
print("Connection to db established")
exect=cursor.execute(f"SELECT * FROM mydb.users WHERE id= {user_id}")
print("select query executed")
record = cursor.fetchall()

for row in record:
    id_from_db = row[0]
    name_from_db = row[1]

# cursor.close()
conn.close()


def db_check(id_db, name_db):
    global db_status
    if id_db == user_id and name_db == user_name:
        db_status = 1
    return db_status


# id_from_db=resp.
# name_from_db = cursor.fetchone()[1]
# print(id_from_db, name_from_db)


db_test = db_check(id_from_db, name_from_db)
if res.status_code == 200 and res.json().get("user_name") == user_name and db_test == 1:
    print("User creation test succeeded")
else:
    print("User creation test failed")
