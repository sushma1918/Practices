'''
Experiment 12 C
Write a python program to get all rows in a pandas dataframe containing given
substring.
'''
import pandas as pd

data_df = pd.read_csv('Credit_card_transactions.csv')

''' Let's suppose here substring is 'Delhi'
Getting all transaction that City have [Delhi] substring.  '''
new_df = data_df[data_df['City'].str.contains("Delhi")]
print(new_df)
