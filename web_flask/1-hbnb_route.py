#!/usr/bin/python3
"""
Script for creating a web application(flask) with two routes
"""
from flask import Flask

app = Flask(__name__)

#route to display 'Hello HBNB!'
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


#route to display 'HBNB'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)