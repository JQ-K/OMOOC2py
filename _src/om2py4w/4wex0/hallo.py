#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
@route('/')
def index():
	return 'Hallo World!'
run(host='127.0.0.1', port=8082,reloader=True)

