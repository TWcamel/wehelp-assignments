import db.db as db
from controllers.home import web_app
from controllers.member import web_app_member
from controllers.error import web_app_error
from flask import Flask
from time import time

app = Flask(
    __name__,
    static_folder="../client",
    static_url_path='/'
)

app.secret_key = str(time())
app.register_blueprint(web_app)
app.register_blueprint(web_app_member)
app.register_blueprint(web_app_error)

if __name__ == "__main__":
    app.run(debug=True, port=int("3000"), host='0.0.0.0')
