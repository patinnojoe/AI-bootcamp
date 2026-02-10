import numpy as np

A = np.array([[1,2], [3, 4]])
determinant_of_A = np.linalg.det(A)

# print(" the determinant is", determinant_of_A)
# print(A)
B = np.array([[2,1], [3,4]])

inverse_B = np.linalg.inv(B)

# print("Inverse of B", inverse_B)
C = np.array([[5,2], [3, 1]])
inverse_C = np.linalg.inv(C)
# print("Inverse of C", inverse_C)
eigenValues, eigenVectors = np.linalg.eig(A)

# print(f"Eigenvalues: {eigenValues} \n EigenVectors: {eigenVectors}" )
D = np.array([[4,2], [1,1]])
eigVal, eigVec = np.linalg.eig(D)

# print(f"EigValue: {eigVal} and EigVec: {eigVec}")

# EXERCISE
exercise_1 = np.array([[3,8,9], [7,2,1], [0,8,5]])
exercise_1_det = np.linalg.det(exercise_1)
exercise_1_inverse = np.linalg.inv(exercise_1)
print(f"Determinant of exercise 1 is: {exercise_1_det}")
print(f"Inverse of exercise 1 is: {exercise_1_inverse}")


