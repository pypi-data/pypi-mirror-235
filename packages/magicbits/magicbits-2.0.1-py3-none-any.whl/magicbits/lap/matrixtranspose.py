import numpy as np

m  = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix : \n",m, end='\n\n')

num = 4
scalarmult = num*m # Scalar Multiplication of M*4

print("Scalar Muliplication matrix m with 4 : \n",scalarmult, end='\n\n')
print("Transpose of Matrix: M \n", m.transpose())