#!/usr/bin/python3

"""

Flask web app.

Running on port 0.0.0.0, port 5000.
Routes:
    hello_hbnb(): returns 'Hello HBNB!'.
    hbnb(): returns 'HBNB'.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns 'Hello HBNB!' at /."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():

    """ returns 'HBNB' at /hbnb """

    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
