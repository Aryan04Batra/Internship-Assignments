import numpy as np
#Convert 1D Array to 2D
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2d = arr1.reshape(2, 3)
print("2D Array:")
print(arr2d)
#Array Attributes
print("\nShape:", arr2d.shape)
print("Dimension:", arr2d.ndim)
print("Data Type:", arr2d.dtype)
print("Item Size:", arr2d.itemsize)
#Create 3x3 Array of all 9
arr = np.full((3, 3), 9)
print("\n3x3 Array of 9:")
print(arr)
#10 Evenly Spaced Values Between 25 and 125
arr = np.linspace(25, 125, 10)
print("\nEvenly Spaced Values:")
print(arr)
#Convert Python List into NumPy Array
lst = [10, 20, 30, 40]
arr = np.array(lst)
print("\nNumPy Array:")
print(arr)
#Reverse a 1D NumPy Array
arr = np.array([10, 20, 30, 40, 50])
print("\nReversed Array:")
print(arr[::-1])
#Create 4x4x3 Array and Extract Value
arr = np.arange(48).reshape(4, 4, 3)
print("\n4x4x3 Array:")
print(arr)
print("\nSecond Set, First Row, Last Column:")
print(arr[1, 0, 2])
#Create 4x4 and Extract Odd Rows & Even Columns
arr = np.arange(1, 17).reshape(4, 4)
print("\n4x4 Array:")
print(arr)
print("\nOdd Rows and Even Columns:")
print(arr[::2, 1::2])
#Slice First Two Rows and First Two Columns
#    of Second Set from 4x4x3 Array
arr = np.arange(48).reshape(4, 4, 3)
print("\nRequired Slice:")
print(arr[1, 0:2, 0:2])
#Replace Odd Numbers with -1 using For Loop
arr = np.array([[23, 56, 78, 93],
                [71, 82, 13, 24]])
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i][j] % 2 != 0:
            arr[i][j] = -1
print("\nAfter Replacing Odd Numbers:")
print(arr)
#Indices of Non-Zero Elements
arr = np.array([1, 0, 2, 0, 3, 0, 4])
print("\nIndices of Non-Zero Elements:")
print(np.nonzero(arr))
#Arithmetic Operations
arr1 = np.array([10, 20, 30])
arr2 = np.array([5, 4, 3])
print("\nAddition:")
print(arr1 + arr2)
print("\nMultiplication:")
print(arr1 * arr2)
#Dot Product
arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])
dot_product = np.dot(arr1, arr2)
print("\nDot Product:")
print(dot_product)