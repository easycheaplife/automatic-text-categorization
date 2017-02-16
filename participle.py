import os
import sys
import chardet
import jieba
import jieba.posseg as pseg
import HTMLParser
from util_tool import *

reload(sys)   
sys.setdefaultencoding('utf-8')

def test():
	# test code
	print sys.getfilesystemencoding()
	file_name = "text/C00002419.txt"
	chardet.detect(file_name)['encoding']
	file = open(file_name,"r")
	for line in file:
		print line.decode('cp936')
	file.close()

def transfer_text(path):
	files = search_directory(path,'txt')
	for input_name in files:
		lines = open(input_name,"r")
		output_file = input_name.replace('txt','dat');
		handle = open(output_file,'w')
		# debug flag
		debug = 0
		for line in lines:
			if 0 != len(line.strip()):
				if input_name == './text/C00002317.txt':
					debug = 1
				handle.write(filter_text(line.decode('cp936'),debug))
		handle.close()
		lines.close()

html_parser = HTMLParser.HTMLParser()
def filter_text(buf,debug):
	if debug:
		print buf
	# get rid of html escape character
	buf = html_parser.unescape(buf)
	buf = buf.strip()
	words = pseg.cut(buf)
	res = []
	part_of_speech = ['x','d','b','m','v','vn','u','t','uj','ul','c','p']
	for word, flag in words:
		if flag in part_of_speech:
			continue	
		res.append(word)	
	# get rid of repeat word
	res = set(res)
	return ' '.join(res)

transfer_text("./text")
