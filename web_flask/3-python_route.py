#!/usr/bin/python3

"""
Flask web application.
The app listens on 0.0.0.0, port 5000.
Routes:
    /: Returns 'Hello HBNB!'.
    /hbnb: Returns 'HBNB'.
    /c/<text>: Returns 'C' followed by the value of <text>.
    /python/(<text>): Returns 'Python' followed by the value of <text>.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):

    """
    Returns 'C' followed by the value of <text>.

    Replace any '_' in <text> with '-'.
    """

    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Returns 'Python' followed by the value of <text>.

    Replace any '_' in <text> with '-'.
    """

    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
