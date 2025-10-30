import matplotlib.pyplot as plt

input_values = list(range(1, 11))
squares = [x ** 2 for x in input_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title
ax.set_title('Squares Numbers', fontsize=24)

# Set label axes
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()
