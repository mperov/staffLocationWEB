#!/bin/env python3

from flask import Flask, jsonify, render_template, request
from getLinuxUserLocation import getLocation
import time

app = Flask(__name__)

@app.route('/add', methods=["POST"])
def add():
    text = getLocation.show(host='localhost', user='coder', port=22, debug=True)
    return jsonify(result=text)

@app.route('/')
def index():
    return render_template('plain.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
