from flask import Blueprint, render_template, redirect, request, session, abort
from jinja2 import TemplateNotFound

web_app = Blueprint("web_app", __name__, template_folder="../client")


@web_app.route('/', defaults={'page': 'index'})
def home(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)
