getwd()
setwd("/Users/jypyk/Documents/General Assembly/gadsdc2/04-ML_KNN")

# Define a function as described to implement 1NN
training_data <- iris[1:75,1:4]
test_data <- iris[76:150,1:4]
labels <- iris[1:150,5]

find_neighbors <- function(training_data, labels, test_data) {
  i <- 1
  distances <- data.frame(i=numeric(), n=numeric(), distance=numeric())
  
  while(i <= nrow(training_data)){
    w <- training_data[i,1]
    x <- training_data[i,2]
    y <- training_data[i,3]
    z <- training_data[i,4]
    
    n <- 1
    temp_distances <- data.frame(i=numeric(), n=numeric(), distance=numeric())
    
    while(n <= nrow(test_data)) {
      a <- test_data[n,1]
      b <- test_data[n,2]
      c <- test_data[n,3]
      d <- test_data[n,4]
      
      current_distance <- sqrt(sum((a - w) ^ 2) + ((b - x) ^ 2) + ((c - y) ^ 2) + ((d - z) ^ 2))
      
      if (nrow(temp_distances) == 0){
        new_row <- data.frame(i=i, n=n, distance=current_distance)
        temp_distances <- rbind(temp_distances, new_row)
      }
      else if(current_distance <= min(temp_distances$distance)) {
        new_row <- data.frame(i=i, n=n, distance=current_distance)
        temp_distances <- rbind(temp_distances, new_row)
      }
      
      n <- n+1
    }
    
    closest_row <- which.min(temp_distances$distance)
    distances <- rbind(distances, temp_distances[closest_row, ])

    i <- i+1
  }
  
  
   apply(distances, 1, add_labels(distances$i,distances$n))
  
}

find_neighbors(training_data, labels, test_data)

# You may want to create other helper functions as well

add_labels <- function(i,n){
  print(labels[n + 75])
}


# Check that your function works as you expect
