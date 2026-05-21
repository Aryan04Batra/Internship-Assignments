# Dictionary Practice
student = {"name": "Aryan","age": 19, "branch": "CSE"}
print("Dictionary:",student)
# Access value
print("Name:", student["name"])
# Add new item
student["college"] = "Engineering College"
# Update value
student["age"] = 20
# Remove item
student.pop("branch")
print(student)

# Tuple Practice
numbers = (10, 20, 30, 40, 50)
print("\nTuple:",numbers)
# Access elements
print("First Element:", numbers[0])
# Length of tuple
print("Length of Tuple:", len(numbers))
# Count and index
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

# Set Practice
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet 1:", set1)
print("Set 2:", set2)
# Add element
set1.add(7)
# Remove element
set1.remove(2)
print("Updated Set 1:", set1)
# Union
print("Union:", set1.union(set2))
# Intersection
print("Intersection:", set1.intersection(set2))