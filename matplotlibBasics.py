import matplotlib.pyplot as plt

# Matplotlib is commonly used for data visualization, offering powerful tools to create and customize a wide variety of static, animated, and interactive plots.

# 1. Line Plot
# ------------

# Simple line plot with data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5)
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# 2. Bar Plot
# -----------

# Bar plot for categorical data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='purple', edgecolor='black')
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# 3. Scatter Plot
# ---------------

# Scatter plot for displaying relationships
x = [5, 7, 8, 9, 10]
y = [10, 15, 7, 20, 25]
sizes = [50, 80, 60, 100, 120]  # Varying sizes for each point

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='green', s=sizes, alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# 4. Histogram
# ------------

# Histogram to show frequency distribution
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 8, 9]

plt.figure(figsize=(8, 5))
plt.hist(data, bins=7, color='orange', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Data Bins")
plt.ylabel("Frequency")
plt.show()

# 5. Customizing the Plot (Multiple Lines)
# ----------------------------------------

# Plotting multiple lines with different styles
x = range(1, 6)
y1 = [1, 4, 9, 16, 25]
y2 = [2, 3, 4, 5, 6]

plt.figure(figsize=(8, 5))
plt.plot(x, y1, label="Squared", color='red', linestyle='--', marker='o')
plt.plot(x, y2, label="Linear", color='blue', linestyle='-', marker='x')
plt.title("Multiple Lines with Legends")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()  # Adds a legend
plt.grid(True)
plt.show()

# 6. Subplots
# -----------

# Creating multiple plots in one figure (subplot)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Line plot in the first subplot
axes[0, 0].plot(x, y1, color='blue')
axes[0, 0].set_title("Line Plot")

# Bar plot in the second subplot
axes[0, 1].bar(categories, values, color='green')
axes[0, 1].set_title("Bar Plot")

# Scatter plot in the third subplot
axes[1, 0].scatter(x, y2, color='purple')
axes[1, 0].set_title("Scatter Plot")

# Histogram in the fourth subplot
axes[1, 1].hist(data, bins=5, color='orange')
axes[1, 1].set_title("Histogram")

# Layout adjustment
plt.tight_layout()
plt.show()

# 7. Pie Chart
# ------------

# Pie chart for proportions
sizes = [15, 30, 45, 10]
labels = ['Category A', 'Category B', 'Category C', 'Category D']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
explode = (0, 0.1, 0, 0)  # "explode" the 2nd slice

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.title("Pie Chart")
plt.show()

# 8. Saving the Figure
# --------------------

# Saving a figure to a file
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label="Squared", color='red', linestyle='--', marker='o')
plt.title("Saved Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.savefig("saved_plot.png")  # Save as a PNG file
print("Plot saved as 'saved_plot.png'")
