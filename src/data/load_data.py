import pandas as pd

def load_data(train_filepath='data/raw/train.csv', test_filepath='data/raw/test.csv'):
    """Load training and testing datasets from CSV files."""
    train_data = pd.read_csv(train_filepath)
    test_data = pd.read_csv(test_filepath)
    return train_data, test_data

if __name__ == "__main__":
    train_data, test_data = load_data()
    print("Training Data:")
    print(train_data.head())  # Display the first few rows of the training data
    print("\nTesting Data:")
    print(test_data.head())   # Display the first few rows of the testing data
