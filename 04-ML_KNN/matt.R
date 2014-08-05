load(iris)
training <- iris[1:125,]
test <- iris[126:150,1:4]
outcome <- "Species"


onenn <- function(training,outcome,test) {
  obs <- length(test[[1]])
  blank <- rep(NA,obs)
  test2 <- cbind(test,blank)
  colnames(test2)[5] = outcome
  merged <- rbind(training,test2)
  apply(merged,1, function(x) { (if (is.na(x[[outcome]])) predict(x))
  return tail(merged,n=obs)
  }

predict <- function(dataset,outcome) {
  apply(merged,1, function(x) print(training[1]))
                                 
                                 iterate(x,dataset,outcome))}
}

iterate <- function(x,dataset) {
  dataset[[distance]] <- find match>
  match <- min dataset distance
  x[[outcome]] == match[[outcome]]
  }


