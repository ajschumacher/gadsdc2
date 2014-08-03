data(iris)

predict <- function(trainset, labels, testdata){
  labels[which.min(apply(trainset, 1, function(traindata) {
    sqrt(sum((testdata-traindata)^2))
  }))]
}

oneNN <- function(dataframe){

  train_index <- sample(.80 * nrow(dataframe))

  train <- dataframe[train_index,]
  test  <- dataframe[-train_index,]

  apply(test, 1, function(testdata){
   predict(train[1:4], train$Species, testdata[1:4])
  })
}

oneNN(iris)


