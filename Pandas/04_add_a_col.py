# How to modify the dataframe
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]

}

df = pd.DataFrame(data)

# Add a coloum approach 1 - adding col via assignment
# using square brackets - df["Col_name"] = new_data

print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)


#  Add a coloum Approach 2 - using insert method(we can insert in precise location)
# df.insert(location(index), "Col_name", some_data)
df.insert(0, "Employee ID", [10,20,30,40,50,60,70,80])
print(df)