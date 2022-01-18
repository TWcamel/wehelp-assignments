from flask import Flask, jsonify, json

def print_and_jsonify(data):
    def decorator(func):
        def wrapper():
            print("data is " + format(data))
            func()
        return wrapper
    return decorator
