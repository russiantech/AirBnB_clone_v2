#!/usr/bin/python3

"""
Our  Flask web application.

Our app listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'

"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():

    """ Hello HBNB! app """

    return "Hello HBNB!"


if __name__ == "__main__":

    app.run(host="0.0.0.0")
