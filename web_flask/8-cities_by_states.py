#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_():
    """display the states and cities listed in alphabetical order"""
    states_ = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states_)


@app.teardown_appcontext
def teardown_db(self):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    """.`"""
    app.run()
