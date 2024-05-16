#!/usr/bin/python3
"""Cities by states
"""
from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.teardown_appcontext
def states_list_teardown(self):
    """Ensures SQLAlchemy session opened to serve dynamic content for HTML
    templates is closed after serving.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Requests list of `State`s ordered by name, which populates HTML
    template served to '/cities_by_states'.
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
