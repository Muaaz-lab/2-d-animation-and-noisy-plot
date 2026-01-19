#2D-Animation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Setup the grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

fig, ax = plt.subplots()
# 2. Initialize the plot
img = ax.imshow(Z, cmap='coolwarm', extent=[-5, 5, -5, 5])
ax.axis("off")

# 3. The update function
def update(frame):
    # Calculate new data
    new_Z = np.sin(X**2 + Y**2 + frame * 0.1)
    # Update the existing image object
    img.set_data(new_Z)
    return [img]

# 4. Create the animation
# blit=True makes the animation faster by only redrawing changed parts
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
#noisy effect
def update(frame):
    # Generating noise inside the loop for a 'flicker' effect
    noise = np.random.normal(0, 0.1, X.shape) 
    
    # Update the math with the current frame and add noise
    new_Z = np.sin(X**2 + Y**2 + frame * 0.1) + noise
    
    img.set_data(new_Z)
    return [img]
