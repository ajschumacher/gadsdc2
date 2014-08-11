#Read health.csv into a list of (row) lists.
#Isolate the age column in a list.
#Calculate the average age.
#Construct a list that has, for each row, the sum of health2 and health5.
#Use comprehension(s) to calculate the average male and female ages.
#Write out a csv file with two columns, sex and average_age, and one row containing the values.

import csv

with open('health.csv','rb') as health:
	reader=csv.reader(health)
	for row in reader:
        print row
	