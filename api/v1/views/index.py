#!/usr/bin/python3
""" index """

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ returns a JSON """
    return jsonify({"status": "OK"})~
