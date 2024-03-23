#!/usr/bin/python3
"""
creating three routes using flask
"""
from flask import Flask, escape

app = Flask(__name__)

#displaying 'Hello HBNB!'
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

#displaying HBNB
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return f'C {escape(text)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
