# Excel Interpreter Library
import pandas as pd

# Visualization Library
import matplotlib.pyplot as plt

# Reading the Excel File
raw_data = pd.read_excel(
    "/Users/miaaaronson/Desktop/VS Code Repositories/Graphing_Basics/Data/Bubble_Temp_Data_Practice.xlsx"
)

# Making the index the time and date
raw_data = raw_data.set_index("Time and Date")

# adding in the smoothed data
smoothed_data = raw_data.rolling(window=500, center=True).mean()
# window controls the amount of points it is averaging

# Plotting the Raw Data
plt.plot(raw_data.index, raw_data["Temperature in C"], label="Raw Data")

# Plotting the Smoothed Data
plt.plot(
    smoothed_data.index,
    smoothed_data["Temperature in C"],
    label="Smoothed Data",
    color="red",
)

plt.ylabel("Temperature in Degrees C")  # yaxis label
plt.title("Bubble Temperature Practice Graph #1 Raw")  # title label

# legend
plt.legend()

# showing the plot
plt.show

