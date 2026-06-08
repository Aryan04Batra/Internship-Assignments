import numpy as np
arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])
print("Original Array:")
print(arr)
arr = np.nan_to_num(arr, nan=0)
print("\nAfter Replacing NaN with 0:")
print(arr)
print("\nTranspose Array:")
print(arr.T)