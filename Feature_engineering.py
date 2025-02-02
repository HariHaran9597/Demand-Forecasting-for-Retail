import pandas as pd

data = pd.read_csv(r'Dataset\walmart.csv')
# One-hot encode categorical variables
data = pd.get_dummies(data, columns=['Gender', 'City_Category', 'Age', 'Stay_In_Current_City_Years'], drop_first=True)

# Label encode 'Product_Category' (if needed)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['Product_Category'] = le.fit_transform(data['Product_Category'])

# Total purchases per user
data['Total_Purchases_User'] = data.groupby('User_ID')['Purchase'].transform('sum')

# Average purchase per product
data['Avg_Purchase_Product'] = data.groupby('Product_ID')['Purchase'].transform('mean')