
# import libraries
import os
import json
import pandas as pd
import time
from patsy import dmatrices
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf

def process_data(dp, df):
    """
    Create a dataframe of all json items
    subsetting the items to only include restaurants
    """
    dl = []
    with open(os.path.join(dp, df), 'rb') as f:
        for l in f.readlines():
            cdl = json.loads(l.replace('\n', ''))
            if 'Restaurants' in cdl['categories']:
                cdl_a = cdl['attributes']      # split out attributes dictionary
                cdl_b = {k: cdl[k] for k in cdl.keys()
                         if k not in ['attributes']}
                cdl = cdl_b.copy()
                cdl.update(cdl_a)                
                dl.append(cdl)
    df = pd.DataFrame(dl)
    # Create a flag for 4+ starts
    df['high_rating'] = df['stars']//4
    return df


def regression(df, rf):
    model = smf.logit(data=df, formula=rf).fit()
    print model.summary()

def main():
    # Yelp data downloaded from here:
    #   https://www.yelp.com/dataset_challenge/dataset
    data = r''      # fill in path of dataset
    data_file = 'yelp_academic_dataset_business.json'

    # Set regression formula
    rf = 'high_rating ~ review_count + state'

    # Create data file
    df_business = process_data(data, data_file)
    
    # Run regression
    regression(df_business, rf)

    print 'End'


if __name__ == '__main__':
    main()

### EOF ###
