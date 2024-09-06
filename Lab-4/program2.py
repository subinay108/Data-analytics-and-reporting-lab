# Specify which column should be used as the index when reading a CSV file

import pandas as pd

df = pd.read_csv('data/student.csv')
df.set_index(['Name'], inplace=True)

print(df)