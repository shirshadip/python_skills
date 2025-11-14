import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Generate heart shape points
t = np.linspace(0, 2 * np.pi, 1000)
x_heart = 16 * np.sin(t)**3
y_heart = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Create particles along the heart
n_particles = 300
particle_indices = np.linspace(0, len(x_heart)-1, n_particles, dtype=int)
particles_x = x_heart[particle_indices]
particles_y = y_heart[particle_indices]

# Initialize scatter plot
scatter = ax.scatter([], [], c=[], s=[], cmap='hot', alpha=0.8, edgecolors='pink', linewidths=0.5)

# Set axis limits
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def init():
    scatter.set_offsets(np.c_[[], []])
    return scatter,

def animate(frame):
    # Pulsing effect
    pulse = 0.85 + 0.15 * np.sin(frame / 10)
    
    # Calculate particle positions with pulse
    x_pos = particles_x * pulse
    y_pos = particles_y * pulse
    
    # Add some floating particles
    float_offset = np.sin(frame / 20 + np.linspace(0, 2*np.pi, n_particles)) * 0.5
    x_pos += float_offset * np.cos(np.linspace(0, 2*np.pi, n_particles))
    y_pos += float_offset * np.sin(np.linspace(0, 2*np.pi, n_particles))
    
    # Color gradient (red to pink)
    colors = np.linspace(0.5, 1.0, n_particles)
    colors = (colors + np.sin(frame / 15) * 0.2) % 1.0
    
    # Size variation with pulse
    sizes = 50 + 50 * np.sin(frame / 10 + np.linspace(0, 4*np.pi, n_particles))
    
    # Update scatter plot
    scatter.set_offsets(np.c_[x_pos, y_pos])
    scatter.set_array(colors)
    scatter.set_sizes(sizes)
    
    return scatter,

# Create animation
anim = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=200, interval=50, blit=True, repeat=True)

plt.title('❤️', color='red', fontsize=60, pad=20)
plt.tight_layout()
plt.show()