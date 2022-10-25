print("matrix multiplication")
import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ndmin = 3)
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]], ndmin = 3)
result = np.matmul(array1, array2)
print(result)


print("matix addition")
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("printing elements of first matrix")
print (A)
print("printing elements of second matrix")
print (B)
print("addition of two matrix")
print (np.add(A, B))

