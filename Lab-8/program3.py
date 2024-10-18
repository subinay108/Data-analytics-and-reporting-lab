# WAPP to implement a Line Chart

import matplotlib.pyplot as plt

noOfHours = [5, 2, 3, 1, 4, 3, 2]
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

plt.plot(days, noOfHours, color='black', marker='o')

plt.xlabel('Days of week')
plt.ylabel('No. of Hours')
plt.title('Line Bar Graph(Days vs no. of hours of study)')

plt.show()