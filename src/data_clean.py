import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Read CSV (listings.csv) into a pandas DataFrame
listings_df = pd.read_csv('data/raw/listings.csv')

# Display the first few rows of the DataFrame
print(listings_df.head())
print(listings_df.info())
print(listings_df.shape)

# Check for missing values
