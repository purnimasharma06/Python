#  merging - combining 2 or more than 2 rows of a df , based on common key col
# pd.merge(df1, df2, on="Col name", how="type of join")

import pandas as pd

df_customer = pd.DataFrame({
    'CustomerID':[1, 2, 3],
    'Name' : ['Ramesh', 'Suresh', 'Kalpesh']
})
df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250, 450, 350]
})

# merge
df_merge = pd.merge(df_customer, df_orders, on="CustomerID", how="inner")
print("Inner Join")
print(df_merge) # jiski keys match ho rahi hai bss wahi data aaya hai 


df_merge = pd.merge(df_customer, df_orders, on="CustomerID", how="outer")
print("Outer Join")
print(df_merge)  # combines all the rows but jo value match nahi hogi usko NaN se fill kar dega 


df_merge = pd.merge(df_customer, df_orders, on="CustomerID", how="left")
print("Left Join")
print(df_merge) # left side wale table ko pura rakhega , jo ki right wale se match karegi baki NaN se fill


df_merge = pd.merge(df_customer, df_orders, on="CustomerID", how="right")
print("Right Join")
print(df_merge) # right side wale table ko pura rakhega, jo ki left wale table se match kregi baki NaN se fill


df_merge = pd.merge(df_customer, df_orders, on="CustomerID", how="cross")
print("Cross Join")
print(df_merge) # suppose you have 1df of m rows and other df of n rows , so in cross join the resultant will be of m x n join, returns all the possible pairs of rows, create combination, matching all the products