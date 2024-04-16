import numpy as np
import pandas as pd
df = pd.read_csv("Customer Data.csv")

# Identify missing values:
missing_values = df.isnull()

# Count the number of missing values in each column:
missing_count = df.isnull().sum()

# Handling missing values:
df_cleaned_rows = df.dropna()  # Remove rows containing missing values
df_cleaned_columns = df.dropna(axis=1)  # Remove columns containing missing values
