import functools
from flask import jsonify


def json_response(func):
    @functools.wraps(func)
    def inner(**kwargs):
        return jsonify(func(**kwargs))
    return inner


def json_response_with_cors(func):
    @functools.wraps(func)
    def inner(**kwargs):
        respose = jsonify(func(**kwargs))
        respose.headers.add('Access-Control-Allow-Origin', '*')
        return respose
    return inner
