# Interpolation - technique by which we fill estimated values in the missing values 
# ex = 10, 20, NaN , 40, 50 - so it fills 30 in place of NaN - by that we get a consistent data - only for numerical col
# preserve data integrity
# smooth trends
# avoid data loss 
#  interpolate() - method y which we can fill estimated values 
# linear, polynomial, time 
# Pass axis = 0-rows 1-col


# ------------------------------ HERE WE WILL FILL ESTIMATED VALUE IN PLACE OF NaN------------------------------------------------
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, None, 78, 92, 88, 95, 80, 89]

}

df = pd.DataFrame(data)
print(df)

df.interpolate(method="linear", axis=0, inplace=True)



# used when we have time series data 
# numeric data with trends 
# avoid dropping rows
