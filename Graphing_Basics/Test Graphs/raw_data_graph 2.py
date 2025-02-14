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

# What parameters we are plotting
plt.plot(raw_data.index, raw_data["Temperature in C"], label="Raw Data")
plt.ylabel("Temperature in Degrees C")  # yaxis label
plt.title("Bubble Temperature Practice Graph #1 Raw")  # title label

# showing the plot
plt.show
