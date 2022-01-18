from flask import Flask, request, json, jsonify, url_for, redirect, session
import lib.json_lib as jb
import lib.member_lib as mb
import os


app = Flask(__name__, static_url_path='')
app.secret_key = os.urandom(24).hex()


@app.route("/")
def index():
    if 'username' in session:
        return redirect(url_for('app_run'))
    return redirect(url_for('signin'))
    # return app.send_static_file('index.html')


@app.route("/signin", methods=["POST"])
def signin():
    member_check_code = mb.check_member(user=request.json)["status_code"]
    # print("123")
    if member_check_code == 1:
        session['username'] = request.json["username"]
        return redirect(url_for('app_run'))
    elif member_check_code == 0:
        return redirect(url_for('error_signin', error_message="wrong_account_or_pwd"))
    elif member_check_code == -1:
        return redirect(url_for('error_signin', error_message="empty_input"))


@app.route("/member")
def app_run():
    if 'username' in session:
        return jsonify({"message": "恭喜您，成功登入系統 🙂"})
    return redirect(url_for('index'))


@app.route("/error/<error_message>")
def error_signin(error_message):
    if error_message == "wrong_account_or_pwd":
        return jsonify({"message": "帳號或密碼錯誤，請重新輸入 😢"})
    elif error_message == "empty_input":
        return jsonify({"message": "請輸入帳號密碼 😥"})


@app.route("/signout", methods=["GET"])
def signout():
    session.pop('username', None)
    return jsonify({"message": "您已經成功登出系統 🚲"})
    # return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=int("5000"), host='0.0.0.0')
