#Siddharth Kulkarni's 1nn, GADS DC 2 8/2/2014
sub <- sample(nrow(iris), floor(nrow(iris)*.3))
train <- iris[sub, ]
test <- iris[-sub, ]
predictions <- data.frame() 

for(i in 1:nrow(test)) {
  #create list of euclidan distances using apply for each i in test
  distance <- apply(train[ ,1:4],1,function(x, y) sqrt(sum((y-x)^2)), y = test[i,1:4])
  #merge the training data with the distance values by rownum
  combined <- merge(distance, train, by="row.names")
  #rename species to PredictSpecies
  colnames(combined)[colnames(combined)=="Species"] <- "PredictSpecies"
  #rename default x distance to eucDist
  colnames(combined)[colnames(combined)=="x"] <- "eucdist"    
  #create a df called nearest which is min row based on euclidan distance 
  nearest <- combined[which.min(combined$eucdist), "PredictSpecies"]  
  #assign the prediction to the row i
  z <- merge(test[i, ],nearest)
  #append the predictions table created earlier with the new record containing the prediction
  predictions <- rbind(predictions, z)
}

predictions
