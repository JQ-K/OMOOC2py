#/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import get, post, request, run, jinja2_view
#import sae.kvdb
from datetime import datetime
import jnote

@get('/note')
@jinja2_view('jnote.html')
def ShowPage():
	notes = jnote.GetNotes()
	return {'notes':notes}

@post('/note')
@jinja2_view('jnote.html')
def CreatNote():
	note = unicode(request.forms.get('newnote'),'utf-8')

	if note:
		jnote.NewNote(note)
	notes = jnote.GetNotes()

	return {'notes': notes}

run (host='127.0.0.1', port=8080, debug=True, reloader=True)
