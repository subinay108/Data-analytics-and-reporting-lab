# WAPP to implement a Horizontal Bar Graph

import matplotlib.pyplot as plt

noOfStudents = [1, 2, 3, 4, 5]
departments = ['DS', 'AI', 'CS', 'Core', 'CSE']

plt.barh(departments, noOfStudents)

plt.xlabel('No. of students')
plt.ylabel('Department')
plt.title('Horizontal Bar Graph(Students)')

plt.show()