
# Set Working directory
os.chdir("/Users/ndeprey/gadsdc/06-python/")


# Read health.csv into a list of (row) lists.
import csv
with open('health.csv', 'rU') as f:
    health = [row for row in csv.reader(f, quoting=csv.QUOTE_NONE)]


# Isolate the age column in a list.
age = [sub_list[2] for sub_list in health]
age = [int(i) for i in age[1:]]

# Calculate the average age.
import numpy
average_age = numpy.mean(age)
print average_age

# Construct a list that has, for each row, the sum of health2 and health5.
sums = [int(sublist[5]) + int(sublist[8]) for sublist in health[1:len(health)]]


# Use comprehension(s) to calculate the average male and female ages.
males = [sublist for sublist in health if sublist[1]=="M"]
females = [sublist for sublist in health if sublist[1]=="F"]

m_avg_age = numpy.mean([int(sublist[2]) for sublist in males])
f_avg_age = numpy.mean([int(sublist[2]) for sublist in females])


# Write out a csv file with two columns, sex and average_age, and one row containing the values.
avg_ages = [['male', 'female'],[m_avg_age, f_avg_age]]

with open('avg.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(avg_ages)
