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

def main():
    print("hello world")

###
# run
###

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)
