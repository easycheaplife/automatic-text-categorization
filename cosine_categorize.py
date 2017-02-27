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
		# compute only once, the same to them if using topic model for sample feather
		break

def categorization_file(vec_file):
	handle_froms = open(vec_file,'r')	
	final_file = vec_file.replace('vec','final')
	handle_final = open(final_file,'w')	
	result_list = []
	accuracy_count = 0
	for from_line in handle_froms:
		from_data = from_line.split()
		handle_tos = open(vec_file,'r')
		for to_line in handle_tos:
			to_data = to_line.split()
			if from_data[0] == to_data[0]:
				continue
			if from_data[0].split('/')[2][0:7] == to_data[0].split('/')[2][0:7]:
				print ("%s %s" % (from_data[0], to_data[0])) 
				accuracy_count += 1
			cosine_value = compute_cosine_value(from_data,to_data)
			tmp = [from_data[0],to_data[0],cosine_value]
			result_list.append(tmp)

	result_list = sorted(result_list,key=lambda x:x[2],reverse=True)
	accuracy_rate = round(round(accuracy_count / 90*89,4) / 100 ,4) 
	handle_final.write("total: "  + str(90*89) + " accuracy_count: " + str(accuracy_count) + " accuracy_rate: " + str(accuracy_rate) + "\n")
	for result in result_list:
		handle_final.write(result[0] + "\t" + result[1] + "\t" + str(result[2]) + "\n")

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

