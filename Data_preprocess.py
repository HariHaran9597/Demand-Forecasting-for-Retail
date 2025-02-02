import pandas as pd

# Load the dataset
data = pd.read_csv(r'Dataset\walmart.csv')

# Features (X)
X = data.drop(columns=['Purchase', 'User_ID', 'Product_ID'])

# Target (y)
y = data['Purchase']

# Display the first 5 rows of features (X)
print(X.head())

# Display the first 5 rows of target (y)
print(y.head())

from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the splits
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")