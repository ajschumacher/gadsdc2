#defining euclidean distance function
ed <- function(x1, y2) {
  return (sqrt((x1[1]-y2[1])^2 + (x1[2]-y2[2])^2 + (x1[3]-y2[3])^2 + (x1[4]- y2[4])^2))
}
#defining knn function, where 130 observations are set to train data and 20 observations are set to test data. 
#use double for-loop method and save results in a vectory by adding to an empty vector for each loop
knn <- function(train, labels, test_data){
  outvec <- c()
  for(n in 1:20){
    for(o in 1:130){
      outvec <- c(outvec,ed(test_data[n,],train[o,])) #create an empty vector named "outvec" using the standard c() notation for a vector.

    }
  }
  return(outvec)
}

#randomize iris rows to un-segment labels
iris = iris[sample(nrow(iris)),]

#pass iris through knn function
result <- knn(iris[1:130,1:4],iris[1:130, 5],iris[131:150,1:4])

#get which.min
which.min(result)