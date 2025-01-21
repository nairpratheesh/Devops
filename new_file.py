from flask import Flask

app = Flask(__name__)

@app.route("/content")
def content():
    f=open("write.txt",'r')
    return 'content is '+f.readline()
@app.route("/register")
def register():

    return 'success 201'
@app.route('/')
def hello():
    return 'Hello, World!'
app.run(host='127.0.0.1', debug=True, port=30000)