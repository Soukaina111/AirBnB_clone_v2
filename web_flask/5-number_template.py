#!/usr/bin/python3
""" Let's get started with Flask"""

from flask import Flask, render_template

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

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def c2(text):
    """ Text2 with spaces"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('number_template.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
