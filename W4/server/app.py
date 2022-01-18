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
    member_check_code=mb.check_member(user = form)["status_code"]
    if member_check_code == 1:
        session['username']="username"
        return redirect(url_for('app_run'))
    elif member_check_code == 0:
        return redirect(url_for('error_signin', error_message="wrong_account_or_pwd"))
    elif member_check_code == -1:
        return redirect(url_for('error_signin', error_message="empty_input"))


@ app.route("/member")
def app_run():
    if 'username' in session:
        return app.response_class(
            response = json.dumps({"message": "恭喜您，成功登入系統 🙂"}),
            status = 200,
            mimetype = 'application/json'
        )
    return redirect(url_for('index'))


@ app.route("/error/<error_message>")
def error_signin(error_message):
    if error_message == "wrong_account_or_pwd":
        return app.response_class(
            response = json.dumps({"message": "帳號或密碼錯誤，請重新輸入"}),
            status = 401,  # Unauthorized (401)
            mimetype = 'application/json'
        )
    elif error_message == "empty_input":
        return app.response_class(
            response = json.dumps({"message": "請輸入帳號密碼"}),
            status = 401,  # Unauthorized (401)
            mimetype = 'application/json'
        )


@ app.route("/signout", methods = ["GET"])
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug = True, port = int("5000"), host = '0.0.0.0')
