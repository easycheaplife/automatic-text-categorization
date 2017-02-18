import os
import sys
import math
from util_tool import *

def generate_files(path):
	files = search_directory(path,'voc')
	for file_name in files:
		generate_file(path,file_name)


def generate_file(path,voc_file):
	feature_vector_file = voc_file.replace('voc','vec')
	feature_vector_handle = open(feature_vector_file,'w')

	files = search_directory(path,'voc')
	for file_name in files:
		'''
		if voc_file == file_name:
			continue
		'''
		feature_vector_val = [file_name]
		# open file again after using it!
		feature_lines = open(voc_file,"r")
		for feature_line in feature_lines:
			feature_data = feature_line.split()
			feature_word = feature_data[0]
			feature_word_no = feature_data[1]
			word_times = get_word_times(file_name,feature_word)
			feature_vector_val.append(str(word_times))
		feature_vector_handle.write("\t" . join(feature_vector_val) + "\n")

	feature_vector_handle.close()
	feature_lines.close()

def get_word_times(voc_file,word_query):
	lines = open(voc_file,"r")
	times = 0
	for line in lines:
		data = line.split()	
		word = data[0]
		if word == word_query:
			times += 1
	lines.close()
	return times

generate_file("./text","./text/C00000810.voc")
generate_files("./text")
