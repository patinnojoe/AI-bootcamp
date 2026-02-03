import numpy as np

A = np.array([[1,5], [3,3]])
B = np.array([[9,0], [10, 8]])
C = np.array([[2,1,3], [1,4,3]])
D = np.array([[1,0,3], [2,1,2]])


# print("Addition", A+B)
# print("substraction", A-B)
# print("Scalar", 3*A)

# MATRIX VECTOR MULTIPLICATION
# M = np.array([[1,2,3], [4,5,6], [7,8,9]])
# v = np.array([1,0,-1])

# print(np.dot(M,v))
I = np.eye(3)
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])

# print(I)
print(np.dot(I, arr), "goat")