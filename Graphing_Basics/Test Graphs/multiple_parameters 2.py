# Excel reading Library
import pandas as pd

# Visualization Library
import matplotlib.pyplot as plt

# Reading the Excel File
mp = pd.read_excel(
    "/Users/miaaaronson/Desktop/VS Code Repositories/Graphing_Basics/Data/Multiple_Parameters_Data_Bubble.xlsx"
)

# Making the index the time and date
mp = mp.set_index("Time and Date")

# Printing the Data in the interactive window
print(mp)

# Defining the figure and the two differnt axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Inputting all the information for the first (left hand side) y axis
ax1.plot(mp.index, mp["EXO Temp in C"], label="Temperature in C", color="blue")
ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature", color="blue")

# Creating a second y axis
ax2 = ax1.twinx()

# Inputting all the information for the second (right hand side) y axis
ax2.plot(mp.index, mp["EXO pH"], label="EXO pH", color="red")
ax2.set_xlabel("Time")
ax2.set_ylabel("pH", color="red")


# legend
plt.legend()

# showing the plot
plt.show
