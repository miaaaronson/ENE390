import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Sample data in the range 13.0 to 13.2
x = np.linspace(0, 10, 100)
y = np.random.uniform(13.0, 13.2, size=100)

fig, ax = plt.subplots(figsize=(8, 6))

# Main plot with full y-range from 0 to 20
ax.plot(x, y, "b.")
ax.set_ylim(0, 20)

# Add an inset zoomed-in on the 13.0 to 13.2 range

axins = inset_axes(ax, width="40%", height="40%", loc="upper right")

# Plot the same data in the inset
axins.plot(x, y, "b.")
axins.set_ylim(13.0, 13.2)

# Customize ticks in the main plot and inset
ax.set_yticks([0, 5, 10, 15, 20])  # Fewer ticks on the main y-axis
axins.set_yticks(np.linspace(13.0, 13.2, 5))  # More ticks on the inset

# Draw lines to indicate the connection between the two sections
ax.indicate_inset_zoom(axins, edgecolor="gray")

plt.show()
