# HW Class 4, 7/30/2014; due 8/4/2014 
# 1NN
#   Write a function to perform a 1 nearest neighbor
#   classification on a dataset.
# Preliminary: get a dataset and partition it into
# training and a test subsets.
#
# Dataset is Human Activity Recognition (HAR) data, using using accelerometer data. 
# 
# Ugulino, W.; Cardador, D.; Vega, K.; Velloso, E.; Milidiu, R.; Fuks, H. Wearable Computing:
# Accelerometers' Data Classification of Body Postures and Movements. Proceedings of 21st
# Brazilian Symposium on Artificial Intelligence. Advances in Artificial Intelligence - SBIA 2012. In: Lecture
# Notes in Computer Science. pp. 52-61. Curitiba, PR: Springer Berlin / Heidelberg, 2012. ISBN
# 978-3-642-34458-9. DOI: 10.1007/978-3-642-34459-6_6.
# http://groupware.les.inf.puc-rio.br/work.jsf?p1=10335
#
# The site didn't have the dataset with the feature vectors, just the raw data.  So I wrote 
# to the first author, who very kindly wrote back apologizing and sent me to a site with the 
# features computed:
#    http://groupware.les.inf.puc-rio.br/static/har/
#
# [To do:insert a brief description of the study; 4 accelerometers, 3 axis
# data for each, and 5 output classes]
#
# THe dataset consists of 165632 observations (each contains readings
# from 10Hz sensors, averaged over 1 sec, overlapping windows.
#  There are 44 vars:
#   6 metadata vars (subject name, gender, ht, wt, age & BMI)
#   12 accelerometer vars (x,y,z readings foreach of 4 sensors)
#   22 computed features (g_accel, pitch, roll, variance on these)
#   1 classification: Levels: sitting sittingdown standing standingup walking 
#
# The authors of this study actually used 11 features to predict
# output class; for this exercise, I will use only 2:
#   avg_total_accel_window
#   stddev_accel
# Along with the output, class, there are only 3 vars.
# Full dataset is Ugulino, reduced set will be Ugulino_red.
Ugulino_red <- Ugulino[,42:44]
dim(Ugulino_red)
head(Ugulino_red)
tail(Ugulino_red)
# In 15 min, couldn't even process a simple count on the double loop
# comparing the test items to the training items.  Computing
# distances would be essentially impossible.
# Reduce number of records by a factor of 1000.

Ugulino_red <- Ugulino[seq(1,dim(Ugulino)[1],by=1000),42:44]
# Check the characteristics of the reduced dataset to the original
summary(Ugulino[,42:44])
summary(Ugulino_red)
# Reduced set represents the original pretty well

# Split the data set Ugulino 3/4 training; 1/4 test
# Since the data is listed in a order that would be good
# to preserve, select a systematic sample of rows for 
# each set to get a reasonably even spread. 
# Choose a random start
sample(1:4, size = 1)  # I did this and got 4
# Add the R survey package - it should have a simple way of
# selecting an systematic SRS.  I don't see such a function.

# Create vectors to select test set
select_test <- 4 + 4 * (1:floor(nrow(Ugulino_red)/4)-1)
# Check that it looks good.
head(select_test, 17)
tail(select_test, 17)
length(select_test)

Ugulino_test = Ugulino_red[select_test,]
head(Ugulino_test, 11)
tail(Ugulino_test, 11)
dim(Ugulino_test)

# Create vectors to select training set; negating select_test
# will be used to drop out the test set, leaving the remaining
# 3/4 of the records as the training set.
select_train <- (-1)*select_test
# Check that it looks good.
head(select_train)
tail(select_train)
length(select_train)

Ugulino_train<-Ugulino_red[select_train,]
# Check that it looks good.
head(Ugulino_train, 11)
tail(Ugulino_train, 11)
dim(Ugulino_train)

# Using the floor above might cause a record to be omitted;
# no big deal, but check it out anyway.
dim(Ugulino_red)[1]-(dim(Ugulino_test)[1]+dim(Ugulino_train)[1])

# Summarize the 3 sets, full, training & test
summary(Ugulino_red)
summary(Ugulino_train)
summary(Ugulino_test)
# Results show that each subset is a good replica of the full set.

#Now reform the training and test sets and the labels
U_class <- Ugulino_train[,3]
# Check
summary(U_class)


##########
# Define a function as described to implement 1NN
# From Kevin, 8/3:
#Here is how to do that prediction: For each point in 
#the test data, you find the "k" most similar points in 
#the training data, and their labels are "votes" for which 
#label you should predict as that test point's label. 
#("Similarity" can be defined by any distance metric you 
#choose, but you but you can just start with euclidian distance.) 
#Majority vote determines the predicted label.

distance <- function(type, x, y){
  if (type=="Euclid"){
    return(sqrt(sum((x-y)^2)))
  }
  else if (type == "cosine")
    return ("No cosines yet")
  else return("Not yet.")
  # Or insert a usage message.
}

#Try it on one train/test comparison
distance("E", Ugulino_train[3,1:2], Ugulino_test[5,1:2])
distance("Euclid", Ugulino_train[3,1:2], Ugulino_test[5,1:2])
# Works.


recognizeActivity <- function(train_data, labels, test_data) {
  dist_from_training <- rep(0,length(labels))
  test_labels <- rep("none", dim(test_data)[1])
  for (i in 1:dim(test_data)[1]){
    for(j in 1:dim(train_data)[1]){        
      dist_from_training[j] <- 
        distance("Euclid", train_data[j,1:2], test_data[i,1:2])
    }
    
    # TO do K NN, get k min_dist points here, and...
    min_dist <- min(dist_from_training)
    # use votes to get the index here:
    index_of_min <- which(dist_from_training == min_dist)

    # There may be more than one index_of_min, choose one at random
    chosen_index <- index_of_min[sample(1:length(index_of_min), 1)]
    test_labels[i] <- labels[chosen_index]

    # Reinitialize distance vector
    dist_from_training <-rep(0,length(labels))   
  }
  
  # This (below) returns an actual label name, while returning test_labels 
  # yields lists of number character strings.
  return(test_labels)
}


# The following should be set up in a function:
evaluatePredictions
test_set_labels <- 
  recognizeActivity(Ugulino_train, U_class, Ugulino_test)
predicted_w_actual <- cbind(Ugulino_test[,3], test_set_labels)
#Viewing predicted_w_actual shows predictions are very good, 
# 34 out of 41 correct = 82.9%.
# This is using only 1/1000 of the data set and 2 out of 11 
# features that the study authors used. Can't wait to try the whole
# data set and add in other features.

# The following returns all FALSE. Figure out what's wrong.
correct_predictions <- test_set_labels == Ugulino_test[,3]
#The following returns just one row, TRUE TRUE.  Figure out what's wrong.
prediction_rate <- predicted_w_actual[1,]== predicted_w_actual[2,])

                                                          


# You may want to create other helper functions as well

# Check that your function works as you expect