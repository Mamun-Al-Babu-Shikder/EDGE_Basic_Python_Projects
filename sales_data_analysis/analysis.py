import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("files/sales_data.csv")

df.dropna(thresh=2, inplace=True)  # remove nan/null data
df.drop_duplicates(inplace=True)  # remove duplicate data
qs_mean = df['Quantity Sold'].mean()  # find mean value for 'Quantity Sold'

# use this approach for complex update
# for i in df['Quantity Sold'].index:
#     if str(df.loc[i , 'Quantity Sold']) == "nan":
#         df.loc[i , 'Quantity Sold'] = qs_mean

# replace NaN data to valid data
df['Quantity Sold'].fillna(qs_mean, inplace=True)
df['Price Per Unit'].fillna(method='bfill', inplace=True)

# cast column existing type to proper type
df['Date'] = pd.to_datetime(df['Date'])
df['Quantity Sold'] = df['Quantity Sold'].astype('int64')

# extends current DataFrame
df['Total Sale'] = df['Quantity Sold'] * df['Price Per Unit']
df['Month Periodic'] = df['Date'].dt.to_period('M')

# how to sort data according to specific column
# print(df[['Date', 'Month Periodic']].sort_values('Month Periodic').to_string(index=False))

# find monthly sold quantity and represent as graph
mp_group = df.groupby('Month Periodic')
mp_qs_df = mp_group['Quantity Sold'].sum().reset_index()
mp_qs_df['Month Periodic'] = mp_qs_df['Month Periodic'].astype(str)
plt.bar(mp_qs_df['Month Periodic'], mp_qs_df['Quantity Sold'])
plt.xlabel('Month')
plt.ylabel('Quantity Sold')
plt.show()

# find monthly total sales and represent as graph
mp_qts_df = mp_group['Total Sale'].sum().reset_index()
mp_qts_df.sort_values(by=['Month Periodic'], ascending=True, inplace=True)
mp_qts_df['Month Periodic'] = mp_qs_df['Month Periodic'].astype(str)
plt.plot(mp_qts_df['Month Periodic'], mp_qts_df['Total Sale'])
plt.xlabel('Month')
plt.ylabel('Total Sale')
plt.show()

# find categories quantity sold and represent as graph
cat_group = df.groupby('Category')
cs_df = cat_group['Quantity Sold'].sum().reset_index()
plt.pie(cs_df['Quantity Sold'], labels=cs_df['Category'], autopct='%1.1f%%')
plt.show()

