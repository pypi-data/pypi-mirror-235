import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[1,2,3], [4,5,6], [7,8,9]])

# Multiplying using numpy built-in Method
print('Multiplication of Matrices using Numpy:\n', np.dot(a,b), end='\n\n')

# Multiplying using For Loop:
# Defining Null Matrix
nullmatrix = np.zeros((3,3))

rows, columns = nullmatrix.shape
for row in range(rows):
    for column in range(columns):
        for val in range(columns):
            nullmatrix[row, column] += a[row, val] * b[val, column]

print('Multiplication of Matrices using Loop:\n', nullmatrix, end='\n\n')