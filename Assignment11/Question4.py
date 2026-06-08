import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("Array:")
print(arr)
print("\nMaximum Value:", np.max(arr))
print("Minimum Value:", np.min(arr))
print("Rows:", arr.shape[0])
print("Columns:", arr.shape[1])
print("\nAll Elements:")
for row in arr:
    for element in row:
        print(element, end=" ")
print()
print("\nSpecific Element [1][2]:", arr[1][2])
sum1 = 0
for row in arr:
    for element in row:
        sum1 += element
print("\nSum =", sum1)