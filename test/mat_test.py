# encoding=utf-8
from numpy import *
from numpy import linalg as la
def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]
    
def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

data1 = loadExData()
print data1
data1 = mat(data1)
print data1
print 'col vector'
print data1[:,0]
print data1[:,4]

print data1[6:,]

def ecludSim(inA,inB):
    return 1.0/(1.0 + la.norm(inA - inB))

def pearsSim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5+0.5*corrcoef(inA, inB, rowvar = 0)[0][1]

def cosSim(inA,inB):
    num = float(inA.T*inB)
    denom = la.norm(inA)*la.norm(inB)
    return 0.5+0.5*(num/denom)

my_mat = data1
print ecludSim(my_mat[:,0],my_mat[:,4])
print ecludSim(my_mat[:,0],my_mat[:,1])

print pearsSim(my_mat[:,0],my_mat[:,4])
print pearsSim(my_mat[:,0],my_mat[:,1])

print cosSim(my_mat[:,0],my_mat[:,4])
print cosSim(my_mat[:,0],my_mat[:,1])

print 'shape test'
data2 = loadExData2()
print data2
data2 = mat(data2)
print data2
shape2 = shape(data2)
print shape2
for i in range(shape2[1]):
	print i

print 'logical_and test'
print logical_and(data2[:,1].A>0, data2[:,2].A>0)
print nonzero(logical_and(data2[:,1].A>0, data2[:,2].A>0))
U,Sigma,VT = la.svd(data2)
print "U"
print U
print "Sigma"
print Sigma
print 'VT'
print VT
Sigma2 = Sigma**2
print Sigma2
print sum(Sigma2*0.9)
print sum(Sigma2[:3])
print 'test eye'
print eye(4)
print Sigma2[:4]
Sig4 = eye(4)*Sigma2[:4]
print 'mat.I'
# matrix中.H,.A,.I代表共轭,转置,逆矩阵
print "Sig4"
print Sig4
print "mat(Sig4).I"
print mat(Sig4).I

print 'data2'
print data2
print 'data2.T'
print data2.T

print "U"
print U
print "U[:,:4]"
print U[:,:4]

print "data2.T * U[:,:4] * mat(Sig4).I"
print data2.T * U[:,:4] * mat(Sig4).I 
