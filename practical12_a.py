'''
Experiment 12
Write a python code to read a csv file using pandas module and print the first and last
five lines of a file.
'''
import pandas as pd

data_df = pd.read_csv('Credit_card_transactions.csv')


'''Using pandas.DataFrame.iloc() to get the first 5 rows. 
Getting first 5 rows from df'''
df_first_5 = data_df.iloc[:5]
print("\nFirst 5 record using pandas ************************")
print(df_first_5)


'''Use pandas.DataFrame.iloc to get last n rows. '''
df_last_5 = data_df.iloc[:-5]
print("\nLast 5 record using pandas ************************")
print(df_last_5)

