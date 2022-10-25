import numpy as np
nums = np.array([[[1, 2, 3],
                [0, 1, 3, 4],
                [90, 91, 93, 94],
                [5, 0, 3, 2]]])
print("original array: ")
print(nums)
print("\n swap rows & columns of the said array in reverse order:")
new_nums = print(nums[::-1, ::-1])
print (new_nums)
