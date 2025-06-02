import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from scipy import signal
from statsmodels.nonparametric.smoothers_lowess import lowess

raw_df_2024 = pd.read_csv(
    "/Users/miaaaronson/Desktop/ENE390/Thesis_Work/Data/ALL_BUBBLE_DATA_2024.csv"
)
raw_df_2023 = pd.read_csv(
    "/Users/miaaaronson/Desktop/ENE390/Thesis_Work/Data/ALL_BUBBLE_DATA_2023.csv"
)
raw_df_2021to032023 = pd.read_csv(
    "/Users/miaaaronson/Desktop/ENE390/Thesis_Work/Data/ALL_BUBBLE_TEMPS_2021to03:2023 2.csv"
)


def clean_water_data(raw_df):
    # Consolidate relevant data by selecting specific columns
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

    # Set the second row as column headers
    df.columns = df.iloc[1]

    # Remove the first two rows and reset index
    df = df[2:].reset_index(drop=True)

    # Convert column names to a list for manipulation
    column_names = df.columns.to_list()

    # Rename specific NaN columns
    column_names[0] = "Time and Date"
    column_names[3] = "pH Value"

    # Set updated column names back to DataFrame
    df.columns = column_names

    # Rename other columns for clarity
    df.rename(
        columns={
            "C": "Temperature (C)",
            "uS/cm": "Specific Conductivity (uS/cm)",
            "%": "ODO (Saturation)",
            "mg/L": "ODO (mg/L)",
        },
        inplace=True,
    )

    # Drop rows where Temperature in Degrees C is NaN
    df = df.dropna(subset=["Temperature (C)"])

    # Convert columns to appropriate data types
    df["Time and Date"] = pd.to_datetime(
        df["Time and Date"], format="%m-%d-%Y %H:%M:%S"
    )
    df["Temperature (C)"] = pd.to_numeric(df["Temperature (C)"], errors="coerce")

    return df


final_2021on = raw_df_2021to032023.iloc[2:]
final_2021on = final_2021on.dropna()
final_2021on.rename(columns={"C": "Temperature (C)"}, inplace=True)
final_2021on["Time and Date"] = pd.to_datetime(
    final_2021on["Time and Date"], format="%m-%d-%Y %H:%M:%S"
)
x_1 = final_2021on["Time and Date"]
y_1 = final_2021on["Temperature (C)"]

final_2024 = clean_water_data(raw_df_2024)
final_2024 = final_2024[["Time and Date", "Temperature (C)"]]
x_3 = final_2024["Time and Date"]
y_3 = final_2024["Temperature (C)"]

final_2023 = clean_water_data(raw_df_2023)
final_2023 = final_2023[["Time and Date", "Temperature (C)"]]
x_2 = final_2023["Time and Date"]
y_2 = final_2023["Temperature (C)"]


all_temp_data = pd.concat([final_2021on, final_2023, final_2024]).reset_index(drop=True)

max_threshold = 13.3
min_threshold = 13

x = all_temp_data["Time and Date"]
y = all_temp_data[
    [
        (all_temp_data["Temperature (C)"] > min_threshold)
        & (all_temp_data["Temperature (C)"] < max_threshold)
    ]
]


# exponential smoothing
exponential_smoothing_model = ExponentialSmoothing(
    y, trend=None, seasonal=None, damped_trend=False
)
fit_model = exponential_smoothing_model.fit()
y_smooth_es = fit_model.predict(
    start=len(all_temp_data["Temperature (C)"]),
    end=len(all_temp_data["Temperature (C)"]),
)
y_smooth_es = fit_model.fittedvalues

# moving average
y_smooth_ma = y.rolling(window=50, center=True).mean()

# SGF
y_smooth_SGF = signal.savgol_filter(y, window_length=150, polyorder=3, mode="nearest")

# lowess
smoothed = lowess(
    all_temp_data["Temperature (C)"], range(len(all_temp_data)), frac=0.05
)

fig, axs = plt.subplots(5, 1, figsize=(6, 10))
plt.subplots_adjust(
    left=0.2,
    bottom=0.13,
    hspace=0.4,
)
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

axs[3].plot(all_temp_data["Temperature (C)"], label="Raw Data", color="#BCD2E8")
axs[3].plot(smoothed[:, 1], label="Smoothed Values", color="#0818A8")
axs[3].set_title("Lowess Smoothing Method")
axs[3].legend()

# SGF graph
axs[4].plot(x, y, label="Raw Data", color="#BCD2E8")
axs[4].plot(x, y_smooth_SGF, label="Smoothed Data", color="#0818A8")
axs[4].set_xticks(x[::10000])
axs[4].tick_params(axis="x", rotation=45)
axs[4].set_title("Savitzky-Golay Filtering Smoothing Method")
axs[4].legend()

plt.show()
