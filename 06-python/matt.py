import csv

with open('health2.csv', 'rU') as f:
	x = [line for line in csv.reader(f)]

age = []
for line in x:
	age.append(line[2])

runsum=0
totalobs=0
for obs in age:
	try:
		runsum += float(obs)
		totalobs += 1
	except:
		continue

avgage=runsum/totalobs

health2and5 = []
for line in x:
	try:
		health2and5.append(float(line[5]) + float(line[8]))
	except:
		health2and5.append('Sum of health2 and health5')

maleages = [float(x[i][2]) for i in range(len(x)) if x[i][1] == 'M']
print 'The average age for males is:  ' + str(round(sum(maleages)/len(maleages), 2))

femaleages = [float(x[i][2]) for i in range(len(x)) if x[i][1] == 'F']
print 'The average age for females is:  ' + str(round(sum(femaleages)/len(femaleages),2))

export = [['Sex', 'Average_age'], ['M', round(sum(maleages)/len(maleages), 2)], ['F', round(sum(femaleages)/len(femaleages),2)]]

with open('analysis.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	for row in export:
		writer.writerow(row)