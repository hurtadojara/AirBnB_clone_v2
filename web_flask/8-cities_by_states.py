#!/usr/bin/python3
'''comentarios'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states_list():
    """'/cities_by_states': 'Display a HTML page: (inside the tag BODY)'"""
    return render_template('8-cities_by_states.html', sts=storage.all("State"))


@app.teardown_appcontext
def use_teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
