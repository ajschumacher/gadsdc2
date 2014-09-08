
# import libraries
import os
import math
import json
import numpy as np
import pandas as pd
import time
from patsy import dmatrices
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
from ggplot import * 


def process_data_restaurant(dp, df):
    """
    Create a dataframe of all json items
    subsetting a ite 
    """
    dl = []
    with open(os.path.join(dp, df), 'rb') as f:
        for l in f.readlines():
            cdl = json.loads(l.replace('\n', ''))
            if 'Restaurants' in cdl['categories']:
                cdl_a = cdl['attributes']
                cdl_b = {k: cdl[k] for k in cdl.keys()
                         if k not in ['attributes']}
                cdl = cdl_b.copy()
                cdl.update(cdl_a)                
                dl.append(cdl)
    df = pd.DataFrame(dl)
    return df

def regression(Y, X):
    model = LinearRegression()
    model.fit(X, Y)
    print "sklearn model score is: ", model.score(X, Y)

def regression2(df, rf):
    model = smf.ols(formula=rf,
                    data=df).fit()
    print model.summary()

def main():
    # Set system variables
    root = r'/Users/DC-MBP/Desktop/final-project'
    temp = os.path.join(root, 'Temp')
    data = r'/Users/DC-MBP/Desktop/yelp-api'
    data_file = 'yelp_academic_dataset_business.json'

    # Set regression formula
    rf = 'stars ~ review_count + state + Caters + Attire + BYOB + Alcohol'

    # Create data file
    df_business = process_data_restaurant(data, data_file)
    
    # Create Vegas data file
    #create distance from town center 36.175, -115.136389
    df_vegas = df_business[df_business.city == "Las Vegas"]
    df_vegas['distance'] = np.sqrt(np.power(df_vegas.latitude-36.175,2) +
                                   np.power(df_vegas.longitude+115.136389,2))
    
    # Create visualizations
    p1 = ggplot(aes(y='stars', x='review_count'),data=df_business)
    print(p1 + geom_point())
    
    p2 = ggplot(aes(y='latitude', x='longitude'), data=df_vegas)
    print(p2 + geom_point())
    
    p3 = ggplot(aes(y='stars', x='distance'), data=df_vegas)
    print(p3 + geom_point())
    
    print 'End'

if __name__ == '__main__':
    main()

### EOF ###
