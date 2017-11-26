import os
from http.client import OK

from flask import jsonify

from dokku_dashboard import app
from dokku_dashboard.dokku import list_apps


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"API": True}), OK.value


@app.route('/apps', methods=['GET'])
def apps():
    return jsonify({"apps": list_apps()}), OK.value


if __name__ == '__main__':
    app.run(debug=app.debug,
            host=os.environ.get('HOST', '0.0.0.0'),
            port=int(os.environ.get('PORT', 5000)))
