# WAPP to draw multi line diagram (Line Graph)
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y1 = [1, 4, 9, 16, 25]
Y2 = [1, 8, 27, 64, 125]


plt.plot(X, Y1, label='y = x ^ 2')
plt.plot(X, Y2, label='y = x ^ 3')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multi Line Diagram')

plt.legend()
plt.show()

