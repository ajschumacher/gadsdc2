import csv
import numpy as np


myLists = []
myAges = []
summedList = []
genderComparison = [['sex', 'average_age']]


localFile = open('health.csv','rU')
myData = csv.reader(localFile)


def createListOfLists():
    for row in myData:
        myLists.append(row)

def isolateAge():
    i = 1
    for row in myLists:
        myAges.append(int(myLists[i][2]))
        if (i < len(myLists) - 1):
            i = i + 1
    print 'The average ages is ' + str(np.mean(myAges))

def constructNewList():
	i = 1
	for row in myLists:
		summedList.append(int(myLists[i][5]) + int(myLists[i][8]))
		if (i < len(myLists) - 1):
			i = i + 1
	print summedList

def avgAgeByGender():
	i = 1
	agesOfMales = []
	agesOfFemales = []
	for row in myLists:
		if (myLists[i][1] == 'M'):
			agesOfMales.append(int(myLists[i][2]))
		elif(myLists[i][1] == 'F'):
			agesOfFemales.append(int(myLists[i][2]))
		else:
			print 'not gender binary'
		if (i < len(myLists) - 1):
			i = i + 1
	genderComparison.append(['Male',np.mean(agesOfMales)])
	genderComparison.append(['Female',np.mean(agesOfFemales)])
	print genderComparison

def writeToFile():
    with open('gender_comparison.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in genderComparison:
            writer.writerow(line)

createListOfLists()
isolateAge()
constructNewList()
avgAgeByGender()
writeToFile()
