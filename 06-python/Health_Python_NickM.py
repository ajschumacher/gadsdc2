# -*- coding: utf-8 -*-
"""
Created on Sat Aug 09 11:48:45 2014

@author: Nick
"""
"""
pull request to gadsdc2/06-python. 

Exercise:

Read health.csv into a list of (row) lists.
Isolate the age column in a list.
Calculate the average age.
Construct a list that has, for each row, the sum of health2 and health5.
Use comprehension(s) to calculate the average male and female ages.
Write out a csv file with two columns, sex and average_age, and one row containing the values.

https://github.com/ajschumacher/gadsdc/blob/master/06-python/health.csv
"""

import pandas
import numpy

#Load the data into a DataFrame
data = pandas.read_csv('C:\Users\Nick\Desktop\Data Science\health.csv')

#View data
data.head(n=5)

#Isolate the age column in list and find average
age = data.age
print age.mean()

#Create list that sums health2 and health5
health_2_5 = data.health2 + data.health5
print health_2_5

#Calculate average male and female age
bygender = data.groupby('gender')
bygender['age'].describe()

#Collapse gender by average age
collapsed = bygender.aggregate(np.mean)
collapsed2x2 = collapsed.age
print collapsed2x2

#Write csv with sex and average age
import csv
with open('C:\Users\Nick\Desktop\Data Science\outsheet.csv', 'w') as output:
    writer = csv.writer(output, delimiter=',')
    writer.writerows(enumerate(collapsed2x2, 1))
