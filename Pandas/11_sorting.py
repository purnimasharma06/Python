# Sorting data 
#  Sorting data in one col
# sort_values()

# df.sort_values(by="Column Name", ascending = True, inplace=True) # Ascending - True, Descending- False



import pandas as pd

data = {
    "Name": ["Arun", "Varun", "Karun"],
    "Age" : [28, 34, 22],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by="Age", ascending = True, inplace=True)
print(df)

# Select multiple cols at once 
df.sort_values(by=["Age", "Salary"], ascending = [True,False], inplace=True)
print(df)
