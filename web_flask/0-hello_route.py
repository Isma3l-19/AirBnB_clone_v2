#!/usr/bin/python3
"""
start a flask web application
"""
from flask import Flask


app = Flask(__name__)


# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    print output as 'Hello HBNB!'
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """
    run the flask app on 0.0.0.0, port 5000
    """
    app.run(host='0.0.0.0', port=5000)