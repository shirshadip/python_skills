import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 1000)
r = np.sin(5 * theta)  # change 5 → number of petals

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y, color='magenta')
plt.axis('equal')
plt.title("Flower Pattern 🌸")
plt.show()
