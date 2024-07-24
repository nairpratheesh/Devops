import datetime

import pymysql

schema_name = "mydb"


# Establishing a connection to DB


# Getting all data from table “users”

def get_user_name_from_db(user_id):
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
    # Getting a cursor from Database
    print("query is", "SELECT name FROM mydb.users where id=", {user_id})
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT name FROM mydb.users where id= {user_id}")
        record = cursor.fetchone()[0]
    except:
        record=None
    cursor.close()
    conn.close()
    return record


def create_new_user(user_id, user_name):
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
    # Getting a cursor from Database
    cursor = conn.cursor()
    # Inserting data into table
    print("inside create user", user_id, user_name)
    try:
        row = cursor.execute(
            f"INSERT into mydb.users (id, name,creation_date) VALUES ({user_id}, '{user_name}', '{datetime.datetime.now()}')")
        cursor.close()
        conn.commit()
        conn.close()
        return row
    except:
        row = 0
        return row


def update_user_name(user_id, user_name):
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
    # Getting a cursor from Database
    cursor = conn.cursor()
    # Inserting data into table
    try:
        status = cursor.execute(f"update mydb.users set name='{user_name}' where id={user_id}")
        cursor.close()
        conn.commit()
        conn.close()
        return status
    except:
        status = 0
        return status


def delete_user_name(user_id):
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
    # Getting a cursor from Database
    cursor = conn.cursor()
    # Inserting data into table
    print("inside delete user", user_id)
    # cursor.execute(f"delete from mydb.users where id=100)")
    # cursor.execute(f"select * from mydb.users where id=100)")
    status=cursor.execute(f"DELETE FROM {schema_name}.users WHERE id ={user_id}")
    print("Status", status)
    cursor.close()
    conn.commit()
    conn.close()
    return status
