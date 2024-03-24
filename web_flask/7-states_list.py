#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of State objects"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=attrgetter('name'))

    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)