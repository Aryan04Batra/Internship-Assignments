import pandas as pd
df1=pd.DataFrame({
    "Id":[101,102,103,104],
    "Name":["Ayush","Anshul","Abhi","Aman"],
    "City":["Jaipur","Lucknow","Pune","Srinagar"]
},index=[1,2,3,4])
df2=pd.DataFrame({
    "Id":[101,102,105,106],
    "Class":[4,8,5,9],
    "Sectoin":["J","L","D","H"]
},index=[1,2,5,6])
print(df1.merge(df2, on="Id", how="inner"))
print(df1.merge(df2,on="Id",how="left"))
print(df1.merge(df2,on="Id",how="right"))
print(df1.join(df2,how="right",lsuffix="l",rsuffix="r"))


