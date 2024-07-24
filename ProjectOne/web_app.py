from random import randint
from flask import Flask

from ProjectOne.db_connector import get_user_name_from_db

app = Flask(__name__)


# using default
@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    # user_name=get_user_name_from_db(user_id)

    user_name= get_user_name_from_db(user_id)
    if user_name is None:
        return "<H1 id='error'>No such user!</H1>"
    else:
        return "<H1 id='user'>" + user_name + "</H1>"



# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', port=5001)
