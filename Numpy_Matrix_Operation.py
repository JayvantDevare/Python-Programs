#Matrix operation using Numpy
#Numpy - NumPy is a package for scientific computing
#which has support for a powerful N-dimensional array object.
#How to install Numpy
#Option 1. open command prompt
#1.1 use command  =  pip install numpy
#Option 2. Download and install Anacoda on windows
#import numpy for using functionalities of numpy

#import numpy library
import numpy as np

#matrix 1
m1=np.array([[1,2,3],[1,2,3],[1,2,3]])

#matrix 2
m2=np.array([[11,22,33],[21,22,23],[31,12,23]])

print("\n Matrix 1\n")
print(m1)

print("\n Matrix 2\n")
print(m2)

#addition of two matrices
m3=m1+m2

print("\n Resulted Addition Matrix \n")
print(m3)


#Multiplication of two matrices
m3=m1.dot(m2)

print("\n Resulted Multiplication Matrix \n")
print(m3)

#Transpose of  matrix
print("\n Resulted Transpose Matrix of m1 \n")
print(m1.transpose())


