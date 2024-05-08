import numpy as np
import matplotlib.pyplot as plt

def plotsamesd(m1, m2, sd):
    x = np.linspace(-5 * sd, 5 * sd)
    f1 = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m1) / sd) ** 2)
    f2 = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m2) / sd) ** 2)

    plt.plot(x, f1, color='blue', label=f'Normal Distribution (Mean={m1}, SD={sd})')
    plt.plot(x, f2, color='yellow', label=f'Normal Distribution (Mean={m2}, SD={sd})')
    
    plt.title("Normal Distribution (Bell Curve)")
    plt.xlabel("Value")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.figtext(0.5, 0.01, "This graph represents a standard normal distribution curve with same mean and standard deviation=1.", ha="center", fontsize=10, bbox={"facecolor":"lightgrey", "alpha":0.5, "pad":5})
    plt.show()

plotsamesd(m1=2, m2=1, sd=1)
