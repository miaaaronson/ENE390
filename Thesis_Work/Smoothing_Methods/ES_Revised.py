import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# importing raw data (like from a raw CSV or excel file that someone downloaded and gave to me)
raw_df = pd.read_csv(
    "/Users/miaaaronson/Desktop/ENE390/Thesis_Work/Data/Bubble Data Compiled - 03_01-19_2022.csv"
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

exponential_smoothing_model = ExponentialSmoothing(
    y, trend=None, seasonal=None, damped_trend=False
)
fit_model = exponential_smoothing_model.fit()

y_smooth = fit_model.predict(
    start=len(df["Temperature in Degrees C"]), end=len(df["Temperature in Degrees C"])
)

# projecting smoothing method onto all of the time points
y_smooth = fit_model.fittedvalues

# plotting
plt.plot(x, y, label="Raw Data", color="#BCD2E8")
plt.plot(x, y_smooth, label="Smoothed Data", color="#0818A8")

# labels
plt.xlabel("Time and Date")
plt.ylabel("Water Temperature in Degrees C")

# rotating the x axis labels so I can read them
plt.xticks(x[::500], rotation=45)
plt.ylim(13.142, 13.1555)
plt.title(
    "Water Temperature of Bubble using an EXO Sonde: 03012022-03182022; Exponential Smoothing Method"
)
plt.legend()

# showing the plot
plt.show()
