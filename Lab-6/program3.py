# WAPP to implement a Double Bar Graph

import matplotlib.pyplot as plt

# Data
sections = ['A', 'B', 'C', 'D', 'E', 'F']
noOfBoys = [10, 20, 30, 40, 50, 6]
noOfGirls = [60, 50, 40, 30, 20, 10]

# Bar Width
bar_width = 0.25

x1 = list(range(len(sections)))
x2 = [i + bar_width for i in x1]

# Create the bar graphs
plt.bar(x1, noOfBoys, bar_width, label='Boys')
plt.bar(x2,noOfGirls, bar_width, label='Girls')

# Graph Details
plt.xticks([(i + j) /2 for i,j in zip(x1, x2)], sections)
plt.title('Double Bar Graph')
plt.xlabel('Sections')
plt.ylabel('No. of students')
plt.legend()

plt.show()