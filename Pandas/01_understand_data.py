import pandas as pd

# Read data from csv file to dataframe
# df = pd.read_csv('file name.csv', encoding='utf-8'/ encoding='latin1')
# print(df)

# If the data is in excel file, we can use read_excel() function to read the data
# df = pd.read_excel('file name.xlsx')

# if the data is in json file, we can use read_json() function to read the data
# df = pd.read_json('file name.json')

# gcsfs 

# How to save data after manipulation -> create dataframe and save it to csv, excel or json file
data = {
    'Name': ['John', 'Alice', 'Bob'], 
    'Age': [25, 30, 35], 
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)  # Create a dataframe from the dictionary
# read
print(df)

# save file in csv
df.to_csv('output.csv', index=False)  # Save the dataframe to a CSV file without the index


# save file in excel
df.to_excel('output.xlsx', index=False)  # Save the dataframe to an Excel file

# save file in json
df.to_json('output.json')  # Save the dataframe to a JSON file