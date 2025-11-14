import matplotlib.pyplot as plt
import numpy as np

for i in range(30):
    circle = plt.Circle((np.random.rand(), np.random.rand()),
                        np.random.rand() * 0.1,
                        color=np.random.rand(3,))
    plt.gca().add_patch(circle)

plt.axis("equal")
plt.axis("off")
plt.title("Colorful Random Circles 🎨")
plt.show()
