#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    if '_' in text:
        content = text.replace('_', ' ')
    else:
        content = text
    return "C " + content

if __name__ == "__main__":
    app.run(host="0.0.0.0")
