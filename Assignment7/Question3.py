import pandas as pd

data = {"Name": ["Aryan", "Rahul", "Aman", "Rohit"], "Marks": [90, 75, 88, 60],"City": ["Delhi", "Mumbai", "Jaipur", "Pune"]}
df = pd.DataFrame(data)
print("Original DataFrame")
print(df)

#Iteration over rows

print("\nIterating Rows")
for index, row in df.iterrows():
    print(index, row["Name"], row["Marks"])

#Select rows based on condition

print("\nStudents with Marks > 80")
print(df[df["Marks"] > 80])

#Select row using iloc[]

print("\nRow using iloc[]")
print(df.iloc[1])

#Limited rows with columns

print("\nLimited Rows and Columns")
print(df.loc[0:2, ["Name", "Marks"]])

#Drop rows based on condition

print("\nAfter Dropping Marks < 70")
df2 = df[df["Marks"] >= 70]
print(df2)

#Insert Row at Given Position

new_row = pd.DataFrame({"Name": ["Karan"],"Marks": [95],"City": ["Chandigarh"]})
df3 = pd.concat([df.iloc[:2], new_row, df.iloc[2:]]).reset_index(drop=True)
print("\nAfter Inserting Row")
print(df3)

#Create List from Rows

print("\nList from Rows")
lst = df.values.tolist()
print(lst)