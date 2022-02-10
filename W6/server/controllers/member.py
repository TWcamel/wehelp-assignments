from flask import Blueprint, render_template, redirect, request, abort, session
from jinja2 import TemplateNotFound
import model.member as mb

web_app_member = Blueprint("web-app-member", __name__,
                           template_folder="../client")


@web_app_member.route('/member')
def member():
    try:
        return "{messages: [{'text': 'Hello, world!'}]}", 200
    except TemplateNotFound:
        abort(404)


@web_app_member.route('/signup', methods=["POST"])
def member_signup():
    form = request.form.to_dict(flat=False)
    res = mb.check_and_add_membership(
        form["name"][0], form["account"][0], form["pwd"][0]
    )
    if res:
        msg = "帳號已經被註冊"
        session["user_status"] = "not_login"
        return redirect(f"/error/?err_msg={msg}")
    return redirect('/')
