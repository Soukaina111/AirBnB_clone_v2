#!/usr/bin/python3
""" Let's get started with Flask"""

from flask import Flask

app = Flask(__name__)

@app.route("/",strict_slashes=False)
def hello_world():
    """ hello HBNB"""
    return "Hello HBNB!"

@app.route("/hbnb",strict_slashes=False)
def hello_world2():
    """ hello 2"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Text with spaces"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
