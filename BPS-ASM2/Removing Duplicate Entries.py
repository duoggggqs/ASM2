import numpy as np
import pandas as pd
# Read data into DataFrame:
df = pd.read_csv("Product Data.csv")

# Find duplicate records
duplicate_entries = df.duplicated()

# Remove duplicate records
df_cleaned = df.drop_duplicates()

# Store the DataFrame with deduplicated records into a CSV file
df_cleaned.to_csv("data_cleaned.csv", index=False)