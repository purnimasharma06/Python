#  How to group data 
#  How to apply aggreagation after grouping

import pandas as pd

data = {
    "Name": ["Arun", "Varun", "Karun", "Tarun", "Marun"],
    "Age" : [28, 34, 22, 34, 28],
    "Salary": [50000, 60000, 45000, 52000, 48000]
}

df = pd.DataFrame(data)
print(df)

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

# ---------- it creates groups based on the unique values in the age column --> 
# df.groupby("Age")["Salary"].sum()
# age 22 = [45000]              
# age 28 = [50000, 48000]
# age 34 = [60000, 52000]

# [Salary].sum() = 
# age 22 = [45000]         = 45000     
# age 28 = [50000, 48000]  = 98000
# age 34 = [60000, 52000]  = 112000


# For multiple cols
print(df.groupby(["Age", "Name"])["Salary"].sum())