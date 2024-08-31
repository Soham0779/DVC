import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

# Load the data
train_df = pd.read_csv('data/raw/train.csv')
test_df = pd.read_csv('data/raw/test.csv')

# Separate features and target
X_train = train_df.drop(columns=['medv', 'ID'])
y_train = train_df['medv']

X_test = test_df.drop(columns=['ID'])
# We don't have the true labels for test set in this example, so we'll just use a dummy y_test
y_test = [0] * len(X_test)

# Train a simple model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate and log metrics
mse = mean_squared_error(y_train, model.predict(X_train))
print(f"Mean Squared Error: {mse}")

input_example = pd.DataFrame({
    "crim": [0.1],
    "zn": [18.0],
    "indus": [2.31],
    "chas": [0],
    "nox": [0.538],
    "rm": [6.575],
    "age": [65.2],
    "dis": [4.09],
    "rad": [1],
    "tax": [296],
    "ptratio": [15.3],
    "black": [396.9],
    "lstat": [4.98]
})

# Log the model with MLflow
mlflow.set_experiment("basic-ml-project")

with mlflow.start_run():
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("mse", mse)

    # Log the model with input example
    input_example = X_train.head(1)  # Using the first row as an example
    mlflow.sklearn.log_model(model, "model", input_example=input_example)
    
    # Log the trained model
    mlflow.sklearn.log_model(model, "model")

    print(f"Run ID: {mlflow.active_run().info.run_id}")
    print(f"Experiment ID: {mlflow.active_run().info.experiment_id}")
