import numpy as np
arr = np.array([6, -8, 73, -110, 45, -2])
print("Original Array:")
print(arr)
arr[arr < 0] = 0
print("\nAfter Replacement:")
print(arr)