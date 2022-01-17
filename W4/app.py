from flask import Flask

app = Flask(__name__, static_url_path='')
# app = Flask(__name__, static_url_path='', static_folder='../frontend/static')


@app.route("/")
def run():
    return "{\"message\":\"Hello World 222\"}"


if __name__ == "__main__":
    app.run(debug=True, port=int("5000"), host='0.0.0.0')
