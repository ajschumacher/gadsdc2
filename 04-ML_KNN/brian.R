assign.score <- function(test.row, labels, training.data, K = 1) {
  training.data$score <- apply(training.data[,1:4], 1, function(x) { sqrt((x[1] - test.row[1])^2 + (x[2] - test.row[2])^2 + (x[3] - test.row[3])^2 + (x[4] - test.row[4])^2)})
  sorted <- training.data[with(training.data, order(score)), ]
  return(sample(sorted[1:K, as.character(labels)], 1))
  # This does not implement the voting functionality.
}

iris.nn <- function(training_data, labels, test_data, K = 1) {
  test_data[labels] <- NA
  predicto <- apply(test_data, 1, function(x){ assign.score(x, labels, training_data) })
  test_data[labels] <- predicto
  return(test_data)
}

outcome = "Species"
scramble <- iris[sample(nrow(iris)),]
train <- scramble[1:120,1:5]
test <- scramble[121:150,1:5]

z <- iris.nn(train, outcome, test, 3)

mean(rep(z$Species == scramble[121:150,]$Species, 4000))

