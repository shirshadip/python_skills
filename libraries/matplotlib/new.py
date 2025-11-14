import matplotlib.pyplot as plt
import numpy as np

# Create figure with black background
fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Parameters for the spiral
n_circles = 150
angle_step = 137.5  # Golden angle in degrees
radius_growth = 0.15

# Generate spiral pattern
for i in range(n_circles):
    # Calculate position using golden angle spiral
    angle = np.radians(i * angle_step)
    distance = radius_growth * np.sqrt(i)
    x = distance * np.cos(angle)
    y = distance * np.sin(angle)
    
    # Calculate circle radius (getting smaller as we go out)
    circle_radius = 0.8 - (i * 0.004)
    
    # Create color gradient from purple to cyan to yellow
    hue = (i / n_circles) * 2
    if hue < 1:
        r = 0.5 + 0.5 * (1 - hue)
        g = 0.2 + 0.6 * hue
        b = 1 - 0.3 * hue
    else:
        r = 1 * (hue - 1)
        g = 0.8 + 0.2 * (hue - 1)
        b = 0.7 - 0.7 * (hue - 1)
    
    # Draw circle with gradient color and transparency
    circle = plt.Circle((x, y), circle_radius, 
                       color=(r, g, b), 
                       alpha=0.6,
                       linewidth=2,
                       edgecolor=(r*0.8, g*0.8, b*0.8),
                       fill=True)
    ax.add_patch(circle)

# Set axis limits
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)

plt.title('Golden Spiral Pattern', color='white', fontsize=16, pad=20)
plt.tight_layout()
plt.show()