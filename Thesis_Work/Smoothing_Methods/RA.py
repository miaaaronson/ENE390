import pandas as pd
import matplotlib.pyplot as plt

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

# create the moving average
y_smooth = df["C"].rolling(window=100).mean()
# changing the window values changes the smoothness of the graph

# contents of the plot
plt.plot(x_values, y_smooth, color="green")

# lables
plt.xlabel("Time and Date")
plt.ylabel("Water Temperature in Degrees C")
plt.title("Water Temperature of Bubble using an EXO Sonde: 01012024-03132024")
plt.ylim(13.15, 13.195)
plt.legend()

# showing the plot
plt.show()
