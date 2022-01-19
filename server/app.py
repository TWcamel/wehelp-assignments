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
    elif member_check_code == 0:
        return redirect(url_for('error_signin', error_message="wrong_account_or_pwd"))
    elif member_check_code == -1:
        return redirect(url_for('error_signin', error_message="empty_input"))


@app.route("/member")
def app_run():
    if 'username' in session:
        # {"message": "恭喜您，成功登入系統 🙂"}, 200
        return app.send_static_file('member.html')
    return redirect(url_for('index'))


@app.route("/error/<error_message>")
def error_signin(error_message):
    if error_message == "wrong_account_or_pwd":
        # jsonify({"message": "帳號或密碼錯誤，請重新輸入"}), 401
        return app.send_static_file('login-fail.html')
    elif error_message == "empty_input":
        # jsonify({"message": "帳號、或密碼輸入錯誤"}), 401
        return app.send_static_file('login-empty.html')


@app.route("/signout", methods=["GET"])
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=int("3000"), host='0.0.0.0')
