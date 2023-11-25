#!/usr/bin/python3

"""
Flask web application.
listens on 0.0.0.0, port 5000.
Routes:
    /:Returns 'Hello HBNB!'.
    /hbnb: Returnss 'HBNB'.
    /c/<text>: Returnss 'C' followed by the value of <text>.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():

    """ Returns 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():

    """ Returnss 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):

    """ Returns 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
