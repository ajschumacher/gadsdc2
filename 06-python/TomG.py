from __future__ import division

import csv

# Read health.csv into a list of lists
with open('health.csv', 'r') as f:
	data = list(list(record) for record in csv.reader(f, delimiter=','))

# Isolate the age column in a list
age = []
for row in data:
	age.append(row[2])
age.remove('age')

# Calculate the average age
age = map(int, age)
length = len(age)
total = sum(age)

print "The average age is: " + str(total/length) 

# Construct a list that has, for each row, the sum of health2 and health5
sums = []
for row in data[1:16]:
	sums.append([row[5], row[8], int(row[5])+int(row[8])])

print sums

# Use comprehension(s) to calculate the average male and female ages.
mAge = [ row[2] for row in data[1:16] if row[1]== 'M' ]
fAge = [ row[2] for row in data[1:16] if row[1]== 'F' ]

mAge = map(int, mAge)
fAge = map(int, fAge)

print "The average male age is: " + str(sum(mAge)/len(mAge))
print "The average female age is: " + str(sum(fAge)/len(fAge))

# Write out a csv file with two columns, sex and average_age, and one row containing the values
f2 = open('output.csv', 'wt')
writer = csv.writer(f2)
writer.writerow( ('ID','Sex', 'Average Age', 'Values') )
sex = ['M', 'F']
ages = [mAge, fAge]
average_age = [sum(mAge)/len(mAge), sum(fAge)/len(fAge)]
for s in range(2):
	writer.writerow( (s, sex[s], average_age[s], ages[s]) )

f.close()
f2.close()
