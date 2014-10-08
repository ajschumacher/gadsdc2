# -*- coding: utf-8 -*-
"""
@author: huey
"""

# to do
# 1. read data and create dataframe
# 2. delete unwanted columns for feature space use
# 3. define X and y for feature space and for later modelling use
# 4. scale
# 5. use sklearn to cross validate
# 6. use SVM, RF, and KNN 

from __future__ import division
import pandas as pd

churn_dataframe = pd.read_csv('/Users/huey/Desktop/FinalProject/LZ_allusers2.csv')

# segment target data
churn_result = churn_dataframe['Churn']
y = np.where(churn_result == 'true.', 1, 0)

# delete unwanted columns
to_delete = ['Churn', 'Account created', 'User_ID']
churn_feat_space = churn_dataframe.drop(to_delete, axis=1)

# get features for future use
features = churn_feat_space.columns

X = churn_feat_space.as_matrix().astype(np.float)

# for scaling

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

# for cross-validating

from sklearn.cross_validation import KFold

# implementing kfolds and iterating through folds; call classifier

def crossvalidate(X,y,clf_class, **kwargs):
    kfold = KFold(len(y), n_folds=4, shuffle=True)
    y_pred = y.copy()
    
    for train_index, test_index in kfold:
        X_train, X_test = X[train_index], X[test_index]
        y_train = y[train_index]
        classifier = clf_class(**kwargs)
        classifier.fit(X_train, y_train)
        y_pred[test_index] = classifier.predict(X_test)
    return y_pred
    
# for passing each cross validating through algorithms 
        
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.neighbors import KNeighborsClassifier as KNN

# get accuracy

import numpy as np

def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

# calculating and interpreting results

print "SVM:"
print "%.3f" % accuracy(y, crossvalidate(X, y, SVC))
print "RF:"
print "%.3f" % accuracy(y, crossvalidate(X, y, RF))
print "KNN:"
print "%.3f" % accuracy(y, crossvalidate(X, y, KNN))

