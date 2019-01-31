#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template, g
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    stuff = list(storage.all("State").values())
    stuff.sort(key=lambda thing: thing.name)
    return render_template("9-states.html", states=stuff)


@app.route('/states/<id>', strict_slashes=False)
def states1(id):
    state = None
    states = storage.all("State")
    for k, v in states.items():
        if v.id == id:
            state = v
    cities = list(storage.all("City").values())
    cities.sort(key=lambda thing: thing.name)
    return render_template("9-states.html",
                           id=id,
                           state=state,
                           cities=cities)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
