# WAPP to draw an area diagram(Area Plot)
import matplotlib.pyplot as plt
import random

X = [1, 2, 3, 4, 5]
Y = [random.randint(1, 10) for i in X]

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Diagram')
plt.fill_between(X, Y)
plt.show()