#!/usr/bin/python3
'''HBNB'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    '''main route '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    '''hbnb route'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def txt_route(text):
    '''text route'''
    return "c {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    ''' Python Route '''
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
