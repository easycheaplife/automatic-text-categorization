# encoding=utf-8
import os
import sys
import math
from util_tool import *
import numpy
from numpy import *
from numpy import linalg as la

test = [[1,1],[7,7]]
U,Sigma,VT = la.svd(test)
print U
print Sigma
print VT

def print_mat(in_mat,thresh = 0.0):
	for i in range(shape(in_mat)[0]):
		for j in range(shape(in_mat)[1]):
			print float(in_mat[i,j]),
		print ''

def categorization_file_svd(vec_file):
	handle_vec = open(vec_file,'r')	
	feather_vec = []
	for line in handle_vec:
		vec = line.split()
		vec = vec[1:]
		vec = [ int (vec) for vec in vec if vec ] 
		feather_vec.append(vec)	
	feather_vec = numpy.array(feather_vec)
	print mat(feather_vec)
	print shape(mat(feather_vec))
	U,Sigma,VT = la.svd(mat(feather_vec))
	Sigma2 = Sigma**2
	print sum(Sigma2) * 0.9
	print sum(Sigma2[:25])
	numSV = 25
	print U
	print VT
	
	'''
	Sigma4 = mat(zeros((numSV,numSV)))
	for k in range(numSV):
		Sigma4[k,k] = Sigma[k]
	reconMat = mat(feather_vec).T * U[:,:numSV] * Sigma4.I
	print shape(mat(feather_vec).T)
	print shape(U[:,:numSV])
	print shape(Sigma4.I)
	print shape(reconMat.T)
	print_mat(reconMat,0.5)
	'''

	'''
	Sigma4 = mat(eye(numSV)*Sigma[:numSV])
	reconMat = U[:,:numSV] * Sigma4 * VT[:numSV,:]
	print shape(U[:,:numSV])
	print shape(Sigma4)
	print shape(VT[:numSV,:])
	'''
categorization_file_svd("./text/C00000810.vec")

