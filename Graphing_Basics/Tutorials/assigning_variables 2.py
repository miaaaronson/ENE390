import pandas as pd

# usually I import my files as excel files, so the following is a conversion to a csv file ... this is not necessary if the file is already in csv format

# create a variable that is the path of the excel file
excel_file_path = "/Users/miaaaronson/Desktop/VS Code Repositories/Graphing_Basics/Data/Bubble_Temp_Data_Practice.xlsx"

# create a dataframe where pandas reads the excel file and storers the data
df = pd.read_excel(
    "/Users/miaaaronson/Desktop/VS Code Repositories/Graphing_Basics/Data/Bubble_Temp_Data_Practice.xlsx"
)

# create a variable that is the path of the excel but changing .xlsx to .csv
csv_file_path = "/Users/miaaaronson/Desktop/VS Code Repositories/Graphing_Basics/Data/Bubble_Temp_Data_Practice.csv"

# conversion from excel to csv using pandas
df.to_csv(csv_file_path, index=False)

# reading the csv file
pd.read_csv(
    "/Users/miaaaronson/Desktop/VS Code Repositories/Graphing_Basics/Data/Bubble_Temp_Data_Practice.csv"
)

# print the first 5 lines of the file in order to verify that it worked - not super necessary, but good to see what the column titles are.
print(df.head())

# assign one parameter to the x-values and the other to the y-values
x_values = df["Time and Date"]
y_values = df["Temperature in C"]

# make sure the the values were correctly assigned
print(x_values)
print(y_values)
