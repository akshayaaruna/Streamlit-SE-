import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import LabelEncoder
import streamlit as st

# label_encoder = LabelEncoder()
# Load your data into a Pandas DataFrame (replace 'data.csv' with your dataset)
data = pd.read_csv('random_dataset.csv')

# Define features (X) and target variable (y)
# X = data.drop(columns=['SalesPercentage'])
X = data[['Year','Season','Products']]  # Features
# X = data[['Year','Season']]  # Features
y = data['SalesPercentage']  # Target variable
# data['SeasonEncoded'] = label_encoder.fit_transform(data['Season'])
# data['ProductEncoded'] = label_encoder.fit_transform(data['Products'])
# Perform one-hot encoding on the 'Season' column

X = pd.get_dummies(X, columns=['Season', 'Products'], drop_first=False)
# X = pd.get_dummies(X, columns=['Season'], drop_first=False)

# Set feature names explicitly
# X.columns = ['Year', 'Season_PostMonsoon', 'Season_Rainy', 'Season_Summer', 'Season_Winter']

# Split the data into 80% training and 20% testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a Linear Regression model
model = LinearRegression()

# Repeat for other product categories

# Train the model using the training data
model.fit(X_train, y_train)


# Print the model's features and their coefficients
print("Model Features and Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")

# Make predictions on the test data
predictions = model.predict(X_test)
# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, predictions)

# Calculate R-squared (R2 score)
r2 = r2_score(y_test, predictions)

print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared (R2 score): {r2}')
# Save the trained model to a file
joblib.dump(model, 'linear_regression_model.pkl')

# Print a message indicating that the model is saved
print('Trained model saved as linear_regression_model.pkl')

