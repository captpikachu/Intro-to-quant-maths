import numpy as np
import matplotlib.pyplot as plt

S0 = 100
mu = 0.08
sigma = 0.2
T = 1
N = 252
M = 100

dt = T / N

Z = np.random.randn(M, N)

returns = (
    (mu - 0.5 * sigma**2) * dt
    + sigma * np.sqrt(dt) * Z
)

price_paths = S0 * np.exp(np.cumsum(returns, axis=1))

plt.plot(price_paths.T, linewidth=0.5)
plt.title("Vectorized GBM Simulation")
plt.xlabel("Time Step")
plt.ylabel("Price")
plt.show()