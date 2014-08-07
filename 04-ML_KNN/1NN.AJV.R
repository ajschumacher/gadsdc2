# Andy Vance - 1NN on Iris example (Class 4 Assignment)
# highly brute force - still learning my way around apply family
# example test case - used sample, then created folds (andy_iris <- iris[sample(nrow(iris)),]), then trng <- andy_iris[1:40,1:5], test <- andy_iris[41:150,1:4]
# simplified labels (to de-factor) - used c("setosa","versicolor","virginica")

ajv_1nn_iris <- function(training.data,labels,test.data) {
  ##Initialize distance values
  distance <- matrix(data = NA,nrow=length(test.data[,1]),ncol=length(training.data[,1]))  
  
  ##Initialize result dataframe
  result1 <- cbind(test.data[,1:4],"Species Guess"=matrix(data=NA,nrow=length(test.data[,1]),ncol=1),Result_1NN=matrix(data=NA, nrow=length(test.data[,1])))
  
  ##Step through the training data
  for (j in 1:length(test.data[,1])) {                                            
    
    ##Step through the test data
    for (i in 1:length(training.data[,1])) {                                              
      ##Calculate distance from all test rows against given training data row
      distance[j,i] <- sqrt(rowSums((test.data[j,1:4]-training.data[i,1:4])^2))     
        
      }
    
    ##calculate the closest training row to the test row.
    nearest.row <- which.min(distance[j,])
    
    ##print(training.data[nearest.row,5])
    
    ##map the result into results dataframe
    result1[j,6] <- training.data[nearest.row,5] 
    
    ## assign label name based on factor output
    if (result1[j,6]==1) {
      result1[j,5] <- "setosa" }
      else {
        if (result1[j,6]==2) {result1[j,5] <- "versicolor"}
      else {result1[j,5] <- "virginica"} }
  }
  
return(result1)

}
