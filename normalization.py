from __future__ import division  
import os
import sys
import math
from util_tool import *

reload(sys)   
sys.setdefaultencoding('utf-8')

sample_flag = 0

def transfer_vocabulary(path):
	files = search_directory(path,'dat')
	# total page in all sample text
	total_page = len(files)
	sample_word = []
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
		vocabulary_list = []
		for word in vocabulary:
			vocabulary_no = vocabulary_no + 1;
			tf_value = compute_tf(vocabulary_back,vocabulary_len,word)
			idf_value,count_word_in_page = compute_idf(path,total_page,word)
			tf_idf_value = round(tf_value * idf_value,4)
			# sort first in cache
			tmp = [word,vocabulary_no,total_page,count_word_in_page,tf_value,idf_value,tf_idf_value]
			vocabulary_list.append(tmp)
		vocabulary_list = sorted(vocabulary_list,key = lambda x:x[6],reverse=True)
		
		# and then write file
		separator = "\t"
		for voc in vocabulary_list:
			vocabulary_handle.write(
					voc[0] + separator + 
					str(voc[1]) + separator + 
					str(voc[2]) + separator + 
					str(voc[3]) + separator + 
					str(voc[4]) + separator + 
					str(voc[5]) + separator +
					str(voc[6]) + "\n"
					)
		# top 10 word as sample
		n = 10
		topN = vocabulary_list[0:n]
		for data in topN:
			sample_word.append(data[0])
		vocabulary_handle.close()
		lines.close()
	if sample_flag:
		sample_file = path + '/sample.dat'
		sample_handle = open(sample_file,'w')
		sample_word = set(sample_word)
		sample_handle.write(" ".join(sample_word))
		sample_handle.close()

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

