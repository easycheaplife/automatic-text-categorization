# encoding=utf-8
import os
import sys
import math
from util_tool import *
import numpy

def categorization_files(path):
	files = search_directory(path,'vec')
	for input_name in files:
		categorization_file(input_name)

def categorization_file(vec_file):
	handle_froms = open(vec_file,'r')	
	final_file = vec_file.replace('vec','final')
	handle_final = open(final_file,'w')	
	for from_line in handle_froms:
		from_data = from_line.split()
		handle_tos = open(vec_file,'r')
		for to_line in handle_tos:
			to_data = to_line.split()
			cosine_value = compute_cosine_value(from_data,to_data)
			handle_final.write(from_data[0] + "\t" + to_data[0] + "\t" + str(cosine_value) + "\n")
		# compute only once, the same to them if using topic model for sample feather
		break
	handle_final.close()

def compute_cosine_value(vec_a,vec_b):
	# the first element is file name, skip it
	len_a = len(vec_a) - 1
	len_b = len(vec_b) - 1
	vec_a = vec_a[1:len_a]
	vec_b = vec_b[1:len_b]
	# conver string to int
	vec_a = [ int (vec_a) for vec_a in vec_a if vec_a ]
	vec_b = [ int (vec_b) for vec_b in vec_b if vec_b ]
	# conver array to vector, if not do this, TypeError: can't multiply sequence by non-int of type 'list'
	vec_a = numpy.array(vec_a)
	vec_b = numpy.array(vec_b)
	#	cos(a,b)=a*b/(|a|+|b|)
	numerator = numpy.sum(vec_a*vec_b) 
	denominator = float(numpy.sqrt(sum(numpy.square(vec_a))) * numpy.sqrt(sum(numpy.square(vec_b))))
	if 0 == denominator:
		return 0
	theta = round(numerator / denominator,4)
	return theta

#categorization_file("./text/C00000810.vec")
categorization_files("./text")

