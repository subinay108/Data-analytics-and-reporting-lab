# WAPP to implement a Bar Chart

import matplotlib.pyplot as plt

noOfStudents = [1, 2, 3, 4, 5]
departments = ['DS', 'AI', 'CS', 'Core', 'CSE']

plt.bar(departments, noOfStudents)

plt.xlabel('Departments')
plt.ylabel('No. of students')
plt.title('Vertical Bar Graph(Students)')

plt.show()