import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

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

decomposition = seasonal_decompose(new_df["Temperature in Degrees C"], period=288)
trend = decomposition.trend
seasonal_decompose = decomposition.seasonal
residual = decomposition.resid

x = new_df["Time and Date"]
y = new_df["Temperature in Degrees C"]

fig, axs = plt.subplots(4, 1, figsize=(6, 10))
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


plt.show()

min_value = new_df["Temperature in Degrees C"].min()
print(min_value)
