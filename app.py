from flask import Flask
from flask import jsonify
from flask import url_for

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def app_run():
	return app.send_static_file('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run()
