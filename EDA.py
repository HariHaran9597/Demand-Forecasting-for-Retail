import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = pd.read_csv(r'Dataset\walmart.csv')
# Plot purchase distribution
sns.histplot(data['Purchase'], bins=50, kde=True)
plt.title('Purchase Distribution')
plt.show()

# Group by product category
sales_by_category = data.groupby('Product_Category')['Purchase'].sum()

# Plot sales by category
sales_by_category.plot(kind='bar')
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()

# Group by gender
sales_by_gender = data.groupby('Gender')['Purchase'].sum()

# Plot sales by gender
sales_by_gender.plot(kind='bar')
plt.title('Sales by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Sales')
plt.show()