######################################
# HOMEWORK ASSIGNMENT
######################################
#Implement a one-nearest-neighbor algorithm as a function in  R  that takes three arguments:
# •A data frame of numeric columns, the training data.
# •A vector of labels for the training data.
# •A data frame with the same columns as the first data frames, this one the data to predict for.

#The function should return a vector of predicted labels for the test data. Choose a function name and a distance metric to use. You can test your function with the  iris  data.

#How do you know you're done?
# •You have a file,  name.R , containing your function definition, in the  04-ML_KNN  directory of the class repo.


#############################################
#Non function test version of the program
##############################################

# You've got training data, which is a set of features with known labels.
traindta<-iris[, 1:4]
labelss<-iris[, 5]

#You've got test data, which is a set of features with unknown labels.
testdata<-iris[, 1:4]

 #You are literally just finding the 1 closest point to the test point in the training data
nearn<-apply(testdata, 1, function(x1) {
    apply(traindta, 1, function(x2) sqrt(sum((x1-x2)^2)))
    
    })

testdata$name <- labelss[apply(nearn, 1, which.min)]    #and using its label to predict the label for your test point.

head(testdata)

#########################################
# Function version of the 1nn program
#########################################

#Function version
onenn<-function(train,labels, test){

nearn<-apply(test, 1, function(x1) {
    apply(train, 1, function(x2) sqrt(sum((x1-x2)^2)))

    })
    
test$name <- labels[apply(nearn, 1, which.min)]
return(test$name)
}

onenn(traindta,labelss, testdata)

