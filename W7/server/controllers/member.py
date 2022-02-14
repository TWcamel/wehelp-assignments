from flask import Blueprint, render_template, redirect, request, abort, session
from jinja2 import TemplateNotFound
import model.member as mb

web_app_member = Blueprint("web-app-member", __name__,
                           template_folder="../client")


@web_app_member.route('/member', defaults={'page': 'member'})
def member(page):
    if 'user' in session and session.get("user_status", "未登入") == "已登入":
        try:
            return render_template(f'{page}.html', user=session['user'])
        except TemplateNotFound:
            abort(404)
    return redirect("/")


@web_app_member.route("/signin", methods=["POST"])
def sign_in():
    form = request.form.to_dict(flat=False)
    res = mb.get_member(
        form["account"][0], form["pwd"][0]
    )
    if not res:
        msg = "帳號、或密碼輸入錯誤"
        session["user_status"] = "未登入"
        return redirect(f"/error/?err_msg={msg}")

    session["user_status"] = "已登入"
    session["user"] = res[0]

    return redirect("/member")


@web_app_member.route('/signup', methods=["POST"])
def signup():
    form = request.form.to_dict(flat=False)

    for key, value in form.items():
        if len(value[0].strip()) == 0:
            msg = f"{key} 欄位不可為空，請重新輸入"
            return redirect(f"/error/?err_msg={msg}")

    if mb.check_and_add_membership(form["name"][0], form["account"][0], form["pwd"][0]):
        msg = "帳號已經被註冊"
        session["user_status"] = "未登入"
        return redirect(f"/error/?err_msg={msg}")

    return redirect("/")


@web_app_member.route('/signout', methods=["GET"])
def sign_out():
    session["user_status"] = "未登入"
    session.pop("user", None)
    return redirect("/")