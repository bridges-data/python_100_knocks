import pandas as pd
import os
path = os.getcwd()

customer_master = pd.read_csv(f'{path}/1/customer_master.csv')
print(customer_master.head(5))

item_master = pd.read_csv(f'{path}/1/item_master.csv')
print(item_master.head(5))

transaction_1 = pd.read_csv(f'{path}/1/transaction_1.csv')
print(transaction_1.head(5))

transaction_detail_1 = pd.read_csv(f'{path}/1/transaction_detail_1.csv')
print(transaction_detail_1.head(5))

