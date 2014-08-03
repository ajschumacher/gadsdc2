

iris

#Visualize data to inform a hypothesis/theory
library(ggplot2)
ggplot(data = iris) + aes(x = Petal.Length, color = Species) + geom_histogram()
ggplot(data = iris) + aes(x = Petal.Width, color = Species) + geom_histogram()
ggplot(data = iris) + aes(x = Sepal.Length, color = Species) + geom_histogram()
ggplot(data = iris) + aes(x = Sepal.Width, color = Species) + geom_histogram()

rm(list=ls())

#Build 1NN function from scratch
knn1 <- function(training.data, training.groups, testing.data) {
  #Form vector that fits length of testing data to last row
    predicted.groups <- vector(length=nrow(testing.data))
  #Peform following operation for each record in testing data until last row (nrow)
  for(a in 1:nrow(testing.data)) {
    #Calculate Euclidean distances
     #(the "1" argument means rows, a "2" would mean columns)
     #(the "a," syntax will perform operation for each row)
    euclid.distance <- apply(training.data, 1, function(x,y) sqrt(sum((x-y)^2)), testing.data[a, ])
    #Sort the Euclidean distances using order function (default is ascending)
    distance.sorted <- order(euclid.distance)  
    #Grab the most minimized distance for training groups and dump into a vector, 1=k 
    predicted.groups[a] <- training.groups[distance.sorted[1]]}
  #Encode as a factor using training group labels
  factor(predicted.groups, labels=levels(training.groups))
}

#Divide data into 2 random samples
n <- nrow(iris)
set.seed(500)
# Create training and testing data by pulling half a sample randomly
randsamp <- sort(sample(1:n, n * (1 / 2)))
# Select only numeric data for calculating distances
# If you have a theory only select columns that matters 
training.data1 <- iris[randsamp, 1:4]
testing.data1 <- iris[-randsamp, 1:4]
# Select categorical columns for grouping points
training.groups1 <- iris[randsamp, 5] 
testing.groups1 <- iris[-randsamp, 5]

#Test knn1 function
predicted.groupsHard <- knn1(training.data1, training.groups1, testing.data1)
# Number of records that didn't match
sum(predicted.groupsHard != testing.groups1)
# Total number of records overall
length(testing.groups1)
#4 misses out of 75 

#Now do it the easy way, pull knn library which helps us calculate and minimize
#euclidean distance betweeen all points in our matrix
library('class')
# Predict groups using the knn function (only using 1 nearest neighbor)
predicted.groupsEasy <- knn(training.data1, testing.data1, training.groups1, k = 1)
# Number of records that didn't match
sum(predicted.groupsEasy != testing.groups1)
# Total number of records overall
length(testing.groups1)
# 4 misses out of 75 
