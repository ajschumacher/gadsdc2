# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 13:20:10 2014

@author: ajv
"""
#Class 6 Assignment (5 August)

import csv
import numpy
with open('/Users/ajv/Desktop/Class/Class6/health.csv', "rU") as f:
    health_1 = [row for row in csv.reader(f.read().splitlines())]
  
rownum = 0
for row in health_1:
    #Save header row
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            #print '%-8s:%s' % (header[colnum],col)
            colnum += 1
    rownum += 1

health_2 = zip(*health_1)

# Calculate average age
age = health_2[2][1:]
age = [float(a) for a in age]
average_age = float(sum(age))/float(len(age))

# Calculate sum of Health2 and Health5
sumh2h5 = range(15)
for i in range(15):
    sumh2h5[i] = health_2[5][i] + health_2[8][i]

#Create separated age lists
male_list = [float(health_2[2][i]) for i in range(15) if health_2[1][i] == "M"]
female_list = [float(health_2[2][i]) for i in range(15) if health_2[1][i] == "F"]

#Calculate averages
male_avg = numpy.average(male_list)
female_avg = numpy.average(female_list)
    
#Write the new stuff to CSV
path = 'output.csv'
with open(path,'wb') as csv_file:
    andywriter = csv.writer(csv_file,delimiter=',')
    data = [['Sex','Average Age'],['M',male_avg], ['F',female_avg]]
    for row in data:
            andywriter.writerow(row)
            

# OLD CODE - for reference
#Calculate average male age - OLD Method (For loop)
#male_count = 0
#male_sum = 0
#male_avg = 0
#for i in range(15):
#    if (health_2[1][i] == "M"):
#        male_sum = male_sum + health_2[2][i]
#        male_count += 1
#    i += i
#male_avg = male_sum / male_count

#Calculate average female age - OLD Method
#female_count = 0
#female_sum = 0
#female_avg = 0
#for i in range(15):
#    if (health_2[1][i] == "F"):
#        female_sum = female_sum + health_2[2][i]
#        female_count += 1
#    i += i
#female_avg = female_sum / female_count



