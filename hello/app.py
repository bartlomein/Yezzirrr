from bot import mainFunction
from flask import Flask
my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return 'Hello World!'


@my_awesome_app.route("/api/rap/<phrase>")
def hello(phrase):
    return mainFunction(phrase)


if __name__ == '__main__':
    my_awesome_app.run()
