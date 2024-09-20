# WAPP to implement a Stack Bar Graph

import matplotlib.pyplot as plt

# Data
sections = ['A', 'B', 'C', 'D', 'E', 'F']
noOfBoys = [20, 32, 34, 30, 36, 32]
noOfGirls = [40, 22, 20, 28, 25, 24]

# Bar Width
bar_width = 0.5

x = list(range(len(sections)))

# Create the bar graphs
plt.bar(x,[b + g for b,g in zip(noOfBoys, noOfGirls)], bar_width, label='Girls')
plt.bar(x, noOfBoys, bar_width, label='Boys')

# Graph Details
plt.xticks(x, sections)
plt.title('Stacked Bar Graph')
plt.xlabel('Sections')
plt.ylabel('No. of students')
plt.legend()

plt.show()