from __future__ import division  
import os
import sys
import math
from util_tool import *

reload(sys)   
sys.setdefaultencoding('utf-8')

def transfer_vocabulary(path):
	files = search_directory(path,'dat')
	# total page in all sample text
	total_page = len(files)
	for input_name in files:
		lines = open(input_name,"r")
		vocabulary = []
		vocabulary_file = input_name.replace('dat','voc');
		vocabulary_handle = open(vocabulary_file,'w')
		for line in lines:
			words = line.split()
			for word in words:
				vocabulary.append(word)

		vocabulary_no = 0;
		# get rid of repeat word
		vocabulary_back = vocabulary;
		vocabulary_len = len(vocabulary)
		vocabulary = set(vocabulary)
		for word in vocabulary:
			vocabulary_no = vocabulary_no + 1;
			tf_value = compute_tf(vocabulary_back,vocabulary_len,word)
			idf_value,count_word_in_page = compute_idf(path,total_page,word)
			tf_idf_value = round(tf_value * idf_value,4)
			separator = "\t"
			vocabulary_handle.write(
					word + separator + 
					str(vocabulary_no) + separator + 
					str(total_page) + separator + 
					str(count_word_in_page) + separator + 
					str(tf_value) + separator + 
					str(idf_value) + separator +
					str(tf_idf_value) + "\n"
					)

		vocabulary_handle.close()
		lines.close()

def compute_tf(vocabulary,vocabulary_len,word):
	count = 0
	for w in vocabulary:
		if w == word:
			count += 1
	return round(count/vocabulary_len,4)

def count_word_in_pages(path,word):
	count = 0
	# to be optmized, it's low efficiency
	files = search_directory(path,'dat')
	for input_name in files:
		lines = open(input_name,"r")
		for line in lines:
			words = line.split()
			find = False
			for w in words:
				if w == word:
					count += 1
					find = True
					break
			if find:
				break
	return count

def compute_idf(path,total_page,word):
	count_page = count_word_in_pages(path,word)	
	return round(math.log(total_page/count_page,2),4),count_page 

transfer_vocabulary("./text")

