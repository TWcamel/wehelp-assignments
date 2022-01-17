from flask import Flask, request, json, jsonify, url_for, redirect
import lib.json_lib as jb
import lib.member_lib as mb


app = Flask(__name__, static_url_path='')
# app = Flask(__name__, static_url_path='', static_folder='../frontend/static')


@app.route("/")
def run():
    return "{\"message\":\"You are now at lading page\"}"


@app.route("/signin", methods=["POST"])
def signIn():
    data = request.json
    member_check_code = mb.check_member(user=data)["status_code"]
    if member_check_code == 1:
        return redirect(url_for('member_signin'))
    elif member_check_code == 0:
        return redirect(url_for('error_signin', error_message="wrong_account_or_pwd"))
    elif member_check_code == -1:
        return redirect(url_for('error_signin', error_message="empty_input"))


@app.route("/member")
def member_signin():
    return jsonify({"message": "恭喜您，成功登入系統 🙂"})


@app.route("/error/<error_message>")
def error_signin(error_message):
    if error_message == "wrong_account_or_pwd":
        return jsonify({"message": "帳號或密碼錯誤，請重新輸入 😢"})
    elif error_message == "empty_input":
        return jsonify({"message": "請輸入帳號密碼 😥"})


if __name__ == "__main__":
    app.run(debug=True, port=int("5000"), host='0.0.0.0')
