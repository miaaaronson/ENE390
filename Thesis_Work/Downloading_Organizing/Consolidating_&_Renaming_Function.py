import pandas as pd


def clean_water_data(raw_df):
    # Consolidate relevant data by selecting specific columns
    df = raw_df[
        [
            "Site",
            "X2",
            "X2.1",
            "X2.2",
            "X2.3",
            "X2.4",
        ]
    ]

    # Set the second row as column headers
    df.columns = df.iloc[1]

    # Remove the first two rows and reset index
    df = df[2:].reset_index(drop=True)

    # Convert column names to a list for manipulation
    column_names = df.columns.to_list()

    # Rename specific NaN columns
    column_names[0] = "Time and Date"
    column_names[3] = "pH Value"

    # Set updated column names back to DataFrame
    df.columns = column_names

    # Rename other columns for clarity
    df.rename(
        columns={
            "C": "Temperature (C)",
            "uS/cm": "Specific Conductivity (uS/cm)",
            "%": "ODO (Saturation)",
            "mg/L": "ODO (mg/L)",
        },
        inplace=True,
    )

    # Drop rows where Temperature in Degrees C is NaN
    df = df.dropna(subset=["Temperature (C)"])

    # Convert columns to appropriate data types
    df["Time and Date"] = pd.to_datetime(
        df["Time and Date"], format="%m-%d-%Y %H:%M:%S"
    )
    df["Temperature (C)"] = pd.to_numeric(df["Temperature (C)"], errors="coerce")

    return df
