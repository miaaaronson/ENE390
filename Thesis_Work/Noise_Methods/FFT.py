import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
