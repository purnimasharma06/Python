import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, None, 78, 92, 88, 95, 80, 89]

}

df = pd.DataFrame(data)
print(df)

# Filling
# fillna(value, inplace = True)
df.fillna(0, inplace=True)
print(df) # This is only valid where you have numerical numbers in the table , and you are replacing it with zero , if you want to replace a str you should handle it separately

# Fill calculated value
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)