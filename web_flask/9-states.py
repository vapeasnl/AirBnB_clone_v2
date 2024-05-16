#!/usr/bin/python3
"""States and State
"""
from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.teardown_appcontext
def states_list_teardown(self):
    """ Ensures SQLAlchemy session opened to serve dynamic content for HTML
    templates is closed after serving.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Requests list of `State`s ordered by name, which populates HTML
    template served to '/cities_by_states'.
    """
    return render_template('9-states.html', id=id,
                           states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
