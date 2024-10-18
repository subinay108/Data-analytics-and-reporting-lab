# WAPP to implement a Scatter Plot

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./datasets/gender_height_weight.csv')
height = df['Height']
weight = df['Weight']

plt.scatter(height, weight)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()