#gridsearch in sklearn
import matplotlib.pyplot as plt
import numpy as np

x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([7, 2, 0, 0, 0, 2, 7])
b = np.array(list(range(-3, 4)))

efinal = []
etotal = []
tab = []

for b0 in b:
    for b1 in b:
        e = []
        for xi, yi in zip(x, y):
            ypredict = (b0 * xi) + (b1 * (xi ** 2))
            ei = abs(ypredict - yi)
            e.append(ei)
        efinal.append(e)
        esum = np.sum(e)
        etotal.append(esum)
        tab.append([b0, b1, esum])

print(tab)
print(tab[np.argmin(etotal)])
min_index = np.argmin(etotal)
best_b0 = tab[min_index][0]
best_b1 = tab[min_index][1]
print("Best b0:", best_b0)
print("Best b1:", best_b1)

# Plotting the surface
ep_array = np.array(etotal).reshape((len(b), len(b)))

# Create a meshgrid of b0 and b1 values
B0, B1 = np.meshgrid(b, b)

fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection="3d")
ax.set_xlabel("b1")
ax.set_ylabel("b2")
ax.set_zlabel("epsilon")
plt.title("Error minimization using grid search")
ax.plot_surface(B0, B1, ep_array, label="Error surface plot")
plt.legend()
plt.show()
