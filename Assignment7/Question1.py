import pandas as pd
#Series from Dictionary

data = {"a": 10,"b": 20,"c": 30}
s1 = pd.Series(data)
print("Series from Dictionary")
print(s1)

#Series from List

lst = [100, 200, 300, 400]
s2 = pd.Series(lst)
print("\nSeries from List")
print(s2)

#Accessing Elements of Series

print("\nAccessing Elements")
print("First Element:", s2[0])
print("Second Element:", s2[1])

print("\nUsing Loop")

for i in s2:
    print(i)