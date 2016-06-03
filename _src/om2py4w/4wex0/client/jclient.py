#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests #requests 使用说明http://docs.python-requests.org/en/master/
from bs4 import BeautifulSoup #beautifulsoup :https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

def main():
	print 'Type "q" or "quit" to exit.'
	print 'Type "l" or "list" to view all the notes.'
	print 'Type anything else as a new note.'

	while True:
		INPUT = raw_input('$ ').strip()#$是输入前的指示符，strip（）消除字符两端的空格
		inp = 	INPUT.lower()#大写转小写
		if inp in ['quit','q']:#设置关键词
			break
		elif inp in ['list','l']:#设置关键词
			print listnotes()
		else:
			addnote(INPUT)


def addnote(note):
	requests.post('http://localhost:8080/note', data = {'newnote':note})
	print 'note added!'

def listnotes():
	r = requests.get('http://localhost:8080/note')
	soup = BeautifulSoup(r.text, 'html.parser')
	lis = soup.find_all('p')
	notes = ''
	for i in lis:
		notes += i.get_text()+'\n'
		return notes

if __name__ == '__main__':
	main()
		
