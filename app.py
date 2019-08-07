from flask import Flask
import main
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getHR/<name>')
def user(name):
    print(name)
    varS = main.mMain(name)
    print(varS)
    jsonR = {
        "HR": "%s" % varS
    }
    return jsonR


if __name__ == '__main__':
    app.run()
