#!/usr/bin/python3
""" create a new view for State taht handles all objects """

from api.v1.views import app_views
from flask import Flask, request, jsonify, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """ retrieves the list of all State objects """
    if request.method == 'GET':
        all_states = storage.all(State)
        all_states = list(key.to_dict() for key in all_states.values())
        return jsonify(all_states)

    if request.method == 'POST':
        r = request.get_json()
        if r is None:
            abort(400, 'Not a JSON')
        if r.get("name") is None:
            abort(400, "Missing name")
        new_state = State(**r)
        storage.new(new_state)
        storage.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def states_by_id(state_id):
    """ retrieves a state by id else handles the errors """
    obj_id = storage.get(State, state_id)
    if request.method == 'GET':
        if obj_id is None:
            abort(404, "Not found")
        return jsonify(obj_id.to_dict())

    if request.method == 'PUT':
        if obj_id is None:
            abort(404, "Not found")
        r = request.get_json()
        if r is None:
            abort(400, "Not a JSON")
        obj_id.update(r)
        return jsonify(obj_id.to_json())

    if request.method == 'DELETE':
        if obj_id:
            obj_id.delete()
            obj_id.save
            return jsonify({}), 200
        else:
            abort(404, "Not found")
