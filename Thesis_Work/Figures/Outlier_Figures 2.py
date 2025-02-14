import matplotlib.pyplot as plt
import seaborn as sns
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

df["Unnamed: 0"] = pd.to_datetime(df["Unnamed: 0"], format="%m-%d-%Y %H:%M:%S")

fig, axes = plt.subplots(1,2, figsize =(10,10))
sns.boxplot(df['C'], ax=axes[1])
sns.boxenplot(df['uS/cm'], ax=axes[0])


plt.show
