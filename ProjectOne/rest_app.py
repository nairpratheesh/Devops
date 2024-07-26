from flask import Flask, request
import os
import signal

from ProjectOne.db_connector import get_user_name_from_db, create_new_user, update_user_name, delete_user_name

app = Flask(__name__)

# local users storage
users = {}
print("Rest app starting")

# for terminating rest api server when required
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'server stopped'


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':

        user_name = get_user_name_from_db(user_id)
        print("user name from rest api", user_name)
        return {'user_name': user_name}, 200  # status code

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        row = create_new_user(user_id, user_name)
        print("from rest app row")
        if row == 1:
            return {'user id': user_id, 'user name': user_name, 'status': 'created'}, 200  # status code

        else:

            return {'status': 'error', 'reason': 'id already exists'}, 500  # Error message
    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        status = update_user_name(user_id, user_name)

        if status == 1:
            return {'status': 'OK', 'user updated': user_name}, 200  # status
        elif status == 0:

            return {'status': 'error', 'reason': 'no such id'}, 500  # status
    elif request.method == 'DELETE':
        # request_data = request.json
        print("rest app before delete call user id is ", user_id)
        status = delete_user_name(user_id)
        print("stats from restapi", status)
        if status == 1:
            return {'status': 'OK', 'user deleted': user_id}, 200  # status
        else:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status


app.run(host='127.0.0.1', port=5000)
print("Rest app started2")
