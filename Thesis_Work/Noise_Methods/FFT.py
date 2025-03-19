from scipy import fftpack
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/miaaaronson/Desktop/ENE390/Thesis_Work/Data/FFT.csv")

df.columns = df.iloc[1]
df = df[2:].reset_index(drop=True)
column_names = df.columns.to_list()
column_names[0] = "Time and Date"
column_names[3] = "pH Value"

df.columns = column_names

df.rename(
    columns={
        "C": "Temperature in Degrees C",
        "uS/cm": "Specific Conductivity in uS/cm",
        "%": "ODO Saturation Percentage",
        "mg/L": "ODO in mg/L",
    },
    inplace=True,
)

df = df.dropna()

df["Time and Date"] = pd.to_datetime(df["Time and Date"], format="%m-%d-%Y %H:%M:%S")
df["Temperature in Degrees C"] = pd.to_numeric(
    df["Temperature in Degrees C"], errors="coerce"
)

new_df = df[["Time and Date", "Temperature in Degrees C"]]
new_df.head()

min_value = new_df["Temperature in Degrees C"].min()
threshold = 13.0
new_df = new_df[new_df["Temperature in Degrees C"] > threshold]

x = new_df["Time and Date"]
y = new_df["Temperature in Degrees C"].values.astype(float)

# Sampling Rate
sampling_rate = 1 / 300  # one data point taken every five minutes (300 seconds)
total_time_seconds = 90 * 24 * 60 * 60  # during a 90 day cycle
t = np.arange(
    0, total_time_seconds, 300
)  # time stamp array from 0 to 90 days in five minute intervals (300 seconds)

# Performing the FFT
y_fft = fftpack.fft(y)
n = len(y)

# Frequency Array
frequency = sampling_rate / 2 * np.linspace(0, 1, n // 2)

# Magnitude
magnitude = 2 / n * np.abs(y_fft[0 : n // 2])

# Create the figure and axes
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

# Plot the time-domain signal (water temperature over time)
ax[0].plot(x, y)
ax[0].set_title("Time Domain: Water Temperature")
ax[0].set_xlabel("Time (seconds)")
ax[0].set_ylabel("Temperature (°C)")

# Plot the frequency-domain signal (magnitude of frequencies)
ax[1].stem(frequency, magnitude)
ax[1].set_title("Frequency Domain: Magnitude of Frequencies")
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")

# Show the plot
plt.tight_layout()
plt.show()
