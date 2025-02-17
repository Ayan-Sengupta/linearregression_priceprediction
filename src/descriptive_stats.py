import pandas as pd

# Read CSV (listings_clean.csv) into a pandas DataFrame
listings_df = pd.read_csv('data/processed/listings_clean.csv')

# descriptive statistics for the cleaned data on the following columns -  Accommodates, bathrooms, bedrooms, review_scores_rating, minimum_nights
desc_stats = listings_df[['accommodates', 'bathrooms', 'bedrooms', 'review_scores_rating', 'minimum_nights']].describe()
print(desc_stats)