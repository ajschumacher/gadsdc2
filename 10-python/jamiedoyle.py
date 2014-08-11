#Read health.csv into a list of (row) lists.
#Isolate the age column in a list.
#Calculate the average age.
#Construct a list that has, for each row, the sum of health2 and health5.
#Use comprehension(s) to calculate the average male and female ages.
#Write out a csv file with two columns, sex and average_age, and one row containing the values.


import csv
datafile = open('health.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)	

#Isolate age column
age=[] 
for row in data:
  age.append(row[2])

#Get rid of header, keep #'s, convert to numbers. Bain of my friday was figuring out how to convert this.
age=map(int,age[1:16]) 

# Mean of list
print sum(age) / float(len(age))

#Construct a list that has, for each row, the sum of health2 and health5.
#This is probably the longest way of doing this...
twosums=[]

health2=[] 
for x in data:
  health2.append(x[5])
twosums.append(sum(map(int,health2[1:16]))) 


health5=[] 
for y in data:
  health5.append(y[8])
twosums.append(sum(map(int,health5[1:16])))   

# Or if it's just the sum with length 15
import numpy as np
healthsum=[np.sum(i) for i in zip(map(int,health2[1:16]), map(int,health5[1:16]))]


#Use comprehension(s) to calculate the average male and female ages. Most inefficent way of doing this, I know.

men=[]

for z in data:
    if z[1]=='M':
        men.append(z[2])

men=map(int,men) 
avmen=sum(men) / float(len(men))         
print sum(men) / float(len(men)) 

women=[]
for q in data:
    if q[1]=='F':
       women.append(q[2])
women=map(int,women)   
avwomen=sum(women) / float(len(women))       
print sum(women) / float(len(women)) 

#Write out a csv file with two columns, sex and average_age, and one row 
#containing the values.

namesz=['M','F']
aves=[avmen,avwomen]
rows = zip(namesz,aves)

import csv

with open('average_gender.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in rows:
       writer.writerow(row)

    
