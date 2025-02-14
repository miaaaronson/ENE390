import pandas as pd

raw_df = pd.read_excel(
    "/Users/miaaaronson/Desktop/VS Code Repositories/Thesis_Work/Data/Downloading_and_Organizing.xlsx"
)

raw_df.head()

df = raw_df[
    [
        "Site",
        "X2 Legacy.12",
        "X2 Legacy.13",
        "X2 Legacy.14",
        "X2 Legacy.15",
        "X2 Legacy.16",
    ]
].copy()

df.dropna(inplace=True)
df.set_index("Site")

df.drop([0])

print(df)
