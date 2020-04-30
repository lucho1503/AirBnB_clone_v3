#!/usr/bin/python3
# returns a JSON object

from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/status', methods=['GET'])
def status():
    """ return a json status """
    if request.method == 'GET':
        return jsonify({"status": "OK"})
