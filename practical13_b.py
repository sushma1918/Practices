'''
Experiment 13 B
Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file.

sample data: medal.csv->
country,gold_medal
United States,46
Great Britain,27
China,26
Russia,19
Germany,17
'''

import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]

colors = ["#800000", "#00FF00", "#BAB86C", "#8C564B", "#D62728"]
explode = (0, 0, 0, 0, 0)  

plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Gold medal achievements of five most successful\n countries in 2016 Summer Olympics")
plt.show()
