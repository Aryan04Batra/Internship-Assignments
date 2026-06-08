import numpy as np
arr = np.array([6, -8, 73, -110, 45, -2])
print("Original Array:")
print(arr)
arr = np.where(arr < 0, 0, arr)
print("\nAfter Replacing Negative Values with Zero:")
print(arr)