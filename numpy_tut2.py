import numpy as np

# arr = np.random.randint(1, 51, size=(5,5))
# arr[arr > 25] = 0

# print(arr)
# print(f"Sum of array: ", np.sum(arr))
# print("Mean of array: ", np.mean(arr))
# print("standard deviation: ", np.std(arr))
# print("statistic along row: ", np.sum(arr, axis=1))
# print("statiscs along column: ", np.sum(arr, axis=0))

arr = np.random.rand(3,3)
print("original: ", arr)
arr[arr >= 0.5] = 1
arr[arr < 0.5] = 0



print(arr)