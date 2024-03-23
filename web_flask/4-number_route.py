#!/usr/bin/python3
"""
creating specified routes using flask web framework
"""
from flask import Flask, escape

app = Flask(__name__)

#route to dislpay 'Hello HBNB!'
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

#route to display 'HBNB'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

#route to display c followed by a text
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f'C {escape(text)}'

#route to display python followed by text(is cool)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'

#Checks if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
