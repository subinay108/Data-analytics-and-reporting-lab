# Read only specific columns from a CSV file

import pandas as pd

columns_to_read = ['Name', 'Gender']

df = pd.read_csv('data/student.csv', usecols=columns_to_read)

print(df)