#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template, g
from models import storage

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


@app.route('/python', strict_slashes=False)
def python():
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python1(text="is cool"):
    if '_' in text:
        content = text.replace('_', ' ')
    else:
        content = text
    return "Python " + content


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        num = "even"
    else:
        num = "odd"
    return render_template("6-number_odd_or_even.html", n=n, num=num)


@app.route('/states_list', strict_slashes=False)
def states_list():
    stuff = list(storage.all("State").values())
    stuff.sort(key=lambda thing: thing.name)
    return render_template("7-states_list.html", storage=stuff)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = list(storage.all("State").values())
    states.sort(key=lambda thing: thing.name)
    cities = list(storage.all("City").values())
    cities.sort(key=lambda thing: thing.name)
    return render_template("8-cities_by_states.html",
                           states=states,
                           cities=cities)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
