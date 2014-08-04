data(iris)

predict <- function(trainset, labels, testdata){
  labels[which.min(apply(trainset, 1, function(traindata) {
    sqrt(sum((testdata-traindata)^2))
  }))]
}

oneNN <- function(dataframe){

  index <- 1:nrow(dataframe)

  trainindex <- sample(index, trunc(.80 * nrow(iris)))

  trainset <- dataframe[trainindex, ]
  testset <- dataframe[-trainindex, ]

  for(i in 1:nrow(testset)) {
    testdata <- testset[i,]
    print(predict(trainset[1:4], trainset$Species, testdata[1:4]))
  }
}

oneNN(iris)


