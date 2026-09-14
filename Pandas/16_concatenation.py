# Data frames of sath me combine krna row wise or col wise 
# pd.concat([df1, df2, axis=0, ignore_index=True]) 0-row wise , 1- col wise, index ko reset krdo jo combined data mila hai  

#  combining vertically
import pandas as pd 

df_reg1 = pd.DataFrame({
    'CustomerID': [1, 2],
    'Name': ["Gopal", "Raju"]
})

df_reg2 = pd.DataFrame({
    'CustomerID':[3, 4],
    'Name':["Ram", "Shyam"]
})

df_concat = pd.concat([df_reg1, df_reg2], axis = 0, ignore_index = True);
print(df_concat)



# Horizontally
df_concat = pd.concat([df_reg1, df_reg2], axis = 1, ignore_index = True);
print(df_concat)
