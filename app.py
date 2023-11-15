from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/me')
def me():
    return 'I am Alejandro!'

@app.route('/ping')
def ping():
    return 'Pong'