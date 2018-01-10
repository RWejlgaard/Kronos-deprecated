from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


def launch():
    app.run(__name__)
