# NaN - not a number 
# None - for object data types 



# How to detect missing data 
# isnull() - returns true - NaN is missing or false - value is present 
import pandas as pd

data = {
    "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, None, 78, 92, 88, 95, 80, 89]

}

df = pd.DataFrame(data)
print(df)

print(df.isnull())

# In one col/row count of how many missing values are there 
# df.isnull().sum()

print(df.isnull().sum())


# handle - Remove
# How to drop missing values 
# dropna(axis = 0, inplace = True) axis = 0 means rows , and axis = 1 means col

# df.dropna(axis = 0, inplace=True)
# print(df)


# Filling
# fillna(value, inplace = True)
df.fillna(0, inplace=True)
print(df)