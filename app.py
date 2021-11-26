#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# REST API for health hackathon
# Title: REST API in python for creating STL files by request
# Author: Vojtěch Petrásek
# Generated: 26/11/2021 11:23:18
##################################################

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

def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        with open('api.key', 'r') as apikey:
            key = apikey.read().replace('\n', '')
        # if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

@app.route('/', methods=['GET'])
def home():
    return "<h1>Czech team - Health hackathon Zürich 2021</h1>"

@app.route('/get_stl', methods=['POST'])
@require_appkey
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