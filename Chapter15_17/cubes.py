from matplotlib import pyplot as plt
x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s = 10)

plt.title('Cubes', fontsize=30)
plt.xlabel('Value')
plt.ylabel('Cube Value')

plt.show()