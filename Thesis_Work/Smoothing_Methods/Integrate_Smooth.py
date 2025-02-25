from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

# importing raw data (like from a raw CSV or excel file that someone downloaded and gave to me)
raw_df = pd.read_csv(
    "/Users/miaaaronson/Desktop/ENE390/Thesis_Work/Data/Bubble Data Compiled - 03_01-19_2022 2.csv"
)

# consolidating relevant data by isolating based on the title of the column
df = raw_df[
    [
        "Site",
        "X2 Legacy.12",
        "X2 Legacy.13",
        "X2 Legacy.14",
        "X2 Legacy.15",
        "X2 Legacy.16",
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

df.head()

# converting the index column to time and date
df["Time and Date"] = pd.to_datetime(df["Time and Date"], format="%m-%d-%Y %H:%M:%S")
df["Temperature in Degrees C"] = pd.to_numeric(
    df["Temperature in Degrees C"], errors="coerce"
)

# assign the variables
x = df["Time and Date"]
y = df["Temperature in Degrees C"]

# smoothed y values
y_smooth = signal.savgol_filter(y, window_length=200, polyorder=3, mode="nearest")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, color="#A7C7E7", markersize=0.1, label="Raw")
ax.plot(x, y_smooth, color="#0818A8", markersize=0.1, label="Smooth")

# labels
ax.set_xlabel("Time and Date")
ax.set_ylabel("Water Temperature in Degrees C")
ax.set_title("Integrated Graph Example Using SGF")
ax.set_ylim(11, 15)
ax.tick_params(axis="x", rotation=45)
ax.legend()


axins = inset_axes(ax, width="30%", height="30%", loc="upper right")
axins.plot(x, y, color="#A7C7E7", markersize=0.1)
axins.plot(x, y_smooth, color="#0818A8", markersize=0.1)
axins.set_ylim(13.144, 13.153)
for label in axins.get_xticklabels():
    label.set_rotation(45)
    label.set_fontsize(7)
