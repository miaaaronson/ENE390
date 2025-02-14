# importing pandas to read the excel file and conver to a csv file
import pandas as pd

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
