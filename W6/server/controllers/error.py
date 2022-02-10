from flask import Blueprint, render_template, redirect, request, abort
from jinja2 import TemplateNotFound
import asyncio

web_app_error = Blueprint("web_app_error", __name__,
                          template_folder="../client")


@web_app_error.route('/error/', defaults={'page': 'login-error'})
def error(page):
    error_message = request.args.get('err_msg')
    try:
        return "{messages: [{'text': 'Hello, error!'}]}", 200
    except TemplateNotFound:
        abort(404)


