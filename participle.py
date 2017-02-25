import os
import sys
import chardet
import jieba
import jieba.posseg as pseg
import jieba.analyse
import HTMLParser
from util_tool import *

reload(sys)   
sys.setdefaultencoding('utf-8')
html_parser = HTMLParser.HTMLParser()
jieba.analyse.set_stop_words("./stop_words.txt")

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
		part_file = input_name.replace('txt','part');
		handle = open(output_file,'w')
		part_handle = open(part_file,'w')
		for line in lines:
			if 0 != len(line.strip()):
				words = filter_text(line.decode('cp936'),part_handle)
				handle.write(' '.join(words))
		part_handle.close()
		handle.close()
		lines.close()

def filter_text(buf,file_handle):
	# get rid of html escape character
	buf = html_parser.unescape(buf)
	buf = buf.strip()
	buf = jieba.analyse.extract_tags(buf)
	buf = " ".join(buf)
	words = pseg.cut(buf)
	res = []
	part_of_speech = ['x','d','b','m','u','t','uj','ul','c','p']
	part_of_speech = ['n','v','vn']
	for word, flag in words:
		file_handle.write("" + word + " " + flag +  "\n")
		if flag not in part_of_speech:
			continue	
		res.append(word)	
	return res

transfer_text("./text")
