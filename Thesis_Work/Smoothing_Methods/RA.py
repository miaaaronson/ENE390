import pandas as pd
import matplotlib.pyplot as plt

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


# What parameters we are plotting
plt.plot(x, y, label="Raw Data", color="#0F52BA")
plt.xlabel("Date")  # x axis label
plt.xticks(x[::500], rotation=45)
plt.ylabel("Temperature in Degrees C")  # yaxis label
plt.title("Raw Data Graph Example")  # title label
plt.legend()

# show the plot
plt.show
