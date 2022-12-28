'''
Experiment 12
(B) Write a python program that mapping external values to dataframe values in Pandas.
'''

import pandas as pd

data_df = pd.read_csv('Credit_card_transactions.csv')

new_data = {'Delhi, India':'New Delhi, India',
           'Greater Mumbai, India':' Mumbai, India'}

print("--------------------  OLD DATA -----------------------------\n ",data_df, end ="\n\n")
data_df = data_df.replace({"City":new_data})
print("--------------------  NEW UPDATED DATA ---------------------\n",data_df)
