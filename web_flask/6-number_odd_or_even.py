#!/usr/bin/python3
"""
script using Flask to create a web application with the specified routes
"""
from flask import Flask, render_template

app = Flask(__name__)

#route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


#route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

#route used to display C with a text
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


#route to display a HTML page if n is an integer and show if it's odd or even
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        return 'Not an integer!'


#oute to display a HTML page indicating if n is even or odd
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    if isinstance(n, int):
        parity = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, parity=parity)
    else:
        return 'Not an integer!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)