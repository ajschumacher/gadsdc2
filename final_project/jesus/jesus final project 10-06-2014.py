# -*- coding: utf-8 -*-
"""
Created on Thu Oct 02 15:34:14 2014

@author: jtrujillo
"""
import pandas as pd
import os
import numpy as np
from math import radians, cos, sin, asin, sqrt
from scipy.stats import mode as md
import operator
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.grid_search import GridSearchCV
from sklearn import linear_model
from sklearn import svm
from sklearn.svm import SVR
import statsmodels.formula.api as smf
import statsmodels.api as sm
  
#change the directory
os.chdir('C:\Users\Jesus\Dropbox\Coding\datos ecobici')
#read our data
travels=pd.read_csv('ecobici.csv', dtype=unicode)
distances=pd.read_csv('ecobici_distancias.csv', dtype=unicode)
users=pd.read_csv('ecobici_usuarios.csv', dtype=unicode)
stations=pd.read_csv('ecobiciestaciones.csv', dtype=unicode)
 
##we will merge our stations datasets to include lat and long distances
 
##we first create a subset of the lat,lon and id of the stations and save it
##as two dataframes. We then change the name of the data frame
departure=stations[['id','latitud','longitud']]
arrival=stations[['id','latitud','longitud']]
departure=departure.rename(columns={'id':'station_removed',
                                    'longitud':'lon1',
                                    'latitud':'lat1'})
arrival=arrival.rename(columns={'id':'station_arrived',
                                    'longitud':'lon2',
                                    'latitud':'lat2'})
 
departure.head()
##we merge this new dataframes to our travels distances
travels=travels.merge(departure, how="left")
travels=travels.merge(arrival, how="left")
##we now define our haversine distance
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km
travels[['lon1','lat1','lon2','lat2']]=travels[['lon1','lat1','lon2','lat2']].astype(float)
 
##we now apply our distance function to our dataframe
travels['distance']=travels.apply(lambda x: haversine(x['lon1'], x['lat1'], x['lon2'], x['lat2']), axis=1)
#we parse for datetime
travels['date_removed']=pd.to_datetime(travels['date_removed'])
travels['date_arrived']=pd.to_datetime(travels['date_arrived'])
travels['time']=travels['date_arrived']-travels['date_removed']
 
#we transform our unitvalue to minutes
travels['duration'] = travels['time'].apply(lambda x: x  / np.timedelta64(1,'m')).astype('int64') % (24*60)
travels.duration.describe()
#we redifine our index to date_removed so we can select our dataset easier
travels2=travels.set_index('date_removed')
travels2.to_csv('complete ecobici database 10-3-14.csv')
del travels


##we will now try to select the 2012 observations
travels2012=travels2['1/1/2012':'31/12/2012']
##we sort our data and export to csv
travels2012.sort_index(axis=0, ascending=True)
travels2012['trips']=1
travels2012.duration.describe()
len(travels2012)
#we use this to map and change values

travels2012.to_csv('2012data.csv', index=True)
#del travels2

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
travels2012.head(1)
####we now resample to aggregate to hourly occurences
hourlycount2=travels2012.resample('H', how={'bike': mode2, 'distance':np.mean, 
                                            'trips':'sum',
    'action': mode2, 'duration':np.mean})
#we sort
hourlycount2.sort_index(axis=0, ascending=True)
#we change the name
hourlycount2['week_days']=hourlycount2.index.weekday
hourlycount2['week_days']=hourlycount2['week_days']+1
hourlycount2['week_days']
hourlycount2['month']=hourlycount2.index.month
hourlycount2['hour']=hourlycount2.index.hour

season = []
for d in hourlycount2.index:
    mon = d.month * 100
    da = d.day
    md = mon + da
    if ((md > 320) and (md < 621)):
        season.append(0) #spring
    elif ((md > 620) and (md < 923)):
        season.append(1) #summer
    elif ((md > 922) and (md < 1223)):
        season.append(2) #fall
    else:
        season.append(3) #winter

hourlycount2['season']=  season

hourlycount2=hourlycount2[(hourlycount2['hour']!=1) & (hourlycount2['hour']!=2) &
(hourlycount2['hour']!=3) &(hourlycount2['hour']!=4)]

hourlycount2['trips'] = hourlycount2['trips'].fillna(0)
hourlycount2['trips']=hourlycount2['trips']+1
hourlycount2['DateMex']=hourlycount2.index
hourlycount2.head(1)
hourlycount2.sort_index(axis=0, ascending=True)
##we filter for hour
#hourlycount2.to_csv('ecobici hourly database.csv')
clime=pd.read_csv('C:\Users\Jesus\Desktop\weather\Mexico Clime 2012.csv')
clime.head()
clime['DateMex']=pd.to_datetime(clime['DateMex'])
clime.sort_index(axis=0, ascending=True)
final=pd.merge(hourlycount2, clime, on='DateMex', how='outer')
final.head(10)
final['DateMex']=pd.to_datetime(final['DateMex'])
final=final.set_index('DateMex')
##time to map values and normalize
final.week_days=(final.index.weekday)+1
final.hour_x=final.index.hour
final.month=final.index.month
season = []
for d in final.index:
    mon = d.month * 100
    da = d.day
    md = mon + da
    if ((md > 320) and (md < 621)):
        season.append(1) #spring
    elif ((md > 620) and (md < 923)):
        season.append(2) #summer
    elif ((md > 922) and (md < 1223)):
        season.append(3) #fall
    else:
        season.append(4) #winter

final['season']=  season

final.head(1)
final['Wind Direction'].value_counts()
final['Wind Direction'].describe()

#we replace distance missing values with mean values:

final['trips']=final['trips'].fillna(1)
final['distance']=final['distance'].fillna(np.mean(final['distance']))
final['duration']=final['duration'].fillna(np.mean(final['duration']))
final['Events']=final['Events'].fillna(1)
final['Humidity']=final['Humidity'].fillna(np.mean(final['Humidity']))
final['WindDirDegrees']=final['WindDirDegrees'].fillna(np.mean(final['WindDirDegrees']))

final['Conditions'] = final['Conditions'].map({'Mostly Cloudy':1, 'Scattered Clouds':2,
'Clear':2, 'Overcast':1, 'Partly Cloudy':1, 'Light Rain':3, 'Light Thunderstorms and Rain':3,
'Haze':1, 'Rain':3, 'Thunderstorm':4, 'Thunderstorms and Rain':4, 'Fog':1, 'Rain Showers':3,
'Widespread Dust':3, 'Thunderstorms with Small Hail':4, 'Heavy Thunderstorms and Rain':4,
'Unknown':2})
final['Conditions']=final['Conditions'].fillna(16)

final['Dew PointF']=final['Dew PointF'].fillna(np.mean(np.mean(final['Dew PointF'])))
final['TemperatureF']=final['TemperatureF'].fillna(np.mean(np.mean(final['TemperatureF'])))
final['VisibilityMPH']=final['VisibilityMPH'].fillna(np.mean(np.mean(final['VisibilityMPH'])))

final['Wind SpeedMPH'] = final['Wind SpeedMPH'].replace('Calm', np.nan) 
final['Wind SpeedMPH'] = final['Wind SpeedMPH'].astype(float)
final['Wind SpeedMPH']=final['Wind SpeedMPH'].fillna(np.mean(np.mean(final['Wind SpeedMPH'])))
final['Wind SpeedMPH'].describe()

#we replace the values of Events
final['Events'] = final['Events'].map({1:1, 'Rain': 2, 'Rain-Thunderstorm': 3, 
'Thunderstorm':4, 'Fog':5, 'Rain-Hail-Thunderstorm':6})
final=final.drop(['bike', 'action','DateUTC', 'duration', 'distance', 'PrecipitationIn', 
           'TimeCST', 'Wind Direction'], axis=1)


final.head(1)
final.to_csv('final_data_model.csv')
##################### MODEL

test_idx = np.random.uniform(0, 1, len(final)) <= 0.3
train = final[test_idx == False]
test = final[test_idx == True]
#train=train.reset_index()
train.describe()
train.head()
len(test)
def normalize(bk):
    bk = (bk - bk.mean()) / (bk.max() - bk.min())
    return bk
pd.isnull(train).any()
train_col=train.columns.tolist()
train_col.remove('trips')
train[train_col] = normalize(train[train_col])

test_idx_1 = np.random.uniform(0, 1, len(train)) <= 0.3
train_train= train[test_idx_1== False]
train_test = train[test_idx_1 == True]
len(train_train)
len(train_test)
X_train = train_train[train_col]
X_test = train_test[train_col]
y_train = train_train['trips']
y_test = train_test['trips']



clf = GradientBoostingRegressor(n_estimators = 2500, max_depth = 4, 
                                learning_rate = 0.0000001, random_state = 0, loss = 'huber')
clf.fit(X_train, y_train)
clf_pred_1 = clf.predict(X_test)
clf_pred_1 = pd.DataFrame(clf_pred_1, index = train_test.index, columns = ['trips'])
clf_pred_1.describe()
clf_pred_1.head()
#there are negative values
clf_pred_1[clf_pred_1 < 0] = 0
clf_pred_1.describe()

print 'Grad Tree R^2 score:'
print r2_score(y_test, clf_pred_1)
#0.296
print 'Grad Tree Mean Squared Error:'
print mean_squared_error(y_test, clf_pred_1)
#22938

def sle(actual, predicted):
    return (np.power(np.log(np.array(actual)+1) -np.log(np.array(predicted)+1), 2))

def rmsle(targets, predictions):
    return np.sqrt((sle(targets, predictions)**2).mean())

print rmsle(y_test, clf_pred_1)

##Bayesian regression
clf = linear_model.BayesianRidge()
clf.fit(X_train, y_train)
clf_pred_1 = clf.predict(X_test)
clf_pred_1 = pd.DataFrame(clf_pred_1, index = train_test.index, columns = ['trips'])
clf_pred_1.describe()
clf_pred_1[clf_pred_1 < 0] = 0

max(y_test)

print 'Grad Tree R^2 score:'
print r2_score(y_test, clf_pred_1)
#0.296
print 'Grad Tree Mean Squared Error:'
print rmsle(y_test, clf_pred_1)


clf = svm.SVR()
clf.fit(X_train, y_train)
clf_pred_1 = clf.predict(X_test)
clf_pred_1 = pd.DataFrame(clf_pred_1, index = train_test.index, columns = ['trips'])
clf_pred_1.describe()
clf_pred_1[clf_pred_1 < 0] = 0

print 'Grad Tree R^2 score:'
print r2_score(y_test, clf_pred_1)
#0.296
print 'Grad Tree Mean Squared Error:'
print rmsle(y_test, clf_pred_1)


svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(X_train, y_train).predict(X_test)
clf_pred_1 = pd.DataFrame(y_rbf, index = train_test.index, columns = ['trips'])
clf_pred_1.describe()
clf_pred_1[clf_pred_1 < 0] = 0

print 'Grad Tree R^2 score:'
print r2_score(y_test, clf_pred_1)
#0.296
print 'Grad Tree Mean Squared Error:'
print rmsle(y_test, clf_pred_1)