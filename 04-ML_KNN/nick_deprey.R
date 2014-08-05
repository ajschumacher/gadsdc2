## split the set into training and test sets (borrowed from the interwebs)
splitdf <- function(dataframe, seed=NULL) {
  if (!is.null(seed)) set.seed(seed)
  index <- 1:nrow(dataframe)
  trainindex <- sample(index, trunc(length(index)/2))
  trainset <- dataframe[trainindex, ]
  testset <- dataframe[-trainindex, ]
  list(trainset=trainset,testset=testset)
}

## simple euclidian distance formula for two vectors of unlimited but equal length
euclid <- function(x,y){
  dist <- c()
  for(i in 1:length(x)){
    dist[i] <- (x[i]-y[i])^2
  }
  eucliddist <- sqrt(sum(dist))
  return(eucliddist)
  }

## Simple nearest neighbor. 
## Outputs "predictiondf" which includes a predicted label for each observation
nearestneighb <- function(testdf,traindf){
  nums <- sapply(traindf,is.numeric)
  for(i in 1:nrow(testdf)){
    dist <- c()
    for(n in 1:nrow(traindf)){
      dist[n] <- euclid(traindf[n,nums],testdf[i,nums])
    }
    #print(min(dist))
    ind <- match(min(dist),dist)
    testdf$prediction[i] <- as.character(traindf$Species[ind])
    assign("predictiondf", testdf, envir = .GlobalEnv)
    #print(testdf$prediction[i])
    #testdf$dist[i] <- min(dist)
  }
}
  
## attempt at implementing k as an argument to the nearestneighb function above
knn <- function(testdf,traindf,k=1){
  nums <- sapply(traindf,is.numeric)
  for(i in 1:nrow(testdf)){
    dist <- c()
    for(n in 1:nrow(traindf)){
      dist[n] <- euclid(traindf[n,nums],testdf[i,nums])
    }
    #print(min(dist))
    ind <- match(head(sort(dist),k),dist)
    for (k in 1:k){
      testdf$prediction[i][k] <- c(as.character(traindf$Species[ind][k]))
    assign("predictiondf", testdf, envir = .GlobalEnv)
    #print(testdf$prediction[i])
    #testdf$dist[i] <- min(dist)
  }
}