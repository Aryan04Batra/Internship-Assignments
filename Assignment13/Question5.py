import numpy as np
from statistics import mode
arr1 = np.array([[10,20],
                 [20,40]])
arr2 = np.array([[20,60],
                 [70,80]])
avg = (arr1 + arr2)/2
print("Average Array:")
print(avg)
combined = np.concatenate((arr1.flatten(),
                           arr2.flatten()))
print("\nMean:", np.mean(combined))
print("Median:", np.median(combined))
print("Mode:", mode(combined))