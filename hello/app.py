from bot import mainFunction
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/api/rap/<phrase>")
def hello(phrase):
    return mainFunction(phrase)


if __name__ == '__main__':
    app.run()
