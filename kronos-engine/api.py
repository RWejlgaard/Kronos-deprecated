from flask import Flask
import os

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


def launch():
    app.run(__name__)
    os.fork()
    return
