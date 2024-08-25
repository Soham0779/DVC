from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

# Load data
train_data = pd.read_csv('data/raw/train.csv')

# Define features and target
X = train_data.drop(columns=['ID', 'medv'])  # Exclude 'ID' and target variable
y = train_data['medv']

# Split the data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_valid)

# Evaluate the model
mse = mean_squared_error(y_valid, y_pred)
print(f"Mean Squared Error: {mse}")
