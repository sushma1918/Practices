'''
Experiment 13
(A) Write a program to get five marks using list and display the marks in pie chart
'''


# Import libraries
from matplotlib import pyplot as plt

# Creating dataset
technology = ["HTML", "CSS","JS","Python","React","MongoDB"]
knowdge = [90,95,80,99,70,80]

# Creating plot
fig = plt.figure(figsize =(8, 7))
plt.pie(knowdge, labels = technology)

# show plot
plt.show()



