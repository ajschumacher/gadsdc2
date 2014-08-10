### GA DS DC Class 06
### Python assigment
### Daniel Chung

#!usr/bin/env python

from __future__ import division
import csv
import os


# 1. Health assignment using a list
def healthAssignmentList(filePath):
    ''' filePath is the string containing the location
                  of the health.csv file
    '''
    inputFile = os.path.join(filePath, 'health.csv')
    outputFile = os.path.join(filePath, 'averageAgeBySex-list.csv')

    # a. Read health.csv into a list of (row) lists
    with open(inputFile, 'rU') as f:
        healthDataList = [i for i in csv.reader(f)]

    # b. Isolate age column in a list
    #     (to do) Update with an error checking mechanism
    ageCol = [i for i, j in enumerate(healthDataList[0]) if j == 'age'][0]
    ageData = [int(r[ageCol]) for r in healthDataList[1:]]
    assert len(healthDataList) == len(ageData) + 1    

    # c. Calculate average age
    averageAge = sum(ageData)/len(ageData)

    # d. Construct a list that has, for each row,
    #    the sum of health2 and health5.
    h2Col = [i for i, j in enumerate(healthDataList[0]) if j == 'health2'][0]
    h5Col = [i for i, j in enumerate(healthDataList[0]) if j == 'health5'][0]
    h2h5Data = [int(r[h2Col])+int(r[h5Col]) for r in healthDataList[1:]]
    assert len(healthDataList) == len(h2h5Data) + 1

    # e. Use comprehension(s) to calculate the average male and female ages.
    genderCol = [i for i, j in enumerate(healthDataList[0])
                 if j == 'gender'][0]
    maleAgeData = [int(r[ageCol])
                   for r in healthDataList[1:]
                   if r[genderCol] == 'M']
    averageMaleAge = sum(maleAgeData)/len(maleAgeData)

    femaleAgeData = [int(r[ageCol])
                   for r in healthDataList[1:]
                   if r[genderCol] == 'F']
    averageFemaleAge = sum(femaleAgeData)/len(femaleAgeData)

    # f. Write out a csv file with two columns,
    #    sex and average_age, and one row containing the values.
    with open(outputFile, 'w') as wf:
        averageAgeData = [['sex', 'average_age'],
                          ['M', averageMaleAge],
                          ['F', averageFemaleAge]]
        csv.writer(wf).writerows(averageAgeData)
    

#2. Health assignment using dictionary
def healthAssignmentDict(filePath):
    ''' filePath is the string containing the location
                  of the health.csv file
    '''
    inputFile = os.path.join(filePath, 'health.csv')
    outputFile = os.path.join(filePath, 'averageAgeBySex-dict.csv')

    # a. Read health.csv into a list of dictionaries for 
    with open(inputFile, 'rU') as f:
        healthDataDict = [i for i in csv.DictReader(f)]

    # b. Isolate age column ina list
    ageData = [int(r['age']) for r in healthDataDict]
    assert len(healthDataDict) == len(ageData)   

    # c. Calculate average age
    averageAge = sum(ageData)/len(ageData)

    # d. Construct a list that has, for each row,
    #    the sum of health2 and health5.
    h2h5Data = [int(r['health2'])+int(r['health5']) for r in healthDataDict]
    assert len(healthDataDict) == len(h2h5Data)

    # e. Use comprehension(s) to calculate the average male and female ages.
    maleAgeData = [int(r['age']) for r in healthDataDict
                   if r['gender'] == 'M']
    averageMaleAge = sum(maleAgeData)/len(maleAgeData)

    femaleAgeData = [int(r['age'])for r in healthDataDict
                   if r['gender'] == 'F']
    averageFemaleAge = sum(femaleAgeData)/len(femaleAgeData)

    # f. Write out a csv file with two columns,
    #    sex and average_age, and one row containing the values.
    with open(outputFile, 'w') as wf:
        averageAgeData = [['sex', 'average_age'],
                          ['M', averageMaleAge],
                          ['F', averageFemaleAge]]
        csv.writer(wf).writerows(averageAgeData)


# 3. Get an average of a stream of numbers
def averageNumbers():
    usr_inp, s, c = 1, 0.0, 0
    while usr_inp:
        usr_inp = raw_input('Enter a number or \'q\' to quit: ')
        if usr_inp == 'q':
            break
        s += int(usr_inp)
        c += 1
        print s/c


# 4. FizzBuzz using list comprehension
def fizzBuzz(n):
    fbList = ['FizzBuzz' if i%15==0
              else 'Fizz' if i%3==0
              else 'Buzz' if i%5==0
              else i
              for i in range(1, n+1)]
    return fbList


if __name__ == '__main__':
    inputPath = r''                 # Input the location of health.csv
    healthAssignmentList(inputPath)
    healthAssignmentDict(inputPath)

    averageNumbers()

    print fizzBuzz(100)


### EOF ###
