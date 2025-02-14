import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(10)
data = np.random.normal(100, 20, 200)

# Create a figure and boxplot
fig, ax = plt.subplots(figsize=(10, 10))
box = ax.boxplot(data, vert=True, patch_artist=False, widths=0.4, medianprops=dict(color='#007791', lw = 3))


# Setting axis limits for better spacing of annotations
ax.set_ylim(35, 160)

# Add labels and lines
ax.annotate('Top 25%', xy=(1.2, 140), xytext=(.55, 133),
            ha='left', va='top', fontsize=12, color = '#0066b2' )
ax.annotate('Middle 50% \n(Interquartile \n Range [IQR])', xy=(1.2, 100), xytext=(.525, 102),
            ha='left', va='center', fontsize=12, color = '#0066b2')
ax.annotate('Bottom 25%', xy=(1.2, 60), xytext=(.55, 72),
            ha='left', va='center', fontsize=12, color = '#0066b2')
ax.annotate('Outliers', xy=(1.05, 155), xytext=(1, 155),
            ha='center', va='center', fontsize=12)
ax.annotate('Outliers', xy=(1.05, 45), xytext=(.95, 37),
            ha='left', va='center', fontsize=12)

# Quartiles and median
ax.annotate('Upper Extreme', xy=(1.05, box['whiskers'][1].get_ydata()[1]), xytext=(1.2, box['whiskers'][1].get_ydata()[1]),
            ha='left', va='center', fontsize=12)
ax.annotate('Third Quartile\n(75th percentile)', xy=(1.05, box['boxes'][0].get_ydata()[0]), xytext=(1.28, box['boxes'][0].get_ydata()[0]),
            ha='left', va='center', fontsize=12)
ax.annotate('Median', xy=(1.05, np.median(data)), xytext=(1.28, np.median(data)),
            ha='left', va='center', fontsize=14, color='#007791')
ax.annotate('First Quartile\n(25th percentile)', xy=(1.05, box['boxes'][0].get_ydata()[2]), xytext=(1.28, box['boxes'][0].get_ydata()[2]),
            ha='left', va='center', fontsize=12)
ax.annotate('Lower Extreme', xy=(1.05, box['whiskers'][0].get_ydata()[1]), xytext=(1.2, box['whiskers'][0].get_ydata()[1]),
            ha='left', va='center', fontsize=12)

#top bracket
ax.plot([.7, .7], [box['whiskers'][1].get_ydata()[1], 115], 'k-', lw=2, color = '#0066b2')
ax.plot([0.7, .75], [box['whiskers'][1].get_ydata()[1], box['whiskers'][1].get_ydata()[1]], 'k-', lw=2, color = '#0066b2')
ax.plot([.7, .75], [115, 115], 'k-', lw=2, color = '#0066b2')


#middle bracket
ax.plot([0.68, 0.68], [box['boxes'][0].get_ydata()[0], box['boxes'][0].get_ydata()[2]], 'k-', lw=2, color = '#0066b2')
ax.plot([0.68, 0.73], [box['boxes'][0].get_ydata()[0], box['boxes'][0].get_ydata()[0]], 'k-', lw=2, color = '#0066b2')
ax.plot([0.68, 0.73], [box['boxes'][0].get_ydata()[2], box['boxes'][0].get_ydata()[2]], 'k-', lw=2, color = '#0066b2')


#bottom bracket
ax.plot([0.7, 0.70], [89, box['whiskers'][0].get_ydata()[1]], 'k-', lw=2, color = '#0066b2')
ax.plot([0.7, .75], [89, 89], 'k-', lw=2, color = '#0066b2')
ax.plot([0.7, 0.75], [box['whiskers'][0].get_ydata()[1], box['whiskers'][0].get_ydata()[1]], 'k-', lw=2, color = '#0066b2')


# Final touches
ax.set_xticks([])
ax.set_yticks(range(50, 170, 25))
ax.set_ylabel('Data Values')

plt.show()