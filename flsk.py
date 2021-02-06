from flask import Flask

#used to handle incoming web requests and send responses
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'