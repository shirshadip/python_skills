import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 20 * np.pi, 2000)
r = np.sin(4 * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y, color='purple')
plt.axis('equal')
plt.title("Hypnotic Sine Spiral 🌀")
plt.show()
