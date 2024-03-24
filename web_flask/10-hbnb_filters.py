#!/usr/bin/python3
"""
starts a web flask application
"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    amenities = storage.all(Amenity).values()
    states = storage.all(State).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    close the SQLAlchemy session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')