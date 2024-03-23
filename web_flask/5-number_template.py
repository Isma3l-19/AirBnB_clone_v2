#!/usr/bin/python3
"""
script using Flask to create a web application with the specified routes
"""
from flask import Flask, render_template

app = Flask(__name__)


#route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


#route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


#route to display c followed by a text
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f'C {text}'


#route to display python followed by text(is cool)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f'Python {text}'


#Checks if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


# Route to display a HTML page if n is an integer
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', number=n)
    else:
        return 'Not an integer!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
