import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from scipy import signal

# importing raw data (like from a raw CSV or excel file that someone downloaded and gave to me)
raw_df = pd.read_csv(
    "/Users/miaaaronson/Desktop/ENE390/Thesis_Work/Data/Smoothing_Data.csv"
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

df = df.dropna(subset=["Temperature in Degrees C"])

df["Time and Date"] = pd.to_datetime(df["Time and Date"], format="%m-%d-%Y %H:%M:%S")
df["Temperature in Degrees C"] = pd.to_numeric(
    df["Temperature in Degrees C"], errors="coerce"
)

x = df["Time and Date"]
y = df["Temperature in Degrees C"]

# exponential smoothing
exponential_smoothing_model = ExponentialSmoothing(
    y, trend=None, seasonal=None, damped_trend=False
)
fit_model = exponential_smoothing_model.fit()
y_smooth_es = fit_model.predict(
    start=len(df["Temperature in Degrees C"]), end=len(df["Temperature in Degrees C"])
)
y_smooth_es = fit_model.fittedvalues

# moving average
y_smooth_ma = y.rolling(window=50, center=True).mean()

# SGF
y_smooth_SGF = signal.savgol_filter(y, window_length=150, polyorder=3, mode="nearest")

fig, axs = plt.subplots(4, 1, figsize=(6, 9))
plt.subplots_adjust(
    left=0.2,
    bottom=0.13,
    hspace=0.4,
)  # Adjust the vertical space between subplots
fig.supylabel("Temperature in Degrees C", fontsize=12)  # Single large y-axis label
fig.supxlabel("Date", fontsize=12)  # Single large x-axis label
for ax in axs[:-1]:
    ax.tick_params(
        axis="x", which="both", bottom=False, top=False, labelbottom=False
    )  # Remove x-axis tick marks


# raw data graph
axs[0].plot(x, y, label="Raw Data", color="#7393B3")
axs[0].set_title("Raw Data")
axs[0].legend()

# ES graph
axs[1].plot(x, y, label="Raw Data", color="#BCD2E8")
axs[1].plot(x, y_smooth_es, label="Smoothed Data", color="#0818A8")
axs[1].set_title("Exponential Smoothing Method")
axs[1].legend()

# MS graph
axs[2].plot(x, y, label="Raw Data", color="#BCD2E8")
axs[2].plot(x, y_smooth_ma, label="Smoothed Data", color="#0818A8")
axs[2].set_title("Moving Average Smoothing Method")
axs[2].legend()

# SGF graph
axs[3].plot(x, y, label="Raw Data", color="#BCD2E8")
axs[3].plot(x, y_smooth_SGF, label="Smoothed Data", color="#0818A8")
axs[3].set_xticks(x[::500])
axs[3].tick_params(axis="x", rotation=45)
axs[3].set_title("Savitzky-Golay Filtering Smoothing Method")
axs[3].legend()

plt.show()
