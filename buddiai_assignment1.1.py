import numpy as np
import math
import matplotlib.pyplot as plt

darts_in = 0
tot_darts = 0
log_scale = [
    0,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
]
#
pis = []
for i in range(len(log_scale) - 1):
    for j in range(log_scale[i], log_scale[i + 1]):
        x = np.random.uniform(-0.5, 0.5)
        y = np.random.uniform(-0.5, 0.5)

        if np.sqrt(x*2 + y*2) <= 0.5:
            darts_in += 1
        tot_darts += 1
#
    pi_estimate = (darts_in / tot_darts) * 4
    print(f"Pi Estimate: {pi_estimate}")
    pis.append(pi_estimate)
#
print(pis)
pis = [4.0, 3.52, 3.052, 3.1348, 3.13928, 3.143092, 3.14142]

plt.xscale("log")
plt.plot(log_scale[1:], pis, label="estimation of Pi", marker=".")
plt.xlabel("Number of Darts Thrown")
plt.ylabel("Estimated Pi Value")
plt.axhline(y=math.pi, color="k", linestyle="--")
plt.title("Monte Carlo Estimation of Pi using uniform random sampling")
plt.legend()
plt.figtext(
    0.45,
    0.3,
    "Monte Carlo simulation to compute the value of pi using repeated uniform random sampling to estimate the probability of dart landing in a circle",
    fontsize=10,
    horizontalalignment="center",
    wrap=True,
    bbox={"facecolor": "grey", "alpha": 0.3, "pad": 5},
)

plt.show()