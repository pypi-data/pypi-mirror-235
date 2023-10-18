import numpy as np

A = np.array([[3, -2], [1, 0]])
print("Matrix A:\n", A, end='\n\n')

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors, end='\n\n')

for i, eigenvalue in enumerate(eigenvalues):
    print("Left:", np.dot(A, eigenvectors[:, i]))
