# bug 5

# Create a list of values -10, -9.8, -9.6, ..., -0.2, 0, 0.2, ..., 10.

h = 0.2
x = [-10 + i*h for i in range(100)]

