import numpy as np
import matplotlib.pyplot as plt

def plotsamem(m, sd1,sd2):
    x = np.linspace(-5 * sd1, 5 * sd1)
    f1 = (1 / (sd1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sd1) ** 2)
    f2 = (1 / (sd2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sd2) ** 2)

    plt.plot(x, f1, color='blue', label=f'Normal Distribution (Mean={m}, SD={sd1})')
    plt.plot(x, f2, color='yellow', label=f'Normal Distribution (Mean={m}, SD={sd2})')
    
    plt.title("Normal Distribution (Bell Curve)")
    plt.xlabel("Value")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.figtext(0.5, 0.01, "This graph represents a standard normal distribution curve with same mean and standard deviation=1.", ha="center", fontsize=10, bbox={"facecolor":"lightgrey", "alpha":0.5, "pad":5})
    plt.show()

plotsamem(m=2, sd1=1, sd2=2)
