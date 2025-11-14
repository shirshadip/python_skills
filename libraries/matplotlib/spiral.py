import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 8 * np.pi, 1000)  # angle values
r = np.linspace(0, 10, 1000)             # radius values

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y, color='cyan')
plt.axis('equal')
plt.title("Spiral Pattern 🌪️")
plt.show()
