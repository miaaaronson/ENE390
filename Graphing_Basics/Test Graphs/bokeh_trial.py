# importing the modules 
from bokeh.plotting import figure, output_file, show 
import pandas as pd

# instantiating the figure object 
graph = figure(title = "Bokeh Line Graph") 

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


# plotting the line graph 
graph.line(x_values, y_values) 

# displaying the model 
show(graph)
