#!/usr/bin/python3
"""
script using Flask to create a web application with three routes
"""
from flask import Flask, escape


app = Flask(__name__)


#Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


#Route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


#Route to display "C " followed by the value of the text variable
@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    processed_text = escape(text).replace('_', ' ')
    return f'C {processed_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)