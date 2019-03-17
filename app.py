from rap import mainFunction
from poetry import poetryFunction
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Go to /api/rap/Insert String that you want raps to '


@app.route("/api/rap/<phrase>")
def hello(phrase):
    return mainFunction(phrase)


@app.route("/api/poetry/<lines>")
def poetry(lines):
    return poetryFunction(lines)


if __name__ == '__main__':
    app.run()
