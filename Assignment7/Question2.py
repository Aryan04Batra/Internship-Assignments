import pandas as pd

#DataFrame from 2D List

data1 = [[1, "Aryan", 90], [2, "Rahul", 85], [3, "Aman", 88]]
df1 = pd.DataFrame(data1, columns=["ID", "Name", "Marks"])
print("DataFrame from 2D List")
print(df1)

#DataFrame from Dictionary

data2 = {"Name": ["Aryan", "Rahul", "Aman"],"City": ["Delhi", "Jaipur", "Mumbai"]}
df2 = pd.DataFrame(data2)
print("\nDataFrame from Dictionary")
print(df2)

#DataFrame from List of Lists

data3 = [["Python", 90],["Java", 80],["C++", 85]]
df3 = pd.DataFrame(data3, columns=["Subject", "Marks"])
print("\nDataFrame from List of Lists")
print(df3)

#DataFrame from List of Tuples

data4 = [("TV", 30000),("Laptop", 60000),("Mobile", 20000)]
df4 = pd.DataFrame(data4, columns=["Product", "Price"])
print("\nDataFrame from List of Tuples")
print(df4)

#DataFrame from List of Dictionaries

data5 = [{"Name": "Aryan", "Age": 19},{"Name": "Rahul", "Age": 20},{"Name": "Aman", "Age": 18}]
df5 = pd.DataFrame(data5)
print("\nDataFrame from List of Dictionaries")
print(df5)