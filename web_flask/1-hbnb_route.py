#!/usr/bin/python3
"""0x04. AirBnB clone - Web framework, task 1. HBNB
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
