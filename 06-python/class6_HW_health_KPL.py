# -*- coding: utf-8 -*-
"""
Started on Mon Aug 11 16:22:49 2014
Finished on Tues Aug 12 1:35 pm

@author: kperez-lopez

Assignment, from Aaron, Wed 8/6/2014 11:06 PM:
•	x Read health.csv into a list of (row) lists.
•	x Isolate the age column in a list.
•	x Calculate the average age.
•	x Construct a list that has, for each row, the sum of health2 and health5.
•	x Use comprehension(s) to calculate the average male and female ages.
•	x Write out a csv file with two columns, sex and average_age, and one 
        row containing the values.
"""
import csv

def add(x,y): return float(x)+float(y)

#def getHealthColAverage(fileName, colName):
# Read health.csv into a list of (row) lists.
#	x Read health.csv into a list of (row) lists.
path = \
str('C:\\Users\\kperez-lopez\\Documents\\GA_dataScience\\Class6_2014_08_06\\')
print '\nThis is my path' + path

with open(path + 'Health.csv', 'rU') as f:
    x = [line for line in csv.reader(f)]

print "\nFollowing is the entire file, health.csv"
print x

print ('_______________\n')

# Pop the header row; transpose x to get the columns more easily as rows.
# The rows will be indexed by their names in header.
header = x.pop(0)

# Copied from https://docs.python.org/2/tutorial/datastructures.html,
#   5.1.4.1. Nested List Comprehensions
transposedX = []
for i in range(len(x[0])):
     transposedX.append([row[i] for row in x])
#print transposedX

#	x Isolate the age column in a list.
ages = transposedX[header.index("age")]
print "\nThe age column is ", ages

#	x Calculate the average age.
print "\nAverage age is ",
print reduce(add, ages) / len(ages)
 
#	x Construct a list that has, for each row, the sum of health2 and health5.
health2 = transposedX[header.index("health2")]
health5 = transposedX[header.index("health5")]

print "\nThe following list is the sum of rows health2 and health5:"
print [health2[j] + health5[j] for j in range(len(transposedX[0]))]  

#	x Use comprehension(s) to calculate the average male and female ages.
genders = transposedX[header.index("gender")]
# Set up gender_info to be the rows of the eventual output file. Average age
# will be calculated and appended to the respective rows.
gender_info = [["GENDER", "AVERAGE AGE"],["female"],["male"]]
#print gender_info

# gender_label could be another row of gender_info, but the loop below is
# already pretty dense.  
gender_label = ["F", "M"]

# Likewise, the loop of list comprehensions below could be a list comprehension 
# itself, but that would be even more incomprehensible.
for g in range(len(gender_label)):
    # skip the header row in gender_info
    gender_info[g+1].append( \
    sum([float(ages[j]) for j in range(len(ages)) if genders[j] == gender_label[g]]) / \
    len([float(ages[j]) for j in range(len(ages)) if genders[j] == gender_label[g]]))
    #print "\ngender info_1 is ", gender_info

# Could this be a list comprehension? Tried it but it couldn't get it to work.
for g in range(len(gender_label)):
    print "\nAverage age for ", gender_info[g+1][0], " is ", gender_info[g+1][1]

#	x Write out a csv file with two columns, sex and average_age, and one 
#               (two rows?)
#        row containing the values.
# What's the csv.writer analog to lines 27, 28 above for csv.reader?
# Figured it out.
with open(path + 'averageAgesByGender.csv', 'wb') as of:
    [csv.writer(of).writerow(gender_info[row]) for row in range(len(gender_info))]
    
of.close()