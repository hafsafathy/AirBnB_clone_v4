#!/usr/bin/python3
"""
Flask
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid


app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def teardown_db(exception):
    """
    after all requests this method calls
    """
    storage.close()


@app.route('/0-hbnb/')
def hbnb_filters(the_id=None):
    """
    handles request to custom template with states, cities & amentities
    """
   stateObj = storage.all('State').values()
    states = dict([state.name, state] for state in stateObj)
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('1-hbnb.html',
                           states=states,
                           amens=amenities,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
