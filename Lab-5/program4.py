# WAPP to draw a multiple area diagram (Area Plot)
import matplotlib.pyplot as plt
import random

X = [1, 2, 3, 4, 5]
Y1 = [random.randint(1, 10) for i in X]
Y2 = [random.randint(1, 10) for i in X]


plt.fill_between(X, Y1, label='Area 1', alpha=0.5, color='skyblue')
plt.fill_between(X, Y2, label='Area 2', alpha=0.5, color='olive')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multi Line Diagram')

plt.legend()
plt.show()