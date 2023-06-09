#!/bin/env python3

from flask import Flask, jsonify, render_template, request
from getLinuxUserLocation import getLocation
from waitress import serve
import inspect

app = Flask(__name__)

#DEBUG=True
DEBUG=False

@app.route('/location/server1', methods=["POST"])
def server1():
    if DEBUG:
        print(inspect.currentframe().f_code.co_name)
    text = getLocation.show(host='localhost', user='coder', filename='/home/runner/.ssh/id_rsa', port=22, debug=DEBUG)
    return jsonify(result=text)

@app.route('/location/server2', methods=["POST"])
def server2():
    if DEBUG:
        print(inspect.currentframe().f_code.co_name)
    text = getLocation.show(host='localhost', user='coder', filename='/home/runner/.ssh/id_rsa', port=1022, debug=DEBUG, old=True)
    return jsonify(result=text)

@app.route("/location/", defaults={"js": "server1"})
@app.route("/location/<any(server1, server2):js>")
def index(js):
    if DEBUG:
        print(inspect.currentframe().f_code.co_name)
    return render_template("/location/" + f"{js}.html", js=js)

if __name__ == '__main__':
    if DEBUG:
        app.run(host='0.0.0.0', port=8080)
    else:
        serve(app, host="0.0.0.0", port=8080)
