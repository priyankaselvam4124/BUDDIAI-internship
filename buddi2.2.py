import numpy as np
import matplotlib.pyplot as plt
num_darts = 1000000
darts_in = []
dart_tot = []

logscale = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

for i in range(1,len(logscale)-1):
    for j in range(logscale[i-1], logscale[i]):
        x = np.random.uniform(-0.5, 0.5)
     
        y = np.random.uniform(-0.5, 0.5)
        distance = np.sqrt(x**2 + y**2)
        darts_in.append(np.count_nonzero(distance <= 0.5))
        dart_tot.append(i)

pi_est = 4 * np.array(darts_in) / np.array(dart_tot)

plt.loglog(dart_tot, pi_est, '-o')
plt.axhline(y=np.pi, color='r', linestyle='--', label="Actual pi")

plt.xlabel('Number of Darts')
plt.ylabel('Estimated Value of Pi')
plt.title('Monte Carlo Estimation of Pi')
plt.legend(["estimated pi"])

plt.show()