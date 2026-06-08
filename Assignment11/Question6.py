import numpy as np
from statistics import mode
arr1 = np.array([
    [10, 20],
    [30, 40]
])
arr2 = np.array([
    [50, 60],
    [70, 80]
])
avg = (arr1 + arr2) / 2
print("Average Array:")
print(avg)
combined = np.concatenate((arr1.flatten(), arr2.flatten()))
print("\nCombined Data:")
print(combined)
print("\nMean =", np.mean(combined))
print("Median =", np.median(combined))
print("Mode =", mode(combined))