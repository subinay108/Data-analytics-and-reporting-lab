# Write a python program to demonstrate various type of data cleaning operation 
# using data exploration and imputation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Age': [25, np.nan, 30, 29, 35, 32, np.nan, 28, 50, 29],
    'Salary': [50000, 60000, np.nan, 52000, 58000, np.nan, 70000, 71000, 75000, 80000],
    'City': ['New York','Los Angeles', 'Chicago', np.nan, 'Houston', np.nan, 'Houston', 'Chicago', 'New York', np.nan],
}


df = pd.DataFrame(data)

# Step1: Data Exploration
print('Initial Dataframe: ')
print(df)

# Check for missing values
print('\nMIssing values: ')
print(df.isnull().sum())

# Check data types
print('\nData types: ')
print(df.dtypes)

# Check Statistics of data
print('\nSummary Statistics: ')
print(df.describe())


# Step2: Handling Missing Values
# Impute missing values for 'Age' with the mean
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)

# Impute missing values for 'Salary' with the median
median_salary = df['Salary'].median()
df['Salary'].fillna(median_salary, inplace=True)

# Impute missing values in 'City' column with mode
df['City'].fillna(df['City'].mode()[0], inplace=True)

# print('\nWithout interpolation')
# print(df)

# Impute missing values in 'Age' column with interpolation
# df['Age'].interpolate(method='linear', limit_direction='forward',inplace=True)

print('\nDataset after imputation')
print(df)

# Step 3: Removing Duplicates
# Let's say there are duplicates (we'll create one for demonstration)
duplicate_row = df.iloc[[0]]
df = pd.concat([df, duplicate_row], ignore_index=True) # Duplicating the first row

print("\nDataFrame with duplicates:")
print(df)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nDataFrame after removing duplicates:")
print(df)

# Step 4: Data Type Conversion
# Convert 'Age' to integer type
df['Age'] = df['Age'].astype(int)

print("\nDataFrame after converting 'Age' to integer:")
print(df)

# Step 5: Handling Outliers
# For demonstration, let's define outliers as values outside of 1.5*IQR
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

# Define the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Replace outliers with the median
df['Salary'] = np.where(df['Salary'] < lower_bound, median_salary, df['Salary'])
df['Salary'] = np.where(df['Salary'] > upper_bound, median_salary, df['Salary'])

print("\nDataFrame after handling outliers in 'Salary':")
print(df)

# Final DataFrame
print("\nFinal Cleaned DataFrame:")
print(df)

# Plot a histogram to visualize the 'Age' column
plt.hist(df['Age'], bins=10)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()