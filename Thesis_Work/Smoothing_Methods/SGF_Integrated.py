import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# creating a data frame from the CSV file that has all of the data we need to use
df = pd.read_csv(
    "/Users/miaaaronson/Desktop/VS Code Repositories/Thesis_Work/Data/Bubble Data Compiled - Copy of Copy of 01_01_2024 - 03_13_2024.csv",
    skiprows=2,
)
df["Unnamed: 0"] = pd.to_datetime(df["Unnamed: 0"])
df = df.drop(
    index=0,
)
print(df.head())

df["Unnamed: 0"] = pd.to_datetime(df["Unnamed: 0"], format="%m-%d-%Y %H:%M:%S")

# assign the variables
x_values = df["Unnamed: 0"]
y_values = df["C"]

# smoothed y values
y_smooth = signal.savgol_filter(
    y_values, window_length=200, polyorder=3, mode="nearest"
)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, y_values, color="#A7C7E7", markersize=0.1, label="Raw")
ax.plot(x_values, y_smooth, color="#0818A8", markersize=0.1, label="Smooth")

# labels
ax.set_xlabel("Time and Date")
ax.set_ylabel("Water Temperature in Degrees C")
ax.set_title("Water Temperature of Bubble using an EXO Sonde: 01012024-03132024")
ax.set_ylim(10, 16)
ax.legend()


axins = inset_axes(ax, width="30%", height="30%", loc="upper right")
axins.plot(x_values, y_values, color="#A7C7E7", markersize=0.1)
axins.plot(x_values, y_smooth, color="#0818A8", markersize=0.1)
axins.set_ylim(13.135, 13.2)

for label in axins.get_xticklabels():
    label.set_rotation(90)
    label.set_fontsize(7)
