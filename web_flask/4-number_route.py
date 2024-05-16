#!/usr/bin/python3
"""Is it a number?
"""
from flask import Flask
from os import environ

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.route('/', strict_slashes=False)
def index():
    """Test method to output simple greeting on localhost port 5000,
    `/` path.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Test method to output simple message on localhost port 5000,
    `/hbnb` path.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_subpath(text):
    """Test method to output simple message on localhost port 5000,
    `/c/` path, converting subpaths into message text.
    """
    return ' '.join(['C', text.replace('_', ' ')])


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_subpath(text='is cool'):
    """Test method to output simple message on localhost port 5000,
    `/python/` path, converting subpaths into message text, with
    a default string.
    """
    return ' '.join(['Python', text.replace('_', ' ')])


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Test method to output simple message on localhost port 5000,
    `/number/` path, only if subpath is an integer.
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
