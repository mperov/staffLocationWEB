#!/bin/env python3

from flask import Flask, jsonify, render_template, request
from getLinuxUserLocation import getLocation
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/location/server1', methods=["POST"])
def server1():
    text = getLocation.show(host='localhost', user='coder', port=22)
    return jsonify(result=text)

@app.route('/location/server2', methods=["POST"])
def server2():
    text = getLocation.show(host='localhost', user='coder', port=1022, debug=True, old=True)
    return jsonify(result=text)

@app.route("/location/", defaults={"js": "server1"})
@app.route("/location/<any(server1, server2):js>")
def index(js):
    return render_template("/location/" + f"{js}.html", js=js)

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    http_server.serve_forever()
