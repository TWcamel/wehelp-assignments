import db.db as db
import os
from controller.home import web_app
from flask import Flask
from time import time


app = Flask(
    __name__,
    static_folder="../client",
    static_url_path='/'
)

app.secret_key = str(time())
app.register_blueprint(web_app)

db.run_db()

if __name__ == "__main__":
    app.run(debug=True, port=int("3000"), host='0.0.0.0')
