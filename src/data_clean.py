import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Read CSV (listings.csv) into a pandas DataFrame
listings_df = pd.read_csv('data/raw/listings.csv')

# Display the first few rows of the DataFrame
# print(listings_df.head())
# print(listings_df.info())
# print(listings_df.shape)

# # find unique location in the dataset 
# print(listings_df['host_location'].unique())


# only looking at Asheville, NC, dropping all other locations including empty ones 
listings_df = listings_df[listings_df['host_location'] == 'Asheville, NC']

# drop rows where price value is missing 
listings_df = listings_df[listings_df['price'].notna()]

# check if price column has any missing values 
price_nullFlag = listings_df['price'].isnull().sum()



# Create a dummy variable column to indicate if review_scores_rating is missing
listings_df['has_review_scores'] = listings_df['review_scores_rating'].notna().astype(int)

# replace missing values in review_scores_rating with a 0 
listings_df['review_scores_rating'] = listings_df['review_scores_rating'].fillna(0)

# check if accommodates, bathrooms, bedrooms, minumum_nights and review_score_ratings columns have any missing values
missing_values = [
    listings_df['accommodates'].isnull().sum(),
    listings_df['bathrooms'].isnull().sum(),
    listings_df['bedrooms'].isnull().sum(),
    listings_df['minimum_nights'].isnull().sum(),
    listings_df['review_scores_rating'].isnull().sum()
]

# loop thrrough missing values list and make sure each entry is 0 
sum = 0
for i in missing_values:
    sum += i
   
print(sum)

# if no missing value, write the df to a new csv file
if price_nullFlag == 0 and sum == 0:
    listings_df.to_csv('data/processed/listings_clean.csv', index=False)





