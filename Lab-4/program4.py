# Skip a specific number of rows when reading a CSV file

import pandas as pd

df = pd.read_csv('data/student.csv', skiprows=[1, 5])

print(df['Name'])