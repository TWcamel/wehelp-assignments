from flask import Blueprint, render_template, redirect, request, abort, session
from jinja2 import TemplateNotFound
import model.member as mb
import util.json_response as js

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


@web_app_member.route('/api/members', methods=["GET"])
@js.json_response
def get_member_info():
    path_param = request.args.to_dict(flat=False)

    res = None

    if 'username' in path_param:
        _data = mb.query_membership(next(iter(path_param["username"])))

        if _data:
            (id, name, username) = _data
            res = {
                "id": id,
                "name": name,
                "username": username
            }

    return {"data": res}


@web_app_member.route('/api/member', methods=["POST"])
def update_member_name():
    header_content_type = request.headers.get("Content-Type", None)

    # TODO: client side redering error page
    if header_content_type != "application/json":
        msg = "請確認 Content-Type 是 application/json"
        session["user_status"] = "未登入"
        return redirect(f"/error/?err_msg={msg}")

    body_info = request.get_json()

    # TODO: client side redering error page
    if "name" not in body_info:
        msg = "請確認 name 欄位是否有正確輸入"
        return redirect(f"/error/?err_msg={msg}")

    # TODO: check membership before update
    affected_rows = mb.update_membership_name(body_info['name'], 'test')

    res_key = "error"

    if affected_rows > 0:
        res_key = "ok"

    return {res_key: True}
