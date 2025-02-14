from hampel import hampel
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "/Users/miaaaronson/Desktop/VS Code Repositories/Thesis_Work/Data/Bubble Data Compiled - Copy of Copy of 01_01_2024 - 03_13_2024.csv",
    skiprows=2,
)
df["Unnamed: 0"] = pd.to_datetime(df["Unnamed: 0"])
df = df.drop(
    index=0,
)
print(df.head())

time_parameter = df['Unnamed: 0']
temperature_parameter = df['C']

temperature_parameter.to_csv(
    "/Users/miaaaronson/Desktop/VS Code Repositories/Thesis_Work/Data/Parameter_Series.csv", 
    index=False
)

combined_df = pd.DataFrame({
    'Time and Date': time_parameter,
    'Temperature': temperature_parameter
})

result = hampel(combined_df ['Temperature'], window_size=10)

plt.plot (time_parameter, combined_df)
plt.show