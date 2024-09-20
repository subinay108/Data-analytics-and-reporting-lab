# WAPP to implement a Multiple Bar Graph


import matplotlib.pyplot as plt

# Data
sections = ['A', 'B', 'C', 'D', 'E', 'F']
subwiseStudents = {
    'AI': [10, 20, 30, 40, 50, 6],
    'Cloud': [5, 10, 40, 30, 20, 9],
    'Image': [8, 25, 22, 56, 32, 27],
    # 'Networking': [1, 2, 3, 4, 5, 6],
}

# Bar Width
bar_width = 0.2

# Create the bar graphs
x = list(range(len(sections)))
offset = 0
for sub in subwiseStudents:
    plt.bar([i + offset * bar_width for i in x], subwiseStudents[sub], bar_width, label=sub)
    offset += 1

# Graph Details
plt.xticks([ i + (len(subwiseStudents) - 2) * bar_width for i in x], sections)
plt.xlabel('Sections')
plt.ylabel('No. of students')
plt.title('Multiple Bar Graph')
plt.legend()

plt.show()