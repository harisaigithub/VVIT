import numpy as np


m = np.array([[1, 2, 3], [2, 3, 4], [4, 5,6]])

print("printing the original square array :\n", m)

w, v = np.linalg.eig(m)

print("printing the eigen values of the given square array:\n", w)

print("printing the right vector of the given square array:\n", v)
