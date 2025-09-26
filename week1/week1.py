import pandas as pd



    # Read csv file from week1 folder
df = pd.read_csv("LI_BUILDING_FOOTPRINTS.csv")
if df.empty:
    raise Exception("Error: Unable locate CSV file!")

# Check first 2 rows
print(df.describe())
print(df.head(3))
