import numpy as np
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("Using Nested Loops:")
for x in arr:
    for y in x:
        for z in y:
            print(z)
print("\nUsing nditer:")
for i in np.nditer(arr):
    print(i)