#!/usr/bin/python3
"""
let's get get started with Flask
"""

from flask import Flask, render_template
from models import *


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ shows listed states sorted """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
