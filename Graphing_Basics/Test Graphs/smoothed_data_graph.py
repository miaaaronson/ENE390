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

# Printing the Data in the interactive window
print(raw_data)

# Applying a Moving Average to smooth out the data points
smoothed_data = raw_data.rolling(window=500, center=True).mean()
# window controls the amount of points it is averaging


# What parameters we are plotting
plt.plot(
    smoothed_data.index,
    smoothed_data["Temperature in C"],
    label="Smoothed Data",
    color="blue",
)
plt.xlabel("Date")  # x axis label
plt.ylabel("Temperature in Degrees C")  # yaxis label
plt.title("Bubble Temperature Practice Graph #1 Smooth")  # title label

# show the plot
plt.show
