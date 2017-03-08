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
	total = 0
	for from_line in handle_froms:
		from_data = from_line.split()
		handle_tos = open(vec_file,'r')
		for to_line in handle_tos:
			to_data = to_line.split()
			if from_data[0] == to_data[0]:
				continue
			if from_data[0].split('/')[2][0:7] == to_data[0].split('/')[2][0:7]:
				total += 1
			# the first element is file name, skip it
			len_from_data = len(from_data) - 1
			len_to_data = len(to_data) - 1
			from_vec = transfer_vec(from_data[1:len_from_data])
			to_vec = transfer_vec(to_data[1:len_to_data])
			cosine_value = compute_cosine_value(from_vec,to_vec)
			tmp = [from_data[0],to_data[0],cosine_value]
			result_list.append(tmp)

	accuracy_count = 0
	result_list = sorted(result_list,key=lambda x:x[2],reverse=True)
	for result in result_list:

		if result[0].split('/')[2][0:7] == result[1].split('/')[2][0:7] and result[2] > 0:
			accuracy_count += 1

	accuracy_rate = round(round(float(accuracy_count) / float(total),4) * 100 ,4) 
	handle_final.write("total: "  + str(total) + " accuracy_count: " + str(accuracy_count) + " accuracy_rate: " + str(accuracy_rate) + "%\n")
	for result in result_list:
		handle_final.write(result[0] + "\t" + result[1] + "\t" + str(result[2]) + "\n")

	handle_final.close()

def transfer_vec(vec):
	# conver string to int
	vec = [ int (vec) for vec in vec if vec ]
	# conver array to vector, if not do this, TypeError: can't multiply sequence by non-int of type 'list'
	vec = numpy.array(vec)
	return vec

def compute_cosine_value(vec_a,vec_b):
	#	cos(a,b)=a*b/(|a|+|b|)
	numerator = numpy.sum(vec_a*vec_b) 
	denominator = float(numpy.sqrt(sum(numpy.square(vec_a))) * numpy.sqrt(sum(numpy.square(vec_b))))
	if 0 == denominator:
		return 0
	theta = round(numerator / denominator,4)
	return theta

#categorization_file("./text/C00000810.vec")
categorization_files("./text")

