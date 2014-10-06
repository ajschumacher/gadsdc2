
# import libraries
import os
import csv
import json
import pandas as pd
import numpy as np
import math
import pickle
import statsmodels.formula.api as smf
from sklearn import neighbors
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split


def process_dictionary(fp):
    with open(fp, 'rb') as f:
        d = {line[0] : int(line[1])
             for line in csv.reader(f, delimiter='\t')}
    return d


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
                # split out attributes dictionary, which is a nested json obj
                cdl_a = cdl['attributes']      
                cdl_b = {k: cdl[k] for k in cdl.keys()
                         if k not in ['attributes']}
                cdl = cdl_b.copy()
                cdl.update(cdl_a)
                if 'Ambience' in cdl.keys():
                    cdl_i = cdl['Ambience']
                    cdl_j = {m : cdl[m] for m in cdl.keys()
                             if m not in ['Ambience']}
                    cdl2 = cdl_j.copy()
                    cdl2.update(cdl_i)
                    if ('romantic' in cdl2.keys() and
                        'touristy' in cdl2.keys() and
                        'trendy' in cdl2.keys()):
                            dl.append(cdl2)
                else:
                    pass
    df = pd.DataFrame(dl)
    
    # Create a flag for 4+ starts
    df['high_rating'] = df['stars']//4
    return df


def process_review(dp, df, rbl):
    dl = []
    counter = 0
    with open(os.path.join(dp, df), 'rb') as f:
        for l in f.readlines():
            counter += 1
            cdl = json.loads(l.replace('\n', ''))
            if cdl['business_id'] in rbl:
                dl.append(cdl)
            # Print out each 100 lines to show progress
            if counter%1000 == 0:
                print '\t', counter
    df = pd.DataFrame(dl)
    return df
    

def run_processing(dd, ddf, yd, ydf, yrf, t):
    """
    This function runs the processing files defined above and then
    creates pickle objects to reduce run time. This only needs to be
    run once
    """
    
    pd.options.mode.chained_assignment = None  # default='warn'
    
    df_business = process_data(yd, ydf)
    df_vegas = df_business[df_business.city == "Las Vegas"]
    df_vegas = df_vegas[df_vegas.open == True]
    df_vegas['credit_card'] = (df_vegas['Accepts Credit Cards']==True).astype(int)
    df_vegas['caters_flag'] = (df_vegas['Caters']==False).astype(int)
    df_vegas['Alcohol'] = df_vegas['Alcohol'].map({'full_bar': 3,
                                                       'beer_and_wine': 2,
                                                       'none': 1,
                                                       float('NaN'):0})
    pickle.dump(df_vegas,
                open(os.path.join(t, 'p_df_vegas.p'), 'w'))
    
    relevant_business = list(df_vegas.business_id)
    pickle.dump(relevant_business,
                open(os.path.join(t, 'p_relevant_business.p'), 'w'))

    reviews = process_review(yd, yrf, relevant_business)
    pickle.dump(reviews,
                open(os.path.join(t, 'p_reviews.p'), 'w'))

    word_dict = process_dictionary(os.path.join(dd, ddf))
    word_list = word_dict.keys()

    review_score = []
    counter = 0
    for rv in reviews.text:
        score = 0
        counter += 1
        
        for wd in rv.split():
            if wd.encode('ascii','ignore') in word_list:
                score += word_dict[wd.encode('ascii','ignore')]
        review_score.append(score)
        
        # Print out each 100 lines to show progress
        if counter%1000==0:
            print counter
    
    print review_score
    
    pickle.dump(review_score,
                open(os.path.join(t, 'p_review_score.p'), 'w'))


def create_analysis_data(t):
    """
    This combines the textual information to the business data set
    
    t is the location of the pickled objects
    """
    reviews = pickle.load(open(os.path.join(t, 'p_reviews.p'), 'rb'))
        
    temp_scores = pickle.load(open(os.path.join(t, 'p_review_score.p'), 'rb'))
        
    review_scores = pd.DataFrame(temp_scores)
    review_scores.columns = ['text_scores']
    
    combined_scores = pd.concat([reviews, review_scores], axis =1)
    collapsed_scores = combined_scores.groupby(['business_id'],
        as_index = False)['text_scores'].mean()
        
    
    df_vegas = pickle.load(open(os.path.join(t, 'p_df_vegas.p'), 'rb'))

    df_vegas_final = pd.merge(df_vegas, collapsed_scores,
                              on='business_id', how='outer')    
    return df_vegas_final

def KNN(df, features, label):
    X = df[features]
    y = df[label]

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size = 0.3,
                                                        random_state = 0)

    knn = neighbors.KNeighborsClassifier(n_neighbors=25)
    knn.fit(X_train, y_train)
    predicted = knn.predict(X_test)
    
    scores = cross_val_score(knn, X, y, cv=10)
    print scores
    print np.mean(scores)
    
    return scores


def regression(df, rf):
    model = smf.logit(data=df, formula=rf).fit()
    print model.summary()
    

def main():
    # Set system variables
    root = r'/Users/DC-MBP/Desktop/final-project'
    temp = os.path.join(root, 'Temp')
    data = os.path.join(root, 'Data')
    dict_data = os.path.join(data, 'AFINN')
    dict_data_file = 'AFINN-111.txt'
    yelp_data = os.path.join(data, 'yelp-api')
    yelp_data_file = 'yelp_academic_dataset_business.json'
    yelp_review_file = 'yelp_academic_dataset_review.json'
        
    # Run processing scripts;
    # Uncomment if it is the first time running this script
    run_processing(dict_data, dict_data_file, yelp_data,
                   yelp_data_file, yelp_review_file, temp)
    
    df_analysis = create_analysis_data(temp)
    
    #KNN
    features_0 = ['latitude', 'longitude', 'review_count', 'credit_card',
                  'Alcohol', 'romantic', 'touristy', 'trendy']
    label_0 = 'stars'
    knn_scores_0 = KNN(df_analysis, features_0, label_0)

    features_1 = ['latitude', 'longitude', 'review_count', 'credit_card',
                  'Alcohol', 'romantic', 'touristy', 'trendy']
    label_1 = 'high_rating'
    knn_scores_1 = KNN(df_analysis, features_1, label_1)
    
    features_2 = ['latitude', 'longitude', 'review_count', 'credit_card',
                  'Alcohol', 'romantic', 'touristy', 'trendy', 'text_scores']
    label_2 = 'high_rating'
    knn_scores_2 = KNN(df_analysis, features_2, label_2)

    # regression
    rf1 = 'high_rating ~ review_count + credit_card + Alcohol + romantic + touristy + trendy + text_scores'
    regression(df_analysis, rf1)

 
    print 'End'


if __name__ == '__main__':    
    main()


### EOF ###
