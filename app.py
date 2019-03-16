from bot import mainFunction
from flask import Flask
app = Flask(__name__)


@app.route("/api/rap/<phrase>")
def hello(phrase):
    return mainFunction(phrase)


if __name__ == '__main__':
    yezzir.run()
