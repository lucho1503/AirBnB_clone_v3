#!/usr/bin/python3
""" returns a JSON object """

from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ return a json status """
    if request.method == 'GET':
        return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """ retrieves the number of eacj object by type """
    if request.method == 'GET':
        res = {}
        classes = {"Amenity": "amenities", "City": "cities", "Place": "places",
                   "Review": "reviews", "State": "states", "User": "users"}
        for k, v in classes.items():
            res[v] = storage.count(k)
        return jsonify(res)
