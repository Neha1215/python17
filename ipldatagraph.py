import matplotlib.pyplot as plt
"""import pandas
result = pandas.read_csv('IPL-TEAMS-DATA.csv')
print(result)"""
import csv

x = []
y = []

with open('IPL-TEAMS-DATA.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[2]))
        y.append(int(row[3]))

plt.bar(x,y, label='chennai super kings')
plt.xlabel('x')
plt.ylabel('y')
plt.title('cricket team analysis from 2008-2019')
plt.legend()
plt.show()