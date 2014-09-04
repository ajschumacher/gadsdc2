import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from patsy import dmatrices, NAAction, build_design_matrices
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import Lasso, LassoLars

def PreProcess(df):
    df['titledescription'] = df['Title'] + ' ' + df['FullDescription']
    df['locationfull'] = df['LocationRaw'] + ' ' + df['LocationNormalized']
    return df

def InitializeTransformers(df):
    vect1 = TfidfVectorizer(max_features=3000)
    vect1.fit([str(x) for x in df['titledescription'].values])
    vect2 = CountVectorizer(binary=True)
    vect2.fit([str(x) for x in train['locationfull'].values])
    (a,b) = dmatrices('SalaryNormalized ~ ContractTime + ContractType + Company + Category + SourceName', 
                   data=df, NA_action=NAAction(on_NA='drop', NA_types=[]))
    builder = b.design_info.builder
    return (vect1,vect2,builder)

def ProcessData(df,vect1,vect2,builder):
    descriptionmatrix = vect1.transform([str(x) for x in df['titledescription'].values])
    locationmatrix = vect2.transform([str(x) for x in df['locationfull'].values])
    # x = build_design_matrices([builder], df, return_type='dataframe', NA_action=NAAction(on_NA='drop', NA_types=[]))
    y = df['SalaryNormalized'].values
    #x_combo = np.hstack([np.asarray(x[0]),descriptionmatrix.toarray(),locationmatrix.toarray()])
    x_combo = np.hstack([descriptionmatrix.toarray(),locationmatrix.toarray()])
    return (np.asarray(y), sparse.coo_matrix(x_combo))

train = PreProcess(pd.read_csv('train.csv'))
(vect1,vect2,builder) = InitializeTransformers(train)
(y, x) = ProcessData(train, vect1, vect2,builder)

(y_test, x_test) = ProcessData(PreProcess(pd.read_csv('solution.csv')),vect1,vect2,builder)

lasso = Lasso()
lasso.fit(x,y)
y_pred = lasso.predict(x_test)

lassolars = LassoLars(alpha=2)
lassolars.fit(x.toarray(),y)
lars_pred = lassolars.predict(x_test)

print np.sqrt(mean_squared_error(y_test, y_pred))

print r2_score(y_test,y_pred)

print np.sqrt(mean_squared_error(y_test,lars_pred))

print r2_score(y_test,lars_pred)