#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# imports
###

import sys

import flask
from flask import request, abort
from functools import wraps

###
# main
###

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Czech team - Health hackathon Zürich 2021</h1>"

@app.route('/get_stl', methods=['POST'])
def get_stl():
    print('post')
    return '200'

###
# run
###

if __name__ == '__main__':
    try:
        app.run()
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)