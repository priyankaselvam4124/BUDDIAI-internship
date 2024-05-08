import numpy as np
import matplotlib.pyplot as plt

# Lagrange's polynomial function
def lagrange(x, y, xi):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Given points
x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([7, 2, 0, 0, 0, 2, 7])

# Plot given points
plt.scatter(x, y, color='red', label='Given Points')

yi=[lagrange(x,y,x[i]) for i in range(len(x))]


# Plot Lagrange's polynomial
plt.plot(x, yi, color='blue', label="Lagrange's Polynomial")

# Add labels and legend
plt.title("Lagrange's Polynomial Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Show plot
plt.grid(True)
plt.show()
