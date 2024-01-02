import pandas as pd
import os
path = os.getcwd()

#transaction
transaction_1 = pd.read_csv(f'{path}/1/transaction_1.csv')
print(transaction_1)
transaction_2= pd.read_csv(f'{path}/1/transaction_2.csv')
print(transaction_2)
transaction = pd.concat([transaction_1,transaction_2],ignore_index=True)
print(transaction)

#transaction_detai
transaction_detail_1 = pd.read_csv(f'{path}/1/transaction_detail_1.csv')
print(transaction_detail_1)
transaction_detail_2 = pd.read_csv(f'{path}/1/transaction_detail_2.csv')
print(transaction_detail_2)
transaction_detail = pd.concat([transaction_detail_1,transaction_detail_2],ignore_index=True)
print(transaction_detail)