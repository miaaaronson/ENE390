from scipy import fftpack
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import signal

raw_df = pd.read_csv(
    "/Users/miaaaronson/Desktop/ENE390/Thesis_Work/Data/ALL_BUBBLE_DATA_2024.csv"
)

# consolidating relevant data by isolating based on the title of the column
df = raw_df[
    [
        "Site",
        "X2",
        "X2.1",
        "X2.2",
        "X2.3",
        "X2.4",
    ]
]

# setting the second row (with an index of 1) as the column headers (getting rid of Legacy.XX)
df.columns = df.iloc[1]

# removing the first two rows because the first intital row (Legacy Row) is not needed and the second row is now the index row (doesnt need to be in data set)
df = df[2:].reset_index(drop=True)

# turning the column names into a list to manipulate names
column_names = df.columns.to_list()

# Assign new names to specific NaN columns by index
column_names[0] = "Time and Date"  # Rename first NaN column
column_names[3] = "pH Value"  # Rename another NaN column

# Set updated column names back to DataFrame
df.columns = column_names

# renaming the column titles to better fit with the data set
df.rename(
    columns={
        "C": "Temperature in Degrees C",
        "uS/cm": "Specific Conductivity in uS/cm",
        "%": "ODO Saturation Percentage",
        "mg/L": "ODO in mg/L",
    },
    inplace=True,
)

df = df.dropna(subset=["Temperature in Degrees C"])

df["Time and Date"] = pd.to_datetime(df["Time and Date"], format="%m-%d-%Y %H:%M:%S")
df["Temperature in Degrees C"] = pd.to_numeric(
    df["Temperature in Degrees C"], errors="coerce"
)

min_threshold = 9
df = df[df["Temperature in Degrees C"] > min_threshold]
max_threshold = 15
df = df[df["Temperature in Degrees C"] < max_threshold]

x = df["Time and Date"]
y = df["Temperature in Degrees C"]
y_smooth = signal.savgol_filter(y, window_length=500, polyorder=3, mode="nearest")

df.head()

plt.plot(x, y)
plt.plot(x, y_smooth)
plt.show()
df.describe()
