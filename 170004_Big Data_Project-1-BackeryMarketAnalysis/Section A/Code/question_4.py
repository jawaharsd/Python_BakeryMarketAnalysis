
#Jawahar_170004



import pandas as pd
import matplotlib.pyplot as plt



Bakery_data_set = pd.read_csv("G:/semester 7/Bigdata-2/Week 7/BreadBasket_DMS.csv")
Bakery_data_set.dropna()
Bakery_data_set = Bakery_data_set[Bakery_data_set['Item'] != 'NONE']

Bakery_data_set['Date'] = pd.to_datetime(Bakery_data_set['Date'])
Bakery_data_set['Time'] = pd.to_datetime(Bakery_data_set['Time'])
Bakery_data_set['Year'] = Bakery_data_set['Date'].dt.year
Bakery_data_set['Month'] = Bakery_data_set['Date'].dt.month
Bakery_data_set['Day'] = Bakery_data_set['Date'].dt.day
Bakery_data_set['Weekday'] = Bakery_data_set['Date'].dt.weekday
Bakery_data_set['Hour'] = Bakery_data_set['Time'].dt.hour

def map_indexes_and_values(df, col):
    df_col = df[col].value_counts()
    x = df_col.index.tolist()
    y = df_col.values.tolist()
    return x, y


print("This is Question 4")
monday_info = Bakery_data_set[Bakery_data_set['Weekday'] == 0]
item, item_count = map_indexes_and_values(monday_info, 'Item')

plt.bar(item[:5], item_count[:5], color='r', label='Monday')
plt.xlabel('Popular items on Monday')
plt.ylabel('Number of Transactions')
plt.show()

print("5 most popular items sold on monday is:","\n", monday_info[:5])