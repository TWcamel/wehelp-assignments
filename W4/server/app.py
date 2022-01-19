from flask import Flask, request, json, jsonify, url_for, redirect, session
import lib.json_lib as jb
import lib.member_lib as mb
import os


app = Flask(__name__, static_url_path='', static_folder='../client')
app.secret_key = os.urandom(24).hex()


@app.route("/")
def index():
    if 'username' in session:
        return redirect(url_for('app_run'))
    return app.send_static_file('index.html')


@app.route("/signin", methods=["POST"])
def signin():
    form = request.form.to_dict(flat=False)
    member_check_code = mb.check_member(user=form)["status_code"]
    if member_check_code == 1:
        session['username'] = "username"
        return redirect(url_for('app_run'))
    elif member_check_code == -1:
        return redirect(url_for('error_signin', err_msg="請輸入帳號、密碼"))
    else:
        return redirect(url_for('error_signin', err_msg="帳號或密碼錯誤"))


@ app.route("/member")
def app_run():
    if 'username' in session:
        return app.send_static_file('member.html'), 200
    return redirect(url_for('index'))


@ app.route("/error/")
def error_signin():  # status code: 401 Unauthorized
    error_message = request.args.get('err_msg')
    if error_message == "請輸入帳號、密碼":
        return app.send_static_file('login-error.html'), 400
    elif error_message == "帳號或密碼錯誤":
        return app.send_static_file('login-error.html'), 401


@ app.route("/signout", methods=["GET"])
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=int("3000"), host='0.0.0.0')
