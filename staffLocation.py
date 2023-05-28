#!/bin/env python3

from flask import Flask, jsonify, render_template, request
from getLinuxUserLocation import getLocation
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/server1', methods=["POST"])
def server1():
    text = getLocation.show(host='localhost', user='coder', port=22)
    return jsonify(result=text)

@app.route('/server2', methods=["POST"])
def server2():
    text = getLocation.show(host='localhost', user='coder', port=1022, debug=True, old=True)
    return jsonify(result=text)

@app.route("/", defaults={"js": "server1"})
@app.route("/<any(server1, server2):js>")
def index(js):
    return render_template(f"{js}.html", js=js)

if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 8080), app)
    http_server.serve_forever()
