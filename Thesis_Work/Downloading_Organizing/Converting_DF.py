import pandas as pd

excel_file = "/Users/miaaaronson/Desktop/VS Code Repositories/Thesis_Work/Data/Downloading_and_Organizing.xlsx"
csv_file = "/Users/miaaaronson/Desktop/VS Code Repositories/Thesis_Work/Data/Downloading_and_Organizing.csv"


df = pd.read_excel (excel_file)
df.to_csv(csv_file, index = False)


print(df.head())