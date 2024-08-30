# Read csv file using pandas
import pandas as pd

df = pd.read_csv('data/student.csv')

print(df)

print(df.describe())

print(df['Gender'].value_counts())
