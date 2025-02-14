import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

sns.boxplot(df["C"])  # specifying which type of plot used to visualize the data
plt.ylabel("Temperature in Degrees C")
plt.title("Box Plot Outliers in Temperatures (C)")
plt.show
