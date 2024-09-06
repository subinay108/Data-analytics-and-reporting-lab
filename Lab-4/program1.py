# Read a CSV file and display the first 5 rows ofthe dataset

import pandas as pd

df = pd.read_csv('data/student.csv')

print(df.head())