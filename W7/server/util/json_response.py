import functools
from flask import jsonify


def json_response(func):
    @functools.wraps(func)
    def inner(**kwargs):
        print(f"calling {func.__name__} function...")
        return jsonify(func(**kwargs))
    return inner
