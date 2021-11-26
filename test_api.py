#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# imports
###

import requests
import sys

###
# main
###

url = 'http://127.0.0.1:5000'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'x-api-key': ''
}

def main():

    with open('api.key', 'r') as apikey:
        key = apikey.read().replace('\n', '')
    headers['x-api-key'] = key

    data = {'a': 40,'b':30}
    r = requests.post(url + '/get_stl',headers=headers,data=data)
    print(r.status_code, r.reason)

###
# run
###

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)
