import pandas as pd

# Load the dataset
data = pd.read_csv(r'Dataset\walmart.csv')

# Display the first 5 rows
print(data.head())

# Check basic info about the dataset
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Fill missing values in 'Purchase' with the mean
data['Purchase'].fillna(data['Purchase'].mean(), inplace=True)