#!/usr/bin/python3
""" create a application with flask """

import os
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

host = os.getenv("HBNB_API_HOST", "0.0.0.0")
port = os.getenv("HBNB_API_PORT", 5000)

app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def close_app(exception):
    """ close the app """
    storage.close()


if __name__ == "__main__":
    """ run the app """
    app.run(host=host, port=port, threaded=True)
