"""
Created on Mon Aug 11 14:36:21 2014
@author: jtrujillo
"""
##load the necessary libraries
import pandas as pd
import numpy as np
import os
##change the directory
os.getcwd()
os.chdir('C:\Users\jtrujillo\Desktop')
##read the csv file
health= pd.read_csv('health.csv', sep=',')
#create list with age
age=health['age']
#calculate the average age
average_age=age.mean()
print(average_age)
#generate a new column with the sum of health 2 and 5
new_health=health['health2']+health['health5']
new_health.head()
#new data frame with average age by sex
#health=pd.DataFrame(health)
age_sex=health.groupby(['gender'])
a=age_sex.agg(np.mean)
age_sex=a[['age']]
age_sex.head()
age_sex=pd.DataFrame(age_sex)
#we save to csv
age_sex.to_csv('newdata.csv')

 

 