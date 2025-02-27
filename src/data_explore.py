import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV (listings_clean.csv) into a pandas DataFrame
listings_df = pd.read_csv('data/processed/listings_clean.csv')

# find correlation b/w the selected colunms - 'accommodates', 'bathrooms', 'bedrooms', 'review_scores_rating', 'minimum_nights'
correlation = listings_df[['accommodates', 'bathrooms', 'bedrooms', 'review_scores_rating', 'minimum_nights']].corr()
# Heatmap of the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

# PLot histograms for the selected columns
def plot_histograms(df, columns):
    for column in columns:
        plt.figure(figsize=(10, 6))
        df[column].plot.hist()
        plt.title(f"Distribution of {column.replace('_', ' ').title()}")
        plt.xlabel(column.replace('_', ' ').title())
        plt.ylabel("Frequency")
        plt.show()

# Columns to plot
columns_to_plot = [
    "accommodates",
    "bathrooms",
    "bedrooms",
    "review_scores_rating",
    "minimum_nights"
]

# Plot histograms
plot_histograms(listings_df, columns_to_plot)