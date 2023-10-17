import numpy as np

multiDArray = [[1,2,3],[4,5,6],[7,8,9]]

print("Matrix Representaion will be:\n", np.asmatrix(multiDArray))
determinant = np.linalg.det(multiDArray)
print('Determinant of a matrix:\n', determinant)

if determinant <= 0:
    print('Inverse of a matrix:\n', np.linalg.inv(multiDArray))
else:
    print('This is an invertible matrix')