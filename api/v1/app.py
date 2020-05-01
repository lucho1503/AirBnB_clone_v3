#!/usr/bin/python3
""" create a application with flask """

import os
from flask import Flask, Blueprint, jsonify, abort
from models import storage
from api.v1.views import app_views
from werkzeug.exceptions import HTTPException
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.url_map.strict_slashes = False

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r'/*': {'origin': host}})


@app.teardown_appcontext
def close_app(exception):
    """ close the app """
    storage.close()


@app.errorhandler(404)
def handle_error_404(exception):
    """ return a 404 page JSON """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """ run the app """
    app.run(host=host, port=port, threaded=True)
