import csv
with open('health.csv', 'rU') as f:
    x = [line for line in csv.reader(f)]
print x

import numpy as np
n = np.array(x)

n[1:,2]
ages = [int(i) for i in n[1:,2]]
np.mean(ages)

healths = n[1:,[5,8]]
sums = [sum([int(i) for i in line]) for line in healths]
print healths
print sums


z = n[1:,[1,2]]
femmes = [x for x in z if x[0] == 'F']
print femmes
f_ages = [int(i[1]) for i in femmes]
f_ave = np.mean(f_ages)
hommes = [x for x in z if x[0] == 'M']
print hommes
h_ages = [int(i[1]) for i in hommes]
h_ave = np.mean(h_ages)

means = [['sex', 'average_age'], ['F', 'M'], [f_ave, h_ave]]
print means

with open('averages.csv', 'wb') as f:
    a = csv.writer(f, delimiter=',')
    a.writerows(means)

import csv
with open('averages.csv', 'rU') as f:
    x = [line for line in csv.reader(f)]
print x