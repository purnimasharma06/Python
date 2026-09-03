# Filtering and Modification

# Selecting colums 
# 1. a series
# 2. dataframe multiple col of data 
# column = df["column name"]
# subset = df[["col1", "col2", .......]]

# filtering rows
# Based on a single condition 
# filter_rows = df[df["salary"] > 50000]

# based on multiple condition
# filter_rows = df[(df["col1"] > val) & (df["col2"] < val)]



# boolean indexing

import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print('Employees with salary > 50000')
print(high_salary)

# Filtering rows: Salary > 50k & Age > 30
filtered = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print('Employee list Age > 30 + Salary > 50000')
print(filtered)

# using or condtition 
filter_or = df[(df['Age'] > 35) | (df['Performance Score'] > 90)]
print('Employees older than 35 or performance score > 90')
print(filter_or)