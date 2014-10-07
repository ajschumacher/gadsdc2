# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 00:04:26 2014

@author: Jesus
"""
import urllib2
import os
import csv
import pandas as pd
import operator
import numpy as np
from dateutil.parser import parse
import datetime
os.chdir('C:\Users\jesus\Desktop\weather')

list1=[]
for m in range(1, 13):
    for d in range(1, 32):
        
        url='http://www.wunderground.com/history/airport/MMMX/2012/'+str(m)+'/'+str(d)+'/DailyHistory.html?req_city=Mexico+City&req_state=&req_statename=Mexico&format=1'
        data = urllib2.urlopen(url)

        for line in data:
            line=line.replace('<br />',"")
            line=line.replace("\n","")
            #del list1[0]
            list1.append(line)
            

len(list1)
list2 = [x for x in list1 if x]
len(list2)
new_k = []
for elem in list2:
    if elem not in new_k:
        new_k.append(elem)
len(new_k)        

with open('test_scrape2.csv', 'wb') as csvfile:
    r = csv.writer(csvfile)
    reader = csv.reader(new_k)#, delimiter=',', quotechar="'")
    
    for record in reader:
        r.writerow(record)
#line=line.replace('/n',"")

clime=pd.read_csv('test_scrape2.csv')
clime['DateUTC']=pd.to_datetime(clime['DateUTC'])
clime['DateUTC']=clime['DateUTC']-datetime.timedelta(hours=6)
clime['DateMex']=pd.to_datetime(clime['DateMex'])

clime=clime.set_index('DateUTC')
clime['Events'].value_counts()
def mode2(algo):
    try:
        counter = {}
        for i in algo:
            counter[i] = counter.get(i, 0) + 1
            if max(counter.iteritems(), key=operator.itemgetter(1))[0]>0:
                beta=max(counter.iteritems(), key=operator.itemgetter(1))[0]    
                return beta
    except IndexError:
        return np.nan
clime.head(1)
####we now resample to aggregate to hourly occurences
hourlyclime=clime.resample('H', how={'TimeCST':'count', 'TemperatureF':
    np.mean, 'Dew PointF':'mean', 'Humidity':'mean',  
    'VisibilityMPH':'mean', 'Wind Direction':mode2, 'Wind SpeedMPH':mode2,
    'Gust SpeedMPH':np.mean, 'PrecipitationIn':'count','Events':mode2, 
    'Conditions':mode2,'WindDirDegrees':'mean', 'DateMex':'max'})

hourlyclime['hour']=hourlyclime.index.hour
hourlyclime=hourlyclime[(hourlyclime['hour']!=1) & (hourlyclime['hour']!=2) &
(hourlyclime['hour']!=3) &(hourlyclime['hour']!=4)]
hourlyclime['DateMex']=hourlyclime.index
hourlyclime.head()
hourlyclime['Events'].value_counts()
hourlyclime.to_csv('Mexico Clime 2012.csv',index=True)