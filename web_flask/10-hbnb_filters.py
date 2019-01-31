#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template, g
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = list(storage.all('State').values())
    states.sort(key=lambda thing: thing.name)
    cities = storage.all('City')
    cities.sort(key=lambda thing: thing.name)
    amenities = storage.all('Amenity')
    amenities.sort(key=lambda thing: thing.name)
    return render_template('10-hbnb_filters.html',
                           states=states,
                           cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
