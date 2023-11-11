# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS
from data import playground, disability


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources={r"/api/*": {"origins": "http://localhost"}})


@app.route('/api/playground')
def get_data():
    return jsonify(playground())

@app.route('/api/disability')
def get_item():
    return jsonify(disability())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)


