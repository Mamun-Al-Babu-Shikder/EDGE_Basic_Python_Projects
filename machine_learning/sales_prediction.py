import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('files/sales_data.csv')

# change data type
df['Date'] = pd.to_datetime(df['Date'])

# add a new column called 'Total Sale Amount'
df['Total Sale Amount'] = df['Price Per Unit'] * df['Quantity Sold']

# add new columns for 'Day', 'Month', 'Year'
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# hence the 'Category' column is label data, so we need to encode it
category_encoder = LabelEncoder()
df['Encoded Category'] = category_encoder.fit_transform(df['Category'])

# extract features and target
X = df[['Day', 'Month', 'Year', 'Encoded Category']]
y = df['Total Sale Amount']

# train the model
model = DecisionTreeRegressor()
model.fit(X, y)

# make prediction
encoded_value = category_encoder.transform(['Electronics'])[0]
data = pd.DataFrame([[2, 5, 2025, encoded_value]], columns=['Day', 'Month', 'Year', 'Encoded Category'])

pred = model.predict(data)
print(pred)
