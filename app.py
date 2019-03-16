from bot import mainFunction
from flask import Flask
yezzir = Flask(__name__)


@yezzir.route("/api/rap/<phrase>")
def hello(phrase):
    return mainFunction(phrase)


if __name__ == '__main__':
    yezzir.run()
