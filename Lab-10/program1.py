# Write a python code to visualize Time Series Data using Seaborn
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# Set the style for Seaborn
sns.set_theme(style='whitegrid')

# Load time series data
df = pd.read_csv('dataset/multiTimeline.csv')
df.columns = ['Date', 'Popularity']

# Visualize the data
plt.figure(figsize=(14, 7))
sns.lineplot(x='Date', y='Popularity', data=df, marker='o')

# Add titles and labels
plt.title('BitCoin Google Web Search Popularity', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Popularity', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid()

# Show the plot
plt.tight_layout()  # Adjust layout to make room for the rotated labels
plt.show()