from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.model_selection import train_test_split

# Read CSV (listings_clean.csv) into a pandas DataFrame
listings_df = pd.read_csv('data/processed/listings_clean.csv')

# Define the independent variables and the dependent variable
# independent variables: 'accommodates', 'bathrooms', 'bedrooms', 'review_scores_rating', 'minimum_nights', 'has_review_scores'
X = listings_df[['accommodates', 'bathrooms', 'bedrooms', 'review_scores_rating', 'minimum_nights', 'has_review_scores']]

# dependent variable: 'price'
y = listings_df['price']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# normalize/scale the features to improve model performance 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fit a linear regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict the prices
y_pred = model.predict(X_test_scaled)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

# Calculate and print additional metrics
mean_price = y.mean()
percentage_error = (rmse / mean_price) * 100

print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"Mean Price: ${mean_price:.2f}")
print(f"Percentage Error: {percentage_error:.2f}%")
print(f"R squared: {model.score(X_test_scaled, y_test):.2f}")

# Model coefficients
print("Model Coefficients (Weights):", model.coef_) # weights
print("Model Intercept (Bias):", model.intercept_) #bias



