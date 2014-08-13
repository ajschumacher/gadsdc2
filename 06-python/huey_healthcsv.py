#read csv file into a list of (row) lists

import csv
with open('/Users/huey/Downloads/health.csv', 'rU') as f:
    x = [line for line in csv.reader(f)]
print x

#isolate the age column in a list
import numpy as np

a = np.array(x)

col = []
for row in a:
    col.append(row[2])
print col

#calculate the average age

col.pop(0)

print np.mean(map(float, col))

###construct list that has, for each row, the sum of health2 and health 5

health2 = []
for row in a:
    health2.append(row[5])
health2.pop(0)

health5 = []
for row in a:
    health5.append(row[8])
health5.pop(0)

int_health2 = map(int, health2)
int_health5 = map(int, health5)

import operator
print map(operator.add, int_health2, int_health5)

#use comprehension(s) to calculate the average male and female ages

age_men = []

for g in x:
    if g[1] == 'M':
        age_men.append(g[2])

avg_age_men = np.mean(map(float,age_men))

print avg_age_men

age_women = []

for g in x:
    if g[1] == 'F':
        age_women.append(g[2])

avg_age_women = np.mean(map(float,age_women))

print avg_age_women

#write out a csv file with two columns, sex and average_age, and one row containing the values.

csv_input = [['sex', 'average age'],['male', avg_age_men],['female', avg_age_women]]

with open('age_gender.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in csv_input:
        writer.writerow(row)
